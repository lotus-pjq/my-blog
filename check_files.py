import os

source_dir = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

print("Looking for specific files:")
target_files = ['博弈论.md', '线性基.md', '树链剖分.md', '莫队算法.md', 'LCA.md', 'FFT.md', '背包专题.md']

for target in target_files:
    if target in os.listdir(source_dir):
        print(f"FOUND: {target}")
    else:
        print(f"NOT FOUND: {target}")

print("\n\nAll files with Chinese characters:")
for f in os.listdir(source_dir):
    if any(ord(c) > 127 for c in f):
        print(f)
        if len([x for x in os.listdir(source_dir) if any(ord(c) > 127 for c in x)]) > 20:
            print("... (too many to list)")
            break
