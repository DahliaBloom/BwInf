<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Sidebar from './components/Sidebar.vue';
</script>

<template>
    <Sidebar  @color-updated="updateSelectedColor" />
    <HelloWorld :selectedColor="selectedColor" class=" bg-slate-600"/>
</template>

<script>
export default {
  components: {
    Sidebar,
    HelloWorld
  },
  data() {
    return {
      selectedColor: "" // Default color
    };
  },
  methods: {
    updateSelectedColor(newColor) {
        console.log(newColor)
      this.selectedColor = newColor;
    }
  }
};
</script>

<style scoped>
</style>
