<template>
  <div>
    <h2>Mapping</h2>
    <div class="d-flex">
      <div id="sub-sidebar">
        <div class="list-group list-group-flush">
          <div class="list-group-item">
            <button type="button" class="btn btn-primary btn-sm" @click="executeMapping">マッピング</button>
          </div>
          <div class="list-group-item">
            <input id="check_sn" type="checkbox" v-model="checkSn"/><label for="check_sn">新日本</label>
          </div>
          <div class="list-group-item">
            <input id="check_az" type="checkbox" v-model="checkAz"/><label for="check_az">あずさ</label>
          </div>
          <div class="list-group-item">
            <input id="check_dt" type="checkbox" v-model="checkDt"/><label for="check_dt">トーマツ</label>
          </div>
          <div class="list-group-item">
            <input id="check_ar" type="checkbox" v-model="checkAr"/><label for="check_ar">あらた</label>
          </div>
        </div>
      </div>
      <div>
        <div id='map'>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import axios from 'axios'

export default {
  name: 'Map',
  data: function() {
    return {
      checkSn:false,
      checkAz:false,
      checkDt:false,
      checkAr:false
    }
  },
  mounted() {
    L.map( 'map', { center: L.latLng( 35.6825, 139.752778 ), zoom: 15 } ).addLayer(
      L.tileLayer( 'http://{s}.tile.osm.org/{z}/{x}/{y}.png' )
    )
  },
  methods: {
    executeMapping: function() {
      axios.get('/api/get_client_gio_info', {params: {check_sn: this.checkSn, check_az: this.checkAz, check_dt: this.checkDt, check_ar: this.checkAr}})
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)
        })
    }
  }
}
</script>

<style>
#map {
  height: 80vh;
  width: 65vw;
}
#sub-sidebar {
  height: 100vh;
  width: 8rem;
}

</style>
