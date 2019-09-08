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
import EmployeesChart from '@/components/chart/EmployeesChart'
import AverageAgeChart from '@/components/chart/AverageAgeChart'
import ServiceYearsChart from '@/components/chart/ServiceYearsChart'
import IncomeChart from '@/components/chart/IncomeChart'
import SalesChart from '@/components/chart/SalesChart'
import OrdinaryIncomeChart from '@/components/chart/OrdinaryIncomeChart'
import NetIncomeChart from '@/components/chart/NetIncomeChart'

Vue.use(Router)

import 'bootstrap/dist/css/bootstrap.css' // added
import 'bootstrap-vue/dist/bootstrap-vue.css' // added

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Root',
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
          component: Chart,
          children: [
            {
              path: '',
              name: 'Chart',
              components: {
                'EmployeesChart': EmployeesChart,
                'AverageAgeChart': AverageAgeChart,
                'ServiceYearsChart': ServiceYearsChart,
                'IncomeChart': IncomeChart,
                'SalesChart': SalesChart,
                'OrdinaryIncomeChart': OrdinaryIncomeChart,
                'NetIncomeChart': NetIncomeChart
              }
            }
          ]
        }
      ]
    }
  ]
})
