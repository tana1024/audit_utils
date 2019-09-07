import Vue from 'vue'
import Vuex from 'vuex'

import {ChartData} from './chart-data'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  modules: {
      chartData: ChartData
  }
})
