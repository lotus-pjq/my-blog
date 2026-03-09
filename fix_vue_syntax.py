import os
import re

# 目标目录
TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

def fix_vue_syntax(content):
    """修复Vue语法冲突"""
    # 将 {{ 替换为 { {（添加空格）
    content = re.sub(r'\{\{', '{ {', content)
    # 将 }} 替换为 } }（添加空格）
    content = re.sub(r'\}\}', '} }', content)
    return content

def main():
    count = 0
    for filename in os.listdir(TARGET_DIR):
        if not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(TARGET_DIR, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 检查是否包含 {{ 或 }}
            if '{{' in content or '}}' in content:
                fixed_content = fix_vue_syntax(content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                
                count += 1
                print(f"[修复] {filename}")
        
        except Exception as e:
            print(f"[错误] {filename}: {e}")
    
    print(f"\n共修复 {count} 个文件")

if __name__ == "__main__":
    main()

