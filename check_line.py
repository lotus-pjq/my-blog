import os

filepath = r"d:\Logseq\BLOG_github\docs\blog\algorithm\网络选拔赛模板.md"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 查找所有 {{ 和 }}
import re
matches = list(re.finditer(r'\{\{|\}\}', content))

if matches:
    print(f"Found {len(matches)} matches:")
    for match in matches[:10]:  # 只显示前10个
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 50)
        context = content[start:end]
        line_num = content[:match.start()].count('\n') + 1
        print(f"\nLine {line_num}, Position {match.start()}:")
        print(repr(context))
else:
    print("No {{ or }} found")
