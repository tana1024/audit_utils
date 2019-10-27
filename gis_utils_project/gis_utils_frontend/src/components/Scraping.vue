<template>
  <div>
    <b-modal id="modal-scraping-confirm" title="確認" @ok="execScraping">
      <p>クライアント情報を更新してもよろしいでしょうか？</p>
    </b-modal>
    <b-modal id="modal-web-api-confirm" title="確認" @ok="execWebApi">
      <p>ニュース情報を更新してもよろしいでしょうか？</p>
    </b-modal>
    <h3>Scraping（クライアント情報スクレイピング）</h3>
    <hr>
    <div class="container-fluid">
      <GlobalMessage/>
    </div>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>法人名</th>
                <th>更新日時</th>
                <th>更新ステータス</th>
                <th>更新件数</th>
                <th>更新ボタン</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>新日本</th>
                <td>{{auditSnInfo.updateDatetime}}</td>
                <td>{{auditSnInfo.updateStatus}}</td>
                <td>{{auditSnInfo.updateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showScrapingModal('sn')">更新</button></td>
            </tr>
            <tr>
                <th>あずさ</th>
                <td>{{auditAzInfo.updateDatetime}}</td>
                <td>{{auditAzInfo.updateStatus}}</td>
                <td>{{auditAzInfo.updateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showScrapingModal('az')">更新</button></td>
            </tr>
            <tr>
                <th>トーマツ</th>
                <td>{{auditDtInfo.updateDatetime}}</td>
                <td>{{auditDtInfo.updateStatus}}</td>
                <td>{{auditDtInfo.updateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showScrapingModal('dt')">更新</button></td>
            </tr>
            <tr>
                <th>あらた</th>
                <td>{{auditArInfo.updateDatetime}}</td>
                <td>{{auditArInfo.updateStatus}}</td>
                <td>{{auditArInfo.updateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showScrapingModal('ar')">更新</button></td>
            </tr>
        </tbody>
    </table>
    <hr>
        <h3>Web API（Web API連携）</h3>
    <hr>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>API名称</th>
                <th>更新日時</th>
                <th>更新ステータス</th>
                <th>更新件数</th>
                <th>更新ボタン</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>NEWS API</th>
                <td>{{webapiNewsInfo.updateDatetime}}</td>
                <td>{{webapiNewsInfo.updateStatus}}</td>
                <td>{{webapiNewsInfo.updateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showWebApiModal()">更新</button></td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
import GlobalMessage from '@/components/global/GlobalMessage'
import api from '@/services/api'

export default {
  name: 'Scraping',
  components: {
    GlobalMessage
  },
  data: function () {
    return {
      scrapingAuditCode: '',
      auditSnInfo: {updateDatetime:'-', updateStatus:'-', updateCount:'-'},
      auditAzInfo: {updateDatetime:'-', updateStatus:'-', updateCount:'-'},
      auditDtInfo: {updateDatetime:'-', updateStatus:'-', updateCount:'-'},
      auditArInfo: {updateDatetime:'-', updateStatus:'-', updateCount:'-'},
      webapiNewsInfo: {updateDatetime:'-', updateStatus:'-', updateCount:'-'}
    }
  },
  created () {
    api.get('/api/scraping/init_scraping')
      .then(response=>{
        console.log('status:', response.status)
        console.log('responseData:', response.data)

        var data = {
                    'sn': [{update_datetime: '-', update_count: '-', status: '-'}],
                    'az': [{update_datetime: '-', update_count: '-', status: '-'}],
                    'dt': [{update_datetime: '-', update_count: '-', status: '-'}],
                    'ar': [{update_datetime: '-', update_count: '-', status: '-'}]
                    }
        data['sn'] = response.data.filter(function(item, index){
          if (item.audit_code == 'sn') return true
        })
        data['az'] = response.data.filter(function(item, index){
          if (item.audit_code == 'az') return true
        })
        data['dt'] = response.data.filter(function(item, index){
          if (item.audit_code == 'dt') return true
        })
        data['ar'] = response.data.filter(function(item, index){
          if (item.audit_code == 'ar') return true
        })

        this.auditSnInfo.updateDatetime = (new Date(data['sn'][0].update_datetime)).toLocaleString()
        this.auditSnInfo.updateStatus = data['sn'][0].status
        this.auditSnInfo.updateCount = data['sn'][0].update_count || '-'
        this.auditAzInfo.updateDatetime = (new Date(data['az'][0].update_datetime)).toLocaleString()
        this.auditAzInfo.updateStatus = data['az'][0].status
        this.auditAzInfo.updateCount = data['az'][0].update_count || '-'
        this.auditDtInfo.updateDatetime = (new Date(data['dt'][0].update_datetime)).toLocaleString()
        this.auditDtInfo.updateStatus = data['dt'][0].status
        this.auditDtInfo.updateCount = data['dt'][0].update_count || '-'
        this.auditArInfo.updateDatetime = (new Date(data['ar'][0].update_datetime)).toLocaleString()
        this.auditArInfo.updateStatus = data['ar'][0].status
        this.auditArInfo.updateCount = data['ar'][0].update_count || '-'

      })

    api.get('/api/scraping/init_webapi')
      .then(response=>{
        console.log('status:', response.status)
        console.log('responseData:', response.data)
        var data = {
                    '1': [{update_datetime: '-', update_count: '-', status: '-'}]
                    }
        data['1'] = response.data.filter(function(item, index){
          if (item.api_id == '1') return true
        })
        this.webapiNewsInfo.updateDatetime = (new Date(data['1'][0].update_datetime)).toLocaleString()
        this.webapiNewsInfo.updateStatus = data['1'][0].status
        this.webapiNewsInfo.updateCount = data['1'][0].update_count || '-'
      })
  },
  methods: {
    showScrapingModal: function(audit_code) {
      this.scrapingAuditCode = audit_code
      this.$bvModal.show('modal-scraping-confirm')
    },
    showWebApiModal: function() {
      this.$bvModal.show('modal-web-api-confirm')
    },
    execScraping: function() {
      api.get('/api/scraping/exec_scraping', {params: {audit_code: this.scrapingAuditCode}})
        .then(response=>{
          console.log('status:',response.status)
          console.log('responseData:',response.data)
          this.$store.dispatch('messageData/setInfoMessage', { message: '更新リクエストを受け付けました。\n更新完了の通知ををメールでご連絡いたします。'})
        })
    },
    execWebApi: function() {
      api.get('/api/scraping/exec_webapi')
        .then(response=>{
          console.log('status:',response.status)
          console.log('responseData:',response.data)
          this.$store.dispatch('messageData/setInfoMessage', { message: '更新リクエストを受け付けました。\n更新完了の通知ををメールでご連絡いたします。'})
        })
    }
  }
}
</script>

<style>
</style>
