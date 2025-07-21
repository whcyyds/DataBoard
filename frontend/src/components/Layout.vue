<template>
  <div class="layout">
    <aside class="sidebar">
      <div class="logo">数据看板</div>
      <ul class="menu">
        <li :class="{active: selected==='line'}" @click="selected='line'">折线图</li>
        <li :class="{active: selected==='dashboard'}" @click="selected='dashboard'">数据大屏</li>
      </ul>
    </aside>
    <main class="content">
      <HelloWorld v-if="selected==='line'" />
      <Dashboard v-else />
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import HelloWorld from './HelloWorld.vue'
import Dashboard from './Dashboard.vue'

const selected = ref<'line'|'dashboard'>('dashboard')
</script>
    
<style scoped> 
.layout {
  display: flex;
  height: 100vh;
  width: 100vw;
  background: #181c2a;
  color: #fff;
  font-family: 'Segoe UI', 'Arial', sans-serif;
  position: fixed;
  top: 0;
  left: 0;
}
.sidebar {
  width: 200px;
  background: linear-gradient(180deg, #232946 0%, #181c2a 100%);
  box-shadow: 2px 0 8px #0004;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 32px;
}
.logo {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 40px;
  letter-spacing: 2px;
  color: #3be8b0;
  text-shadow: 0 0 8px #3be8b088;
}
.menu {
  list-style: none;
  padding: 0;
  width: 100%;
}
.menu li {
  padding: 16px 0;
  text-align: center;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  font-size: 1.1rem;
  letter-spacing: 1px;
}
.menu li.active, .menu li:hover {
  background: #3be8b022;
  color: #3be8b0;
}
.content {
  flex: 1;
  
  overflow: auto;
}
</style> 