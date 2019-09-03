<template>
  <div>
    <h3>Map（クライアントアドレスマッピング）</h3>
    <div class="d-flex">
      <div id="sub-sidebar">
        <div class="list-group list-group-flush">
          <div class="list-group-item">
            <button type="button" class="btn btn-primary btn-sm" @click="executeMapping">マッピング</button>
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
require('leaflet-sprite/dist/leaflet.sprite.js')

delete  L.Icon.Default.prototype._getIconUrl

L.Icon.Default.mergeOptions({
  iconUrl         : require( 'leaflet/dist/images/marker-icon.png' ),
  iconRetinaUrl   : require( 'leaflet/dist/images/marker-icon-2x.png' ),
  shadowUrl       : require( 'leaflet/dist/images/marker-shadow.png' )
})
L.Icon.Default.imagePath = 'leaflet/dist/images/';

export default {
  name: 'Map',
  data: function() {
    return {
      checkSn: false,
      checkAz: false,
      checkDt: false,
      checkAr: false,
      map: null,
      list_marker: []
    }
  },
  mounted() {
    this.map = L.map( 'map', { center: L.latLng( 35.6825, 139.752778 ), zoom: 13 } ).addLayer(
      L.tileLayer( 'http://{s}.tile.osm.org/{z}/{x}/{y}.png' )
    )
  },
  methods: {
    executeMapping: function() {
      axios.get('/api/get_client_gio_info', {params: {check_sn: this.checkSn, check_az: this.checkAz, check_dt: this.checkDt, check_ar: this.checkAr}})
        .then(response=>{
          console.log('status:', response.status)
          console.log('responseData:', response.data)

          if (this.list_marker != null) {
            for (let item of this.list_marker) {
              this.map.removeLayer(item)
            }
          }

          for (let item of response.data) {
            let colors = {sn: 'yellow', az: 'blue', dt: 'green', ar: 'orange'}
            let marker = L.marker([item.latitude, item.longitude], {icon: L.spriteIcon(colors[item.audit_code])}).addTo(this.map)
            marker.bindPopup('<p>' + item.s_code + ':' + item.name + '</p><p>' + item.street_address + '</p>')
            this.list_marker.push(marker)
          }

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

</style>
