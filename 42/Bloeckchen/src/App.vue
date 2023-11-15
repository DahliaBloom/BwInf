<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Sidebar from './components/Sidebar.vue';
</script>

<template>
    <div class=" h-full w-full flex flex-row bg-background-900">
    <Sidebar  @color-updated="updateSelectedColor" class=" h-screen border-secondary-400 rounded-2xl border mr-2"/>
    <HelloWorld :selectedColor="selectedColor" class=" border-secondary-400 rounded-2xl border"/>
    </div>
</template>

<script>
export default {
  components: {
    Sidebar,
    HelloWorld
  },
  data() {
    return {
      selectedColor: "red" // Default color
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
