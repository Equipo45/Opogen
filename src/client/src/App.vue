<style scoped>
.home {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

header {
  text-align: center;
  margin-bottom: 20px;
}

main {
  margin-bottom: 40px;
}

section {
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #0056b3;
}

footer {
  text-align: center;
  color: #666;
}
</style>

<template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

