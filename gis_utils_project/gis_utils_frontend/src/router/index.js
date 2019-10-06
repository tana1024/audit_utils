import Vue from 'vue'
import BootstrapVue, { LayoutPlugin } from 'bootstrap-vue' // added
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Portal from '@/components/Portal'
import Information from '@/components/Information'
import Scraping from '@/components/Scraping'
import Map from '@/components/Map'
import Chart from '@/components/Chart'
import store from '@/store/store'

Vue.use(Router)
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css' // added
import 'bootstrap-vue/dist/bootstrap-vue.css' // added

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Root',
      component: Login
    },
    {
      path: '/login',
      name: 'Login',
      meta: { requiresAuth: true },
      component: Login
    },
    {
      path: '/portal',
      component: Portal,
      children: [
        {
          path: '',
          name: 'Portal',
          component: Information
        },
        {
          path: 'information',
          name: 'Information',
          component: Information
        },
        {
          path: 'scraping',
          name: 'Scraping',
          component: Scraping
        },
        {
          path: 'map',
          name: 'Map',
          component: Map
        },
        {
          path: 'chart',
          name: 'Chart',
          component: Chart
        }
      ]
    }
  ]
})

/**
 * Routerによって画面遷移する際に毎回実行される
 */
router.beforeEach((to, from, next) => {

  const isLoggedIn = store.getters['authData/isLoggedIn']
  const token = localStorage.getItem('access')
  console.log('to.path=', to.path)
  console.log('isLoggedIn=', isLoggedIn)

  // ログインが必要な画面に遷移しようとした場合
  if (to.matched.some(record => record.meta.requiresAuth)) {

    // ログインしている状態の場合
    if (isLoggedIn) {
      console.log('User is already logged in. So, free to next.')
      next()

      // ログインしていない状態の場合
    } else {
      // まだ認証用トークンが残っていればユーザー情報を再取得
      if (token != null) {
        console.log('User is not logged in. Trying to reload again.')

        store.dispatch('auth/reload')
          .then(() => {
            // 再取得できたらそのまま次へ
            console.log('Succeeded to reload. So, free to next.')
            next()
          })
          .catch(() => {
            // 再取得できなければログイン画面へ
            forceToLoginPage(to, from, next)
          })
      } else {
        // 認証用トークンが無い場合は、ログイン画面へ
        forceToLoginPage(to, from, next)
      }
    }
  } else {
    // ログインが不要な画面であればそのまま次へ
    console.log('Go to public page.')
    next()
  }
})

/**
 * ログイン画面へ強制送還
 */
function forceToLoginPage (to, from, next) {
  console.log('Force user to login page.')
  next({
    path: '/login',
    // 遷移先のURLはクエリ文字列として付加
    query: { next: to.fullPath }
  })
}

export default router
