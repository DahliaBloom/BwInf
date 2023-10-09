<template>
    <div class="h-full p-2 justify-around flex flex-col flex-wrap">
    <div class="flex flex-col">
        <button class="w-16 h-16 bg-red-600 rounded-lg border-4 my-2" :class="this.selectedBlock=='red'?'border-accent-400':'border-slate-600'" @click="chooseRed"> Red</button>
        <button class="w-16 h-16 bg-red-500 rounded-lg border-4 my-2" :class="this.selectedBlock=='red2'?'border-accent-400':'border-slate-600'" @click="chooseRed2"> Red 2</button>
    </div>
    <button class="w-16 h-16 bg-blue-600 rounded-lg border-4 " :class="this.selectedBlock=='blue'?'border-accent-400':'border-slate-600'" @click="chooseBlue">Blue</button>
    <button class="w-16 h-16 bg-slate-400 rounded-lg border-4 " :class="this.selectedBlock=='white'?'border-accent-400':'border-slate-600'" @click="chooseWhite">White</button>
</div>
</template>
  
  <script>
  export default {
    data() {
      return {
        selectedBlock: "red"
      };
    },
    methods: {
      chooseRed(){
        this.selectedBlock="red"
      },
      chooseRed2(){
        this.selectedBlock="red2"
      },
      chooseBlue(){
        this.selectedBlock="blue"
      },
      chooseWhite(){
        this.selectedBlock="white"
      }
    },
    watch: {
    selectedBlock(newColor) {
      this.$emit('color-updated', newColor);
    }
  }
}
  </script>
  
  <style scoped>
  </style>
  