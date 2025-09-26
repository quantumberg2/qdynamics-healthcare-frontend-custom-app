<template>
  <!-- Back to Top Button -->
  <button
    v-show="isVisible"
    @click="scrollToTop"
    class="fixed bottom-6 right-6 bg-sky-600 text-white p-2 rounded-full shadow-lg hover:bg-blue-700 transition"
  >
    <i class="fas fa-chevron-up"></i>
  </button>

  <!-- WhatsApp Button -->
  <a
    href="https://wa.me/919876543210" 
    target="_blank"
    class="fixed bottom-20 right-6 bg-green-500 text-white p-2 rounded-full shadow-lg hover:bg-green-600 transition"
  >
    <i class="fab fa-whatsapp"></i>
  </a>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const isVisible = ref(false)

const toggleVisibility = () => {
  isVisible.value = window.scrollY > 200
}

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

onMounted(() => {
  window.addEventListener('scroll', toggleVisibility)
})

onBeforeUnmount(() => {
  window.removeEventListener('scroll', toggleVisibility)
})
</script>
