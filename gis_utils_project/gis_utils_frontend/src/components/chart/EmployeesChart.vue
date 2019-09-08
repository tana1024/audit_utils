<script>
import { Bar } from 'vue-chartjs'
import { mapState } from 'vuex'

export default {
  name: 'EmployeesChart',
  extends: Bar,
  data() {
      return {
          chartData: {
              labels: ['0-100', '100-300', '300-1000', '1000-3000', '3000-10000', '10000-'],
              datasets: [{
                  label: '',
                  backgroundColor:'rgba(255, 60, 60, 0.3)',
                  data: [0, 0, 0, 0, 0, 0]
              }]
          },
          options: {
              title: {
                  display: true,
                  text: '従業員数グラフ'
              },
              scales: {
                  yAxes: [{
                          ticks: {
                              beginAtZero: true,
                          }
                  }]
              }
          }
      }
  },
  computed: {
    ...mapState({
      "aggregateList": state => state.chartData.aggregateList,
    }),
  },
  mounted: function() {
    this.renderChart(this.chartData, this.options)
  },
  methods: {
    plot: function() {
      for (let agData of this.aggregateList) {
        if (agData.audit_code = 'sn') {
          this.genChartData(agData)
        }
      }
      this.renderChart(this.chartData, this.options)
    },
    genChartData (agData) {
      let param = {label: '新日本', backgroundColor:'rgba(255, 255, 0, 0.3)',
                  data:
                    [agData.count_1_100, agData.count_100_300, agData.count_300_1000,
                     agData.count_1000_3000, agData.count_3000_10000, agData.count_10000_over]
                  }
      this.chartData.datasets = [param]
    }
  }
}
</script>
