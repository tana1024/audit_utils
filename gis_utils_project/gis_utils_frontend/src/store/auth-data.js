import api from '@/services/api'

// 認証情報
export const AuthData = {
  namespaced: true,

  state: {
    username: '',
    isLoggedIn: false
  },
  getters: {
    username: state => state.username,
    isLoggedIn: state => state.isLoggedIn
  },
  mutations: {
    set (state, payload) {
      state.username = payload.user.username
      state.isLoggedIn = true
    },
    clear (state) {
      state.username = ''
      state.isLoggedIn = false
    }
  },

  actions: {
     // ログイン
    login (context, payload) {
      return api.post('/api/auth/jwt/create/', {
        'username': payload.username,
        'password': payload.password
      })
      .then(response => {
        // 認証用トークンをlocalStorageに保存
        localStorage.setItem('access', response.data.access)
        console.log('access:', response.data.access)
        // ユーザー情報を取得してstoreのユーザー情報を更新
        return context.dispatch('reload')
          .then(user => user)
      })
    },

    // ログアウト
    logout (context) {
      // 認証用トークンをlocalStorageから削除
      localStorage.removeItem('access')
      // storeのユーザー情報をクリア
      context.commit('clear')
    },

    // ユーザー情報更新
    reload (context) {
      return api.get('/api/auth/users/me/')
        .then(response => {
          const user = response.data
          // storeのユーザー情報を更新
          context.commit('set', { user: user })
          console.log('username:', user.username)
          return user
        })
    }
  }
}
