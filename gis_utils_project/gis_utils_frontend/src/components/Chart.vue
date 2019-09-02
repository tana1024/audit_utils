<template>
  <div>
    テストです。
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Chart',
  created() {
    axios.get('https://' + window.location.host + '/api/get_client_employee_chart_data')
      .then(response=>{
        console.log('status:', response.status)
        console.log('responseData:', response.data)
      })
  }
}
</script>
<style>
</style>
