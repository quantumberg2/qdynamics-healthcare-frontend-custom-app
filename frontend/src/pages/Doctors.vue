<template>
  <section class="py-6 bg-white ">
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
            :src="doctor.image"
            alt="doctor"
            class="w-full h-64 object-cover"
             loading="lazy"
          />

          <!-- Info Section -->
          <div class="bg-blue-100 text-center py-4">
            <h3 class="text-gray-800 font-semibold">{{ doctor.name }}</h3>
            <p class="text-blue-800 font-bold tracking-widest uppercase">
              {{ doctor.speciality }}
            </p>

            <!-- Social Links -->
            <div class="flex justify-center space-x-4 mt-3 text-gray-600">
              <a href="#"><i class="fab fa-linkedin-in"></i></a>
              <a href="#"><i class="fab fa-facebook-f"></i></a>
              <a href="#"><i class="fab fa-instagram"></i></a>
            </div>
          </div>

          <!-- View Profile -->
          <button
            class="w-full bg-blue-900 text-white py-2 font-medium hover:bg-blue-800"
          >
            View Profile
          </button>
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
      doctors: [
        { name: "Doctor 1", speciality: "Neurology", image: "/images/doctor1.jpg" },
        { name: "Doctor 2", speciality: "Neurology", image: "/images/doctor2.jpg" },
        { name: "Doctor 3", speciality: "Neurology", image: "/images/doctor3.jpg" },
        { name: "Doctor 4", speciality: "Neurology", image: "/images/doctor1.jpg" },
        { name: "Doctor 5", speciality: "Neurology", image: "/images/doctor2.jpg" },
        { name: "Doctor 6", speciality: "Neurology", image: "/images/doctor3.jpg" },
      ],
    };
  },
};
</script>

<style scoped>
/* Fix slide spacing */
.carousel__slide {
  padding: 0 !important;
}

/* Ensure equal card widths */
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
