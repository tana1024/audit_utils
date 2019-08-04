<template>
  <div id="base">
    <router-view @sign_in="login"/>
  </div>
</template>

<script>
export default {
  name: 'Base'
//  ,
//  methods: {
//    login: function() {
//      $router.push('portal')
//    }
//  }
}
</script>

<style>
</style>
