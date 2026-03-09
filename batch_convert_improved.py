import os
import re
from datetime import datetime

SOURCE_DIR = r"d:\Logseq\pages"
TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

EXCLUDE_FILES = [
    "今日计划", "英语写作", "雅思", "大物", "数据结构实验", "计组", 
    "星穹", "梯子", "debug", "tmp", "美赛", "ACM.*整理", "ACM.*总览", 
    "ACM.*指南", "未命名", "contents", "template", "Devin", "ICPC英文", 
    "英文单词", "logseq用法", "牛客2题解", "D-数字积木", "GPT第一问思路",
    "最终公式汇总", "Force Balance", "Vector_Balance", "星穹之海的点燃"
]

CATEGORY_MAP = {
    "博弈": "博弈论", "SG": "博弈论", "Nim": "博弈论", "威佐夫": "博弈论",
    "树状数组": "数据结构", "Splay": "数据结构", "字典树": "数据结构",
    "trie": "数据结构", "笛卡尔树": "数据结构", "莫队": "数据结构",
    "线段树": "数据结构", "分块": "数据结构", "单调队列": "数据结构",
    "LCA": "图论", "树的": "图论", "树上": "图论", "树形DP": "图论",
    "树链剖分": "图论", "DSU on Tree": "图论",
    "筛法": "数论", "欧几里得": "数论", "欧拉": "数论", "莫比乌斯": "数论",
    "原根": "数论", "BSGS": "数论", "卢卡斯": "数论", "Pollard": "数论",
    "FFT": "数学", "NTT": "数学", "多项式": "数学", "高斯消元": "数学",
    "背包": "动态规划", "数位DP": "动态规划", "状压DP": "动态规划",
    "hash": "字符串", "哈希": "字符串", "最小表示法": "字符串",
    "计算几何": "计算几何", "坐标": "计算几何",
    "Codeforces": "题解", "ICPC": "题解", "CCPC": "题解", "洛谷": "题解",
}

def should_exclude(filename):
    for pattern in EXCLUDE_FILES:
        if re.search(pattern, filename, re.IGNORECASE):
            return True
    return False

def get_category(filename, content):
    text = filename + " " + content[:500]
    for keyword, category in CATEGORY_MAP.items():
        if re.search(keyword, text, re.IGNORECASE):
            return category
    return "其他"

def clean_logseq_syntax(content):
    """改进的清理函数"""
    # 移除 collapsed:: true
    content = re.sub(r'\s*collapsed::\s*true\s*', '', content)
    
    # 移除 id::
    content = re.sub(r'\s*id::\s*[a-f0-9-]+\s*', '', content)
    
    # 移除 title:: 行
    content = re.sub(r'^title::\s*.+$\n?', '', content, flags=re.MULTILINE)
    
    # 转换 Logseq 内部链接 [[xxx]] 为普通文本
    content = re.sub(r'\[\[([^\]]+)\]\]', r'`\1`', content)
    
    # 移除 LOGBOOK
    content = re.sub(r':LOGBOOK:.*?:END:', '', content, flags=re.DOTALL)
    
    # 移除 TODO/DONE
    content = re.sub(r'^\s*(TODO|DONE)\s+', '', content, flags=re.MULTILINE)
    
    # 移除图片属性 {:height xxx, :width xxx}
    content = re.sub(r'\{:[^}]+\}', '', content)
    
    # 移除图片引用
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', content)
    
    # 转换 Logseq 缩进为 Markdown 标准格式
    # Logseq 使用 tab 缩进，转换为列表
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        # 计算缩进级别
        indent_level = 0
        stripped = line.lstrip('\t ')
        indent_level = len(line) - len(stripped)
        
        # 如果是列表项（以 - 开头）
        if stripped.startswith('- '):
            # 保持原有的 - 
            new_lines.append('  ' * (indent_level // 2) + stripped)
        else:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    
    # 清理多余空行（超过2个连续空行）
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def extract_title(filename, content):
    """改进的标题提取"""
    # 从文件名提取
    title = filename.replace('.md', '')
    
    # 尝试从内容第一个 # 标题提取
    match = re.search(r'^#\s+(.+?)(?:\s*[:：])?$', content, re.MULTILINE)
    if match:
        extracted = match.group(1).strip()
        # 避免提取到奇怪的标题
        if len(extracted) > 0 and len(extracted) < 100:
            title = extracted
    
    return title

def extract_tags(content):
    """提取标签"""
    tags_match = re.search(r'^tags::\s*(.+)$', content, re.MULTILINE)
    if tags_match:
        tags_line = tags_match.group(1)
        # 分割标签，移除 # 符号
        tags = [tag.strip().replace('#', '').replace('算法/', '') 
                for tag in re.split(r'[#\s]+', tags_line) if tag.strip()]
        return tags
    return ['算法']

def generate_frontmatter(title, category, tags):
    """生成 frontmatter"""
    date = datetime.now().strftime('%Y-%m-%d')
    tags_yaml = '\n'.join([f'  - {tag}' for tag in tags if tag])
    
    return f"""---
title: {title}
date: {date}
category: {category}
tags:
{tags_yaml}
outline: deep
---

"""

def convert_file(source_path, target_dir):
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(source_path)
        
        # 提取标签
        tags = extract_tags(content)
        
        # 清理内容
        content = clean_logseq_syntax(content)
        
        # 提取标题
        title = extract_title(filename, content)
        
        # 判断分类
        category = get_category(filename, content)
        
        # 生成 frontmatter
        frontmatter = generate_frontmatter(title, category, tags)
        
        # 组合最终内容
        final_content = frontmatter + content
        
        # 保存文件
        target_path = os.path.join(target_dir, filename)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True, filename, category
        
    except Exception as e:
        return False, filename, str(e)

def main():
    print("开始批量转换ACM笔记...")
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    total = 0
    success = 0
    excluded = 0
    failed = []
    category_count = {}
    
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.md'):
            continue
        
        total += 1
        
        if should_exclude(filename):
            excluded += 1
            print(f"[跳过] {filename}")
            continue
        
        source_path = os.path.join(SOURCE_DIR, filename)
        result, name, info = convert_file(source_path, TARGET_DIR)
        
        if result:
            success += 1
            category_count[info] = category_count.get(info, 0) + 1
            print(f"[成功] {name} -> {info}")
        else:
            failed.append((name, info))
            print(f"[失败] {name} - {info}")
    
    print("\n" + "="*50)
    print(f"总文件数: {total}")
    print(f"排除: {excluded} | 成功: {success} | 失败: {len(failed)}")
    print("\n分类统计:")
    for category, count in sorted(category_count.items()):
        print(f"  {category}: {count}篇")
    
    if failed:
        print("\n失败文件:")
        for name, error in failed[:10]:  # 只显示前10个
            print(f"  {name}: {error}")

if __name__ == "__main__":
    main()

