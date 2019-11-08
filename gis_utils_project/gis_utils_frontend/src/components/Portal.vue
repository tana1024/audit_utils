<template>
  <div id="portal">
    <div class="d-flex" id="wrapper">
      <!-- Sidebar -->
      <div class="bg-light border-right" id="sidebar-wrapper">
        <GlobalSideHeader/>
        <div id="sidebar-menu" class="list-group list-group-flush">
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
        <GlobalMainHeader/>
        <div id="main-panel" class="container-fluid">
          <router-view/>
        </div>
      </div>
      <!-- /#page-content-wrapper -->
    </div>
  </div>
</template>

<script>
import GlobalSideHeader from '@/components/global/GlobalSideHeader'
import GlobalMainHeader from '@/components/global/GlobalMainHeader'

export default {
  name: 'Portal',
  components: {
    GlobalSideHeader,
    GlobalMainHeader
  }
}
</script>

<style scoped>

  #sidebar-wrapper {
    margin-left: -15rem;
    -webkit-transition: margin .25s ease-out;
    -moz-transition: margin .25s ease-out;
    -o-transition: margin .25s ease-out;
    transition: margin .25s ease-out;
  }

  #sidebar-menu {
    min-height: 90vh;
    width: 14.5rem;
  }

  #page-content-wrapper {
    min-width: 100vw;
  }

  #wrapper.toggled #sidebar-wrapper {
    margin-left: 0;
  }

  #main-panel {
    min-height: 90vh;
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
