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
          <ul class="nav nav-tabs">
            <li class="nav-item">
              <a @click="select('1')" class="nav-link" v-bind:class="{'active bg-primary text-white': isActive === '1'}">従業員数</a>
            </li>
            <li class="nav-item">
              <a @click="select('2')" class="nav-link" v-bind:class="{'active bg-primary text-white': isActive === '2'}">年数</a>
            </li>
            <li class="nav-item">
              <a @click="select('3')" class="nav-link" v-bind:class="{'active bg-primary text-white': isActive === '3'}">業種</a>
            </li>
          </ul>
        </div>
        <!-- タブ内容 -->
        <div class="tab-content">
          <div class="tab-pane" v-show="isActive === '1'" v-bind:class="{'active': isActive === '1'}">
            <router-view class="chart" name="EmployeesChart"/>
          </div>
          <div class="tab-pane" v-show="isActive === '2'" v-bind:class="{'active': isActive === '2'}">
            <router-view name="IndustryChart"/>
          </div>
          <div class="tab-pane" v-show="isActive === '3'" v-bind:class="{'active': isActive === '3'}">
            <router-view name="ServiceYearsVsIncomeChart"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Chart',
  data: function () {
    return {
      isActive: '1',
      checkSn: false,
      checkAz: false,
      checkDt: false,
      checkAr: false
    }
  },
  created() {
    axios.get('https://' + window.location.host + '/api/get_client_employee_chart_data')
      .then(response=>{
        console.log('status:', response.status)
        console.log('responseData:', response.data)
      })
  },
  methods: {
    select: function(id) {
      this.isActive = id
    },
    executePlot: function() {
    }
  }
}
</script>
<style>
#sub-sidebar {
  height: 100vh;
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
.chart {
  width: 500px;
  height: 500px;
}
</style>
