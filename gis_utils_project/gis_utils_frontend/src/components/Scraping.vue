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
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" @click="exec_scraping('sn')">更新</button></td>
            </tr>
            <tr>
                <th>あずさ</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" @click="exec_scraping('az')">更新</button></td>
            </tr>
            <tr>
                <th>トーマツ</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" @click="exec_scraping('dt')">更新</button></td>
            </tr>
            <tr>
                <th>あらた</th>
                <td>-</td>
                <td>-</td>
                <td><button class="btn btn-sm btn-primary" @click="exec_scraping('ar')">更新</button></td>
            </tr>
        </tbody>
    </table>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Scraping',
  methods: {
    exec_scraping: function(audit_code) {
      console.log(audit_code)
      axios.get("https://" + window.location.host + "/api/spots/")
        .then(response=>{
          console.log("status:",response.status)
          console.log("responseData:",response.data)
        })
    }
  }
}
</script>

<style>
</style>
