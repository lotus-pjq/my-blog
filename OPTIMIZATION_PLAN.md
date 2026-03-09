# VitePress 博客优化方案

## 问题总结

### 1. 内容渲染问题
- ❌ Logseq 特殊语法未清理（`collapsed::`, `id::`）
- ❌ 图片路径错误
- ❌ 内部链接 `[[xxx]]` 未转换
- ❌ 缩进层级丢失
- ❌ Frontmatter 信息错误

### 2. 侧边栏问题
- ❌ 没有左侧导航栏
- ❌ 没有右侧目录大纲
- ❌ 没有面包屑导航

### 3. 页面布局问题
- ❌ 没有上下篇导航
- ❌ 没有最后更新时间

## 解决方案

### 方案1：改进批量转换脚本 ✅

**文件：** `batch_convert_improved.py`

**改进点：**
1. 更好的 Logseq 语法清理
2. 正确提取标题和分类
3. 转换内部链接为代码格式
4. 保留缩进结构
5. 添加 `outline: deep` 到 frontmatter

**使用方法：**
```bash
cd d:\Logseq\BLOG_github
python batch_convert_improved.py
```

### 方案2：优化 VitePress 配置 ✅

**文件：** `docs/.vitepress/config.mjs`

**新增配置：**

```javascript
// 1. 左侧边栏 - 按分类组织
sidebar: {
  '/blog/algorithm/': [
    {
      text: '🎮 博弈论',
      collapsed: false,
      items: [
        { text: '博弈论总结', link: '/blog/algorithm/博弈论' },
        // ...
      ]
    },
    // 其他分类...
  ]
}

// 2. 右侧大纲
outline: {
  level: [2, 3],
  label: '目录'
}

// 3. 文档页脚导航
docFooter: {
  prev: '上一篇',
  next: '下一篇'
}

// 4. 最后更新时间
lastUpdated: {
  text: '最后更新'
}
```

### 方案3：在 Markdown 文件中启用深度大纲

**在每个笔记的 frontmatter 中添加：**
```yaml
---
title: 博弈论
outline: deep  # 显示 h2, h3, h4 级别标题
---
```

### 方案4：自定义样式优化

**文件：** `docs/.vitepress/theme/style.css`

**添加：**
```css
/* 优化代码块样式 */
.vp-doc div[class*='language-'] {
  margin: 1rem 0;
  border-radius: 8px;
}

/* 优化表格样式 */
.vp-doc table {
  display: block;
  overflow-x: auto;
  margin: 1rem 0;
}

/* 优化侧边栏宽度 */
.VPSidebar {
  width: 280px;
}

/* 优化大纲宽度 */
.aside {
  width: 240px;
}
```

## 实施步骤

### 第一步：重新转换所有笔记

```bash
# 1. 清空旧文件
cd d:\Logseq\BLOG_github\docs\blog\algorithm
Remove-Item * -Force

# 2. 运行改进的转换脚本
cd d:\Logseq\BLOG_github
python batch_convert_improved.py

# 3. 修复 Vue 语法冲突
python fix_vue_syntax.py
```

### 第二步：更新配置文件

手动编辑 `docs/.vitepress/config.mjs`，添加：
- 左侧边栏配置
- 右侧大纲配置
- 文档页脚配置

### 第三步：测试构建

```bash
npm run docs:build
```

### 第四步：部署

```bash
git add .
git commit -m "Optimize blog layout and content rendering"
git push origin main
```

## 预期效果

### 左侧边栏
```
📚 算法笔记
  ← 返回博客首页
  📑 算法归档

🎮 博弈论
  博弈论总结
  Multi-SG游戏
  Every-SG游戏

📊 数据结构
  莫队算法
  Splay树
  ...
```

### 右侧大纲
```
目录
  总结做题策略
    1.必胜/必败分析
      原理
      适用条件
    2.SG函数
      使用条件
      完整分析
```

### 页面底部
```
← 上一篇: Multi-SG游戏    下一篇: 威佐夫博弈 →

最后更新: 2026-03-09
```

## 参考项目

1. **VuePress 官方文档** - 侧边栏最佳实践
2. **Vite 官方文档** - 大纲配置示例
3. **Anthony Fu 的博客** - 简洁优雅的布局

## 下一步优化

1. 添加标签云页面
2. 添加时间线视图
3. 添加评论系统
4. 添加阅读时间估算
5. 添加相关文章推荐

