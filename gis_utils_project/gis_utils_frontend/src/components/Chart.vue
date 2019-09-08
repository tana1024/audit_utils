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
          <div class="bg-success text-white pl-2">財務情報</div>
          <ul class="nav nav-tabs">
            <li class="nav-item">
              <a @click="selectLeftTab('1')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === '1'}">従業員数</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('2')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === '2'}">平均年齢</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('3')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === '3'}">平均勤続年数</a>
            </li>
            <li class="nav-item">
              <a @click="selectLeftTab('4')" class="nav-link" v-bind:class="{'active bg-primary text-white': isLeftActive === '4'}">年収</a>
            </li>
          </ul>
        </div>
        <!-- タブ内容 -->
        <div class="tab-content">
          <div class="tab-pane" v-show="isLeftActive === '1'" v-bind:class="{'active': isLeftActive === '1'}">
            <router-view ref="EmployeesChart" class="chart" name="EmployeesChart"/>
          </div>
          <div class="tab-pane" v-show="isLeftActive === '2'" v-bind:class="{'active': isLeftActive === '2'}">
            <router-view name="AverageAgeChart"/>
          </div>
          <div class="tab-pane" v-show="isLeftActive === '3'" v-bind:class="{'active': isLeftActive === '3'}">
            <router-view name="ServiceYearsChart"/>
          </div>
          <div class="tab-pane" v-show="isLeftActive === '4'" v-bind:class="{'active': isLeftActive === '4'}">
            <router-view name="IncomeChart"/>
          </div>
        </div>
      </div>
      <div>
        <div>
          <div class="bg-success text-white pl-2">従業員情報</div>
          <ul class="nav nav-tabs">
            <li class="nav-item">
              <a @click="selectRightTab('1')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === '1'}">売上</a>
            </li>
            <li class="nav-item">
              <a @click="selectRightTab('2')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === '2'}">経常利益</a>
            </li>
            <li class="nav-item">
              <a @click="selectRightTab('3')" class="nav-link" v-bind:class="{'active bg-primary text-white': isRightActive === '3'}">当期純利益</a>
            </li>
          </ul>
        </div>
        <!-- タブ内容 -->
        <div class="tab-content">
          <div class="tab-pane" v-show="isRightActive === '1'" v-bind:class="{'active': isRightActive === '1'}">
            <router-view class="chart" name="SalesChart"/>
          </div>
          <div class="tab-pane" v-show="isRightActive === '2'" v-bind:class="{'active': isRightActive === '2'}">
            <router-view name="OrdinaryIncomeChart"/>
          </div>
          <div class="tab-pane" v-show="isRightActive === '3'" v-bind:class="{'active': isRightActive === '3'}">
            <router-view name="NetIncomeChart"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import { mapMutations } from 'vuex'

export default {
  name: 'Chart',
  data: function () {
    return {
      isLeftActive: '1',
      isRightActive: '1',
      checkSn: false,
      checkAz: false,
      checkDt: false,
      checkAr: false
    }
  },
  methods: {
    selectLeftTab: function(id) {
      this.isLeftActive = id
    },
    selectRightTab: function(id) {
      this.isRightActive = id
    },
    executePlot: function() {
      axios.get('https://' + window.location.host + '/api/get_client_employee_chart_data', {params: {check_sn: this.checkSn, check_az: this.checkAz, check_dt: this.checkDt, check_ar: this.checkAr}})
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
          this.setData(response.data)
          this.$refs['EmployeesChart'].plot()
        })
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
