<template>
  <div class="responsive-grid w-1/2 p-4" :style="'grid-template-columns: repeat(' + this.gridSize + ', 1fr);'">
    <div :class="'square border' + (squareColors[index] != '' ? 'border-none' : ' border-primary-400')"
      v-for="(content, index) in gridContent" :key="index" @mouseenter="handleMouseEnter(index)"
      @mouseleave="handleMouseLeave(index)" @click="handleClick(index)"
      :style="{ backgroundColor: (squareColors[index] == 'lightpink' | squareColors[index] == 'lightyellow' | squareColors[index] == 'lightgreen' | squareColors[index] == 'lightblue' | squareColors[index] == 'lightgray' | squareColors[index] == '' ? squareColors[index] : ''), border: none }">
      <div class="square-content">
        <img v-if="(squareColors[index] == 'white' || squareColors[index] == 'W' || squareColors[index] == 'DW')"
          class="w-full h-full scale-[1.03]" src="../assets/white.png" />
        <img v-if="(squareColors[index] == 'red' || squareColors[index] == 'R' || squareColors[index] == 'DR')"
          class="w-full h-full scale-[1.03]" src="../assets/red.png" />
        <img v-if="(squareColors[index] == 'darkred' || squareColors[index] == 'r' || squareColors[index] == 'Dr')"
          class="w-full h-full scale-[1.03]" src="../assets/darkred.png" />
        <img v-if="(squareColors[index] == 'blue' || squareColors[index] == 'B' || squareColors[index] == 'DB')"
          class="w-full h-full scale-[1.03]" src="../assets/blue.png" />
        <img v-if="(squareColors[index] == 'darkwhite' || squareColors[index] == 'w' || squareColors[index] == 'Dw')"
          class="w-full h-full scale-[1.03]" src="../assets/darkwhite.png" />
        <img v-if="(squareColors[index] == 'LW')" class="w-full h-full scale-[1.03]" src="../assets/whitelit.png" />
        <img v-if="(squareColors[index] == 'LR')" class="w-full h-full scale-[1.03]" src="../assets/redlit.png" />
        <img v-if="(squareColors[index] == 'Lr')" class="w-full h-full scale-[1.03]" src="../assets/darkredlit.png" />
        <img v-if="(squareColors[index] == 'LB')" class="w-full h-full scale-[1.03]" src="../assets/bluelit.png" />
        <img v-if="(squareColors[index] == 'Lw')" class="w-full h-full scale-[1.03]" src="../assets/darkwhitelit.png" />
        <button
          v-if="(squareColors[index] == 'yellow') || (squareColors[index][0] == 'D' && squareColors[index][1] == 'Q')"
          class="w-full h-full scale-[1.03]" @click="squareColors[index] = 'darkyellow'"><img
            src="../assets/yellow.png"></button>
        <button
          v-if="(squareColors[index] == 'darkyellow') || (squareColors[index][0] == 'L' && squareColors[index][1] == 'Q')"
          class="w-full h-full scale-[1.03]" @click="squareColors[index] = 'yellow'"><img
            src="../assets/yellowlit.png"></button>
        <button
          v-if="(squareColors[index] != '' && squareColors[index] != 'X' && (squareColors[index] == 'green' || (squareColors[index][0] == 'Q') || (squareColors[index][0] == 'D' && squareColors[index][1] == 'L')))"
          class="w-full h-full scale-[1.03]"><img src="../assets/green.png"></button>
        <button
          v-if="(squareColors[index] != '' && squareColors[index] != 'X' && (squareColors[index] == 'darkgreen' || (squareColors[index][0] == 'L' && squareColors[index][1] == 'L')))"
          class="w-full h-full scale-[1.03]"><img src="../assets/greenlit.png"></button>
        <p>{{ gridContent[index] }} {{ getSquareLabel(index) }}</p>
      </div>
    </div>
  </div>
  <div class="flex gap-4 flex-col pt-4">
    <div class="flex justify-around w-full">
      <button
        @click="console.log(this.squareColors); this.redoStack = []; this.undoStack.push(JSON.parse(JSON.stringify(this.squareColors)).map(item => ['lightpink', 'lightyellow', 'lightgreen', 'lightblue', 'lightgray'].includes(item) ? '' : item)); this.inViewState = true; this.applyLights(this.cutie(this.formatColors(this.squareColors))); this.calculateTable()"
        class="btn-primary btn">APPLY</button>
      <button v-if="this.undoStack.length > 0" @click="undo" class="btn-primary btn"><span
          class="material-symbols-outlined">
          undo
        </span></button>
      <button v-else @click="undo" class="btn-primary btn btn-disabled"><span class="material-symbols-outlined">
          undo
        </span></button>
      <button v-if="this.redoStack.length > 0" @click="redo" class="btn-primary btn"><span
          class="material-symbols-outlined">
          redo
        </span></button>
      <button v-else @click="redo" class="btn-primary btn btn-disabled"><span class="material-symbols-outlined">
          redo
        </span></button>
      <button @click="sliderChanged" class="btn-primary btn"><span class="material-symbols-outlined">
          disabled_by_default
        </span></button>
    </div>
    <div class="flex gap-4">
      <input type="range" min="2" max="32" class="range" step="1" v-model="gridSize" @input="sliderChanged" />{{
        this.gridSize }}
    </div>
    <InputField @file-uploaded="textUploaded"></InputField>
    <div class="overflow-x-auto rounded-lg border border-accent-200">
      <table class="table w-full ">
        <thead>
          <tr>
            <th v-for="(header, index) in this.headers()" :key="index" class="text-2xl">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, rowIndex) in this.parsedRows()" :key="rowIndex">
            <td v-for="(cell, cellIndex) in row" :key="cellIndex" :class="{ 'bg-yellow-200': cell === 'An' }">
              {{ cell }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import InputField from './inputField.vue';

export default {
  data() {
    return {
      gridSize: 16,
      gridContent: Array(16 * 16).fill(""),
      squareColors: Array(16 * 16).fill(""),
      undoStack: [],
      redoStack: [],
      inViewState: false,
      tableString: ""
    };
  },
  props: ['selectedColor'],
  methods: {
    headers() {
      let headerRow = this.tableString.split("\n")[0];
      return headerRow.split("|").map(h => h.trim()).filter(h => h);
    },
    parsedRows() {
      return this.tableString
        .split("\n")
        .slice(2) // Skip the header and separator
        .map(row =>
          row.split("|").map(cell => cell.trim()).filter(cell => cell)
        );
    },
    getSquareLabel(index) {
      const row = String.fromCharCode(65 + Math.floor(index / this.gridSize));
      const col = (index % this.gridSize) + 1;
      return `${row}${col}`;
    },
    textUploaded(text) {
      let l = text.split('\n').map(line => line.trim().split(' ').filter(word => word !== ''));
      let res = []

      this.gridSize = Number(l[0][0] > l[0][1] ? l[0][0] : l[0][1])
      this.sliderChanged()

      for (let y = 1; y < l.length - 1; y++) {
        let tmp = []
        for (let x = 0; x < l[y].length; x++) {
          if (l[y][x] == 'W') {
            tmp.push('W')
            l[y][x + 1] = 'w'
          }
          else if (l[y][x][0] == 'L') {
            tmp.push('D' + l[y][x])
          }
          else if (l[y][x][0] == 'Q') {
            tmp.push('D' + l[y][x])
          }
          else {
            tmp.push(l[y][x])
          }
        }
        while (tmp.length < this.gridSize) {
          tmp.push('X')
        }
        res.push(tmp)
      }
      while (res.length < this.gridSize) {
        res.push(Array(this.gridSize).fill("X"))
      }
      this.applyLights(res)
      this.undoStack.push(JSON.parse(JSON.stringify(this.squareColors)));
      this.inViewState = false;
      this.redoStack = [];
    },
    sliderChanged() {
      this.gridContent = Array(this.gridSize * this.gridSize).fill("");
      this.squareColors = Array(this.gridSize * this.gridSize).fill("");
      this.undoStack = [];
      this.redoStack = [];
      this.inViewState = false;
    },
    calculateTable() {
      let lights = []
      let outputs = []
      for (let i = 0; i < this.squareColors.length; i++) {
        if ((this.squareColors[i][0] == "L" || this.squareColors[i][0] == "D") && this.squareColors[i][1] == "Q") {
          lights.push([i, this.squareColors[i]])
        }
        if ((this.squareColors[i][0] == "L" || this.squareColors[i][0] == "D") && this.squareColors[i][1] == "L") {
          outputs.push([i, this.squareColors[i]])
        }
      }

      const combinations = Math.pow(2, lights.length);
      const table = [];
      let squareColorsClone = this.formatColors(JSON.parse(JSON.stringify(this.squareColors))).flat()

      console.log("squareColorsClone:")
      console.log(squareColorsClone)

      console.log("Lights:")
      console.log(lights)

      for (let i = 0; i < combinations; i++) {
        // Get binary string e.g., "01" for the combination
        const binaryString = i.toString(2).padStart(lights.length, '0');

        // Prepare squareColors for the current combination
        const squareColors = [];

        let squareColorsClone = this.formatColors(JSON.parse(JSON.stringify(this.squareColors))).flat()

        binaryString.split('').forEach((bit, index) => {
          if (bit == 0) {
            squareColorsClone[lights[index][0]] = `DQ${squareColorsClone[lights[index][0]].substring(2)}`;
          }
          else {
            squareColorsClone[lights[index][0]] = `LQ${squareColorsClone[lights[index][0]].substring(2)}`;
          }
        });

        let squareColorsCloneClone = []
        let y = []

        for (let l of squareColorsClone) {
          if (y.length == this.gridSize) {
            squareColorsCloneClone.push(y);
            y = [];
          }
          if ((l[0] == "L" || l[0] == "D") && (l[1] != "L" && l[1] != "Q")) {
            y.push(l[1])
          }
          else {
            y.push(l)
          }
        }
        squareColorsCloneClone.push(y)

        // Call cutie() and get the result for the current combination
        const cutieResult = this.cutie(squareColorsCloneClone).flat();
        console.log("cutieResult:")
        console.log(cutieResult)

        // Map the cutieResult to the outputs array format
        const outputStrings = outputs.map(output => cutieResult[output[0]]);

        // Store the combination and its corresponding outputs
        table.push({ combination: binaryString, outputs: outputStrings });
      }

      let tableString = "| "
      lights.forEach(light => tableString += light[1].slice(1) + " | ")
      outputs.forEach(light => tableString += light[1].slice(1) + " | ")
      tableString += "\n"
      outputs.forEach(light => tableString += "+-----")
      tableString += "+"

      for (let x of table) {
        tableString += "\n| "
        for (let b of x.combination.split("")) {
          tableString += ((b == "0" ? "Aus" : "An") + " | ")
        }
        console.log(x.outputs)
        for (let b of x.outputs) {
          tableString += (b[0] == "D" ? "Aus" : "An") + "| "
        }
      }

      console.log(tableString)

      this.tableString = tableString

      console.log(table)
    },
    handleMouseEnter(index) {
      // Change the color of the hovered square
      // Change the color of the square to the left
      const leftSquareIndex = index - 1;
      if (this.selectedColor == "yellow") {
        if (this.squareColors[index] == '') {
          this.squareColors.splice(index, 1, "lightyellow");
        }
      }
      else if (this.selectedColor == "green") {
        if (this.squareColors[index] == '') {
          this.squareColors.splice(index, 1, "lightgreen");
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
      if (this.selectedColor == "yellow" && this.squareColors[index] == "lightyellow") {
        this.squareColors.splice(index, 1, "");
      }
      else if (this.selectedColor == "green" && this.squareColors[index] == "lightgreen") {
        this.squareColors.splice(index, 1, "");
      }
      else if (this.isLegal(index, leftSquareIndex)) {
        this.squareColors.splice(leftSquareIndex, 1, "");
        this.squareColors.splice(index, 1, "");
      }
    },
    cutie(l) {
      console.log("cutie received:")
      console.log(l)
      for (let y = 0; y < l.length; y++) {
        for (let x = 0; x < l[y].length; x++) {
          if (l[y][x] == 'X') {
            //l[y][x]=''
          }
          else if (l[y][x][1] == 'L') {
            if (l[y - 1][x][0] == 'L') {
              l[y][x] = 'LL' + l[y][x].slice(2);
            }
            else {
              l[y][x] = 'DL' + l[y][x].slice(2);
            }
          }
          else if (l[y][x] == 'B') {
            if (l[y - 1][x][0] == 'L') {
              l[y][x] = 'LB';
            }
          }
          else if (l[y][x] == 'R') {
            if (l[y - 1][x][0] == 'L') {
              l[y][x] = 'DR';
              l[y][x + 1] = 'Dr';
            }
            else {
              l[y][x] = 'LR';
              l[y][x + 1] = 'Lr';
            }
          }
          else if (l[y][x] == 'r') {
            if (l[y - 1][x + 1][0] == 'L') {
              l[y][x] = 'Dr';
              l[y][x + 1] = 'DR';
            }
            else {
              l[y][x] = 'Lr';
              l[y][x + 1] = 'LR';
            }
          }
          else if (l[y][x] == 'W') {
            if (l[y - 1][x + 1][0] == 'L' && l[y - 1][x][0] == 'L') {
              l[y][x] = 'DW';
              l[y][x + 1] = 'Dw';
            }
            else {
              l[y][x] = 'LW';
              l[y][x + 1] = 'Lw';
            }
          }
        }
      }
      console.log("cutie has decided:")
      console.log(l)
      return l;
    },
    applyLights(l) {
      console.log(l)
      for (let y = 0; y < this.gridSize; y++) {
        for (let x = 0; x < this.gridSize; x++) {
          this.squareColors[y * this.gridSize + x] = (l[y][x][0] == 'L' ? l[y][x] : (l[y][x] == 'X' ? '' : l[y][x]));
        }
      }
    },
    handleClick(index) {
      if (this.inViewState) {
        this.squareColors = JSON.parse(JSON.stringify(this.undoStack.pop()));
        this.inViewState = false;
        this.undoStack = [];
        this.redoStack = [];
      }
      else {
        this.undoStack.push(JSON.parse(JSON.stringify(this.squareColors)).map(item => ['lightpink', 'lightyellow', 'lightgreen', 'lightblue', 'lightgray'].includes(item) ? '' : item));
      }
      console.log(this.cutie(this.formatColors(this.squareColors)));
      // Call the method when clicked
      this.clicked(index);
      this.redoStack = [];
    },
    undo() {
      if (this.undoStack.length > 0) {
        // Push the current state to redoStack
        this.redoStack.push(JSON.parse(JSON.stringify(this.squareColors)));
        // Pop the last state from undoStack and set it as current state
        this.squareColors = JSON.parse(JSON.stringify(this.undoStack.pop()));
      }
    },
    redo() {
      if (this.redoStack.length > 0) {
        // Push the current state to undoStack
        this.undoStack.push(JSON.parse(JSON.stringify(this.squareColors)));
        // Pop the last state from redoStack and set it as current state
        this.squareColors = JSON.parse(JSON.stringify(this.redoStack.pop()));
      }
    },
    hoveredOver(index) {
      // Implement your logic for when the square is hovered over
    },
    formatColors() {
      let tmp = [];
      let y = [];

      let i = 0;
      let j = 0;
      for (let l of this.squareColors) {
        if (y.length == this.gridSize) {
          tmp.push(y);
          y = [];
        }
        switch (l) {
          case 'red':
            y.push('R');
            break;
          case 'darkred':
            y.push('r');
            break;
          case 'blue':
            y.push('B');
            break;
          case 'white':
            y.push('W');
            break;
          case 'darkwhite':
            y.push('W');
            break;
          case 'yellow':
            y.push('DQ' + i);
            i++;
            break;
          case 'darkyellow':
            y.push('LQ' + i);
            i++;
            break;
          case 'darkgreen':
            y.push('LL' + j);
            j++;
            break;
          case 'green':
            y.push('DL' + j);
            j++;
            break;
          case '':
            y.push('X');
            break;
          default:
            y.push(l);
            break;
        }
      }
      tmp.push(y);
      return tmp;
    },
    isLegal(index, leftSquareIndex) {
      return (leftSquareIndex >= 0 && (this.squareColors[index] == "lightblue" || this.squareColors[index] == "lightpink" || this.squareColors[index] == "lightyellow" || this.squareColors[index] == "lightgreen" || this.squareColors[index] == "lightgray" || this.squareColors[index] == "") && (this.squareColors[leftSquareIndex] == "lightblue" || this.squareColors[leftSquareIndex] == "lightpink" || this.squareColors[leftSquareIndex] == "lightyellow" || this.squareColors[leftSquareIndex] == "lightgreen" || this.squareColors[leftSquareIndex] == "lightgray" || this.squareColors[leftSquareIndex] == "") && leftSquareIndex % this.gridSize != this.gridSize - 1);
    },
    lighterColor() {
      if (this.selectedColor == "blue") {
        return "lightblue";
      }
      else if (this.selectedColor == "red" || this.selectedColor == "red2") {
        return "lightpink";
      }
      else if (this.selectedColor == "white") {
        return "lightgray";
      }
      else if (this.selectedColor == "yellow") {
        return "lightyellow";
      }
      else if (this.selectedColor == "green") {
        return "lightgreen";
      }
    },
    getGrid() {
      let i = 0;
      let grid = [];
      for (let s of this.squareColors) {
        if (i % this.gridSize == 0) {
          grid.push([]);
        }
        grid[(i - (i % this.gridSize)) / this.gridSize].push(s);
        i -= -1;
      }
      return grid;
    },
    clicked(index) {
      // Implement your logic for when the square is clicked
      const leftSquareIndex = index - 1;
      if (this.selectedColor == "yellow") {
        if (this.squareColors[index] == 'lightyellow') {
          this.squareColors.splice(index, 1, "yellow");
        }
      }
      else if (this.selectedColor == "green") {
        if (this.squareColors[index] == 'lightgreen') {
          this.squareColors.splice(index, 1, "green");
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
  components: { InputField }
};
</script>

<style scoped>
.responsive-grid {
  display: grid;
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
