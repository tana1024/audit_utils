<script>
import { Scatter } from 'vue-chartjs'
import { mapState } from 'vuex'

export default {
  name: 'AverageAgeChart',
  extends: Scatter,
  data() {
      return {
          CONST_AUDIT_CORP_NAME: {'sn': '新日本', 'az': 'あずさ', 'dt': 'トーマツ', 'ar': 'あらた'},
          CONST_BACK_GROUND_COLOR: {
            'sn': 'rgba(255, 255, 0)',
            'az': 'rgba(0, 0, 255)',
            'dt': 'rgba(0, 255, 0)',
            'ar': 'rgba(255, 127, 0)'
          },
          chartData: {
              datasets: [{
                  label: '',
                  backgroundColor:'rgb(0, 0, 0)',
                  pointRadius: 1,
                  data: [{ x: 0, y: 0 },{ x: 0, y: 0 },{ x: 0, y: 0 }]
              }]
          },
          options: {
              title: {
                  display: true,
                  text: '平均年齢グラフ'
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

      this.chartData.datasets[0] = this.genChartData('sn')
      this.chartData.datasets[1] = this.genChartData('az')
      this.chartData.datasets[2] = this.genChartData('dt')
      this.chartData.datasets[3] = this.genChartData('ar')
      this.renderChart(this.chartData, this.options)
    },
    genChartData (audit_code) {

      let filterList = this.aggregateList.filter(function(item, index) {
        if (item.audit_code == audit_code) return true
      })
      let scatterList = filterList.map(function(value) {
        return {x: parseFloat(value.average_age), y:value.income}
      })
      return {
          label: this.CONST_AUDIT_CORP_NAME[audit_code],
          backgroundColor: this.CONST_BACK_GROUND_COLOR[audit_code],
          data: scatterList
      }
    }
  }
}
</script>
