<template>
  <div id="profile">
    <div class="row">
      <div class="col-4 mt-5 pl-5">
        Profile
      </div>
      <div class="col-8 mt-5">
        <div class="mb-2">
          <label for="username">Username</label>
        </div>
        <div class="mb-3">
          <b-form-input id="username" v-model="userName" class="w-50"></b-form-input>
        </div>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-4 mt-3 pl-5">
        Password
      </div>
      <div class="col-8 mt-3">
        <div class="mb-2">
          <label for="c-password">Current Password</label>
        </div>
        <div class="mb-3">
          <b-form-input id="c-password" v-model="cPassword" placeholder="enter current your password" class="w-50"></b-form-input>
        </div>
        <div class="mb-2">
          <label for="n-password">New Password</label>
        </div>
        <div class="mb-3">
          <b-form-input id="n-password" v-model="nPassword" placeholder="enter a new password" class="w-50" v-b-tooltip.hover title="Password must be 8 or more characters."></b-form-input>
        </div>
        <div class="mb-2">
          <label for="cn-password">Confirm New Password</label>
        </div>
        <div class="mb-4">
          <b-form-input id="cn-password" v-model="cnPassword" placeholder="enter the password again" class="w-50"></b-form-input>
        </div>
        <div class="mb-3">
          <b-button id="cp-button" variant="primary">Update Password</b-button>
        </div>
      </div>
    </div>
    <hr>
    <div class="row">
      <div class="col-4 mt-3 mb-5 pl-5">
        Close Account
      </div>
      <div class="col-8 mb-5 mt-3">
        <div>
          <b-button id="ca-button" variant="danger">Close this Account</b-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Profile',
  data: function() {
    return {
      userName: 'gisutils'
    }
  }
}
</script>

<style scoped>

  #profile {
    overflow-y: auto;
    overflow-x: hidden;
    height: 80vh;
  }

</style>

