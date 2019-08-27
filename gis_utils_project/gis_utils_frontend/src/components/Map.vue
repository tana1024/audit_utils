<template>
    <div id='map'>
    </div>
</template>
<script>
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'

export default {
  name: 'Map',
  mounted() {
    L.map( 'map', { center: L.latLng( 35.6825, 139.752778 ), zoom: 15 } ).addLayer(
      L.tileLayer( 'http://{s}.tile.osm.org/{z}/{x}/{y}.png' )
    )
  }
}
</script>

<style>
#map { height: 400px; width: 600px}
</style>
