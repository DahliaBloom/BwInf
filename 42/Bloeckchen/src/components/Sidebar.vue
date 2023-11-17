<template>
    <div class="h-full p-2 ml-2 justify-around flex flex-col flex-wrap">
    <div class="flex flex-col">
        <button class=" w-[120px] h-16 bg-red-700 rounded-lg border-4 my-2 flex flex-row justify-center " :class="this.selectedBlock=='red'?'border-accent-400':'border-slate-600'" @click="chooseRed"><img class="max-h-full max-w-full" src="../assets/red.png"><img class="max-h-full max-w-full" src="../assets/darkred.png"></button>
        <button class=" w-[120px] h-16 bg-red-700 rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='red2'?'border-accent-400':'border-slate-600'" @click="chooseRed2"><img class="max-h-full max-w-full" src="../assets/darkred.png"><img class="max-h-full max-w-full" src="../assets/red.png"></button>
    </div>
    <button class="w-[120px] h-16 bg-blue-700 rounded-lg border-4 my-2 flex flex-row justify-center " :class="this.selectedBlock=='blue'?'border-accent-400':'border-slate-600'" @click="chooseBlue"><img class="max-h-full max-w-full" src="../assets/blue.png"><img class="max-h-full max-w-full" src="../assets/blue.png"></button>
    
    <button class="w-[120px] h-16 bg-white rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='white'?'border-accent-400':'border-slate-600'" @click="chooseWhite"><img class="max-h-full max-w-full" src="../assets/white.png"><img class="max-h-full max-w-full" src="../assets/darkwhite.png"></button>

    <button class="w-[120px] h-16 bg-yellow-300 rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='yellow'?'border-accent-400':'border-slate-600'" @click="chooseYellow"><img class="max-h-full max-w-full" src="../assets/yellow.png"></button>
    <button class="w-[120px] h-16 bg-yellow-300 rounded-lg border-4 my-2 flex flex-row justify-center" :class="this.selectedBlock=='green'?'border-accent-400':'border-slate-600'" @click="chooseGreen"><img class="max-h-full max-w-full" src="../assets/greenlit.png"></button>

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
      },
      chooseYellow(){
        this.selectedBlock="yellow"
      },
      chooseGreen(){
        this.selectedBlock="green"
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
  