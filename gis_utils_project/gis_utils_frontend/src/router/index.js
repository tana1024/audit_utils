import Vue from 'vue'
import BootstrapVue, { LayoutPlugin } from 'bootstrap-vue' // added
import Router from 'vue-router'
//import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import Portal from '@/components/Portal'
import Information from '@/components/Information'
import Scraping from '@/components/Scraping'
import Map from '@/components/Map'


Vue.use(Router)

import 'bootstrap/dist/css/bootstrap.css' // added
import 'bootstrap-vue/dist/bootstrap-vue.css' // added

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/portal',
      component: Portal,
      children: [
        {
          path: '',
          name: 'Information',
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
        }
      ]
    }
  ]
})
