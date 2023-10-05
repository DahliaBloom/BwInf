<template>
    <button @click="chooseRed"> Red</button>
    <button @click="chooseBlue">Blue</button>
    <button @click="chooseWhite">White</button>
</template>
  
  <script>
  export default {
    data() {
      return {
        selectedBlock: ""
      };
    },
    methods: {
      chooseRed(){
        this.selectedBlock="red"
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
  