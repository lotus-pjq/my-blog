import DefaultTheme from 'vitepress/theme'
import './style.css'
import BlogIndex from './components/BlogIndex.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('BlogIndex', BlogIndex)
  }
}
