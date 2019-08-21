<template>
  <div>
    <h1 class="mt-4">Scraping</h1>
    <h2>担当会社情報ステータス</h2>
    <table class="table table-bordered table-hover">
        <thead>
            <tr>
                <th>法人名</th>
                <th>更新日時</th>
                <th>更新ステータス</th>
                <th>更新ボタン</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>新日本</th>
                <td>{{snUpdateDatetime}}</td>
                <td>{{snUpdateStatus}}</td>
                <td><button class="btn btn-sm btn-primary" @click="execScraping('sn')">更新</button></td>
            </tr>
            <tr>
                <th>あずさ</th>
                <td>{{azUpdateDatetime}}</td>
                <td>{{azUpdateStatus}}</td>
                <td><button class="btn btn-sm btn-primary" @click="execScraping('az')">更新</button></td>
            </tr>
            <tr>
                <th>トーマツ</th>
                <td>{{dtUpdateDatetime}}</td>
                <td>{{dtUpdateStatus}}</td>
                <td><button class="btn btn-sm btn-primary" @click="execScraping('dt')">更新</button></td>
            </tr>
            <tr>
                <th>あらた</th>
                <td>{{arUpdateDatetime}}</td>
                <td>{{arUpdateStatus}}</td>
                <td><button class="btn btn-sm btn-primary" @click="execScraping('ar')">更新</button></td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Scraping',
  data: function () {
    return {
      snUpdateDatetime:'-',
      snUpdateStatus:'-',
      azUpdateDatetime:'-',
      azUpdateStatus:'-',
      dtUpdateDatetime:'-',
      dtUpdateStatus:'-',
      arUpdateDatetime:'-',
      arUpdateStatus:'-'
    }
  },
  created () {
      axios.get('https://' + window.location.host + '/api/init_scraping')
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
          this.snUpdateStatus = response.status
        })
  },
  methods: {
    execScraping: function(audit_code) {
      if (!confirm('クライアント情報を更新してもよろしいでしょうか？')) {
        return
      }
      axios.get('https://' + window.location.host + '/api/exec_scraping', {params: {audit_code: audit_code}})
        .then(response=>{
          console.log('status:',response.status)
          console.log('responseData:',response.data)
          alert('更新リクエストを受け付けました。\n更新完了の通知ををメールでご連絡いたします。')
        })
    }
  }
}
</script>

<style>
</style>
