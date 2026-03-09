import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Junlong.dev",
  description: "个人博客 · 作品集 · 笔记",
  lang: 'zh-CN',
  base: '/my-blog/',
  
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#7BA3D1' }],
  ],

  themeConfig: {
    nav: [
      { text: '关于', link: '/#about' },
      { text: '博客', link: '/blog/' },
      { text: '项目', link: '/projects/' },
      { text: '联系', link: '/#contact' },
    ],

    sidebar: {
      '/blog/algorithm/': [
        {
          text: '📚 算法笔记',
          items: [
            { text: '← 返回博客首页', link: '/blog/' },
            { text: '📑 算法归档', link: '/blog/algorithm-archive' },
          ]
        },
        {
          text: '🎮 博弈论',
          collapsed: false,
          items: [
            { text: '博弈论总结', link: '/blog/algorithm/博弈论' },
            { text: 'Multi-SG游戏', link: '/blog/algorithm/Multi-SG' },
            { text: 'Every-SG游戏', link: '/blog/algorithm/Every-SG' },
            { text: 'Anti-SG与SJ定理', link: '/blog/algorithm/Anti-SG游戏与SJ定理' },
          ]
        },
        {
          text: '📊 数据结构',
          collapsed: true,
          items: [
            { text: '莫队算法', link: '/blog/algorithm/莫队算法' },
            { text: 'Splay树', link: '/blog/algorithm/Splay树' },
            { text: '线段树进阶', link: '/blog/algorithm/线段树进阶训练' },
          ]
        },
        {
          text: '🌲 图论',
          collapsed: true,
          items: [
            { text: 'LCA', link: '/blog/algorithm/LCA' },
            { text: '树链剖分', link: '/blog/algorithm/树链剖分' },
            { text: '树形DP', link: '/blog/algorithm/树形DP' },
          ]
        },
        {
          text: '🔢 数论',
          collapsed: true,
          items: [
            { text: 'BSGS算法', link: '/blog/algorithm/BSGS算法' },
            { text: '原根', link: '/blog/algorithm/原根' },
          ]
        },
        {
          text: '📐 数学',
          collapsed: true,
          items: [
            { text: 'FFT', link: '/blog/algorithm/FFT' },
            { text: 'NTT', link: '/blog/algorithm/NTT' },
            { text: '线性基', link: '/blog/algorithm/线性基' },
          ]
        },
        {
          text: '💡 动态规划',
          collapsed: true,
          items: [
            { text: '背包专题', link: '/blog/algorithm/背包专题' },
            { text: '数位DP', link: '/blog/algorithm/数位DP' },
            { text: '状压DP', link: '/blog/algorithm/状压DP' },
          ]
        },
      ],
      '/blog/': [
        {
          text: '博客文章',
          items: [
            { text: '所有文章', link: '/blog/' },
            { text: '算法归档', link: '/blog/algorithm-archive' },
          ]
        }
      ],
    },

    outline: {
      level: [2, 3],
      label: '目录'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/lotus-pjq' },
    ],

    footer: {
      message: '基于 VitePress 构建，持续整理算法、建模与项目记录',
      copyright: 'Copyright © 2024-present'
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索',
            buttonAriaLabel: '搜索'
          },
          modal: {
            noResultsText: '无法找到相关结果',
            resetButtonTitle: '清除查询条件',
            footer: {
              selectText: '选择',
              navigateText: '切换'
            }
          }
        }
      }
    },

    docFooter: {
      prev: '上一篇',
      next: '下一篇'
    },

    lastUpdated: {
      text: '最后更新'
    }
  },

  markdown: {
    lineNumbers: true,
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  },
})
