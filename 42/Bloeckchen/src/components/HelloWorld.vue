<template>
  <div class="responsive-grid w-1/2">
    <div
      class="square border border-secondary-300"
      v-for="(content, index) in gridContent"
      :key="index"
      @mouseenter="handleMouseEnter(index)"
      @mouseleave="handleMouseLeave(index)"
      @click="handleClick(index)"
      :style="{ backgroundColor: squareColors[index] }"
    >
      <div class="square-content">
        <p>{{ gridContent[index] }} {{ getSquareLabel(index) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      gridSize: 16,
      gridContent: Array(16 * 16).fill(""),
      squareColors: Array(16 * 16).fill(""),
    };
  },
  props: ['selectedColor'],
  methods: {
    getSquareLabel(index) {
      const row = String.fromCharCode(65 + Math.floor(index / this.gridSize));
      const col = (index % this.gridSize) + 1;
      return `${row}${col}`;
    },
    handleMouseEnter(index) {
      // Change the color of the hovered square

      // Change the color of the square to the left
      const leftSquareIndex = index - 1;
      if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, this.lighterColor());
        this.squareColors.splice(index, 1, this.lighterColor());
      }

      // Call the method when hovered
      this.hoveredOver(index);
    },
    handleMouseLeave(index) {
      // Reset the color on mouse leave
      const leftSquareIndex = index - 1;
      if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, "");
        this.squareColors.splice(index, 1, "");
        console.log("YEEEEt")
      }
    },
    handleClick(index) {
      // Call the method when clicked
      this.clicked(index);
    },
    hoveredOver(index) {
      // Implement your logic for when the square is hovered over
      console.log("Square hovered over:", index);
    },
    isLegal(index, leftSquareIndex){
      return (leftSquareIndex >= 0 && (this.squareColors[index]=="lightblue" || this.squareColors[index] == "lightpink" || this.squareColors[index] == "lightgray" || this.squareColors[index]=="") && (this.squareColors[leftSquareIndex]=="lightblue" ||this.squareColors[leftSquareIndex]=="lightpink" || this.squareColors[leftSquareIndex]=="lightgray" || this.squareColors[leftSquareIndex]=="") && leftSquareIndex%16!=15)
    },
    lighterColor() {
      if (this.selectedColor=="blue"){
        return "lightblue"
      }
      else if (this.selectedColor=="red"){
        return "lightpink"
      }
      else if (this,this.selectedColor=="white"){
        return "lightgray"
      }
    },
    clicked(index) {
      // Implement your logic for when the square is clicked
      console.log("Square clicked:", index);
      const leftSquareIndex = index - 1;
      if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, this.selectedColor);
        this.squareColors.splice(index, 1, this.selectedColor);
      }
    },
  },
};
</script>

<style scoped>
.responsive-grid {
  display: grid;
  grid-template-columns: repeat(16, 1fr);
  gap: 5px;
}

.square {
  position: relative;
  width: 100%;
  aspect-ratio: 1/1;
  overflow: hidden;
}

.square::before {
  content: "";
  display: block;
  padding-top: 100%; /* Create the square */
}

.square-content {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}
</style>
