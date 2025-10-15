<template>
<section class="relative min-h-[70vh] lg:h-[90vh] flex items-center">
    <!-- Image -->
    <img src="https://qtest.quantumberg.com/files/Banner_image_50.png" 
         alt="Banner" 
         class="absolute inset-0 w-full h-full object-cover z-0">

    <!-- Overlay -->
    <div class="absolute inset-0 bg-white/50 z-10"></div>

    <!-- Content -->
    <div class="relative container mx-auto px-6 lg:px-20 flex flex-col lg:flex-row items-center justify-between w-full z-20">
        <!-- Left Side Text -->
        <div class="max-w-lg text-center lg:text-left space-y-4 sm:space-y-6 lg:ml-12 mx-auto mb-5">
            <p class="uppercase tracking-wider text-sky-600 font-bold text-[18px]">
                Caring for Life
            </p>
            <h1 class="text-[46px] font-bold text-blue-900 leading-snug">
                Leading the Way <br />
                in <span class="text-sky-600">Medical Excellence</span>
            </h1>
            <RouterLink to="/services" class="bg-sky-200 text-blue-900 px-5 sm:px-6 py-2 sm:py-3 rounded-full font-medium hover:bg-sky-300 transition text-sm sm:text-base inline-block text-center">
                Our Services
            </RouterLink>
        </div>
    </div>
</section>


<!-- Cards Section (half inside banner, half outside) -->
<div class="-mt-16 relative z-10 px-4 sm:px-6 lg:px-20">
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 max-w-5xl mx-auto">
    
    <!-- Card 1 -->
    <router-link to="/AppointmentPage">
      <div class="bg-[#1F2B6C] text-white rounded-lg shadow-lg flex flex-row items-center justify-between p-6">
        <p class="font-semibold text-lg sm:text-base">Book an Appointment</p>
        <i class="fas fa-calendar-alt text-[#BFD2F8] text-[40px]"></i>
      </div>
    </router-link>

    <!-- Card 2 -->
    <router-link to="/doctorsList">
      <div class="bg-[#BFD2F8] text-blue-900 rounded-lg shadow-lg flex flex-row items-center justify-between p-6">
        <p class="font-semibold text-lg sm:text-base">Find Doctors</p>
        <i class="fas fa-user-friends text-[#1F2B6C] text-[40px]"></i>
      </div>
    </router-link>

    <!-- Card 3 -->
    <div class="bg-sky-500 text-white rounded-lg shadow-lg flex flex-row items-center justify-between p-6">
      <p class="font-semibold text-lg sm:text-base">Emergency Call</p>
      <i class="fas fa-phone-volume text-[#1F2B6C] text-[40px]"></i>
    </div>
    
  </div>
</div>

<section class="py-8 bg-white text-center">
    <!-- Heading -->
    <p class="uppercase text-sky-600 font-bold tracking-wide text-[14px] mb-2">
        Welcome to Meddical
    </p>
    <h2 class="text-[28px] md:text-[32px] font-bold text-blue-900 mb-2">
        A Great Place to Receive Care
    </h2>

    <!-- Paragraph -->

    <p class="max-w-2xl mx-auto text-gray-600 mb-6 text-[16px] leading-relaxed">
        We are committed to providing compassionate, patient-centered care in a safe and welcoming
        environment. Our team of experienced professionals ensures that every individual receives
        personalized attention, modern treatments, and the support they need for a healthier future.
    </p>

    <!-- Learn More Button -->
    <button class="inline-flex items-center space-x-2 text-sky-600 font-semibold hover:text-sky-800 transition">
        <span>Learn More</span>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7" />
        </svg>
    </button>

    <!-- Image -->
    <div class="mt-5">
        <img src="/images/doctors_team.jpg" alt="Doctors Group" class="w-full max-w-5xl mx-auto rounded-lg shadow-md" loading="lazy"/>

    </div>
</section>
<HomePageServices />
<div class=" mt-3 w-full max-w-5xl mx-auto text-center">

    <p class="uppercase text-sky-600 font-bold tracking-wide text-[14px] ">
        Always Caring
    </p>
    <h2 class="text-[28px] md:text-[32px] font-bold text-blue-900 ">
        Our Specialties
    </h2>
    <!-- Grid with 16 cards -->
    <div class="grid grid-cols-4 w-full mt-2">
        <div v-for="(item, index) in specialties" :key="index" class="flex flex-col items-center justify-center p-6 border border-gray-200 hover:bg-[#1F2B6C] hover:text-white transition">
            <!-- Example icon -->
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-10 h-10 text-sky-600 group-hover:text-white">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 
       2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 
       3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 
       3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                <polyline stroke="white" stroke-width="2" fill="none" points="6,12 10,12 12,8 14,14 18,14" />
            </svg>
            <h3 class="text-sm font-medium text-center">{{ item }}</h3>
        </div>
    </div>
</div>
<section class="mt-4 relative w-full bg-cover bg-center" style="background-image: url('https://qtest.quantumberg.com/files/bgDoctor.png');">
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <div class="relative max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-2 items-center gap-8 px-6 py-12">
        <!-- Left Side (Text) -->
        <div>
            <h2 class="text-[28px] font-bold text-[#1F2B6C] mb-4">
                Book an Appointment
            </h2>
            <p class="text-gray-700 leading-relaxed">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
                placerat scelerisque tortor ornare ornare. Convallis felis vitae
                tortor augue. Velit nascetur proin massa in. Consequat faucibus
                porttitor enim et.
            </p>
        </div>

        <!-- Right Side (Form) -->
        <div class="w-full max-w-md bg-[#1F2B6C] text-white">
            <form class="border">
                <!-- Grid Inputs with Lines -->
                <div class="grid grid-cols-2  ">
                    <input type="text" placeholder="Name" class="bg-transparent px-3 py-2 placeholder-white focus:outline-none" />
                    <select class="bg-transparent px-3 py-2 focus:outline-none">
                        <option>Gender</option>
                    </select>

                    <input type="email" placeholder="Email" class="bg-transparent px-3 py-2 placeholder-white focus:outline-none" />
                    <input type="tel" placeholder="Phone" class="bg-transparent px-3 py-2 placeholder-white focus:outline-none" />
                    <select class="bg-transparent px-3 py-2 focus:outline-none">
                        <option>Doctor</option>
                    </select>
                     <select class="bg-transparent px-3 py-2 focus:outline-none">
                        <option>Department</option>
                    </select>
                    <input type="text" placeholder="Date" onfocus="(this.type='date')" class="bg-transparent placeholder-white px-3 py-2 focus:outline-none" />
                    <input type="text" placeholder="Time" onfocus="(this.type='time')" class="bg-transparent placeholder-white px-3 py-2 focus:outline-none" />
                 </div>

                <!-- Message Box -->
                <textarea placeholder="Message" rows="4" class="w-full bg-transparent placeholder-white px-3 py-2
         outline-none focus:outline-none border-0 focus:border-0 focus:ring-0"></textarea>

                <!-- Submit Button -->
                <button type="submit" class="w-full bg-[#BFD2F8] text-[#1F2B6C] font-bold py-2 hover:bg-blue-400 transition-colors ">
                    SUBMIT
                </button>
            </form>
        </div>
    </div>
</section>
<Doctors />
<Contact />
</template>

<script>
import Doctors from './Doctors.vue'
import Contact from './Contact.vue'
import HomePageServices from './HomePageServices.vue'
export default {
    name: 'Home page',
    components: {
        Doctors,
        Contact,
        HomePageServices
    },

    data() {
        return {
            specialties: [
                "Neurology", "Bones", "Oncology", "Otorhinolaryngology",
                "Ophthalmology", "Cardiovascular", "Pulmonology", "Renal Medicine",
                "Gastroenterology", "Urology", "Dermatology", "Gynaecology",
                "Orthopedics", "Radiology", "Pediatrics", "General Surgery"
            ]
        };
    }
};
</script>
