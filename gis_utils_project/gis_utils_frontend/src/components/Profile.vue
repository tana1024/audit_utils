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
          <label for="cpassword">Current Password</label>
        </div>
        <div class="mb-3">
          <b-form-input id="cpassword" v-model="cPassword" placeholder="enter current your password" class="w-50"></b-form-input>
        </div>
        <div class="mb-2">
          <label for="npassword">New Password</label>
        </div>
        <div class="mb-3">
          <b-form-input id="npassword" v-model="nPassword" placeholder="enter a new password" class="w-50"></b-form-input>
        </div>
        <div class="mb-2">
          <label for="cnpassword">Confirm New Password</label>
        </div>
        <div class="mb-3">
          <b-form-input id="cnpassword" v-model="cnPassword" placeholder="enter the password again" class="w-50"></b-form-input>
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
      userName: 'gisutils',
      cPassowrd: 'abcde'
    }
  }
}
</script>

<style>
</style>

