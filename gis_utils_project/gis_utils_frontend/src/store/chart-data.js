export const ChartData = {
  namespaced: true,
  state: {
      aggregateList: []
  },
  mutations: {
    setAggregateList (state, aggregateList) {
      state.aggregateList = aggregateList
    }
  }
}
