import os
import re

TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

def fix_markdown_syntax(content):
    """修复Markdown语法问题"""
    
    # 修复：列表项后直接跟代码块
    # - 代码- ```C++ 改为 - 代码\n\n```C++
    content = re.sub(r'(^-\s+[^\n]+)-\s*```', r'\1\n\n```', content, flags=re.MULTILINE)
    
    # 修复：未闭合的HTML标签（移除所有HTML标签）
    content = re.sub(r'<[^>]+>', '', content)
    
    # 修复：cin.tie(nullptr) 等C++代码中的冒号问题
    # 确保代码块内的内容不被Vue解析
    lines = content.split('\n')
    in_code_block = False
    fixed_lines = []
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        # 如果不在代码块中，检查是否有可能被Vue误解析的内容
        if not in_code_block:
            # 转义单独的冒号（但保留在代码块标记中的）
            if '::' in line and not line.strip().startswith('```'):
                # 保留frontmatter中的冒号
                if not line.strip().endswith(':'):
                    pass  # 暂时不处理
        
        fixed_lines.append(line)
    
    content = '\n'.join(fixed_lines)
    
    return content

def main():
    print("修复Markdown语法问题...")
    
    fixed_count = 0
    error_count = 0
    
    for filename in os.listdir(TARGET_DIR):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(TARGET_DIR, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            fixed_content = fix_markdown_syntax(content)
            
            if fixed_content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                fixed_count += 1
                print(f"[修复] {filename}")
        
        except Exception as e:
            error_count += 1
            print(f"[错误] {filename}: {e}")
    
    print(f"\n修复完成: {fixed_count}个文件, {error_count}个错误")

if __name__ == "__main__":
    main()

