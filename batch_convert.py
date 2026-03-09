import os
import re
from datetime import datetime

# 源目录和目标目录
SOURCE_DIR = r"d:\Logseq\pages"
TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

# 需要排除的文件（日常/非算法内容）
EXCLUDE_FILES = [
    "今日计划", "英语写作", "雅思", "大物", "数据结构实验", "计组", 
    "星穹", "梯子", "debug", "tmp", "美赛", "ACM.*整理", "ACM.*总览", 
    "ACM.*指南", "未命名", "contents", "template", "Devin", "ICPC英文", 
    "英文单词", "logseq用法", "牛客2题解", "D-数字积木", "GPT第一问思路",
    "最终公式汇总", "Force Balance", "Vector_Balance", "星穹之海的点燃"
]

# 分类映射
CATEGORY_MAP = {
    # 数据结构
    "树状数组": "数据结构",
    "Splay": "数据结构",
    "字典树": "数据结构",
    "trie": "数据结构",
    "笛卡尔树": "数据结构",
    "莫队": "数据结构",
    "线段树": "数据结构",
    "分块": "数据结构",
    "单调队列": "数据结构",
    "LCA": "图论",
    "树的": "图论",
    "树上": "图论",
    "树形DP": "图论",
    "树链剖分": "图论",
    "DSU on Tree": "图论",
    
    # 数论
    "筛法": "数论",
    "欧几里得": "数论",
    "欧拉": "数论",
    "莫比乌斯": "数论",
    "原根": "数论",
    "BSGS": "数论",
    "卢卡斯": "数论",
    "Pollard": "数论",
    "Min_25": "数论",
    "类欧": "数论",
    "组合数": "数论",
    "斯特林": "数论",
    "勒让德": "数论",
    "剩余系": "数论",
    
    # 数学
    "FFT": "数学",
    "NTT": "数学",
    "多项式": "数学",
    "高斯消元": "数学",
    "矩阵": "数学",
    "斐波那契": "数学",
    "蔡勒": "数学",
    
    # DP
    "背包": "动态规划",
    "数位DP": "动态规划",
    "状压DP": "动态规划",
    "LIS": "动态规划",
    "LCS": "动态规划",
    
    # 字符串
    "hash": "字符串",
    "哈希": "字符串",
    "最小表示法": "字符串",
    "回文": "字符串",
    
    # 计算几何
    "计算几何": "计算几何",
    "坐标": "计算几何",
    "距离": "计算几何",
    "扫描线": "计算几何",
    
    # 博弈论
    "博弈": "博弈论",
    "SG": "博弈论",
    "Nim": "博弈论",
    "威佐夫": "博弈论",
    
    # 题解
    "Codeforces": "题解",
    "Educational": "题解",
    "ICPC": "题解",
    "CCPC": "题解",
    "洛谷": "题解",
    "牛客": "题解",
    "杭电": "题解",
    "P[0-9]": "题解",
}

def should_exclude(filename):
    """判断文件是否应该排除"""
    for pattern in EXCLUDE_FILES:
        if re.search(pattern, filename, re.IGNORECASE):
            return True
    return False

def get_category(filename, content):
    """根据文件名和内容判断分类"""
    text = filename + " " + content[:500]
    
    for keyword, category in CATEGORY_MAP.items():
        if re.search(keyword, text, re.IGNORECASE):
            return category
    
    return "其他"

def clean_logseq_syntax(content):
    """清理Logseq特有语法"""
    # 移除collapsed::
    content = re.sub(r'\s*collapsed::\s*true', '', content)
    
    # 移除id::
    content = re.sub(r'\s*id::\s*[a-f0-9-]+', '', content)
    
    # 移除title::（保留在frontmatter中）
    content = re.sub(r'^title::\s*.+$', '', content, flags=re.MULTILINE)
    
    # 转换Logseq链接 [[xxx]] 为普通文本
    content = re.sub(r'\[\[([^\]]+)\]\]', r'\1', content)
    
    # 移除LOGBOOK
    content = re.sub(r':LOGBOOK:.*?:END:', '', content, flags=re.DOTALL)
    
    # 移除TODO标记
    content = re.sub(r'^\s*TODO\s+', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*DONE\s+', '', content, flags=re.MULTILINE)
    
    return content

def extract_title(filename, content):
    """提取标题"""
    # 优先从文件名提取
    title = filename.replace('.md', '')
    
    # 尝试从内容中提取第一个标题
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        title = match.group(1).strip()
    
    return title

def generate_frontmatter(title, category, tags):
    """生成VitePress frontmatter"""
    date = datetime.now().strftime('%Y-%m-%d')
    
    frontmatter = f"""---
title: {title}
date: {date}
category: {category}
tags:
{tags}
description: {title}相关的算法笔记和代码模板
---

"""
    return frontmatter

def convert_file(source_path, target_dir):
    """转换单个文件"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = os.path.basename(source_path)
        
        # 提取已有的tags
        tags_match = re.search(r'^tags::\s*(.+)$', content, re.MULTILINE)
        if tags_match:
            tags_line = tags_match.group(1)
            tags = [tag.strip() for tag in tags_line.split('#') if tag.strip()]
            tags_yaml = '\n'.join([f'  - {tag}' for tag in tags])
        else:
            tags_yaml = '  - 算法'
        
        # 清理内容
        content = clean_logseq_syntax(content)
        
        # 提取标题
        title = extract_title(filename, content)
        
        # 判断分类
        category = get_category(filename, content)
        
        # 生成frontmatter
        frontmatter = generate_frontmatter(title, category, tags_yaml)
        
        # 组合最终内容
        final_content = frontmatter + content
        
        # 生成目标文件名（转换为URL友好格式）
        target_filename = filename.lower()
        target_filename = re.sub(r'[^\w\s-]', '', target_filename)
        target_filename = re.sub(r'[-\s]+', '-', target_filename)
        
        # 保存文件
        target_path = os.path.join(target_dir, target_filename)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        return True, filename, category
        
    except Exception as e:
        return False, filename, str(e)

def main():
    """主函数"""
    print("开始批量转换ACM笔记...")
    
    # 确保目标目录存在
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # 统计
    total = 0
    success = 0
    excluded = 0
    failed = []
    
    category_count = {}
    
    # 遍历源目录
    for filename in os.listdir(SOURCE_DIR):
        if not filename.endswith('.md'):
            continue
        
        total += 1
        
        # 检查是否排除
        if should_exclude(filename):
            excluded += 1
            print(f"[跳过] {filename} - 日常内容")
            continue
        
        source_path = os.path.join(SOURCE_DIR, filename)
        
        # 转换文件
        result, name, info = convert_file(source_path, TARGET_DIR)
        
        if result:
            success += 1
            category_count[info] = category_count.get(info, 0) + 1
            print(f"[成功] {name} -> {info}")
        else:
            failed.append((name, info))
            print(f"[失败] {name} - {info}")
    
    # 输出统计
    print("\n" + "="*50)
    print("转换完成！")
    print(f"总文件数: {total}")
    print(f"排除文件: {excluded}")
    print(f"成功转换: {success}")
    print(f"失败: {len(failed)}")
    print("\n分类统计:")
    for category, count in sorted(category_count.items()):
        print(f"  {category}: {count}篇")
    
    if failed:
        print("\n失败文件:")
        for name, error in failed:
            print(f"  {name}: {error}")

if __name__ == "__main__":
    main()

