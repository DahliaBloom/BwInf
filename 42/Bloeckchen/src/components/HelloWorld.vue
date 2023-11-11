<template>
  <div class="responsive-grid w-1/2 p-4">
    <div :class="'square border' + (squareColors[index] != '' ? 'border-none' : ' border-primary-400')"
      v-for="(content, index) in gridContent" :key="index" @mouseenter="handleMouseEnter(index)"
      @mouseleave="handleMouseLeave(index)" @click="handleClick(index)"
      :style="{ backgroundColor: (squareColors[index] == 'lightpink' | squareColors[index] == 'lightyellow' | squareColors[index] == 'lightblue' | squareColors[index] == 'lightgray' | squareColors[index] == '' ? squareColors[index] : ''), border: none }">
      <div class="square-content">
        <img v-if="(squareColors[index] == 'white' || squareColors[index] == 'W')" class="w-full h-full scale-[1.03]"
          src="../assets/white.png" />
        <img v-if="(squareColors[index] == 'red' || squareColors[index] == 'R')" class="w-full h-full scale-[1.03]"
          src="../assets/red.png" />
        <img v-if="(squareColors[index] == 'darkred' || squareColors[index] == 'r')" class="w-full h-full scale-[1.03]"
          src="../assets/darkred.png" />
        <img v-if="(squareColors[index] == 'blue' || squareColors[index] == 'B')" class="w-full h-full scale-[1.03]"
          src="../assets/blue.png" />
        <img v-if="(squareColors[index] == 'darkwhite' || squareColors[index] == 'w')" class="w-full h-full scale-[1.03]"
          src="../assets/darkwhite.png" />
        <img v-if="(squareColors[index] == 'LW')" class="w-full h-full scale-[1.03]" src="../assets/whitelit.png" />
        <img v-if="(squareColors[index] == 'LR')" class="w-full h-full scale-[1.03]" src="../assets/redlit.png" />
        <img v-if="(squareColors[index] == 'Lr')" class="w-full h-full scale-[1.03]" src="../assets/darkredlit.png" />
        <img v-if="(squareColors[index] == 'LB')" class="w-full h-full scale-[1.03]" src="../assets/bluelit.png" />
        <img v-if="(squareColors[index] == 'Lw')" class="w-full h-full scale-[1.03]" src="../assets/darkwhitelit.png" />
        <img v-if="(squareColors[index] == 'yellow')" class="w-full h-full scale-[1.03]" src="../assets/yellow.png" />
        <p>{{ gridContent[index] }} {{ getSquareLabel(index) }}</p>
      </div>
    </div>
  </div>
  <button @click="this.applyLights(this.cutie(this.formatColors(this.squareColors)))"
    class="h-full w-full text-white">APPLY</button>
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

      if (this.selectedColor == "yellow") {
        console.log(this.squareColors[index])
        if (this.squareColors[index] == '') {
          this.squareColors.splice(index, 1, "lightyellow");
        }
      }
      else if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, this.lighterColor());
        this.squareColors.splice(index, 1, this.lighterColor());
      }

      // Call the method when hovered
      this.hoveredOver(index);
    },
    handleMouseLeave(index) {
      // Reset the color on mouse leave
      const leftSquareIndex = index - 1;
      if (this.selectedColor == "yellow" && this.squareColors[index]=="lightyellow") {
        this.squareColors.splice(index, 1, "");
      }
      else if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, "");
        this.squareColors.splice(index, 1, "");
        console.log("YEEEEt")
      }
    },
    cutie(l) {
      for (let y = l.length - 1; y >= 0; y--) {
        for (let x = 0; x < l[y].length; x++) {
          if (l[y][x] == 'X') {
            //l[y][x]=''
          }
          else if (l[y][x] == 'B') {
            if (l[y + 1][x][0] == 'L') {
              l[y][x] = 'LB'
            }
          }
          else if (l[y][x] == 'R') {
            if (l[y + 1][x][0] == 'L') {
              l[y][x] = 'DR'
              l[y][x + 1] = 'Dr'
            } else {
              l[y][x] = 'LR'
              l[y][x + 1] = 'Lr'
            }
          }
          else if (l[y][x] == 'r') {
            if (l[y + 1][x + 1][0] == 'L') {
              l[y][x] = 'Dr'
              l[y][x + 1] = 'DR'
            } else {
              l[y][x] = 'Lr'
              l[y][x + 1] = 'LR'
            }
          }
          else if (l[y][x] == 'W') {
            if (l[y + 1][x + 1][0] == 'L' && l[y + 1][x][0] == 'L') {
              l[y][x] = 'DW'
              l[y][x + 1] = 'Dw'
            } else {
              l[y][x] = 'LW'
              l[y][x + 1] = 'Lw'
            }
          }
        }
      }
      return l
    },
    applyLights(l) {
      for (let y = 0; y < this.gridSize; y++) {
        for (let x = 0; x < this.gridSize; x++) {
          this.squareColors[y * this.gridSize + x] = (l[y][x][0] == 'L' ? l[y][x] : (l[y][x] == 'X' ? '' : l[y][x][1]))
        }
      }
      console.log(this.squareColors)
    },
    handleClick(index) {

      console.log(this.cutie(this.formatColors(this.squareColors)))
      // Call the method when clicked
      this.clicked(index);
    },
    hoveredOver(index) {
      // Implement your logic for when the square is hovered over
      console.log("Square hovered over:", index);
    },
    formatColors() {
      let tmp = []
      let y = []
      for (let l of this.squareColors) {
        if (y.length == this.gridSize) {
          tmp.push(y)
          y = []
        }
        switch (l) {
          case 'red': y.push('R'); break;
          case 'darkred': y.push('r'); break;
          case 'blue': y.push('B'); break;
          case 'white': y.push('W'); break;
          case 'darkwhite': y.push('W'); break;
          case 'yellow': y.push('LL'); break;
          default: y.push('X'); break;
        }
      }
      tmp.push(y)
      console.log(tmp)
      return tmp
    },
    isLegal(index, leftSquareIndex) {
      return (leftSquareIndex >= 0 && (this.squareColors[index] == "lightblue" || this.squareColors[index] == "lightpink" || this.squareColors[index] == "lightyellow" || this.squareColors[index] == "lightgray" || this.squareColors[index] == "") && (this.squareColors[leftSquareIndex] == "lightblue" || this.squareColors[leftSquareIndex] == "lightpink" || this.squareColors[leftSquareIndex] == "lightyellow" || this.squareColors[leftSquareIndex] == "lightgray" || this.squareColors[leftSquareIndex] == "") && leftSquareIndex % 16 != 15)
    },
    lighterColor() {
      if (this.selectedColor == "blue") {
        return "lightblue"
      }
      else if (this.selectedColor == "red" || this.selectedColor == "red2") {
        return "lightpink"
      }
      else if (this.selectedColor == "white") {
        return "lightgray"
      }
      else if (this.selectedColor == "yellow") {
        return "lightyellow"
      }
    },
    getGrid() {
      let i = 0;
      let grid = []
      for (let s of this.squareColors) {
        if (i % 16 == 0) {
          grid.push([])
        }
        grid[(i - (i % 16)) / 16].push(s)
        i -= -1
      }
      return grid
    },
    clicked(index) {
      console.log(this.getGrid())
      // Implement your logic for when the square is clicked
      console.log("Square clicked:", index);
      const leftSquareIndex = index - 1;
      if (this.selectedColor=="yellow"){
        console.log(this.squareColors[index])
        if (this.squareColors[index] == 'lightyellow') {
          this.squareColors.splice(index, 1, "yellow");
        }
      }
      else if (this.isLegal(index, leftSquareIndex)) {
        if (this.selectedColor == "red" || this.selectedColor == "white") {
          this.squareColors.splice(leftSquareIndex, 1, this.selectedColor);
          this.squareColors.splice(index, 1, "dark" + this.selectedColor);
        }
        else if (this.selectedColor == "red2") {
          this.squareColors.splice(leftSquareIndex, 1, "darkred");
          this.squareColors.splice(index, 1, "red");
        }
        else if (this.selectedColor == "white2") {
          this.squareColors.splice(leftSquareIndex, 1, "darkwhite");
          this.squareColors.splice(index, 1, "white");
        }
        else {
          this.squareColors.splice(leftSquareIndex, 1, this.selectedColor);
          this.squareColors.splice(index, 1, this.selectedColor);
        }
      }
    },
  },
};
</script>

<style scoped>
.responsive-grid {
  display: grid;
  grid-template-columns: repeat(16, 1fr);
  gap: 0px;
  height: fit-content;
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
  padding-top: 100%;
  /* Create the square */
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
