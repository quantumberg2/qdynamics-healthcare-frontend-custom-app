<template>
  <section class="py-6 bg-white">
    <!-- Heading -->
    <div class="text-center mb-10">
      <h4 class="text-sm font-bold tracking-widest text-blue-600 uppercase">
        Trusted Care
      </h4>
      <h2 class="text-[28px] font-bold text-gray-900">Our Doctors</h2>
    </div>

    <!-- Carousel -->
    <Carousel
      :items-to-show="3"
      :wrap-around="true"
      :breakpoints="{
        0: { itemsToShow: 1 },
        768: { itemsToShow: 2 },
        1024: { itemsToShow: 3 }
      }"
      class="max-w-4xl mx-auto"
    >
      <Slide v-for="(doctor, index) in doctors" :key="index">
        <div class="bg-white rounded-lg shadow-md overflow-hidden flex flex-col">
          <!-- Image -->
          <img
            :src="doctor.image || '/images/PlaceholderImages.png'"
            :alt="doctor.first_name"
            class="w-full h-64 object-cover"
            loading="lazy"
          />

          <!-- Info Section -->
          <div class="bg-blue-100 text-center py-1">
            <h3 class="text-gray-800 font-semibold">{{ doctor.first_name }}</h3>
            <p class="text-blue-800 font-bold tracking-widest uppercase">
              {{ doctor.department }}
            </p>

            <!-- Social Links -->
            <div class="flex justify-center space-x-4 mt-2 text-gray-600">
              <a v-if="doctor.custom_linkedin" :href="doctor.custom_linkedin" target="_blank"><i class="fab fa-linkedin-in"></i></a>
              <a v-if="doctor.custom_facebook" :href="doctor.custom_facebook" target="_blank"><i class="fab fa-facebook-f"></i></a>
              <a v-if="doctor.custom_twitter" :href="doctor.custom_twitter" target="_blank"><i class="fab fa-twitter"></i></a>
            </div>
          </div>

          <!-- View Profile -->
      <router-link
  :to="{ name: 'ViewProfile', params: { id: doctor.name } }"
  class="block w-full bg-blue-900 text-white py-2 font-medium text-center hover:bg-blue-800"
>
  View Profile
</router-link>

        </div>
      </Slide>

      <!-- Navigation Dots -->
      <template #addons>
        <Pagination />
      </template>
    </Carousel>
  </section>
</template>

<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide, Pagination } from "vue3-carousel";

export default {
  name: "DoctorsCarousel",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      doctors: [],
    };
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
  mounted() {
    this.fetchDoctors();
  },
};
</script>

<style scoped>
.carousel__slide {
  padding: 0 !important;
}

.carousel__viewport {
  overflow: hidden;
}
.carousel__track {
  display: flex;
}
.carousel__slide {
  flex: 1 0 auto;
}
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
