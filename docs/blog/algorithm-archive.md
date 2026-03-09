---
title: 算法笔记归档
---

<script setup>
import { ref, computed } from 'vue'

const selectedCategory = ref('全部')
const selectedTag = ref('全部')

const categories = ['全部', '数据结构', '图论', '数论', '数学', '动态规划', '字符串', '计算几何', '博弈论', '题解']

const articles = [
  // 博弈论
  { title: '博弈论完全指南：从必胜必败到SG函数', link: './game-theory-guide', category: '博弈论', tags: ['博弈论', 'SG函数', 'Nim游戏'], date: '2026-03-09' },
  { title: 'Multi-SG游戏详解', link: './multi-sg', category: '博弈论', tags: ['博弈论', 'SG函数'], date: '2026-03-09' },
  { title: 'Every-SG游戏详解', link: './every-sg', category: '博弈论', tags: ['博弈论', 'SG函数'], date: '2026-03-09' },
  { title: 'Anti-SG游戏与SJ定理', link: './anti-sg游戏与sj定理', category: '博弈论', tags: ['博弈论', 'SG函数'], date: '2026-03-09' },
  { title: '威佐夫博弈', link: './威佐夫博弈', category: '博弈论', tags: ['博弈论'], date: '2026-03-09' },
  { title: '斐波那契博弈', link: './斐波那契博弈fibonacci-nim', category: '博弈论', tags: ['博弈论'], date: '2026-03-09' },
  
  // 线性基
  { title: '线性基完全指南：从高斯消元到贪心构造', link: './linear-basis-guide', category: '数学', tags: ['线性基', '高斯消元', '异或'], date: '2026-03-09' },
  
  // 树链剖分
  { title: '树链剖分完全指南：从理论到实战', link: './heavy-light-decomposition', category: '图论', tags: ['树链剖分', '图论', '线段树'], date: '2026-03-09' },
  
  // 数据结构
  { title: '树状数组与逆序对', link: './树状数组逆序对', category: '数据结构', tags: ['树状数组', '数据结构'], date: '2026-03-09' },
  { title: 'Splay树详解', link: './splay树', category: '数据结构', tags: ['Splay', '平衡树'], date: '2026-03-09' },
  { title: '字典树Trie详解', link: './字典树trie', category: '数据结构', tags: ['字典树', 'Trie'], date: '2026-03-09' },
  { title: '01Trie详解', link: './01trie', category: '数据结构', tags: ['字典树', 'Trie'], date: '2026-03-09' },
  { title: '莫队算法详解', link: './莫队算法', category: '数据结构', tags: ['莫队', '分块'], date: '2026-03-09' },
  { title: '线段树进阶训练', link: './线段树进阶训练', category: '数据结构', tags: ['线段树'], date: '2026-03-09' },
  { title: '动态开点线段树', link: './动态开点线段树', category: '数据结构', tags: ['线段树'], date: '2026-03-09' },
  { title: '分块算法', link: './分块算法', category: '数据结构', tags: ['分块'], date: '2026-03-09' },
  { title: '单调队列', link: './单调队列', category: '数据结构', tags: ['单调队列'], date: '2026-03-09' },
  { title: '笛卡尔树', link: './笛卡尔树', category: '数据结构', tags: ['笛卡尔树'], date: '2026-03-09' },
  
  // 图论
  { title: 'LCA最近公共祖先', link: './lca', category: '图论', tags: ['LCA', '图论', '倍增'], date: '2026-03-09' },
  { title: '树形DP详解', link: './树形dp', category: '图论', tags: ['树形DP', 'DP'], date: '2026-03-09' },
  { title: '树上启发式合并DSU on Tree', link: './树上启发式合并dsu-on-tree', category: '图论', tags: ['DSU on Tree', '图论'], date: '2026-03-09' },
  { title: '树的重心', link: './树的重心', category: '图论', tags: ['树'], date: '2026-03-09' },
  { title: '树的直径', link: './树的直径', category: '图论', tags: ['树'], date: '2026-03-09' },
  { title: '树的中心', link: './树的中心', category: '图论', tags: ['树'], date: '2026-03-09' },
  { title: '树上前缀和', link: './树上前缀和', category: '图论', tags: ['树'], date: '2026-03-09' },
  
  // 数论
  { title: '筛法板子', link: './筛法板子', category: '数论', tags: ['筛法', '素数'], date: '2026-03-09' },
  { title: '扩展欧几里得算法', link: './扩展欧几里得算法', category: '数论', tags: ['扩欧', '数论'], date: '2026-03-09' },
  { title: '欧拉函数与莫比乌斯函数', link: './欧拉函数莫比乌斯函数预处理', category: '数论', tags: ['欧拉函数', '莫比乌斯'], date: '2026-03-09' },
  { title: '原根详解', link: './原根', category: '数论', tags: ['原根', '数论'], date: '2026-03-09' },
  { title: 'BSGS算法', link: './bsgs算法', category: '数论', tags: ['BSGS', '离散对数'], date: '2026-03-09' },
  { title: '卢卡斯定理', link: './卢卡斯定理', category: '数论', tags: ['卢卡斯', '组合数'], date: '2026-03-09' },
  { title: 'Pollard-rho大数质因数分解', link: './pollard-rho大数质因数分解', category: '数论', tags: ['Pollard-rho', '质因数分解'], date: '2026-03-09' },
  { title: 'Min_25筛', link: './min_25筛', category: '数论', tags: ['Min_25筛', '筛法'], date: '2026-03-09' },
  { title: '类欧几里得算法', link: './类欧几里得算法学习', category: '数论', tags: ['类欧几里得'], date: '2026-03-09' },
  { title: '第二类斯特林数', link: './第二类斯特林数', category: '数论', tags: ['斯特林数', '组合数学'], date: '2026-03-09' },
  
  // 数学
  { title: 'FFT快速傅里叶变换', link: './fft', category: '数学', tags: ['FFT', '多项式'], date: '2026-03-09' },
  { title: 'NTT数论变换', link: './ntt', category: '数学', tags: ['NTT', '多项式'], date: '2026-03-09' },
  { title: '高斯消元板子', link: './高斯消元板子', category: '数学', tags: ['高斯消元'], date: '2026-03-09' },
  { title: '多项式乘法逆元', link: './多项式乘法逆元模板', category: '数学', tags: ['多项式'], date: '2026-03-09' },
  { title: '模意义下逆矩阵', link: './模意义下逆矩阵', category: '数学', tags: ['矩阵'], date: '2026-03-09' },
  
  // 动态规划
  { title: '背包专题', link: './背包专题', category: '动态规划', tags: ['背包', 'DP'], date: '2026-03-09' },
  { title: '数位DP', link: './数位dp', category: '动态规划', tags: ['数位DP'], date: '2026-03-09' },
  { title: '状压DP', link: './状压dp', category: '动态规划', tags: ['状压DP'], date: '2026-03-09' },
  { title: '最长上升子序列LIS', link: './最长上升子序列lis', category: '动态规划', tags: ['LIS', 'DP'], date: '2026-03-09' },
  { title: '最长公共子序列LCS', link: './最长公共子序列lcs', category: '动态规划', tags: ['LCS', 'DP'], date: '2026-03-09' },
  
  // 字符串
  { title: 'Hash板子', link: './hash板子', category: '字符串', tags: ['哈希', '字符串'], date: '2026-03-09' },
  { title: '双哈希模板', link: './xde的双哈希模板', category: '字符串', tags: ['哈希', '字符串'], date: '2026-03-09' },
  { title: '最小表示法', link: './最小表示法', category: '字符串', tags: ['最小表示法'], date: '2026-03-09' },
  
  // 计算几何
  { title: '计算几何模板整理', link: './计算几何模板整理', category: '计算几何', tags: ['计算几何'], date: '2026-03-09' },
  { title: '平面坐标系旋转', link: './平面直角系坐标系旋转点绕坐标系旋转a点绕b点旋转', category: '计算几何', tags: ['计算几何', '坐标变换'], date: '2026-03-09' },
  { title: '曼哈顿距离与切比雪夫距离转换', link: './曼哈顿距离和切比雪夫距离的转换', category: '计算几何', tags: ['计算几何', '距离'], date: '2026-03-09' },
]

const filteredArticles = computed(() => {
  return articles.filter(article => {
    const categoryMatch = selectedCategory.value === '全部' || article.category === selectedCategory.value
    const tagMatch = selectedTag.value === '全部' || article.tags.includes(selectedTag.value)
    return categoryMatch && tagMatch
  })
})

const allTags = computed(() => {
  const tags = new Set(['全部'])
  articles.forEach(article => {
    article.tags.forEach(tag => tags.add(tag))
  })
  return Array.from(tags)
})
</script>

<style scoped>
.algorithm-archive {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.filter-section {
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.filter-group {
  margin-bottom: 1rem;
}

.filter-group:last-child {
  margin-bottom: 0;
}

.filter-label {
  font-weight: 600;
  margin-bottom: 0.5rem;
  color: var(--vp-c-text-1);
}

.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.filter-btn {
  padding: 0.4rem 1rem;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg);
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.9rem;
}

.filter-btn:hover {
  border-color: var(--vp-c-brand);
  color: var(--vp-c-brand);
}

.filter-btn.active {
  background: var(--vp-c-brand);
  color: white;
  border-color: var(--vp-c-brand);
}

.stats {
  text-align: center;
  margin: 2rem 0;
  padding: 1rem;
  background: var(--vp-c-bg-soft);
  border-radius: 8px;
}

.stats-number {
  font-size: 2rem;
  font-weight: bold;
  color: var(--vp-c-brand);
}

.stats-label {
  color: var(--vp-c-text-2);
  margin-top: 0.5rem;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.article-card {
  padding: 1.5rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  transition: all 0.3s;
  background: var(--vp-c-bg);
}

.article-card:hover {
  border-color: var(--vp-c-brand);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.article-category {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand);
  border-radius: 4px;
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
}

.article-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0.5rem 0;
}

.article-title a {
  color: var(--vp-c-text-1);
  text-decoration: none;
}

.article-title a:hover {
  color: var(--vp-c-brand);
}

.article-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  margin-top: 0.5rem;
}

.article-tag {
  padding: 0.2rem 0.5rem;
  background: var(--vp-c-bg-soft);
  border-radius: 3px;
  font-size: 0.75rem;
  color: var(--vp-c-text-2);
}

.article-date {
  margin-top: 0.5rem;
  font-size: 0.85rem;
  color: var(--vp-c-text-3);
}

.no-results {
  text-align: center;
  padding: 3rem;
  color: var(--vp-c-text-2);
}
</style>

<div class="algorithm-archive">
  <h1>算法笔记归档</h1>
  <p class="lead">共收录 {{ articles.length }} 篇算法笔记，涵盖数据结构、图论、数论、数学、动态规划等多个领域</p>

  <div class="filter-section">
    <div class="filter-group">
      <div class="filter-label">📂 按分类筛选</div>
      <div class="filter-buttons">
        <button 
          v-for="cat in categories" 
          :key="cat"
          :class="['filter-btn', { active: selectedCategory === cat }]"
          @click="selectedCategory = cat; selectedTag = '全部'"
        >
          {{ cat }}
        </button>
      </div>
    </div>

    <div class="filter-group">
      <div class="filter-label">🏷️ 按标签筛选</div>
      <div class="filter-buttons">
        <button 
          v-for="tag in allTags" 
          :key="tag"
          :class="['filter-btn', { active: selectedTag === tag }]"
          @click="selectedTag = tag"
        >
          {{ tag }}
        </button>
      </div>
    </div>
  </div>

  <div class="stats">
    <div class="stats-number">{{ filteredArticles.length }}</div>
    <div class="stats-label">
      {{ selectedCategory === '全部' && selectedTag === '全部' ? '全部文章' : '筛选结果' }}
    </div>
  </div>

  <div v-if="filteredArticles.length > 0" class="articles-grid">
    <div v-for="article in filteredArticles" :key="article.link" class="article-card">
      <span class="article-category">{{ article.category }}</span>
      <h3 class="article-title">
        <a :href="article.link">{{ article.title }}</a>
      </h3>
      <div class="article-tags">
        <span v-for="tag in article.tags" :key="tag" class="article-tag">{{ tag }}</span>
      </div>
      <div class="article-date">{{ article.date }}</div>
    </div>
  </div>

  <div v-else class="no-results">
    <p>😕 没有找到符合条件的文章</p>
    <p>试试调整筛选条件</p>
  </div>
</div>

