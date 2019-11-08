<template>
  <div id="settings">
    <div class="d-flex" id="wrapper">
      <!-- Sidebar-header -->
      <div class="bg-light border-right border-bottom" id="sidebar-wrapper">
        <GlobalSideHeader/>
      </div>
      <!-- /#sidebar-header-wrapper -->
      <!-- Page Content header -->
      <div id="page-content-wrapper">
        <GlobalMainHeader/>
      </div>
      <!-- /#page-content-header-wrapper -->
    </div>
    <div class="container-fluid">
      <div>
        <ul class="nav nav-tabs">
          <li class="nav-item">
            <a @click="selectTab('profile')" class="nav-link" v-bind:class="{'active bg-secondary text-white': isActive === 'profile'}">Profile</a>
          </li>
          <li class="nav-item">
            <a @click="selectTab('account')" class="nav-link" v-bind:class="{'active bg-secondary text-white': isActive === 'account'}">Account</a>
          </li>
          <li class="nav-item">
            <a @click="selectTab('parameter')" class="nav-link" v-bind:class="{'active bg-secondary text-white': isActive === 'parameter'}">Parameter</a>
          </li>
        </ul>
      </div>
      <div>
        <router-view/>
      </div>
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
  },
  data: function () {
    return {
      isActive: 'profile'
    }
  },
  methods: {
    selectTab: function(id) {
      this.isActive = id
      this.$router.push({path: '/settings/' + id})
    }
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

  #page-content-wrapper {
    min-width: 100vw;
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
