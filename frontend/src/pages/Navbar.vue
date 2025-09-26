<template>
  <div class="container-fluid">
    <header class="fixed top-0 left-0 w-full z-50">
      <!-- Top Header -->
      <div class="flex items-center justify-between bg-white px-[30px] sm:px-[150px] py-1">
        <!-- Logo -->
        <RouterLink to="/" class="no-underline">
          <div class="text-[28px] font-bold tracking-wide cursor-pointer">
            <span class="text-gray-800">HEALTH</span
            ><span class="text-sky-600">CARE</span>
          </div>
        </RouterLink>

        <!-- Contact Info (hidden on small screens) -->
        <div class="hidden lg:flex space-x-12 text-sm font-medium">
          <!-- Emergency -->
          <div class="flex items-center space-x-2">
            <i class="fas fa-phone-volume text-sky-600 text-xl"></i>
            <div>
              <p class="text-xs text-gray-600">EMERGENCY</p>
              <p class="text-sky-600">(237) 681-812-255</p>
            </div>
          </div>

          <!-- Work Hour -->
          <div class="flex items-center space-x-2">
            <i class="fas fa-clock text-sky-600 text-xl"></i>
            <div>
              <p class="text-xs text-gray-600">WORK HOUR</p>
              <p class="text-sky-600">09:00 - 20:00 Everyday</p>
            </div>
          </div>

          <!-- Location -->
          <div class="flex items-center space-x-2">
            <i class="fas fa-map-marker-alt text-sky-600 text-xl"></i>
            <div>
              <p class="text-xs text-gray-600">LOCATION</p>
              <p class="text-sky-600">0123 Some Place</p>
            </div>
          </div>
        </div>

        <!-- Mobile Hamburger -->
        <button
          class="lg:hidden text-blue-900 focus:outline-none"
          @click="toggleMenu"
        >
          <svg
            v-if="!isOpen"
            xmlns="http://www.w3.org/2000/svg"
            class="h-7 w-7"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
          <svg
            v-else
            xmlns="http://www.w3.org/2000/svg"
            class="h-7 w-7"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Navbar -->
      <nav class="text-white" style="background-color: #1f2b6c">
        <div
          class="flex items-center justify-between px-[30px] sm:px-[150px] py-2 relative"
        >
          <!-- Links (hidden on mobile) -->
          <ul class="hidden lg:flex space-x-8 text-xl font-medium">
            <li>
              <RouterLink to="/" class="hover:text-blue-400 transition">
                Home
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/aboutUs" class="hover:text-blue-400 transition">
                About Us
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/services" class="hover:text-blue-400 transition">
                Services
              </RouterLink>
            </li>
            <li>
              <RouterLink
                to="/doctorsList"
                class="hover:text-blue-400 transition"
              >
                Doctors
              </RouterLink>
            </li>
            <li>
              <RouterLink to="/contactUs" class="hover:text-blue-400 transition">
                Contact
              </RouterLink>
            </li>
          </ul>

          <!-- Right side (Search + Button) -->
          <div class="hidden lg:flex items-center space-x-4">
            <!-- Search -->
            <button class="hover:text-sky-300">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="w-5 h-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M21 21l-4.35-4.35M17 10a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </button>

            <!-- Appointment Button -->
            <RouterLink to="/AppointmentPage">
              <button
                class="bg-sky-200 text-blue-900 px-5 py-1 rounded-full font-medium hover:bg-sky-300"
              >
                Appointment
              </button>
            </RouterLink>
          </div>
        </div>

        <!-- Mobile Menu -->
        <transition name="fade">
          <div
            v-if="isOpen"
            class="lg:hidden px-6 pb-4 space-y-4 text-lg font-medium"
          >
            <RouterLink to="/" class="block">Home</RouterLink>
            <RouterLink to="/aboutUs" class="block">About us</RouterLink>
            <RouterLink to="/services" class="block">Services</RouterLink>
            <RouterLink to="/doctorsList" class="block">Doctors</RouterLink>
            <RouterLink to="/contactUs" class="block">Contact</RouterLink>

            <!-- Appointment button in mobile -->
            <RouterLink
              to="/AppointmentPage"
              class="block w-full text-center bg-sky-200 text-blue-900 px-5 py-2 rounded-full font-medium hover:bg-sky-300"
            >
              Appointment
            </RouterLink>
          </div>
        </transition>
      </nav>
    </header>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const isOpen = ref(false);

    const toggleMenu = () => {
      isOpen.value = !isOpen.value;
    };

    return {
      isOpen,
      toggleMenu,
    };
  },
};
</script>

<style>
/* Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* ✅ Global active class for Vue Router */
.router-link-exact-active {
  @apply text-sky-400 font-bold;
}
</style>
