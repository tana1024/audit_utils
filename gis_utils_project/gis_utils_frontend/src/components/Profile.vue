<template>
  <div id="profile">
    <b-modal id="modal-update-password-confirm" title="確認" @ok="submitUpdatePassword">
      <p>パスワードを更新してもよろしいでしょうか？</p>
    </b-modal>
    <div class="container-fluid">
      <GlobalMessage/>
    </div>
    <div id="scroll-area">
      <div class="row">
        <div class="col-4 mt-5 pl-5">
          Profile
        </div>
        <div class="col-8 mt-5">
          <div class="mb-2">
            <label for="username">Username</label>
          </div>
          <div class="mb-3">
            <b-form-input id="username" v-model="userName" disabled class="w-50"></b-form-input>
          </div>
        </div>
      </div>
      <hr>
      <div class="row">
        <div class="col-4 mt-3 pl-5">
          Update Password
        </div>
        <div class="col-8 mt-3">
          <div class="mb-2">
            <label for="cPassword">Current Password</label>
          </div>
          <div class="mb-3">
            <validation-provider v-slot="{ errors }" rules="required" name="CurrentPassword">
              <b-form-input id="cPassword" type="password" v-model="cPassword" placeholder="enter current your password" class="w-50"></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-2">
            <label for="nPassword">New Password</label>
          </div>
          <div class="mb-3">
            <validation-provider v-slot="{ errors }" rules="required|alpha_dash|min:8|max:50|password:ConfirmNewPassword" name="NewPassword" ref="vnPassword">
              <b-form-input id="nPassword" type="password" v-model="nPassword" placeholder="enter a new password" class="w-50" v-b-tooltip.hover title="Password must be 8 or more characters."></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-2">
            <label for="cnPassword">Confirm New Password</label>
          </div>
          <div class="mb-4">
            <validation-provider v-slot="{ errors }" rules="required|alpha_dash|min:8|max:50" name="ConfirmNewPassword">
              <b-form-input id="cnPassword" type="password" v-model="cnPassword" placeholder="enter the password again" class="w-50"></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-3">
            <b-button id="cpButton" variant="primary" @click="showUpdatePasswordModal">Update Password</b-button>
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
  </div>
</template>
<script>
import GlobalMessage from '@/components/global/GlobalMessage'
import api from '@/services/api'
import { ValidationProvider, ValidationObserver, localize, extend } from 'vee-validate'
import ja from 'vee-validate/dist/locale/ja.json'
import * as rules from 'vee-validate/dist/rules'

for (let rule in rules) {
  extend(rule, rules[rule])
}
extend('password', {
  validate: (value, { other }) => value === other,
  message: 'The password confirmation does not match.',
  params: [{ name: 'other', isTarget: true }]
});

localize('ja', ja)

export default {
  name: 'Profile',
  components: {
    GlobalMessage,
    ValidationProvider,
    ValidationObserver
  },
  data: function() {
    return {
      userName: this.$store.state.authData.username,
      cPassword: '',
      nPassword: '',
      cnPassword: ''
    }
  },
  methods: {
    showUpdatePasswordModal: function() {
      this.$bvModal.show('modal-update-password-confirm')
    },
    submitUpdatePassword: function() {
        api.post('/api/auth/users/set_password/', {
            'new_password': this.nPassword,
            're_new_password': this.cnPassword,
            'current_password': this.cPassword
        }).then(response => {
          this.$store.dispatch('messageData/setInfoMessage', { message: 'パスワードが正常に更新されました。' })
        })
    }
  }
}
</script>

<style scoped>

  #scroll-area {
    overflow-y: auto;
    overflow-x: hidden;
    height: 80vh;
  }

</style>

