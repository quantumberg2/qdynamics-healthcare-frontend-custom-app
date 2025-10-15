<template>
<section class="mt-8 relative w-full bg-cover h-72" style="background-image: url('/images/DoctorsTeam.png'); background-position: center 25%;">
    <!-- White transparent overlay -->
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <!-- Content above overlay -->
    <div class="relative z-10 flex items-center justify-center h-full">
        <h1 class="text-7xl font-bold text-blue-900">About Us</h1>
    </div>
</section>

<section class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6 items-center px-6 md:px-12 max-w-6xl mx-auto">
    <div>
        <img src="/images/doctors-group.jpg" alt="doctor-nurses" class="w-full h-74 rounded-lg shadow-md" />
    </div>

    <!-- Right Side (Content) -->
    <div>
        <p class="text-blue-600 font-semibold uppercase tracking-wide">
            Welcome to Hospital Name
        </p>
        <h2 class="text-[26px]  font-bold text-blue-900 leading-snug mt-2">
            Best Care for Your Good Health
        </h2>

        <!-- Bullet Points -->
        <div class="grid grid-cols-2 gap-3 mt-3">
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                A Passion for Healing
            </p>
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                5-Star Care
            </p>
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                All our best
            </p>
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                Believe in Us
            </p>
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                Always Caring
            </p>
            <p class="flex items-center text-gray-700 text-base">
                <span class="w-3 h-3 bg-blue-600 rounded-full mr-2"></span>
                A Legacy of Excellence
            </p>
        </div>

        <!-- Description -->
        <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat scelerisque
            tortor ornare ornare. Quisque placerat scelerisque tortor ornare ornare. Convallis felis
            vitae tortor augue. Velit nascetur proin massa in. Consequat faucibus porttitor enim et.
        </p>
        <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat scelerisque
            tortor ornare ornare. Convallis felis vitae tortor augue. Velit nascetur proin massa in.
        </p>
    </div>
</section>
 <section
    class=" mt-5 relative w-full bg-cover bg-center h-80 flex items-center justify-center"
    style="background-image: url('/images/DoctorHand.png');"
  >
    <!-- Overlay -->
    <div class="absolute inset-0 bg-[#1F2B6C] bg-opacity-70"></div>

    <!-- Carousel -->
    <div class="relative z-10 text-center px-6 max-w-2xl">
      <Carousel
        :items-to-show="1"
        :wrap-around="true"
        :autoplay="3000"
        :transition="1000"
      >
        <Slide v-for="(testimonial, index) in testimonials" :key="index">
          <div class="flex flex-col items-center">
            <!-- Quote Icon -->
            <div class="text-[40px] text-white mb-4">"</div>

            <!-- Quote Text -->
            <p class="text-white  md:text-4xl leading-relaxed">
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
  <Doctors />
  <Contact />
</template>
<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination } from 'vue3-carousel'
import Doctors from './Doctors.vue'
import Contact from './Contact.vue'

export default {
  name: 'About us',
  components: {
    Carousel,
    Slide,
    Pagination,
    Doctors,
    Contact
  },
  data() {
    return {
      testimonials: [
        {
          quote:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat scelerisque tortor ornare ornare.',
          author: 'John Doe',
        },
        {
          quote:
            'Velit nascetur consequat faucibus porttitor enim et. Quisque placerat scelerisque felis vitae tortor augue.',
          author: 'Jane Smith',
        },
        {
          quote:
            'Consectetur adipiscing elit. Quisque placerat scelerisque tortor ornare ornare.',
          author: 'Michael Johnson',
        },
      ],
    }
  },
}
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
