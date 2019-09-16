<script>
import { Bar } from 'vue-chartjs'
import { mapState } from 'vuex'

export default {
  name: 'IncomeChart',
  extends: Bar,
  data() {
      return {
          CONST_AUDIT_CORP_NAME: {'sn': '新日本', 'az': 'あずさ', 'dt': 'トーマツ', 'ar': 'あらた'},
          CONST_BACK_GROUND_COLOR: {
            'sn': 'rgba(255, 255, 0, 0.3)',
            'az': 'rgba(0, 0, 255, 0.3)',
            'dt': 'rgba(0, 255, 0, 0.3)',
            'ar': 'rgba(255, 127, 0, 0.3)'
          },
          chartData: {
              labels: ['0-400', '400-600', '600-800', '800-1000', '1000-1300', '1300-'],
              datasets: [{
                  label: '',
                  backgroundColor:'rgba(0, 0, 0, 0)',
                  data: [0, 0, 0, 0, 0, 0]
              }]
          },
          options: {
              title: {
                  display: true,
                  text: '年収グラフ'
              },
              scales: {
                  yAxes: [{
                    display: true,
                    scaleLabel: {
                       display: true,
                       labelString: 'クライアント数'
                    },
                    ticks: {
                        beginAtZero: true,
                    }
                  }],
                  xAxes: [{
                    display: true,
                    scaleLabel: {
                       display: true,
                       labelString: '年収'
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
      let datasets = []

      for (let agData of this.aggregateList) {
        datasets.push(this.genChartData(agData))
      }
      this.chartData.datasets = datasets
      this.renderChart(this.chartData, this.options)
    },
    genChartData (agData) {
      let audit_code = agData.audit_code
      delete agData['audit_code']
      return {
          label: this.CONST_AUDIT_CORP_NAME[audit_code],
          backgroundColor: this.CONST_BACK_GROUND_COLOR[audit_code],
          data: Object.values(agData)
      }
    }
  }
}
</script>

