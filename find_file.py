import os

TARGET_DIR = r"d:\Logseq\BLOG_github\docs\blog\algorithm"

for filename in os.listdir(TARGET_DIR):
    if '网络' in filename or '选拔' in filename or '模板' in filename:
        print(filename)

