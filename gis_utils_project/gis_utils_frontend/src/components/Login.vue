<template>
  <div id="login" class="d-flex flex-column">
    <div class="container-fluid">
      <GlobalMessage/>
    </div>
    <div class="container-fluid my-auto">
        <b-form class="form-signin" @submit.prevent="submitLogin">
        <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <b-form-input type="text" id="inputUsername" placeholder="Username" v-model="username" required autofocus>
            </b-form-input>
            <b-form-input type="password" id="inputPassword" placeholder="Password" v-model="password" required>
            </b-form-input>
        <b-button type="submit" variant="primary" class="btn-lg btn-block">Sign in</b-button>
        </b-form>
    </div>
  </div>
</template>

<script>
import GlobalMessage from '@/components/global/GlobalMessage'

export default {
  name: 'Login',
  components: {
    GlobalMessage
  },
  data: function() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitLogin: function() {
      this.$store.dispatch('authData/login', {username: this.username, password: this.password })
      this.$router.push({path: 'portal'})
    }
  }
}
</script>

<style scoped>
  #login {
    height: 100%;
  }

  #login {
    min-height: 100vh;
    -ms-flex-align: center;
    align-items: center;
    padding-bottom: 40px;
    background-color: #f5f5f5;
  }

  .form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
  }
  .form-signin .checkbox {
    font-weight: 400;
  }
  .form-signin .form-control {
    position: relative;
    box-sizing: border-box;
    height: auto;
    padding: 10px;
    font-size: 16px;
  }
  .form-signin .form-control:focus {
    z-index: 2;
  }
  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }
  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }
</style>
