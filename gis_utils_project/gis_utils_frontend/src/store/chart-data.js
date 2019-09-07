export const ChartData = {
  namespaced: true,
  state: {
      count: 0
  },
  mutations: {
    setting (state) {
      state.count = 99
    }
  }
}
