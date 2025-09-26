<template>
<!-- Hero Section -->
<section class="mt-8 relative w-full bg-cover h-72" style="background-image: url('/images/doctorpatient.png'); background-position: center 25%;">
    <!-- White transparent overlay -->
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <!-- Content above overlay -->
    <div class="relative z-10 flex items-center justify-center h-full">
        <h1 class="text-7xl font-bold text-blue-900">Services</h1>
    </div>
</section>
<section class="max-w-5xl mx-auto py-12 px-4">
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <!-- Loop through 6 cards -->
      <div
        v-for="(card, index) in cards"
        :key="index"
        class="group bg-white rounded-lg shadow-md overflow-hidden cursor-pointer transition duration-300 hover:bg-blue-900 hover:text-white">
        <img
          :src="card.image"
          alt="Service"
          class="w-full h-48 object-cover transition duration-300 group-hover:opacity-30"/>
        <div class="p-4">
          <h3
            class="text-lg font-semibold text-gray-900 group-hover:text-white transition">
            {{ card.title }}
          </h3>
          <p
            class="mt-2 text-sm text-gray-600 group-hover:text-gray-200 transition">
            {{ card.description }}
          </p>
          <a
            href="#"
            class="mt-2 inline-flex items-center text-sm font-semibold text-blue-600 group-hover:text-white hover:underline transition">
            Learn More <i class="fa-solid fa-arrow-right ml-2"></i>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const cards = [
  {
    image: "/images/doctor-patient.jpg",
    title: "Free Checkup",
    description:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis facilisis, nunc sit amet.",
  },
  {
    image: "/images/doctor-patient.jpg",
    title: "Doctor Consultation",
    description:
      "Get expert advice from top doctors. Our consultation service get the right treatment at the right time.",
  },
  {
    image: "/images/doctor-patient.jpg",
    title: "Diagnostics",
    description:
      "Accurate and reliable diagnostic services to help identify your health issues quickly and effectively.",
  },
  {
    image: "/images/doctor-patient.jpg",
    title: "Pharmacy",
    description:
      "Order genuine medicines with ease. Fast delivery and affordable prices for all your healthcare needs.",
  },
  {
    image: "/images/doctor-patient.jpg",
    title: "Ambulance Service",
    description:
      "24/7 emergency ambulance service to provide immediate medical support whenever you need it.",
  },
  {
    image: "/images/doctor-patient.jpg",
    title: "Lab Tests",
    description:
      "Wide range of lab tests available at your doorstep. Get accurate reports quickly and easily.",
  },
];
</script>
