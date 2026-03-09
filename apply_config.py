"""Apply generated articles and sidebar to the actual config files"""

# Read generated articles
with open(r'd:\Logseq\BLOG_github\docs\generated_articles.js', 'r', encoding='utf-8') as f:
    new_articles = f.read()

# Read current archive
with open(r'd:\Logseq\BLOG_github\docs\blog\algorithm-archive.md', 'r', encoding='utf-8') as f:
    archive = f.read()

# Find the articles array with proper bracket matching
start_marker = 'const articles = ['
start_pos = archive.find(start_marker)
if start_pos == -1:
    raise Exception("Could not find 'const articles = [' in archive")

# Count brackets to find the matching ]
bracket_count = 0
pos = start_pos + len(start_marker) - 1
for i in range(pos, len(archive)):
    if archive[i] == '[':
        bracket_count += 1
    elif archive[i] == ']':
        bracket_count -= 1
        if bracket_count == 0:
            end_pos = i + 1
            break

new_archive = archive[:start_pos] + new_articles + archive[end_pos:]

old_cats = "const categories = ['全部', '数据结构', '图论', '数论', '数学', '动态规划', '字符串', '计算几何', '博弈论', '题解']"
new_cats = "const categories = ['全部', '博弈论', '数据结构', '图论', '数论', '数学', '动态规划', '字符串', '计算几何', '题解', '其他']"
new_archive = new_archive.replace(old_cats, new_cats)

with open(r'd:\Logseq\BLOG_github\docs\blog\algorithm-archive.md', 'w', encoding='utf-8') as f:
    f.write(new_archive)

print(f'算法归档已更新 (替换了 {start_pos}-{end_pos} 位置)')

# Now update sidebar in config.mjs
with open(r'd:\Logseq\BLOG_github\docs\generated_sidebar.js', 'r', encoding='utf-8') as f:
    new_sidebar = f.read()

with open(r'd:\Logseq\BLOG_github\docs\.vitepress\config.mjs', 'r', encoding='utf-8') as f:
    config = f.read()

sidebar_start = "'/blog/algorithm/': ["
start_pos = config.find(sidebar_start)
if start_pos == -1:
    raise Exception("Could not find sidebar config")

bracket_count = 0
pos = start_pos + len(sidebar_start) - 1
for i in range(pos, len(config)):
    if config[i] == '[':
        bracket_count += 1
    elif config[i] == ']':
        bracket_count -= 1
        if bracket_count == 0:
            end_pos = i + 1
            break

new_config = config[:start_pos] + new_sidebar.strip() + config[end_pos:]

with open(r'd:\Logseq\BLOG_github\docs\.vitepress\config.mjs', 'w', encoding='utf-8') as f:
    f.write(new_config)

print('侧边栏配置已更新')
