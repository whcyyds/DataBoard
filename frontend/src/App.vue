<script setup lang="ts">
import Layout from './components/Layout.vue'
</script>

<template>
  <Layout />
</template>

<style>
/* 全局样式，确保全屏显示 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body {
  height: 100%;
  overflow: hidden;
}

#app {
  height: 100vh;
  width: 100vw;
}
</style>
