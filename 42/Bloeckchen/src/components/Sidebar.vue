<template>
    <div class="h-full p-2 ml-2 justify-around flex flex-col flex-wrap">
    <div class="flex flex-col">
        <button class=" w-[120px] h-16 bg-red-700 rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='red'?'border-accent-400':'border-slate-600'" @click="chooseRed"><img src="../assets/red.png"><img src="../assets/darkred.png"></button>
        <button class=" w-[120px] h-16 bg-red-700 rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='red2'?'border-accent-400':'border-slate-600'" @click="chooseRed2"><img src="../assets/darkred.png"><img src="../assets/red.png"></button>
    </div>
    <button class="w-[120px] h-16 bg-blue-700 rounded-lg border-4 my-2 flex flex-row justify-center " :class="this.selectedBlock=='blue'?'border-accent-400':'border-slate-600'" @click="chooseBlue"><img src="../assets/blue.png"><img src="../assets/blue.png"></button>
    <button class="w-[120px] h-16 bg-white rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='white'?'border-accent-400':'border-slate-600'" @click="chooseWhite"><img src="../assets/white.png"><img src="../assets/white.png"></button>
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
  