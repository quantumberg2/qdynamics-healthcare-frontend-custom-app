<template>
<!-- Banner -->
<section class="mt-8 relative w-full bg-cover h-72" style="background-image: url('/images/Appointment.jpg');">
    <!-- White transparent overlay -->
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>

    <!-- Content above overlay -->
    <div class="relative z-10 flex items-center justify-center h-full text-center px-4">
        <h1 class="text-3xl md:text-5xl lg:text-7xl font-bold text-blue-900">
            Book an Appointment
        </h1>
    </div>
</section>

<!-- Form + Schedule -->
<section class="max-w-4xl mx-auto px-4 sm:px-6 py-10 grid grid-cols-1 lg:grid-cols-2 gap-6">
    <!-- Left Column (Form) -->
    <div class="w-full">
        <!-- Headings -->
        <div class="mb-6 text-center lg:text-left">
            <h2 class="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#1F2B6C] tracking-wide">
                Book an Appointment
            </h2>
            <p class="text-sm text-gray-700 mt-2">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque placerat scelerisque tortor ornare ornare.
                Convallis felis vitae tortor augue. Velit nascetur proin massa in. Consequat faucibus porttitor enim et.
            </p>
        </div>

        <!-- Form -->
        <div class="bg-[#BFD2F8] text-[#1F2B6C] overflow-hidden">
            <form class="border border-blue-900">
                <!-- Grid Inputs -->
                <div class="grid grid-cols-1 sm:grid-cols-2">
                    <input type="text" placeholder="Name" class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none sm:border-b-0 sm:border-r" />
                    <select class="bg-transparent px-3 py-2 focus:outline-none ">
                        <option>Gender</option>
                    </select>

                    <input type="email" placeholder="Email" class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none  sm:border-r" />
                    <input type="tel" placeholder="Phone" class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none " />
 <select class="bg-transparent px-3 py-2 focus:outline-none ">
                        <option>Department</option>
                    </select>
                     <select class="bg-transparent px-3 py-2 focus:outline-none  sm:border-r">
                        <option>Doctor</option>
                    </select>
                    <input type="text" placeholder="Date" onfocus="(this.type='date')" class="bg-transparent placeholder-[#1F2B6C] px-3 py-2 focus:outline-none  sm:border-r" />
                    <input type="text" placeholder="Time" onfocus="(this.type='time')" class="bg-transparent placeholder-[#1F2B6C] px-3 py-2 focus:outline-none " />

                   
                   
                </div>

                <!-- Message Box -->
                <textarea placeholder="Message" rows="4" class="w-full bg-transparent placeholder-[#1F2B6C] px-3 py-2 outline-none border-none focus:outline-none focus:ring-0"></textarea>

                <!-- Submit Button -->
                <button type="submit" class="w-full bg-[#1F2B6C] text-[#BFD2F8] font-bold py-2 hover:bg-blue-400 transition-colors">
                    SUBMIT
                </button>
            </form>
        </div>
    </div>

    <!-- Right Column (Schedule Card) -->
    <div class="max-w-xl mx-auto lg:mx-0 bg-[#1F2B6C] text-white shadow-lg p-6 w-full">
        <!-- Title -->
        <h2 class="text-6xl sm:text-4xl lg:text-6xl font-bold text-center mb-4">Schedule Hours</h2>

        <div class="space-y-3">
            <div v-for="(day, index) in schedule" :key="index" class="flex items-center">
                <!-- Left column fixed width -->
                <span class="w-28">{{ day.day }}</span>

                <!-- Line expands automatically -->
                <span class="border-b border-gray-400 w-6 mx-2 inline-block"></span>

                <!-- Right column fixed width -->
                <span class="w-64 text-right">{{ day.time }}</span>
            </div>
        </div>

        <!-- Divider -->
        <div class="border-b border-gray-400 my-4"></div>

        <!-- Emergency Section -->
        <div class="text-center">
            <p class="font-bold text-lg">Emergency</p>
            <p class="text-gray-200 flex items-center justify-center gap-2 mt-2">
                <i class="fas fa-phone"></i> (237) 681-812-255
            </p>
        </div>
    </div>
</section>

<!-- Map -->
<section class="h-[300px] sm:h-[400px] max-w-5xl mx-auto px-2">
    <iframe class="w-full h-full rounded-lg shadow-md" src="https://www.google.com/maps?q=No.1376,+2nd+floor,+13th+Cross,+Sarakki+Main+Rd,+1st+Phase,+J.+P.+Nagar,+Bengaluru,+Karnataka+560078&output=embed" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
    </iframe>
</section>

<Contact />
</template>

<script>
import Contact from './Contact.vue';
export default {
    name: 'ScheduleCard',
    components: {
        Contact
    },
    data() {
        return {
            form: {
                name: '',
                email: '',
                subject: '',
                message: ''
            },
            schedule: [
                { day: 'Monday', time: '09:00 AM - 07:00 PM' },
                { day: 'Tuesday', time: '09:00 AM - 07:00 PM' },
                { day: 'Wednesday', time: '09:00 AM - 07:00 PM' },
                { day: 'Thursday', time: '09:00 AM - 07:00 PM' },
                { day: 'Friday', time: '09:00 AM - 07:00 PM' },
                { day: 'Saturday', time: '09:00 AM - 07:00 PM' },
                { day: 'Sunday', time: 'Closed' }
            ]
        };
    },
    methods: {
        handleSubmit() {
            alert(`Form submitted: ${JSON.stringify(this.form)}`);
        }
    }
};
</script>
