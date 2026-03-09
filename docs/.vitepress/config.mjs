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
      '/blog/': [
        {
          text: '博客文章',
          items: [
            { text: '所有文章', link: '/blog/' },
          ]
        }
      ],
      '/projects/': [
        {
          text: '项目展示',
          items: [
            { text: '所有项目', link: '/projects/' },
          ]
        }
      ],
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

