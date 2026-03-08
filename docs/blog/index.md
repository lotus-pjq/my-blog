---
title: Blog
---

<div class="blog-page-custom">
  <div class="page-header-custom">
    <div class="section-kicker-custom">Blog</div>
    <h1>文章归档</h1>
    <p class="page-desc-custom">记录算法竞赛、数学建模、技术研究与个人思考。</p>
  </div>

  <div class="posts-list-custom">
    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Algorithm</span>
        <span>2026-03-01</span>
      </div>
      <div class="post-meta-custom">
        <span>题解方法</span>
        <span>8 min</span>
      </div>
      <h3>算法竞赛中的结构化思维</h3>
      <p>从笛卡尔树到状态搜索，记录我在竞赛题中如何把直觉整理成可复用的方法。深入探讨数据结构的选择、状态转移的设计，以及如何在比赛中快速定位解题思路。</p>
      <a href="/blog/algorithm-structured-thinking" class="post-readmore-custom">继续阅读 →</a>
    </article>

    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Modeling</span>
        <span>2026-02-24</span>
      </div>
      <div class="post-meta-custom">
        <span>研究笔记</span>
        <span>11 min</span>
      </div>
      <h3>连续时间电池 SOC 建模笔记</h3>
      <p>整理二阶 RC、KiBaM 与温度修正项如何组合成一个可落地的智能手机电池模型。包含参数拟合方法、实验数据处理和模型验证流程。</p>
      <a href="/blog/battery-soc-modeling" class="post-readmore-custom">继续阅读 →</a>
    </article>

    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Design</span>
        <span>2026-02-17</span>
      </div>
      <div class="post-meta-custom">
        <span>设计记录</span>
        <span>6 min</span>
      </div>
      <h3>把个人博客做得更像作品集</h3>
      <p>在不过度花哨的前提下，让技术博客也能保留一点轻二次元与个人表达。探讨如何在保持专业性的同时，为博客注入个人风格和视觉美感。</p>
      <a href="/blog/blog-as-portfolio" class="post-readmore-custom">继续阅读 →</a>
    </article>

    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Tutorial</span>
        <span>2026-02-10</span>
      </div>
      <div class="post-meta-custom">
        <span>技术教程</span>
        <span>12 min</span>
      </div>
      <h3>使用 VitePress 搭建静态博客</h3>
      <p>从零开始搭建一个现代化的静态博客，包括主题定制、内容管理、SEO 优化和自动部署。适合想要拥有自己博客的开发者。</p>
      <a href="/blog/vitepress-blog-guide" class="post-readmore-custom">继续阅读 →</a>
    </article>

    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Algorithm</span>
        <span>2026-02-03</span>
      </div>
      <div class="post-meta-custom">
        <span>数据结构</span>
        <span>15 min</span>
      </div>
      <h3>图论算法精选题解</h3>
      <p>整理常见图论算法的应用场景和实现技巧，包括最短路、最小生成树、网络流等经典问题的解题思路和代码实现。</p>
      <a href="/blog/graph-algorithms" class="post-readmore-custom">继续阅读 →</a>
    </article>

    <article class="post-card-custom">
      <div class="post-topline-custom">
        <span>Thoughts</span>
        <span>2026-01-27</span>
      </div>
      <div class="post-meta-custom">
        <span>个人思考</span>
        <span>5 min</span>
      </div>
      <h3>关于学习方法的一些思考</h3>
      <p>分享我在算法学习和项目实践中总结的一些方法论，包括如何高效学习新知识、如何系统化整理笔记、如何保持长期的学习动力。</p>
      <a href="/blog/learning-methods" class="post-readmore-custom">继续阅读 →</a>
    </article>
  </div>
</div>

<style>
.blog-page-custom {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.page-header-custom {
  margin-bottom: 3rem;
  text-align: center;
}

.page-header-custom h1 {
  margin: 10px 0 0;
  font-size: clamp(2.5rem, 4vw, 3.5rem);
  line-height: 1.2;
  color: #1e293b;
}

.page-desc-custom {
  margin: 16px auto 0;
  max-width: 600px;
  font-size: 1.1rem;
  color: #64748b;
  line-height: 1.7;
}

.posts-list-custom {
  display: grid;
  gap: 24px;
}

.post-card-custom {
  border-radius: 24px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(255, 255, 255, 0.92);
  padding: 28px;
  box-shadow: 0 12px 40px rgba(148, 163, 184, 0.09);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  backdrop-filter: blur(16px);
}

.post-card-custom:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 50px rgba(148, 163, 184, 0.16);
}

.post-topline-custom {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  font-size: 0.85rem;
  color: #64748b;
}

.post-meta-custom {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 14px;
}

.post-meta-custom span {
  display: inline-flex;
  padding: 6px 12px;
  border-radius: 999px;
  border: 1px solid rgba(255, 255, 255, 0.92);
  background: rgba(255, 255, 255, 0.64);
  color: #475569;
  font-size: 0.82rem;
}

.post-card-custom h3 {
  margin: 18px 0 0;
  font-size: 1.5rem;
  color: #1e293b;
  line-height: 1.3;
}

.post-card-custom p {
  margin: 14px 0 0;
  color: #475569;
  line-height: 1.8;
  font-size: 1rem;
}

.post-readmore-custom {
  display: inline-flex;
  margin-top: 18px;
  color: #0369a1 !important;
  font-size: 0.95rem;
  font-weight: 600;
  text-decoration: none;
  transition: transform 0.18s ease;
}

.post-readmore-custom:hover {
  transform: translateX(4px);
}

.section-kicker-custom {
  font-size: 0.9rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@media (max-width: 768px) {
  .post-card-custom {
    padding: 20px;
  }

  .post-card-custom h3 {
    font-size: 1.25rem;
  }
}
</style>
