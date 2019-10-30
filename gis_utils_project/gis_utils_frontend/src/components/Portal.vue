<template>
  <div id="dashboard">
    <div class="d-flex" id="wrapper">
      <!-- Sidebar -->
      <div class="bg-light border-right" id="sidebar-wrapper">
        <div class="sidebar-heading">GIS Utils</div>
        <div class="list-group list-group-flush">
          <router-link to="/portal/information" class="list-group-item list-group-item-action bg-light">Information</router-link>
          <router-link to="/portal/map"  class="list-group-item list-group-item-action bg-light">Map</router-link>
          <router-link to="/portal/chart" class="list-group-item list-group-item-action bg-light">Chart</router-link>
          <router-link to="/portal/scraping"  class="list-group-item list-group-item-action bg-light">Scraping</router-link>
          <a href="#" class="list-group-item list-group-item-action bg-light">Profile</a>
          <a href="#" class="list-group-item list-group-item-action bg-light">Setting</a>
        </div>
      </div>
      <!-- /#sidebar-wrapper -->
      <!-- Page Content -->
      <div id="page-content-wrapper">
        <b-modal id="modal-logout-confirm" title="確認" @ok="execLogout">
          <p>ログアウトしてもよろしいでしょうか？</p>
        </b-modal>

        <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
          <button class="btn btn-primary" id="menu-toggle">Toggle Menu</button>

          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>

          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <b-dropdown id="dropdown-1" right v-bind:text="'user : ' + getUsername">
                <b-dropdown-item>First Action</b-dropdown-item>
                <b-dropdown-item>Second Action</b-dropdown-item>
                <b-dropdown-item>Third Action</b-dropdown-item>
                <b-dropdown-divider></b-dropdown-divider>
                <b-dropdown-item @click="showLogoutModal()">Sign out</b-dropdown-item>
              </b-dropdown>
            </ul>
          </div>
        </nav>
        <div class="container-fluid">
          <router-view/>
        </div>
      </div>
      <!-- /#page-content-wrapper -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'Portal',
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
      this.$router.push({path: 'login'})
    }
  }
}
</script>

<style scoped>

  #sidebar-wrapper {
    min-height: 100vh;
    margin-left: -15rem;
    -webkit-transition: margin .25s ease-out;
    -moz-transition: margin .25s ease-out;
    -o-transition: margin .25s ease-out;
    transition: margin .25s ease-out;
  }

  #sidebar-wrapper .sidebar-heading {
    padding: 0.875rem 1.25rem;
    font-size: 1.2rem;
  }

  #sidebar-wrapper .list-group {
    width: 15rem;
  }

  #page-content-wrapper {
    min-width: 100vw;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: 0;
  }

  @media (min-width: 768px) {
    #sidebar-wrapper {
      margin-left: 0;
    }

    #page-content-wrapper {
      min-width: 0;
      width: 100%;
    }

    #wrapper.toggled #sidebar-wrapper {
      margin-left: -15rem;
    }
  }
</style>
