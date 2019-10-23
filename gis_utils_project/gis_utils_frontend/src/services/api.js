import axios from 'axios'
import store from '@/store/store'

const api = axios.create({
  baseURL: ((process.env.NODE_ENV === 'production')? 'https://' + window.location.host : 'https://' + process.env.PORT + '-' + window.location.hostname.slice(5)),
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
  }
})

// 共通前処理
api.interceptors.request.use(function (config) {
  // メッセージをクリア
  store.dispatch('messageData/clearMessages')
  // 認証用トークンがあればリクエストヘッダに乗せる
  const token = localStorage.getItem('access')
  if (token) {
    config.headers.Authorization = 'JWT ' + token
    return config
  }
  return config
}, function (error) {
  return Promise.reject(error)
})

// 共通エラー処理
api.interceptors.response.use(function (response) {
  return response
}, function (error) {
  console.log('error.response=', error.response)
  const status = error.response ? error.response.status : 500

  // エラーの内容に応じてstoreのメッセージを更新
  let message
  if (status === 400) {
    // バリデーションNG
    let messages = [].concat.apply([], Object.values(error.response.data))
    store.dispatch('messageData/setWarningMessages', { messages: messages })

  } else if (status === 401) {
    // 認証エラー
    const token = localStorage.getItem('access')
    if (token != null) {
      message = 'ログイン有効期限切れ'
    } else {
      message = '認証エラー'
    }
    store.dispatch('authData/logout')
    store.dispatch('messageData/setErrorMessage', { message: message })

  } else if (status === 403) {
    // 権限エラー
    message = '権限エラー'
    store.dispatch('messageData/setErrorMessage', { message: message })

  } else {
    // その他のエラー
    message = '想定外エラー'
    store.dispatch('messageData/setErrorMessage', { message: message })
  }
  return Promise.reject(error)
})

export default api
