<template>
  <div class="page-shell">
    <section class="page-panel page-intro">
      <div class="page-kicker">Blog</div>
      <h1 class="page-heading">文章归档</h1>
      <p class="page-lead">技术博客、算法笔记与项目记录</p>
      <div style="margin-top: 1.5rem;">
        <a href="./algorithm-archive" class="cta-button">
          📚 浏览全部算法笔记 (145篇)
        </a>
      </div>
    </section>

    <section class="page-grid">
      <article class="page-card page-card--featured">
        <div class="page-kicker">Featured</div>
        <h3><a href="./algorithm-archive">算法笔记归档</a></h3>
        <p>145篇算法竞赛笔记，涵盖数据结构、图论、数论、数学、动态规划等领域。支持分类和标签筛选。</p>
        <div class="tag-row">
          <span>数据结构 15篇</span>
          <span>数论 22篇</span>
          <span>图论 10篇</span>
          <span>题解 46篇</span>
        </div>
      </article>

      <article v-for="article in featuredArticles" :key="article.link" class="page-card">
        <div class="post-meta">
          <span>{{ article.category }}</span>
          <span>{{ article.date }}</span>
          <span>{{ article.tag }}</span>
        </div>
        <h3><a :href="article.link">{{ article.title }}</a></h3>
        <p>{{ article.description }}</p>
      </article>

      <article class="page-card page-card--wide">
        <div class="page-kicker">Stats</div>
        <h3>内容统计</h3>
        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-number">145</div>
            <div class="stat-label">算法笔记</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">9</div>
            <div class="stat-label">算法分类</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">46</div>
            <div class="stat-label">题解</div>
          </div>
        </div>
        <p class="muted-note">所有笔记均来自ACM竞赛学习过程，持续整理更新中。</p>
      </article>
    </section>
  </div>
</template>

<script setup>
import { withBase } from 'vitepress'

const featuredArticles = [
  {
    title: '博弈论完全指南：从必胜必败到SG函数',
    link: withBase('/blog/algorithm/博弈论.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '算法模板',
    description: '系统总结博弈论中的必胜必败分析、SG函数理论及常见博弈模型，包含完整的代码模板和经典例题。'
  },
  {
    title: '线性基完全指南：从高斯消元到贪心构造',
    link: withBase('/blog/algorithm/线性基.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '算法模板',
    description: '详解线性基的多种构造方法、性质分析及经典应用，包含高斯消元、贪心法、前缀线性基等完整模板。'
  },
  {
    title: '树链剖分完全指南：从理论到实战',
    link: withBase('/blog/algorithm/树链剖分.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '算法模板',
    description: '详解树链剖分的原理、实现和应用，包含完整的代码模板和复杂度证明。'
  },
  {
    title: '莫队算法详解',
    link: withBase('/blog/algorithm/莫队算法.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '数据结构',
    description: '离线处理区间查询问题的经典算法，包含普通莫队、带修莫队等多种变体。'
  },
  {
    title: 'LCA最近公共祖先',
    link: withBase('/blog/algorithm/LCA.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '图论',
    description: '树上查询两节点最近公共祖先的多种算法实现，包含倍增、Tarjan等方法。'
  },
  {
    title: 'FFT快速傅里叶变换',
    link: withBase('/blog/algorithm/FFT.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '数学',
    description: '多项式乘法的高效算法，O(nlogn)时间复杂度，包含完整实现和应用场景。'
  },
  {
    title: '背包专题',
    link: withBase('/blog/algorithm/背包专题.html'),
    category: 'Algorithm',
    date: '2026-03-09',
    tag: '动态规划',
    description: '01背包、完全背包、多重背包等经典DP问题的系统总结和优化技巧。'
  }
]
</script>

<style scoped>
.cta-button {
  display: inline-block;
  padding: 0.8rem 1.5rem;
  background: var(--vp-c-brand);
  color: white;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.cta-button:hover {
  background: var(--vp-c-brand-dark);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.tag-row span {
  padding: 0.3rem 0.6rem;
  background: var(--vp-c-bg-soft);
  border-radius: 4px;
  font-size: 0.85rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.stat-item {
  text-align: center;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 6px;
}

.stat-number {
  font-size: 2rem;
  font-weight: bold;
  color: var(--vp-c-brand);
}

.stat-label {
  color: var(--vp-c-text-2);
  margin-top: 0.5rem;
}

.muted-note {
  margin-top: 1rem;
  color: var(--vp-c-text-2);
  font-size: 0.94rem;
}
</style>

