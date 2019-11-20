<template>
  <div id="account">
    <b-modal id="modal-create-account-confirm" title="確認" @show="reValidate()" @ok="submit">
      <!-- @showは、確認ダイアログが表示される際に、パスワードのvalidateがエラーになってしまうため、ダイアログを表示する際に再度validateを実行する。 -->
      <p>アカウントを登録してもよろしいでしょうか？</p>
    </b-modal>
    <div class="container-fluid">
      <GlobalMessage/>
    </div>
    <div class="row">
      <div class="col-4 mt-5 pl-5">
        Create Account
      </div>
      <div class="col-8 mt-5">
        <validation-observer v-slot="{ invalid }">
          <div class="mb-2">
            <label for="username">Username</label>
          </div>
          <div class="mb-3">
            <validation-provider v-slot="{ errors }" rules="required|alpha_dash|max:50" name="Username">
              <b-form-input type="text" id="username" v-model="userName" class="w-50"></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-2">
            <label for="password">Password</label>
          </div>
          <div class="mb-3">
            <validation-provider v-slot="{ errors }" rules="required|alpha_dash|min:8|max:50|password:ConfirmPassword" name="Password" ref="vPassword">
              <b-form-input type="password" id="password" v-model="password" placeholder="enter a password" class="w-50" v-b-tooltip.hover title="Password must be 8 or more characters."></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-2">
            <label for="cPassword">Confirm Password</label>
          </div>
          <div class="mb-4">
            <validation-provider v-slot="{ errors }" rules="required|alpha_dash|min:8|max:50" name="ConfirmPassword">
              <b-form-input type="password" id="cPassword" v-model="cPassword" placeholder="enter the password again" class="w-50"></b-form-input>
              <p v-show="errors.length" class="alert alert-danger w-50">
                {{ errors[0] }}
              </p>
            </validation-provider>
          </div>
          <div class="mb-3">
            <b-button id="caButton" variant="primary" :disabled="invalid" @click="showCreateAccountModal">Create Account</b-button>
          </div>
        </validation-observer>
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
  name: 'Account',
  components: {
    GlobalMessage,
    ValidationProvider,
    ValidationObserver
  },
  data: function () {
    return {
      userName: '',
      password: '',
      cPassword: '',
    }
  },
  methods: {
    showCreateAccountModal: function() {
      this.$bvModal.show('modal-create-account-confirm')
    },
    reValidate: function() {
      this.$refs.vPassword.validate()
    },
    submit: function() {
        api.post('/api/auth/users/', {
            'username': this.userName,
            'password': this.password
        }).then(response => {
          this.$store.dispatch('messageData/setInfoMessage', { message: 'userが正常に登録されました。' })
        })
    }
  }
}
</script>

<style scoped>

  #account {
    overflow-y: auto;
    overflow-x: hidden;
    height: 80vh;
  }

</style>
