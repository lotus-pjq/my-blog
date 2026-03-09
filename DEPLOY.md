# 部署到 GitHub 的命令

# 1. 初始化 Git 仓库
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "Initial commit: Personal blog with VitePress"

# 4. 设置主分支
git branch -M main

# 5. 添加远程仓库
git remote add origin https://github.com/lotus-pjq/my-blog.git

# 6. 推送到 GitHub
git push -u origin main

# 完成后：
# 1. 访问 https://github.com/lotus-pjq/my-blog
# 2. 点击 Settings → Pages
# 3. Source 选择 "GitHub Actions"
# 4. 等待 1-2 分钟
# 5. 访问 https://lotus-pjq.github.io/my-blog/

