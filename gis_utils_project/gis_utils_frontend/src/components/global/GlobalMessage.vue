<template>
  <!-- メッセージエリア -->
  <div id="global-message">
    <b-alert variant="danger" dismissible v-model="showError" show v-show="messageError" class="mb-0">
      {{ messageError }}
    </b-alert>
    <b-alert
      variant="warning" dismissible v-model="showWarnings" show v-show="messageWarnings.length > 0" class="mb-0">
      <p v-for="warning in messageWarnings" class="mb-0">{{ warning }}</p>
    </b-alert>
    <b-alert variant="info" dismissible v-model="showInfo" show v-show="messageInfo" class="mb-0">
      {{ messageInfo }}
    </b-alert>
  </div>
</template>

<script>
export default {
  name: 'GlobalMessage',
  data() {
    return {
      showError: true,
      showWarnings: true,
      showInfo: true
    }
  },
  computed: {
    messageError: function () {
      this.showError = true
      return this.$store.state.messageData.error
    },
    messageWarnings: function() {
      this.showWarnings = true
      return this.$store.state.messageData.warnings
    },
    messageInfo: function() {
      this.showInfo = true
      return this.$store.state.messageData.info
    }
  }
}
</script>
