<template>
  <div>
    <h3>Chart（クライアント情報チャート）</h3>
    <div class="d-flex">
      <div id="sub-sidebar">
        <div class="list-group list-group-flush">
          <div class="list-group-item">
            <button type="button" class="btn btn-primary btn-sm" @click="executePlot">プロット</button>
          </div>
          <div class="list-group-item">
            <input id="check_sn" type="checkbox" v-model="checkSn"/><label class="ck_sn_label" for="check_sn">新日本</label>
          </div>
          <div class="list-group-item">
            <input id="check_az" type="checkbox" v-model="checkAz"/><label class="ck_az_label" for="check_az">あずさ</label>
          </div>
          <div class="list-group-item">
            <input id="check_dt" type="checkbox" v-model="checkDt"/><label class="ck_dt_label" for="check_dt">トーマツ</label>
          </div>
          <div class="list-group-item">
            <input id="check_ar" type="checkbox" v-model="checkAr"/><label class="ck_ar_label" for="check_ar">あらた</label>
          </div>
        </div>
      </div>
      <div>
        <div>
          <div class="bg-success text-white pl-2">従業員情報</div>
          <ul class="nav nav-tabs">
            <li class="nav-item">
              <a @click="selectLeftTab('employees')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === 'employees'}">従業員数</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('average_age')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === 'average_age'}">平均年齢</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('service_years')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === 'service_years'}">平均勤続年数</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('income')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === 'income'}">年収</a>
            </li>
          </ul>
        </div>
        <!-- タブ内容 -->
        <div class="tab-content">
          <div class="tab-pane" v-show="isLeftActive === 'employees'" v-bind:class="{'active': isLeftActive === 'employees'}">
            <EmployeesChart ref="EmployeesChart" />
          </div>
          <div class="tab-pane" v-show="isLeftActive === 'average_age'" v-bind:class="{'active': isLeftActive === 'average_age'}">
            <AverageAgeChart ref="AverageAgeChart" />
          </div>
          <div class="tab-pane" v-show="isLeftActive === 'service_years'" v-bind:class="{'active': isLeftActive === 'service_years'}">
            <ServiceYearsChart ref="ServiceYearsChart" />
          </div>
          <div class="tab-pane" v-show="isLeftActive === 'income'" v-bind:class="{'active': isLeftActive === 'income'}">
            <IncomeChart ref="IncomeChart" />
          </div>
        </div>
      </div>
      <div>
        <div>
          <div class="bg-success text-white pl-2">財務情報</div>
          <ul class="nav nav-tabs">
            <li class="nav-item">
              <a @click="selectRightTab('sales')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === 'sales'}">売上</a>
            </li>
            <li class="nav-item">
              <a @click="selectRightTab('ordinary_income')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === 'ordinary_income'}">経常利益</a>
            </li>
            <li class="nav-item">
              <a @click="selectRightTab('net_income')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === 'net_income'}">当期純利益</a>
            </li>
          </ul>
        </div>
        <!-- タブ内容 -->
        <div class="tab-content">
          <div class="tab-pane" v-show="isRightActive === 'sales'" v-bind:class="{'active': isRightActive === 'sales'}">
            <SalesChart ref="SalesChart" />
          </div>
          <div class="tab-pane" v-show="isRightActive === 'ordinary_income'" v-bind:class="{'active': isRightActive === 'ordinary_income'}">
            <OrdinaryIncomeChart ref="OrdinaryIncomeChart" />
          </div>
          <div class="tab-pane" v-show="isRightActive === 'net_income'" v-bind:class="{'active': isRightActive === 'net_income'}">
            <NetIncomeChart ref="NetIncomeChart"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { mapMutations } from 'vuex'
import EmployeesChart from '@/components/chart/EmployeesChart'
import AverageAgeChart from '@/components/chart/AverageAgeChart'
import ServiceYearsChart from '@/components/chart/ServiceYearsChart'
import IncomeChart from '@/components/chart/IncomeChart'
import SalesChart from '@/components/chart/SalesChart'
import OrdinaryIncomeChart from '@/components/chart/OrdinaryIncomeChart'
import NetIncomeChart from '@/components/chart/NetIncomeChart'

export default {
  name: 'Chart',
  components: {
      EmployeesChart, AverageAgeChart, ServiceYearsChart, IncomeChart,
      SalesChart, OrdinaryIncomeChart, NetIncomeChart
  },
  data: function () {
    return {
      tabToComponent: {employees: 'EmployeesChart', average_age: 'AverageAgeChart', service_years: 'ServiceYearsChart', income: 'IncomeChart',
                      sales: 'SalesChart', ordinary_income: 'OrdinaryIncomeChart', net_income: 'NetIncomeChart'},
      isLeftActive: 'employees',
      isRightActive: 'sales',
      checkSn: false,
      checkAz: false,
      checkDt: false,
      checkAr: false
    }
  },
  methods: {
    selectLeftTab: function(id) {
      this.isLeftActive = id
      axios.get('https://' + window.location.host + '/api/chart/get_client_' + this.isLeftActive + '_chart_data', {params: {check_sn: this.checkSn, check_az: this.checkAz, check_dt: this.checkDt, check_ar: this.checkAr}})
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
          this.setData(response.data)
          this.$refs[this.tabToComponent[this.isLeftActive]].plot()
        })
    },
    selectRightTab: function(id) {
      this.isRightActive = id
      axios.get('https://' + window.location.host + '/api/chart/get_client_' + this.isRightActive + '_chart_data', {params: {check_sn: this.checkSn, check_az: this.checkAz, check_dt: this.checkDt, check_ar: this.checkAr}})
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
          this.setData(response.data)
          this.$refs[this.tabToComponent[this.isRightActive]].plot()
        })
    },
    executePlot: function() {
      this.selectLeftTab(this.isLeftActive)
      this.selectRightTab(this.isRightActive)
    },
    ...mapMutations({
      setAggregateList: 'chartData/setAggregateList'
    }),
    setData (data) {
      this.setAggregateList(data)
    }
  }
}
</script>
<style>
#sub-sidebar {
  height: 80vh;
  width: 8rem;
}

.ck_sn_label {
  color: yellow;
}
.ck_az_label {
  color: blue;
}
.ck_dt_label {
  color: green;
}
.ck_ar_label {
  color: orange;
}
.tab-content {
  height: 35vh;
  width: 35vw;
}
</style>
