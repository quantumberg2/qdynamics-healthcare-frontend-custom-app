<template>
  <section
    class="mt-8 relative w-full bg-cover h-72"
    style="background-image: url('/images/DoctorsTeam.png'); background-position: center 25%;"
  >
    <!-- White transparent overlay -->
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <!-- Content above overlay -->
    <div class="relative z-10 flex items-center justify-center h-full">
      <h1 class="text-7xl font-bold text-blue-900">Doctors</h1>
    </div>
  </section>

  <section class="py-10 px-6 max-w-5xl mx-auto">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div
        v-for="doctor in doctors"
        :key="doctor.id"
        class="bg-white shadow-md rounded-lg overflow-hidden"
      >
        <!-- Doctor Image -->
        <img
          :src="doctor.image"
          :alt="doctor.doctor_name"
          class="w-full h-64 object-cover"
        />

        <!-- Info Section -->
        <div class="bg-blue-100 text-center py-4">
          <h3 class="text-gray-800 font-semibold">
            {{ doctor.doctor_name }}
          </h3>
          <p class="text-blue-900 font-bold tracking-widest text-sm">
            {{ doctor.specialization }}
          </p>

          <!-- Social Icons -->
          <div class="flex justify-center space-x-4 mt-3">
            <a
              v-if="doctor.linkedin"
              :href="doctor.linkedin"
              target="_blank"
              class="text-gray-600 hover:text-blue-600"
            >
              <i class="fab fa-linkedin"></i>
            </a>
            <a
              v-if="doctor.facebook"
              :href="doctor.facebook"
              target="_blank"
              class="text-gray-600 hover:text-blue-600"
            >
              <i class="fab fa-facebook"></i>
            </a>
            <a
              v-if="doctor.twitter"
              :href="doctor.twitter"
              target="_blank"
              class="text-gray-600 hover:text-blue-600"
            >
              <i class="fab fa-twitter"></i>
            </a>
          </div>
        </div>

        <!-- Button -->
        <div class="bg-blue-900 text-center py-2">
          <button class="text-white font-medium">View Profile</button>
        </div>
      </div>
    </div>
  </section>

  <section
    class="mb-3 relative w-full bg-cover bg-center h-80 flex items-center justify-center"
    style="background-image: url('/images/DoctorHand.png');"
  >
    <!-- Overlay -->
    <div class="absolute inset-0 bg-[#1F2B6C] bg-opacity-70"></div>

    <!-- Carousel -->
    <div class="relative z-10 text-center px-6 max-w-2xl">
      <Carousel :items-to-show="1" :wrap-around="true" :autoplay="3000" :transition="1000">
        <Slide v-for="(testimonial, index) in testimonials" :key="index">
          <div class="flex flex-col items-center">
            <!-- Quote Icon -->
            <div class="text-[40px] text-white mb-4">"</div>

            <!-- Quote Text -->
            <p class="text-white md:text-4xl leading-relaxed">
              {{ testimonial.quote }}
            </p>

            <!-- Author -->
            <h3
              class="mt-4 text-white font-medium border-t border-white pt-2 inline-block"
            >
              {{ testimonial.author }}
            </h3>
          </div>
        </Slide>

        <!-- Pagination -->
        <template #addons>
          <Pagination />
        </template>
      </Carousel>
    </div>
  </section>
</template>

<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination } from "vue3-carousel";

export default {
  name: "DoctorGrid",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      doctors: [],
      testimonials: [
        {
          quote:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat scelerisque tortor ornare ornare.",
          author: "John Doe",
        },
        {
          quote:
            "Velit nascetur consequat faucibus porttitor enim et. Quisque placerat scelerisque felis vitae tortor augue.",
          author: "Jane Smith",
        },
        {
          quote:
            "Consectetur adipiscing elit. Quisque placerat scelerisque tortor ornare ornare.",
          author: "Michael Johnson",
        },
      ],
    };
  },
  mounted() {
    this.fetchDoctors();
  },
  methods: {
    async fetchDoctors() {
      try {
        const res = await fetch(
          "/api/method/healthcare_app.api.App_api.get_doctors"
        );
        const data = await res.json();
        this.doctors = data.message || [];
      } catch (err) {
        console.error("Failed to fetch doctors:", err);
      }
    },
  },
};
</script>

<style scoped>
.carousel__pagination {
  display: flex;
  gap: var(--vc-pgn-gap);
  justify-content: center;
  left: 50%;
  list-style: none;
  margin: 0;
  padding: 0;
  position: absolute;
  transform: translateX(-50%);
  bottom: -16px !important;
}
</style>
