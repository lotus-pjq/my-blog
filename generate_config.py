"""
1. 修复所有文件的 frontmatter category（之前 batch_convert 分类不准确）
2. 生成完整的 articles 数组和 sidebar 配置
"""
import os
import re
import json

ALGORITHM_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

# 更精确的分类规则，用元组保证顺序，长匹配优先
CATEGORY_RULES = [
    # 博弈论
    (r'博弈|威佐夫|斐波那契.*Nim|Anti-SG|Every-SG|Multi-SG|Nim游戏|点格棋|删边游戏', '博弈论'),
    # 数据结构
    (r'树状数组|Splay|字典树|[Tt]rie|笛卡尔树|莫队|线段树|分块|单调队列|扫描线|动态开点', '数据结构'),
    # 图论
    (r'LCA|树的重心|树的直径|树的中心|树上前缀|树上启发|树形DP|树链剖分|DSU on Tree', '图论'),
    # 数论
    (r'BSGS|筛法|欧几里得|欧拉函数|莫比乌斯|原根|卢卡斯|Pollard|Min_25|斯特林|剩余系|勒让德|数论|质因数', '数论'),
    # 数学
    (r'FFT|NTT|多项式|高斯消元|线性基|矩阵|组合数|斐波那契|分数规划|高精度|蔡勒|XOR和路径|数位和|位数字|求和优化|位运算|__builtin', '数学'),
    # 动态规划
    (r'背包|数位DP|状压DP|LIS|最长上升|最长公共|LCS', '动态规划'),
    # 字符串
    (r'[Hh]ash|哈希|最小表示法|回文|字符串', '字符串'),
    # 计算几何
    (r'计算几何|坐标|曼哈顿|切比雪夫|棱堡|平面', '计算几何'),
    # 题解 - 比赛相关
    (r'Codeforces|Educational|ICPC|CCPC|杭电多校|牛客|^P\d{4,5}|^CF\d|洛谷|模板题大全|网络选拔赛|^B\.\s|^F\.\s|^G\.\s|^I\.\s|萌新向典题|Yokohama|Petrozavodsk|XJTUPC|MX-X17|SFMOI|JLOI|JSOI|SCOI|HAOI|BJWC|CQOI|WC2011|星辰之力|xor图', '题解'),
]

def get_category(filename, content_start=""):
    text = filename + " " + content_start
    for pattern, category in CATEGORY_RULES:
        if re.search(pattern, text, re.IGNORECASE):
            return category
    return "其他"

def extract_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    info = {'title': '', 'date': '', 'category': '', 'tags': []}

    fm_match = re.match(r'^---\n(.*?)\n---\n?', content, re.DOTALL)
    body_start = content[fm_match.end():fm_match.end()+800] if fm_match else content[:800]
    if fm_match:
        fm = fm_match.group(1)
        m = re.search(r'^title:\s*(.+)$', fm, re.MULTILINE)
        if m:
            info['title'] = m.group(1).strip()
        m = re.search(r'^date:\s*(.+)$', fm, re.MULTILINE)
        if m:
            info['date'] = m.group(1).strip()
        m = re.search(r'^category:\s*(.+)$', fm, re.MULTILINE)
        if m:
            info['category'] = m.group(1).strip()
        tags = re.findall(r'^\s{2}-\s+(.+)$', fm, re.MULTILINE)
        info['tags'] = [t.strip() for t in tags]

    return info, body_start

def fix_frontmatter_category(filepath, correct_category):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fm_match = re.match(r'^(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not fm_match:
        return False

    fm = fm_match.group(2)
    if re.search(r'^category:\s*.+$', fm, re.MULTILINE):
        new_fm = re.sub(r'^category:\s*.+$', f'category: {correct_category}', fm, flags=re.MULTILINE)
    else:
        new_fm = fm + f'\ncategory: {correct_category}'

    if new_fm != fm:
        new_content = fm_match.group(1) + new_fm + fm_match.group(3) + content[fm_match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    articles = []
    fixed = 0

    for filename in sorted(os.listdir(ALGORITHM_DIR)):
        if not filename.endswith('.md'):
            continue

        filepath = os.path.join(ALGORITHM_DIR, filename)
        info, content_start = extract_frontmatter(filepath)

        title = info['title'] or filename.replace('.md', '')
        date = info['date'] or '2026-03-09'
        tags = info['tags'] or ['算法']

        correct_category = get_category(filename, content_start)

        if info['category'] != correct_category:
            if fix_frontmatter_category(filepath, correct_category):
                fixed += 1
                print(f"  [分类修正] {filename}: {info['category']} -> {correct_category}")

        link_name = filename.replace('.md', '')
        link = f'/blog/algorithm/{link_name}'

        articles.append({
            'title': title,
            'link': link,
            'category': correct_category,
            'tags': tags,
            'date': date,
            'filename': filename,
        })

    print(f"\n修正了 {fixed} 个文件的分类")

    by_category = {}
    for a in articles:
        cat = a['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(a)

    print(f"\n总计: {len(articles)} 篇文章")
    print(f"按分类统计:")
    for cat, items in sorted(by_category.items(), key=lambda x: -len(x[1])):
        print(f"  {cat}: {len(items)} 篇")

    cat_order = ['博弈论', '数据结构', '图论', '数论', '数学', '动态规划', '字符串', '计算几何', '题解', '其他']

    lines = []
    for cat in cat_order:
        if cat not in by_category:
            continue
        lines.append(f"  // {cat}")
        for a in sorted(by_category[cat], key=lambda x: x['title']):
            tags_str = json.dumps(a['tags'], ensure_ascii=False)
            safe_title = a['title'].replace("'", "\\'")
            safe_link = a['link']
            lines.append(f"  {{ title: '{safe_title}', link: '{safe_link}', category: '{a['category']}', tags: {tags_str}, date: '{a['date']}' }},")

    articles_js = "const articles = [\n" + "\n".join(lines) + "\n]"

    out_dir = os.path.dirname(os.path.dirname(ALGORITHM_DIR))
    with open(os.path.join(out_dir, 'generated_articles.js'), 'w', encoding='utf-8') as f:
        f.write(articles_js)
    print(f"\narticles 数组已写入 generated_articles.js")

    category_icons = {
        '博弈论': '🎮', '数据结构': '📊', '图论': '🌲', '数论': '🔢',
        '数学': '📐', '动态规划': '💡', '字符串': '🔤', '计算几何': '📍',
        '题解': '📝', '其他': '📦',
    }

    sidebar_groups = []
    for cat in cat_order:
        if cat not in by_category:
            continue
        icon = category_icons.get(cat, '📄')
        items = sorted(by_category[cat], key=lambda x: x['title'])
        collapsed = 'true' if cat != '博弈论' else 'false'
        item_lines = []
        for a in items:
            display = a['title']
            if len(display) > 35:
                display = display[:33] + '...'
            safe_display = display.replace("'", "\\'")
            item_lines.append(f"            {{ text: '{safe_display}', link: '{a['link']}' }}")

        sidebar_groups.append(f"""        {{
          text: '{icon} {cat}',
          collapsed: {collapsed},
          items: [
{(',' + chr(10)).join(item_lines)},
          ]
        }}""")

    sidebar_js = f"""      '/blog/algorithm/': [
        {{
          text: '📚 算法笔记',
          items: [
            {{ text: '← 返回博客首页', link: '/blog/' }},
            {{ text: '📑 算法归档', link: '/blog/algorithm-archive' }},
          ]
        }},
{(',' + chr(10)).join(sidebar_groups)},
      ]"""

    with open(os.path.join(out_dir, 'generated_sidebar.js'), 'w', encoding='utf-8') as f:
        f.write(sidebar_js)
    print(f"sidebar 配置已写入 generated_sidebar.js")

if __name__ == '__main__':
    main()
