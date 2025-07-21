<script setup lang="ts">
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

// 发货统计数据
const totalMeters = ref(125680)
const totalAmount = ref(2568000)
const salesData = ref([
  { name: '张三', yesterday: 1250, today: 1380 },
  { name: '李四', yesterday: 980, today: 1120 },
  { name: '王五', yesterday: 1560, today: 1420 },
  { name: '赵六', yesterday: 890, today: 1050 },
  { name: '钱七', yesterday: 1340, today: 1280 }
])

const chartRef = ref<HTMLElement | null>(null)
let chartInstance: any = null

function renderChart() {
  if (!chartRef.value) return
  if (!chartInstance) chartInstance = echarts.init(chartRef.value)
  
  const option = {
    title: {
      text: '业务员发货统计',
      left: 'center',
      textStyle: { 
        color: '#00ffff',
        fontSize: 18,
        fontWeight: 'bold'
      }
    },
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    legend: {
      data: ['昨天', '今天'],
      bottom: 10,
      textStyle: { color: '#fff' }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '15%',
      top: '15%',
      containLabel: true
    },
    xAxis: {
      type: 'category',
      data: salesData.value.map(item => item.name),
      axisLine: { lineStyle: { color: '#00ffff' } },
      axisLabel: { color: '#fff' }
    },
    yAxis: {
      type: 'value',
      axisLine: { lineStyle: { color: '#00ffff' } },
      axisLabel: { color: '#fff' },
      splitLine: { lineStyle: { color: 'rgba(0,255,255,0.1)' } }
    },
    series: [
      {
        name: '昨天',
        type: 'bar',
        data: salesData.value.map(item => item.yesterday),
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#00ffff' },
            { offset: 1, color: 'rgba(0,255,255,0.3)' }
          ])
        }
      },
      {
        name: '今天',
        type: 'bar',
        data: salesData.value.map(item => item.today),
        itemStyle: {
          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
            { offset: 0, color: '#ff6b6b' },
            { offset: 1, color: 'rgba(255,107,107,0.3)' }
          ])
        }
      }
    ],
    backgroundColor: 'transparent'
  }
  
  chartInstance.setOption(option)
}

onMounted(() => {
  renderChart()
  window.addEventListener('resize', () => {
    chartInstance && chartInstance.resize()
  })
})
</script>

<template>
  <div class="dashboard">
    <!-- 左侧面板 -->
    <div class="left-panel">
      <div class="panel-title">系统概览</div>
      <div class="panel-content">
        <div class="info-card">
          <div class="info-icon">📊</div>
          <div class="info-text">待处理订单</div>
          <div class="info-value">156</div>
        </div>
        <div class="info-card">
          <div class="info-icon">🚚</div>
          <div class="info-text">在途货物</div>
          <div class="info-value">89</div>
        </div>
      </div>
    </div>

    <!-- 中间面板 - 发货统计 -->
    <div class="center-panel">
      <div class="stats-header">
        <div class="stat-card">
          <div class="stat-icon">📏</div>
          <div class="stat-content">
            <div class="stat-label">总发货米数</div>
            <div class="stat-value">{{ totalMeters.toLocaleString() }}</div>
          </div>
        </div>
        <div class="stat-card">
          <div class="stat-icon">💰</div>
          <div class="stat-content">
            <div class="stat-label">总发货金额</div>
            <div class="stat-value">¥{{ (totalAmount / 10000).toFixed(1) }}万</div>
          </div>
        </div>
      </div>
      
      <div class="chart-container">
        <div ref="chartRef" class="chart"></div>
      </div>
    </div>

    <!-- 右侧面板 -->
    <div class="right-panel">
      <div class="panel-title">实时监控</div>
      <div class="panel-content">
        <div class="monitor-item">
          <div class="monitor-label">系统状态</div>
          <div class="monitor-value online">在线</div>
        </div>
        <div class="monitor-item">
          <div class="monitor-label">数据库</div>
          <div class="monitor-value online">正常</div>
        </div>
        <div class="monitor-item">
          <div class="monitor-label">网络延迟</div>
          <div class="monitor-value">12ms</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  display: flex;
  height: 100%;
  gap: 20px;
  padding: 20px;
    background: 
    linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)),
    url('/images/background.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
  position: relative;
  overflow: hidden;
}

.dashboard::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
  radial-gradient(circle at 50% 50%, transparent 0%, rgba(0, 0, 0, 0.4) 100%);
  pointer-events: none;
  z-index: 0;
}

.dashboard > * {
  position: relative;
  z-index: 1;
}

/* 左侧面板 */
.left-panel {
  width: 280px;
  background: rgba(0, 255, 255, 0.05);
  border: 1px solid rgba(0, 255, 255, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  padding: 20px;
}

.panel-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #00ffff;
  margin-bottom: 20px;
  text-align: center;
  text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.panel-content {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.info-card {
  background: rgba(0, 255, 255, 0.1);
  border-radius: 10px;
  padding: 15px;
  text-align: center;
  border: 1px solid rgba(0, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.info-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 255, 255, 0.3);
}

.info-icon {
  font-size: 2rem;
  margin-bottom: 10px;
}

.info-text {
  color: #ccc;
  font-size: 0.9rem;
  margin-bottom: 5px;
}

.info-value {
  color: #00ffff;
  font-size: 1.5rem;
  font-weight: bold;
  text-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

/* 中间面板 */
.center-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.stats-header {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.stat-card {
  background: linear-gradient(135deg, rgba(0, 255, 255, 0.1) 0%, rgba(255, 107, 107, 0.1) 100%);
  border: 1px solid rgba(0, 255, 255, 0.3);
  border-radius: 15px;
  padding: 25px;
  display: flex;
  align-items: center;
  gap: 15px;
  min-width: 200px;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 255, 255, 0.3);
}

.stat-icon {
  font-size: 2.5rem;
  filter: drop-shadow(0 0 10px rgba(0, 255, 255, 0.5));
}

.stat-content {
  flex: 1;
}

.stat-label {
  color: #ccc;
  font-size: 0.9rem;
  margin-bottom: 5px;
}

.stat-value {
  color: #00ffff;
  font-size: 1.8rem;
  font-weight: bold;
  text-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
}

.chart-container {
  flex: 1;
  background: rgba(0, 255, 255, 0.05);
  border: 1px solid rgba(0, 255, 255, 0.2);
  border-radius: 15px;
  padding: 20px;
  backdrop-filter: blur(10px);
}

.chart {
  width: 100%;
  height: 100%;
  min-height: 400px;
}

/* 右侧面板 */
.right-panel {
  width: 280px;
  background: rgba(255, 107, 107, 0.05);
  border: 1px solid rgba(255, 107, 107, 0.2);
  border-radius: 15px;
  backdrop-filter: blur(10px);
  padding: 20px;
}

.monitor-item {
  background: rgba(255, 107, 107, 0.1);
  border-radius: 10px;
  padding: 15px;
  margin-bottom: 15px;
  border: 1px solid rgba(255, 107, 107, 0.3);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.monitor-label {
  color: #ccc;
  font-size: 0.9rem;
}

.monitor-value {
  color: #ff6b6b;
  font-weight: bold;
  text-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
}

.monitor-value.online {
  color: #00ff88;
  text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
}

/* 动画效果 */
@keyframes glow {
  0%, 100% { box-shadow: 0 0 5px rgba(0, 255, 255, 0.3); }
  50% { box-shadow: 0 0 20px rgba(0, 255, 255, 0.6); }
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; }
  50% { opacity: 1; }
}

.stat-card {
  animation: glow 3s ease-in-out infinite;
}

.stat-card:nth-child(2) {
  animation-delay: 1.5s;
}

.info-card {
  animation: float 4s ease-in-out infinite;
}

.info-card:nth-child(2) {
  animation-delay: 2s;
}

.monitor-item {
  animation: pulse 3s ease-in-out infinite;
}

.monitor-item:nth-child(2) {
  animation-delay: 1s;
}

.monitor-item:nth-child(3) {
  animation-delay: 2s;
}
</style> 