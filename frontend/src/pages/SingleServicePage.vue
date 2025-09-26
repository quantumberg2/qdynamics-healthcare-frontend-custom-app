<template>
<!-- Hero Section -->
<section class="mt-8 relative w-full bg-cover h-72" style="background-image: url('/images/SingleService.jpg'); background-position: center 25%;">
    <!-- White transparent overlay -->
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <!-- Content above overlay -->
    <div class="relative z-10 flex items-center justify-center h-full">
        <h1 class="text-7xl font-bold text-blue-900">Free Checkup</h1>
    </div>
</section>
<div class="max-w-6xl mx-auto px-6 lg:px-12 py-6">
    <!-- First column smaller, second column bigger -->
    <div class="grid grid-cols-1 lg:grid-cols-[1fr_2fr] gap-8 items-start">

        <!-- Left Column - Services (narrow) -->
        <div class="flex flex-col">
            <!-- Free Checkup -->
            <div class="bg-[#1F2B6C] p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-10 h-10 text-blue-600 transition group-hover:text-white">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 1.343-3 3v1H8l-1 1v2h2v4h2v-4h2v4h2v-4h2v-2l-1-1h-1v-1c0-1.657-1.343-3-3-3zM12 2a10 10 0 100 20 10 10 0 000-20z" />
                </svg>
                <h3 class="text-lg font-semibold text-white mt-2 group-hover:text-white">Free Checkup</h3>
            </div>

            <!-- DNA Testing -->
            <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8 text-blue-600 transition group-hover:text-white">
                    <path d="M6 2c6 6 12 6 12 0" />
                    <path d="M6 22c6-6 12-6 12 0" />
                    <path d="M6 2v4c0 2 2 4 6 4s6 2 6 4v4" />
                    <path d="M6 22v-4c0-2 2-4 6-4s6-2 6-4V6" />
                </svg>
                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">DNA Testing</h3>
            </div>

            <!-- Cardiogram -->
            <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-600 transition group-hover:text-white">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 
           2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 
           3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 
           3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                    <polyline stroke="white" stroke-width="2" fill="none" points="6,12 10,12 12,8 14,14 18,14" />
                </svg>
                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">Cardiogram</h3>
            </div>

            <!-- Blood Bank -->
            <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-blue-600">
                    <path d="M12 2C12 2 5 10 5 15a7 7 0 0014 0c0-5-7-13-7-13z" />
                </svg>

                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">Blood Bank</h3>
            </div>

            <!-- Orthopedic -->
            <div class="bg-white p-3 border border-[#1F2B6C] flex flex-col items-center transition cursor-pointer">
                <!-- Orthopedic / Bone Icon -->
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8 text-blue-600">
                    <path d="M5 7a3 3 0 1 1 4-4 3 3 0 0 0 6 0 3 3 0 1 1 4 4 3 3 0 0 0 0 6 3 3 0 1 1-4 4 3 3 0 0 0-6 0 3 3 0 1 1-4-4 3 3 0 0 0 0-6z" />
                </svg>

                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">Orthopedic</h3>
            </div>
        </div>

        <!-- Right Column - Content (wide) -->
        <div>
            <img src="/images/doctor-patient.jpg" alt="doctor-patient" class="w-full h-64 object-cover rounded-lg shadow-lg mb-4 " />

            <p class="uppercase font-bold text-[20px] md:text-[24px] text-gray-900 mb-3">
                A passion for putting patients first.
            </p>

            <ul class="grid grid-cols-2 gap-4 list-none">
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>A Passion for Healing
                </li>
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>All our best
                </li>
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>A Legacy of Excellence
                </li>
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>5-Star Care
                </li>
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>Believe in Us
                </li>
                <li class="flex items-center">
                    <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>Always Caring
                </li>
            </ul>

            <p class="text-gray-600 mt-2 text-sm md:text-base leading-relaxed">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Quisque placerat scelerisque tortor ornare ornare.
                Convallis felis vitae tortor augue. Velit nascetur proin massa in.
                Consequat faucibus porttitor enim et.
            </p>

            <p class="text-gray-600 mt-2 text-sm md:text-base leading-relaxed">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Quisque placerat scelerisque. Convallis felis vitae tortor augue.
                Velit nascetur proin massa in.
            </p>
        </div>
    </div>
</div>
<Doctors />
</template>
<script>
import Doctors from './Doctors.vue';

export default {
  name: "SingleServicePage",
  components: {
  Doctors,
  },
};
</script>