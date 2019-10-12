<template>
  <div>
    <b-modal id="modal-confirm" title="確認" @ok="execScraping">
      <p>クライアント情報を更新してもよろしいでしょうか？</p>
    </b-modal>
    <h3>Scraping（クライアント情報スクレイピング）</h3>
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
                <td>{{snUpdateDatetime}}</td>
                <td>{{snUpdateStatus}}</td>
                <td>{{snUpdateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showModal('sn')">更新</button></td>
            </tr>
            <tr>
                <th>あずさ</th>
                <td>{{azUpdateDatetime}}</td>
                <td>{{azUpdateStatus}}</td>
                <td>{{azUpdateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showModal('az')">更新</button></td>
            </tr>
            <tr>
                <th>トーマツ</th>
                <td>{{dtUpdateDatetime}}</td>
                <td>{{dtUpdateStatus}}</td>
                <td>{{dtUpdateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showModal('dt')">更新</button></td>
            </tr>
            <tr>
                <th>あらた</th>
                <td>{{arUpdateDatetime}}</td>
                <td>{{arUpdateStatus}}</td>
                <td>{{arUpdateCount}}</td>
                <td><button class="btn btn-sm btn-primary" @click="showModal('ar')">更新</button></td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'
import GlobalMessage from '@/components/global/GlobalMessage'

export default {
  name: 'Scraping',
  components: {
    GlobalMessage
  },
  data: function () {
    return {
      scraping_audit_code: '',
      snUpdateDatetime:'-',
      snUpdateStatus:'-',
      snUpdateCount:'-',
      azUpdateDatetime:'-',
      azUpdateStatus:'-',
      azUpdateCount:'-',
      dtUpdateDatetime:'-',
      dtUpdateStatus:'-',
      dtUpdateCount:'-',
      arUpdateDatetime:'-',
      arUpdateStatus:'-',
      arUpdateCount:'-'
    }
  },
  created () {
      axios.get('https://' + window.location.host + '/api/scraping/init_scraping')
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)

          var data = {
                      'sn': {0: {update_datetime: '-', update_count: '-', status: '-'} },
                      'az': {0: {update_datetime: '-', update_count: '-', status: '-'} },
                      'dt': {0: {update_datetime: '-', update_count: '-', status: '-'} },
                      'ar': {0: {update_datetime: '-', update_count: '-', status: '-'} }
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

          this.snUpdateDatetime = (new Date(data['sn'][0].update_datetime)).toLocaleString()
          this.snUpdateStatus = data['sn'][0].status
          this.snUpdateCount = data['sn'][0].update_count || '-'
          this.azUpdateDatetime = (new Date(data['az'][0].update_datetime)).toLocaleString()
          this.azUpdateStatus = data['az'][0].status
          this.azUpdateCount = data['az'][0].update_count || '-'
          this.dtUpdateDatetime = (new Date(data['dt'][0].update_datetime)).toLocaleString()
          this.dtUpdateStatus = data['dt'][0].status
          this.dtUpdateCount = data['dt'][0].update_count || '-'
          this.arUpdateDatetime = (new Date(data['ar'][0].update_datetime)).toLocaleString()
          this.arUpdateStatus = data['ar'][0].status
          this.arUpdateCount = data['ar'][0].update_count || '-'

        })
  },
  methods: {
    showModal: function(audit_code) {
      this.scraping_audit_code = audit_code
      this.$bvModal.show('modal-confirm')
    },
    execScraping: function() {
      this.$store.dispatch('messageData/setInfoMessage', { message: '更新リクエストを受け付けました。\n更新完了の通知ををメールでご連絡いたします。'})
      // axios.get('https://' + window.location.host + '/api/scraping/exec_scraping', {params: {audit_code: this.scraping_audit_code}})
      //   .then(response=>{
      //     console.log('status:',response.status)
      //     console.log('responseData:',response.data)
      //     $store.dispatch('messageData/setInfoMessage', { message: '更新リクエストを受け付けました。\n更新完了の通知ををメールでご連絡いたします。'})
      //   })
    }
  }
}
</script>

<style>
</style>
