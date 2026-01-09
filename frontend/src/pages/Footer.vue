<template>
  <footer class="bg-[#1F2B6C] text-white py-6">
    <div
      class="max-w-5xl mx-auto px-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-6"
    >
      <!-- Logo + Text -->
      <div>
        <h2 class="text-2xl font-bold mb-4">HEALTHCARE</h2>
        <p class="text-gray-300">
          Leading the Way in Medical Excellence, Trusted Care.
        </p>
      </div>

      <!-- Important Links -->
      <div>
        <h3 class="font-semibold mb-4">Important Links</h3>
        <ul class="space-y-2 text-gray-300">
          <li>
            <RouterLink to="/appointmentPage" class="hover:text-white">
              Appointment
            </RouterLink>
          </li>
          <li>
            <RouterLink to="/doctorsList" class="hover:text-white">
              Doctors
            </RouterLink>
          </li>
          <li>
            <RouterLink to="/services" class="hover:text-white">
              Services
            </RouterLink>
          </li>
          <li>
            <RouterLink to="/aboutUs" class="hover:text-white">
              About Us
            </RouterLink>
          </li>
        </ul>
      </div>

      <!-- Contact Us -->
      <div>
        <h3 class="font-semibold mb-4">Contact Us</h3>
        <ul class="space-y-2 text-gray-300">
          <li>Call: (237) 681-812-255</li>
          <li>Email: filidneeeesoc@gmail.com</li>
          <li>Address: 0123 Some place</li>
        </ul>
      </div>

      <!-- Newsletter -->
      <div>
        <h3 class="font-semibold mb-4">Newsletter</h3>

        <div class="flex">
          <input
            type="email"
            placeholder="Enter your email address"
            class="w-full px-3 py-2 rounded-l-md text-gray-900 focus:outline-none"
          />
          <button
            type="button"
            class="bg-blue-600 px-4 rounded-r-md hover:bg-blue-700"
          >
            <i class="fas fa-paper-plane"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Divider -->
    <div
      class="border-t border-gray-600 mt-6 pt-4 max-w-5xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center"
    >
      <p class="text-gray-400 text-sm">
        © 2021 Hospital’s name. All Rights Reserved by PNTEC-LTD
      </p>

      <div class="flex space-x-4 mt-2 md:mt-0">
        <a href="#" class="text-gray-400 hover:text-white">
          <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="#" class="text-gray-400 hover:text-white">
          <i class="fab fa-facebook-f"></i>
        </a>
        <a href="#" class="text-gray-400 hover:text-white">
          <i class="fab fa-instagram"></i>
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>
