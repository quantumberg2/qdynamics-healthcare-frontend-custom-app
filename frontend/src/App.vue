<template>
  <div>
    <!-- Navbar -->
    <Navbar />

    <!-- Add top padding to account for navbar height -->
    <div class="pt-[63px]">
      <router-view />
    </div>

    <Footer />

    <!-- Floating Buttons -->
    <BackToTop />
  </div>
</template>

<script setup>
import Navbar from './pages/Navbar.vue'
import Footer from './pages/Footer.vue'
import BackToTop from './pages/BackToTop.vue'
</script>

<style>
* {
  font-family: "robot0", sans-serif;
}
</style>
