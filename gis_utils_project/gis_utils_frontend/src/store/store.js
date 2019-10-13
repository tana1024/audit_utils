import Vue from 'vue'
import Vuex from 'vuex'

import {ChartData} from './chart-data'
import {AuthData} from './auth-data'
import {MessageData} from './message-data'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== 'production',
  modules: {
      chartData: ChartData,
      authData: AuthData,
      messageData: MessageData
  }
})
