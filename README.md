# Personal Blog

一个基于 VitePress 的现代化个人博客，采用清爽的设计风格。

## ✨ 特性

- 🎨 **清爽的设计风格** - 柔和的配色，优雅的视觉体验
- 📱 **响应式设计** - 完美适配各种设备
- ⚡ **极致性能** - 基于 VitePress，静态生成，加载速度快
- 🔍 **内置搜索** - 支持全站内容搜索
- 📝 **Markdown 优先** - 专注于内容创作
- 🚀 **自动部署** - GitHub Actions 自动构建和部署

## 📦 技术栈

- **框架**: VitePress
- **UI 框架**: Vue 3
- **部署**: GitHub Pages

## 🚀 快速开始

### 安装依赖

```bash
npm install
```

### 开发模式

```bash
npm run docs:dev
```

访问 http://localhost:5173

### 构建生产版本

```bash
npm run docs:build
```

### 预览生产版本

```bash
npm run docs:preview
```

## 📁 项目结构

```
BLOG_github/
├── docs/                    # 文档目录
│   ├── .vitepress/         # VitePress 配置
│   │   ├── config.mjs      # 站点配置
│   │   └── theme/          # 自定义主题
│   ├── blog/               # 博客文章
│   ├── projects/           # 项目展示
│   ├── public/             # 静态资源
│   └── index.md            # 首页
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 配置
├── package.json
└── README.md
```

## 📝 内容管理

### 添加博客文章

1. 在 `docs/blog/` 目录下创建新的 Markdown 文件
2. 添加 frontmatter 元数据：

```markdown
---
title: 文章标题
date: 2024-03-08
category: 分类
tags:
  - 标签1
  - 标签2
---

# 文章标题

文章内容...
```

3. 在 `docs/blog/index.md` 中添加文章卡片
4. 提交并推送到 GitHub，自动部署

### 更新首页

直接编辑 `docs/index.md` 文件即可。

### 更新项目

编辑 `docs/projects/index.md` 文件。

## 🎨 自定义配置

### 修改个人信息

在以下文件中修改：
- `docs/.vitepress/config.mjs` - 站点配置
- `docs/index.md` - 首页内容
- `docs/blog/index.md` - 博客列表
- `docs/projects/index.md` - 项目列表

### 更换背景图片

替换 `docs/public/wallpaper.jpg` 文件。

## 🚀 部署到 GitHub Pages

### 方法一：使用 username.github.io 仓库（推荐）

1. 创建名为 `username.github.io` 的仓库（username 是你的 GitHub 用户名）
2. 推送代码：

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/username.github.io.git
git push -u origin main
```

3. 在仓库 Settings → Pages，Source 选择 "GitHub Actions"
4. 访问 `https://username.github.io/`

### 方法二：使用普通仓库

1. 创建任意名称的仓库（如 `my-blog`）
2. 在 `docs/.vitepress/config.mjs` 中取消注释并设置 base：

```javascript
base: '/my-blog/', // 改成你的仓库名
```

3. 推送代码并配置 Pages
4. 访问 `https://username.github.io/my-blog/`

## 📄 License

MIT License

---

**享受写作和分享的乐趣！** ✨
