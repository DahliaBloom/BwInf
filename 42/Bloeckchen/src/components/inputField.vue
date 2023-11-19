<script setup>
import { onBeforeMount, ref, defineEmits } from 'vue'

const pgn = ref('')
const emit = defineEmits(['file-uploaded'])

function dropHandler(e) {
  e.preventDefault()

  const handleFileRead = (content) => {
    console.log(content)
    emit('file-uploaded', content)
  }

  if (e.dataTransfer.items) {
    // Use DataTransferItemList interface to access the file(s)
    [...e.dataTransfer.items].forEach((item, i) => {
      // If dropped items aren't files, reject them
      if (item.kind === 'file') {
        const reader = new FileReader()
        reader.onload = (ev) => handleFileRead(ev.target.result)
        reader.readAsText(item.getAsFile())
      }
    })
  } else {
    // Use DataTransfer interface to access the file(s)
    [...e.dataTransfer.files].forEach((file, i) => {
      const reader = new FileReader()
      reader.onload = (ev) => handleFileRead(ev.target.result)
      reader.readAsText(file)
    })
  }
}
</script>


<template>
  <div
    @drop="dropHandler($event)"
    @dragover.prevent
    @dragenter.prevent
    class="w-full h-32 input-primary input rounded-2xl mt-5 grid place-content-center bg-secondary-400"
  >
    <h3 class="text-lg font-bold">Drag your .txt input file here for upload🫶</h3>
  </div>
</template>
