// グローバルメッセージ
export const MessageData = {
  namespaced: true,
  state: {
    error: '',
    warnings: [],
    info: ''
  },
  getters: {
    error: state => state.error,
    warnings: state => state.warnings,
    info: state => state.info
  },
  mutations: {
    setStateErrorMessage (state, payload) {
      state.error = payload.error
    },
    setStateWarningsMessage (state, payload) {
      state.warnings = payload.warnings
    },
    setStateInfoMessage (state, payload) {
      state.info = payload.info
    },
    clear (state) {
      state.error = ''
      state.warnings = []
      state.info = ''
    }
  },
  actions: {
    // エラーメッセージ表示
    setErrorMessage (context, payload) {
      context.commit('setStateErrorMessage', { 'error': payload.message })
    },
    // 警告メッセージ（複数）表示
    setWarningMessages (context, payload) {
      context.commit('setStateWarningsMessage', { 'warnings': payload.messages })
    },
    // インフォメーションメッセージ表示
    setInfoMessage (context, payload) {
      context.commit('setStateInfoMessage', { 'info': payload.message })
    },
    // 全メッセージ削除
    clearMessages (context) {
      context.commit('clear')
    }
  }
}
