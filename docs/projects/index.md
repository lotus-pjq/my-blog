---
title: Projects
---

<div class="projects-page-custom">
  <div class="page-header-custom">
    <div class="section-kicker-custom">Portfolio</div>
    <h1>项目与研究</h1>
    <p class="page-desc-custom">展示我的研究项目、开源贡献和个人作品。</p>
  </div>

  <div class="projects-grid-custom">
    <article class="project-card-large-custom">
      <div class="project-badge-custom featured-custom">Featured</div>
      <h2>Battery SOC Research</h2>
      <p>连续时间 SOC 建模与温度修正实验整理。基于二阶 RC 等效电路模型和 KiBaM 模型，结合温度效应进行参数拟合和实验验证。</p>
      <div class="project-highlights-custom">
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">研究方向</div>
          <div class="highlight-value-custom">锂电池建模</div>
        </div>
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">应用场景</div>
          <div class="highlight-value-custom">智能手机电池管理</div>
        </div>
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">状态</div>
          <div class="highlight-value-custom">进行中</div>
        </div>
      </div>
      <div class="project-stack-custom">Python / NumPy / SciPy / Matplotlib / Modeling</div>
      <div class="project-links-custom">
        <a href="#" class="project-link-custom">查看详情 →</a>
        <a href="#" class="project-link-custom">研究笔记 →</a>
      </div>
    </article>

    <article class="project-card-large-custom">
      <div class="project-badge-custom featured-custom">Featured</div>
      <h2>Competitive Programming Notes</h2>
      <p>算法题解、构造思路与数据生成经验总结。整理了图论、动态规划、数据结构等常见算法的解题模板和思维方法。</p>
      <div class="project-highlights-custom">
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">内容类型</div>
          <div class="highlight-value-custom">题解 + 模板</div>
        </div>
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">覆盖范围</div>
          <div class="highlight-value-custom">图论 / DP / 数据结构</div>
        </div>
        <div class="highlight-item-custom">
          <div class="highlight-label-custom">更新频率</div>
          <div class="highlight-value-custom">持续更新</div>
        </div>
      </div>
      <div class="project-stack-custom">C++ / Algorithm / Data Structure / Problem Solving</div>
      <div class="project-links-custom">
        <a href="#" class="project-link-custom">查看题解 →</a>
        <a href="https://github.com/yourusername/cp-notes" class="project-link-custom">GitHub →</a>
      </div>
    </article>

    <article class="project-card-custom">
      <h3>Creative Blog Design</h3>
      <p>带有轻二次元气质的个人博客视觉探索。使用 VitePress 构建，注重视觉美感和用户体验。</p>
      <div class="project-stack-custom">VitePress / Vue / CSS / Design</div>
      <div class="project-links-custom">
        <a href="/" class="project-link-custom">在线预览 →</a>
      </div>
    </article>

    <article class="project-card-custom">
      <h3>Algorithm Visualizer</h3>
      <p>算法可视化工具，帮助理解常见算法的执行过程。支持排序、搜索、图论等多种算法的动态演示。</p>
      <div class="project-stack-custom">JavaScript / Canvas / Animation</div>
      <div class="project-links-custom">
        <a href="#" class="project-link-custom">查看演示 →</a>
      </div>
    </article>

    <article class="project-card-custom">
      <h3>Data Structure Library</h3>
      <p>常用数据结构的 C++ 实现库，包含线段树、树状数组、并查集等竞赛常用数据结构。</p>
      <div class="project-stack-custom">C++ / Template / STL</div>
      <div class="project-links-custom">
        <a href="#" class="project-link-custom">GitHub →</a>
      </div>
    </article>

    <article class="project-card-custom">
      <h3>Math Modeling Toolkit</h3>
      <p>数学建模工具集，包含常用的数据处理、可视化和模型评估工具。</p>
      <div class="project-stack-custom">Python / Pandas / Scikit-learn</div>
      <div class="project-links-custom">
        <a href="#" class="project-link-custom">文档 →</a>
      </div>
    </article>
  </div>
</div>

<style>
.projects-page-custom {
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

.projects-grid-custom {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.project-card-large-custom {
  grid-column: span 2;
  border-radius: 28px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(255, 255, 255, 0.92);
  padding: 32px;
  box-shadow: 0 12px 40px rgba(148, 163, 184, 0.09);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  backdrop-filter: blur(16px);
  position: relative;
}

.project-card-custom {
  border-radius: 24px;
  border: 1px solid rgba(148, 163, 184, 0.22);
  background: rgba(255, 255, 255, 0.92);
  padding: 24px;
  box-shadow: 0 12px 40px rgba(148, 163, 184, 0.09);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
  backdrop-filter: blur(16px);
}

.project-card-large-custom:hover,
.project-card-custom:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 50px rgba(148, 163, 184, 0.16);
}

.project-badge-custom {
  display: inline-flex;
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 16px;
}

.featured-custom {
  background: linear-gradient(135deg, #dbeafe, #fce7f3);
  color: #075985;
}

.project-card-large-custom h2 {
  margin: 0;
  font-size: 1.8rem;
  color: #1e293b;
  line-height: 1.3;
}

.project-card-custom h3 {
  margin: 0;
  font-size: 1.25rem;
  color: #1e293b;
  line-height: 1.3;
}

.project-card-large-custom p,
.project-card-custom p {
  margin: 14px 0 0;
  color: #475569;
  line-height: 1.8;
  font-size: 1rem;
}

.project-highlights-custom {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin: 24px 0;
}

.highlight-item-custom {
  padding: 16px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.92);
}

.highlight-label-custom {
  font-size: 0.75rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 6px;
}

.highlight-value-custom {
  font-size: 0.95rem;
  color: #1e293b;
  font-weight: 600;
}

.project-stack-custom {
  display: inline-flex;
  margin-top: 18px;
  padding: 8px 14px;
  border-radius: 999px;
  border: 1px solid rgba(226, 232, 240, 0.92);
  background: #f8fafc;
  color: #475569;
  font-size: 0.82rem;
}

.project-links-custom {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 20px;
}

.project-link-custom {
  color: #0369a1 !important;
  font-size: 0.95rem;
  font-weight: 600;
  text-decoration: none;
  transition: transform 0.18s ease;
}

.project-link-custom:hover {
  transform: translateX(4px);
}

.section-kicker-custom {
  font-size: 0.9rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@media (max-width: 1024px) {
  .projects-grid-custom {
    grid-template-columns: 1fr;
  }

  .project-card-large-custom {
    grid-column: span 1;
  }

  .project-highlights-custom {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .project-card-large-custom {
    padding: 24px;
  }

  .project-card-large-custom h2 {
    font-size: 1.5rem;
  }
}
</style>
