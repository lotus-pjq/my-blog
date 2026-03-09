import os
import re
from datetime import datetime
from collections import defaultdict

SOURCE_DIR = r"d:\Logseq\pages"
TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"
JOURNALS_DIR = r"d:\Logseq\journals"

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

def build_page_date_map():
    """从journals中提取每个page的创建日期"""
    page_dates = {}
    
    for journal_file in os.listdir(JOURNALS_DIR):
        if not journal_file.endswith('.md'):
            continue
        
        # 从文件名提取日期 2025_08_01.md -> 2025-08-01
        date_str = journal_file.replace('.md', '').replace('_', '-')
        
        journal_path = os.path.join(JOURNALS_DIR, journal_file)
        try:
            with open(journal_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 查找所有 [[page_name]] 引用
            page_refs = re.findall(r'\[\[([^\]]+)\]\]', content)
            
            for page_name in page_refs:
                # 只记录第一次出现的日期（最早的日期）
                if page_name not in page_dates:
                    page_dates[page_name] = date_str
        
        except Exception as e:
            print(f"[警告] 读取journal失败: {journal_file} - {e}")
    
    return page_dates

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
    content = re.sub(r'\s*collapsed::\s*true\s*', '', content)
    content = re.sub(r'\s*id::\s*[a-f0-9-]+\s*', '', content)
    content = re.sub(r'^title::\s*.+$\n?', '', content, flags=re.MULTILINE)
    content = re.sub(r'\[\[([^\]]+)\]\]', r'`\1`', content)
    content = re.sub(r':LOGBOOK:.*?:END:', '', content, flags=re.DOTALL)
    content = re.sub(r'^\s*(TODO|DONE)\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'\{:[^}]+\}', '', content)
    content = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', content)
    
    # 转换缩进
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        indent_level = 0
        stripped = line.lstrip('\t ')
        indent_level = len(line) - len(stripped)
        
        if stripped.startswith('- '):
            new_lines.append('  ' * (indent_level // 2) + stripped)
        else:
            new_lines.append(line)
    
    content = '\n'.join(new_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content

def extract_title(filename, content):
    title = filename.replace('.md', '')
    match = re.search(r'^#\s+(.+?)(?:\s*[:：])?$', content, re.MULTILINE)
    if match:
        extracted = match.group(1).strip()
        if len(extracted) > 0 and len(extracted) < 100:
            title = extracted
    return title

def extract_tags(content):
    tags_match = re.search(r'^tags::\s*(.+)$', content, re.MULTILINE)
    if tags_match:
        tags_line = tags_match.group(1)
        tags = [tag.strip().replace('#', '').replace('算法/', '') 
                for tag in re.split(r'[#\s]+', tags_line) if tag.strip()]
        return tags
    return ['算法']

def generate_frontmatter(title, category, tags, date):
    """生成 frontmatter，使用实际创建日期"""
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

def convert_file(source_path, target_dir, page_dates):
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(source_path)
        page_name = filename.replace('.md', '')
        
        # 从journals获取创建日期
        date = page_dates.get(page_name, datetime.now().strftime('%Y-%m-%d'))
        
        tags = extract_tags(content)
        content = clean_logseq_syntax(content)
        title = extract_title(filename, content)
        category = get_category(filename, content)
        
        frontmatter = generate_frontmatter(title, category, tags, date)
        final_content = frontmatter + content
        
        target_path = os.path.join(target_dir, filename)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True, filename, category, date
        
    except Exception as e:
        return False, filename, str(e), None

def main():
    print("步骤1: 从journals提取笔记创建日期...")
    page_dates = build_page_date_map()
    print(f"  找到 {len(page_dates)} 个笔记的日期记录")
    
    print("\n步骤2: 开始批量转换ACM笔记...")
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    total = 0
    success = 0
    excluded = 0
    failed = []
    category_count = {}
    date_count = defaultdict(int)
    
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.md'):
            continue
        
        total += 1
        
        if should_exclude(filename):
            excluded += 1
            continue
        
        source_path = os.path.join(SOURCE_DIR, filename)
        result, name, info, date = convert_file(source_path, TARGET_DIR, page_dates)
        
        if result:
            success += 1
            category_count[info] = category_count.get(info, 0) + 1
            if date:
                date_count[date[:7]] += 1  # 按月统计
            print(f"[成功] {name} -> {info} ({date})")
        else:
            failed.append((name, info))
            print(f"[失败] {name} - {info}")
    
    print("\n" + "="*50)
    print(f"总文件数: {total}")
    print(f"排除: {excluded} | 成功: {success} | 失败: {len(failed)}")
    
    print("\n分类统计:")
    for category, count in sorted(category_count.items()):
        print(f"  {category}: {count}篇")
    
    print("\n时间分布:")
    for month, count in sorted(date_count.items())[:10]:
        print(f"  {month}: {count}篇")
    
    if failed:
        print("\n失败文件:")
        for name, error in failed[:10]:
            print(f"  {name}: {error}")

if __name__ == "__main__":
    main()

