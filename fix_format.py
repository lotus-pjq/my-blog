"""
修复从 Logseq 转换而来的 Markdown 文件格式问题
主要修复：
1. 代码块（```）前的缩进导致 VitePress 不渲染
2. 表格行前的缩进导致 VitePress 不渲染
3. 残留的 Logseq 格式（tags::、bullet points 等）
4. Logseq 缩进（tab+space）导致的深层嵌套格式问题
"""

import os
import re

ALGORITHM_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 分离 frontmatter 和正文
    frontmatter = ""
    body = content
    fm_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if fm_match:
        frontmatter = fm_match.group(1)
        body = content[len(frontmatter):]

    # 移除 tags:: 行（Logseq 格式残留）
    body = re.sub(r'^\s*tags::\s*.+$\n?', '', body, flags=re.MULTILINE)

    # 移除 collapsed:: true
    body = re.sub(r'\s*collapsed::\s*true\s*', '\n', body)

    # 移除 id:: 行
    body = re.sub(r'\s*id::\s*[a-f0-9-]+\s*', '\n', body)

    # 第一遍：处理代码块和表格的缩进
    body = fix_code_blocks_and_tables(body)

    # 第二遍：对剩余的缩进行做全局清理
    body = fix_remaining_indentation(body)

    # 修复 "- ### " 等 bullet + heading 组合
    body = re.sub(r'^(\s*)- (#{1,6}\s)', r'\2', body, flags=re.MULTILINE)

    # 修复 "- > " 引用在 bullet 内
    body = re.sub(r'^(\s*)- (>\s)', r'\2', body, flags=re.MULTILINE)

    # 移除孤立的 "- " 行（仅有 bullet 无内容）
    body = re.sub(r'^\s*-\s*$\n', '', body, flags=re.MULTILINE)

    # 清理 Logseq ==高亮== 为 **加粗**（VitePress 不支持 ==）
    # body = re.sub(r'==([^=]+)==', r'**\1**', body)

    # 清理连续空行（超过2个）
    body = re.sub(r'\n{3,}', '\n\n', body)

    result = frontmatter + body

    if result != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False


def strip_logseq_indent(line):
    """移除 Logseq 风格的缩进（tab+空格组合）"""
    # 移除行首的 tab 和空格混合缩进
    return line.lstrip('\t').lstrip(' ')


def fix_remaining_indentation(body):
    """
    第二遍清理：处理第一遍遗漏的缩进行。
    对于仍以 tab 开头的非代码块行，移除 tab 缩进。
    """
    lines = body.split('\n')
    result = []
    in_code = False

    for line in lines:
        # 追踪代码块状态
        stripped = line.lstrip()
        if re.match(r'^\s*`{3,}', line):
            in_code = not in_code
            result.append(line)
            continue

        if in_code:
            result.append(line)
            continue

        # 不在代码块中：如果行以 tab 开头，去掉 tab 缩进
        if line.startswith('\t'):
            # 保留 list 项的适当缩进
            cleaned = line.lstrip('\t')
            # 如果去掉tab之后以空格开头，也去掉多余空格（Logseq风格: tab + spaces）
            if cleaned.startswith('  ') and not cleaned.lstrip().startswith('-'):
                cleaned = cleaned.lstrip()
            result.append(cleaned)
        else:
            result.append(line)

    return '\n'.join(result)


def fix_code_blocks_and_tables(body):
    """
    逐行处理，修复代码块和表格的缩进。
    策略：
    - 代码块 fence（```）：移除所有前导空白
    - 代码块内容：移除公共前导空白（dedent）
    - 表格行（|开头，去掉前导空白后）：移除所有前导空白
    """
    lines = body.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        # 检测代码块开始（可能被缩进、可能有前导 "- "）
        fence_match = re.match(r'^[\s\t]*(?:-\s+)?(`{3,})([\w+#.-]*)\s*$', line)
        if fence_match:
            fence_ticks = fence_match.group(1)
            lang = fence_match.group(2)

            # 输出代码块开始 fence
            result.append(f'{fence_ticks}{lang}')
            i += 1

            # 收集代码块内容直到结束 fence
            code_lines = []
            found_end = False
            end_pattern = re.compile(r'^[\s\t]*' + re.escape(fence_ticks) + r'\s*$')
            while i < len(lines):
                code_line = lines[i]
                if end_pattern.match(code_line):
                    found_end = True
                    i += 1
                    break
                code_lines.append(code_line)
                i += 1

            # Dedent 代码块内容
            if code_lines:
                dedented = dedent_lines(code_lines)
                result.extend(dedented)

            result.append(fence_ticks)
            continue

        # 检测表格行（去掉空白和可能的 "- " 后以 | 开头）
        table_check = re.sub(r'^[\s\t]*(?:-\s+)?', '', line)
        if table_check.startswith('|') and '|' in table_check[1:]:
            # 收集所有连续的表格行
            table_lines = []
            while i < len(lines):
                tl = lines[i]
                tl_clean = re.sub(r'^[\s\t]*(?:-\s+)?', '', tl)
                if tl_clean.startswith('|') and '|' in tl_clean[1:]:
                    table_lines.append(tl_clean)
                    i += 1
                elif tl.strip() == '' and table_lines:
                    break
                else:
                    break

            # 移除表格前可能的孤立 "- " 行
            if result and re.match(r'^\s*-\s*$', result[-1]):
                result.pop()

            # 确保表格前有空行（Markdown 表格需要）
            if result and result[-1].strip() != '':
                result.append('')
            result.extend(table_lines)
            if i < len(lines) and lines[i].strip() != '':
                result.append('')
            continue

        # 普通行
        result.append(line)
        i += 1

    return '\n'.join(result)


def dedent_lines(lines):
    """移除代码行的公共前导空白"""
    if not lines:
        return lines

    # 找出非空行的最小缩进
    min_indent = float('inf')
    for line in lines:
        if line.strip():  # 跳过空行
            # 将 tab 展开为空格（1 tab = 1 level）
            expanded = line.expandtabs(2)
            leading = len(expanded) - len(expanded.lstrip())
            min_indent = min(min_indent, leading)

    if min_indent == float('inf') or min_indent == 0:
        return lines

    # 移除公共缩进
    result = []
    for line in lines:
        if line.strip():
            expanded = line.expandtabs(2)
            result.append(expanded[min_indent:])
        else:
            result.append('')
    return result


def main():
    print(f"扫描目录: {ALGORITHM_DIR}")
    fixed_count = 0
    total = 0
    fixed_files = []

    for filename in sorted(os.listdir(ALGORITHM_DIR)):
        if not filename.endswith('.md'):
            continue
        total += 1
        filepath = os.path.join(ALGORITHM_DIR, filename)

        try:
            if fix_file(filepath):
                fixed_count += 1
                fixed_files.append(filename)
                print(f"  [修复] {filename}")
            else:
                print(f"  [无变化] {filename}")
        except Exception as e:
            print(f"  [错误] {filename}: {e}")

    print(f"\n完成: 共 {total} 个文件, 修复了 {fixed_count} 个文件")
    if fixed_files:
        print(f"\n修复的文件列表:")
        for f in fixed_files:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
