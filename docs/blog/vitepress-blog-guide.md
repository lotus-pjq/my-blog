---
title: 使用 VitePress 搭建个人博客完整指南
date: 2024-03-08
category: 前端
tags:
  - VitePress
  - Vue
  - 静态站点
---

# 使用 VitePress 搭建个人博客完整指南

## 前言

在这个教程中，我将分享如何使用 VitePress 从零开始搭建一个现代化的个人博客。VitePress 是一个基于 Vite 和 Vue 3 的静态站点生成器，它提供了出色的开发体验和性能。

## 为什么选择 VitePress？

- ⚡ **极快的开发体验** - 基于 Vite，热更新几乎是即时的
- 🎨 **高度可定制** - 可以使用 Vue 组件自定义主题
- 📝 **Markdown 优先** - 专注于内容创作
- 🔍 **内置搜索** - 无需额外配置
- 🚀 **优秀的性能** - 生成的静态页面加载速度快

## 项目初始化

首先，创建一个新的项目目录并初始化：

```bash
mkdir my-blog
cd my-blog
npm init -y
npm install -D vitepress vue
```

## 目录结构

推荐的目录结构如下：

```
my-blog/
├── docs/
│   ├── .vitepress/
│   │   ├── config.js
│   │   └── theme/
│   │       ├── index.js
│   │       ├── Layout.vue
│   │       └── style.css
│   ├── blog/
│   │   └── index.md
│   ├── projects/
│   └── index.md
├── package.json
└── README.md
```

## 配置 VitePress

在 `docs/.vitepress/config.js` 中配置站点信息：

```javascript
import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "我的博客",
  description: "个人技术博客",
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '博客', link: '/blog/' },
    ],
  }
})
```

## 自定义主题

VitePress 允许你完全自定义主题。创建 `docs/.vitepress/theme/index.js`：

```javascript
import DefaultTheme from 'vitepress/theme'
import './style.css'

export default {
  extends: DefaultTheme,
}
```

## 添加 Tailwind CSS

安装 Tailwind CSS：

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

配置 `tailwind.config.js`：

```javascript
export default {
  content: [
    "./docs/.vitepress/**/*.{js,ts,vue}",
    "./docs/**/*.md",
  ],
  theme: {
    extend: {},
  },
}
```

## 部署到 GitHub Pages

创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      - run: npm ci
      - run: npm run docs:build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: docs/.vitepress/dist
```

## 写作流程

1. 在 `docs/blog/` 目录下创建新的 Markdown 文件
2. 添加 frontmatter 元数据
3. 编写内容
4. 提交到 Git
5. 自动部署

## 总结

VitePress 是一个强大而灵活的静态站点生成器，非常适合搭建个人博客。它结合了 Vue 的强大功能和 Markdown 的简洁性，让你可以专注于内容创作。

## 参考资源

- [VitePress 官方文档](https://vitepress.dev/)
- [Vue 3 文档](https://vuejs.org/)
- [Tailwind CSS 文档](https://tailwindcss.com/)

