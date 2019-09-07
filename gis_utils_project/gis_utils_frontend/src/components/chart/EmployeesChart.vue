<script>
import { Bar } from 'vue-chartjs'
import { mapState } from 'vuex'

export default {
  name: 'EmployeesChart',
  extends: Bar,
  data() {
      return {
          chartData: {
              labels: ['Janualy', 'Februaly', 'March'],
              datasets: [{
                  label: 'sample',
                  backgroundColor:'rgba(255, 60, 60, 0.3)',
                  data: [20, 40, 60]
              }]
          },
          options: {
              title: {
                  display: true,
                  text: 'Bar chart'
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
      "count": state => state.chartData.count,
    }),
  },
  mounted: function() {
    alert('start')
    this.renderChart(this.chartData, this.options)
  },
  methods: {
    execute: function() {
      alert(this.count)
    }
  }
}
</script>
