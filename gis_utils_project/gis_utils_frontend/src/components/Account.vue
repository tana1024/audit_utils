<template>
  <div id="account">
    <div class="row">
      <div class="col-4 mt-5 pl-5">
        Create Account
      </div>
      <div class="col-8 mt-5">
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
          <validation-provider v-slot="{ errors }" rules="required|alpha_dash|max:50" name="Password">
            <b-form-input type="password" id="password" v-model="password" placeholder="enter a password" class="w-50" v-b-tooltip.hover title="Password must be 8 or more characters."></b-form-input>
            <p v-show="errors.length" class="alert alert-danger w-50">
              {{ errors[0] }}
            </p>
          </validation-provider>
        </div>
        <div class="mb-2">
          <label for="c-password">Confirm Password</label>
        </div>
        <div class="mb-4">
          <validation-provider v-slot="{ errors }" rules="required|alpha_dash|max:50" name="Confirm Password">
            <b-form-input type="password" id="c-password" v-model="cPassword" placeholder="enter the password again" class="w-50"></b-form-input>
            <p v-show="errors.length" class="alert alert-danger w-50">
              {{ errors[0] }}
            </p>
          </validation-provider>
        </div>
        <div class="mb-3">
          <b-button id="ca-button" variant="primary">Create Account</b-button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ValidationProvider, ValidationObserver, localize, extend } from 'vee-validate'
import ja from 'vee-validate/dist/locale/ja.json'
import * as rules from 'vee-validate/dist/rules'

for (let rule in rules) {
  extend(rule, rules[rule])
}

localize('ja', ja)

export default {
  name: 'Account',
  components: {
    ValidationProvider,
    ValidationObserver
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
