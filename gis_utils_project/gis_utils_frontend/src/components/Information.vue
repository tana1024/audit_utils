<template>
  <div>
    <h3>Information(News API 連携情報)</h3>
    <hr>
    <div class="container">
      <!-- Example row of columns -->
      <div class="row" v-for="ii in i">
        <div class="col-md-4" v-for="jj in ii == i? j: 3">
          <h5 v-b-tooltip.hover v-bind:title="news[(ii-1)*3+jj-1].title_jp">{{news[(ii-1)*3+jj-1].title}}</h5>
          <p v-b-tooltip.hover v-bind:title="news[(ii-1)*3+jj-1].description_jp">{{news[(ii-1)*3+jj-1].description}}</p>
          <p><a class="btn btn-primary" v-bind:href="news[(ii-1)*3+jj-1].url" target="_blank" rel="noopener noreferrer" role="button">View details &raquo;</a></p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import GlobalMessage from '@/components/global/GlobalMessage'
import api from '@/services/api'

export default {
  name: 'Information',
  components: {
    GlobalMessage
  },
  data: function () {
    return {
      length: 0,
      i: 0,
      j: 0,
      news: []
    }
  },
  created () {
    api.get('/api/information/init_information')
      .then(response=>{
        console.log('status:', response.status)
        console.log('responseData:', response.data)
        this.news = response.data.slice(0,9)
        this.length = this.news.length
        this.i = Math.ceil(this.news.length / 3)
        this.j = this.news.length != 0 && this.news.length % 3 == 0? 3: this.news.length % 3
      })
  },
  methods: {
  }
}
</script>

<style>
</style>
