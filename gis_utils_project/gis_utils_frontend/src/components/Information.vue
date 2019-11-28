<template>
  <div id="information">
    <div class="d-flex mb-n4">
      <h3 class="col-6 ml-n3">Information(News API 連携情報)</h3>
      <div class="col-3 pr-2 mt-2">
        <p class="text-right"><label for="selected">Topic select : </label></p>
      </div>
      <div class="col-3 mt-1">
        <b-form-select id="selected" v-model="selected" :options="options" size="sm" @change="publish_information"></b-form-select>
      </div>
    </div>
    <hr>
    <div id="info-area" class="container">
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
      news: [],
      selected: 'PwC',
      options: [
        {value: 'ErnstYoung', text: 'EY'},
        {value: 'KPMG', text: 'KPMG'},
        {value: 'Deloitte', text: 'Deloitte'},
        {value: 'PwC', text: 'PwC'}
      ],
    }
  },
  created () {
    this.publish_information()
  },
  methods: {
    publish_information: function () {
      api.get('/api/information/init_information',{ params: { selected: this.selected } } )
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
          this.news = response.data.slice(0,9)
          this.length = this.news.length
          this.i = Math.ceil(this.news.length / 3)
          this.j = this.news.length != 0 && this.news.length % 3 == 0? 3: this.news.length % 3
        })
    }
  }
}
</script>

<style scoped>

  #info-area {
    overflow-y: auto;
    height: 80vh;
  }

</style>
