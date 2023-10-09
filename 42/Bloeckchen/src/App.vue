<script setup>
import HelloWorld from './components/HelloWorld.vue'
import Sidebar from './components/Sidebar.vue';
</script>

<template>
    <div class="h-full w-full flex flex-row ">
    <Sidebar  @color-updated="updateSelectedColor" class=" h-screen"/>
    <HelloWorld :selectedColor="selectedColor" class=" bg-slate-600"/>
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
