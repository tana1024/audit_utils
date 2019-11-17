<template>
  <div id="global-main-header">
    <b-modal id="modal-logout-confirm" title="確認" @ok="execLogout">
      <p>ログアウトしてもよろしいでしょうか？</p>
    </b-modal>
    <nav id="main-heading" class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
      <button class="btn btn-primary" id="menu-toggle">Toggle Menu</button>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link to="/portal" class="nav-link">Home<span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item mr-2">
            <a class="nav-link" href="https://github.com/tana1024/gis_utils" target="_blank">Link</a>
          </li>
          <b-dropdown id="dropdown-1" right v-bind:text="'user : ' + getUsername">
            <b-dropdown-item to="/settings">Profile</b-dropdown-item>
            <b-dropdown-item @click="showLogoutModal()">Sign out</b-dropdown-item>
          </b-dropdown>
        </ul>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: 'GlobalMainHeader',
  computed: {
    getUsername: function () {
      return this.$store.state.authData.username
    }
  },
  methods: {
    showLogoutModal: function() {
      this.$bvModal.show('modal-logout-confirm')
    },
    execLogout: function() {
      this.$store.dispatch('authData/logout')
      this.$router.push('/login')
    }
  }
}
</script>
<style scoped>
  #main-heading {
    min-height: 7vh;
  }
</style>

