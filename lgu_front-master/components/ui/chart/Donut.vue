<!-- components/ui/chart/DonutChart.vue -->
<template>

  
  <div>
    <svg :width="size" :height="size" viewBox="0 0 32 32">
      <circle
        v-for="(item, index) in data"
        :key="index"
        :r="radius"
        :cx="center"
        :cy="center"
        :stroke="colors[index]"
        :stroke-width="strokeWidth"
        :stroke-dasharray="getDashArray(item.value)"
        :transform="getTransform(index)"
        fill="none"
      />
      <text
        :x="center"
        :y="center"
        class="text-center"
        font-size="10"
        text-anchor="middle"
        dominant-baseline="middle"
      >
        {{ totalCount }}
      </text>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { defineProps, computed } from 'vue'

const props = defineProps<{
  data: Array<{ name: string; value: number }>;
  colors: string[];
  size?: number;
  strokeWidth?: number;
}>()

const totalCount = computed(() => {
  return props.data.reduce((total, item) => total + item.value, 0)
})

const center = 16 // Center of the SVG
const radius = 14 // Radius of the circle
const strokeWidth = props.strokeWidth || 4 // Default stroke width

const getDashArray = (value: number) => {
  const total = totalCount.value
  return total ? `${(value / total) * (2 * Math.PI * radius)} ${2 * Math.PI * radius}` : `0 ${2 * Math.PI * radius}`
}

const getTransform = (index: number) => {
  const angle = props.data.slice(0, index).reduce((acc, item) => acc + (item.value / totalCount.value) * 360, 0)
  return `rotate(${angle} ${center} ${center})`
}
</script>

<style scoped>
.text-center {
  fill: black;
}
</style>
