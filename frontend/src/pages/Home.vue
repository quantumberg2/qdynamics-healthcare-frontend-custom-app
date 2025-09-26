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
        <img src="/images/DoctorsTeam.png" alt="Doctors Group" class="w-full max-w-5xl mx-auto rounded-lg shadow-md" loading="lazy"/>

    </div>
</section>
<section class="py-2 bg-white text-center">
    <!-- Heading -->
    <p class="uppercase text-sky-600 font-bold tracking-wide text-[14px] ">
        Care you can believe in
    </p>
    <h2 class="text-[28px] md:text-[32px] font-bold text-blue-900 ">
        Our Services
    </h2>

    <!-- Responsive Container -->
    <div class="flex flex-col lg:flex-row items-center justify-between gap-8 px-6 lg:px-16">

        <!-- Left Side - Cards -->
        <div class="w-full lg:w-1/4 flex flex-col">
            <!-- Free Checkup -->
            <router-link to="/SingleServicePage">
                <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition hover:bg-sky-100 hover:text-white cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-10 h-10 text-blue-600 group-hover:text-white">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 1.343-3 3v1H8l-1 1v2h2v4h2v-4h2v4h2v-4h2v-2l-1-1h-1v-1c0-1.657-1.343-3-3-3zM12 2a10 10 0 100 20 10 10 0 000-20z" />
                    </svg>
                    <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">
                        Free Checkup
                    </h3>
                </div>
            </router-link>

            <!-- DNA Testing -->
            <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition hover:bg-sky-100 hover:text-white cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-8 h-8 text-blue-600 group-hover:text-white">
                    <path d="M6 2c6 6 12 6 12 0" />
                    <path d="M6 22c6-6 12-6 12 0" />
                    <path d="M6 2v4c0 2 2 4 6 4s6 2 6 4v4" />
                    <path d="M6 22v-4c0-2 2-4 6-4s6-2 6-4V6" />
                </svg>
                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">
                    DNA Testing
                </h3>
            </div>

            <!-- Cardiogram -->
            <div class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition hover:bg-sky-100 hover:text-white cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-sky-600 group-hover:text-white">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 
       2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 
       3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 
       3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                    <polyline stroke="white" stroke-width="2" fill="none" points="6,12 10,12 12,8 14,14 18,14" />
                </svg>
                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">
                    Cardiogram
                </h3>
            </div>

            <!-- Blood Bank -->
            <div class="bg-white p-3 border border-[#1F2B6C] flex flex-col items-center transition hover:bg-sky-100 hover:text-white cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-8 h-8 text-blue-600">
                    <path d="M12 2C12 2 5 10 5 15a7 7 0 0014 0c0-5-7-13-7-13z" />
                </svg>
                <h3 class="text-lg font-semibold text-[#1F2B6C] mt-2 group-hover:text-white">
                    Blood Bank
                </h3>
            </div>

            <!-- View All Button -->
            <div class="flex justify-center">
                <button class="bg-[#1F2B6C] text-white w-full py-2 font-semibold hover:bg-[#162052] transition">
                    View All
                </button>
            </div>
        </div>

        <!-- Center Content -->
        <div class="w-full lg:w-1/2 text-left">
            <p class="uppercase font-bold text-[20px] md:text-[24px] text-gray-900 mb-3">
                A passion for putting patients first.
            </p>
            <div class="container mx-auto px-4">
                <ul class="grid grid-cols-2 gap-4 list-disc list-inside">
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        A Passion for Healing
                    </li>
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        All our best
                    </li>
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        A Legacy of Excellence
                    </li>
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        5-Star Care
                    </li>
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        Believe in Us
                    </li>
                    <li class="flex items-center">
                        <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
                        Always Caring
                    </li>
                </ul>
            </div>

            <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Quisque placerat scelerisque tortor ornare ornare.
                Convallis felis vitae tortor augue. Velit nascetur proin massa in.
                Consequat faucibus porttitor enim et.
            </p>
            <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Quisque placerat scelerisque. Convallis felis vitae tortor augue.
                Velit nascetur proin massa in.
            </p>
        </div>

        <!-- Right Side Images -->
        <div class="w-full lg:w-1/4 space-y-4">
            <img src="/images/doctor-patient.jpg" alt="doctor-patient" class="w-full h-48 object-cover rounded-lg shadow-lg" loading="lazy" />
            <img src="/images/doctor-nurses.jpg" alt="doctor-nurses" class="w-full h-48 object-cover rounded-lg shadow-lg" loading="lazy"/>
        </div>
    </div>
</section>
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
export default {
    name: 'Home page',
    components: {
        Doctors,
        Contact
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
