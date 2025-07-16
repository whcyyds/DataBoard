<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

const chartRef = ref<HTMLElement | null>(null)
const chartInstance = ref<any>(null)
const xData = ref<string[]>([])
const yData = ref<number[]>([])

async function fetchData() {
  const res = await fetch('http://localhost:8000/api/data')
  const data = await res.json()
  xData.value = data.x
  yData.value = data.y
  renderChart()
}



function renderChart() {
  if (!chartRef.value) return
  if (!chartInstance.value) {
    chartInstance.value = echarts.init(chartRef.value)
  }
  chartInstance.value.setOption({
    title: { text: '数据看板示例' },
    tooltip: {},
    xAxis: { data: xData.value },
    yAxis: {},
    series: [{
      name: '数值',
      type: 'line',
      data: yData.value
    }]
  })
}

onMounted(() => {
  fetchData()
  window.addEventListener('resize', () => {
    chartInstance.value && chartInstance.value.resize()
  })
})
</script>

<template>
  <h1>数据看板</h1>
  <div ref="chartRef" style="width: 1200px; height: 800px;"></div>
</template>

<style scoped>
</style>
