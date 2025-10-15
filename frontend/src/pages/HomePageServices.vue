<template>
  <section class="py-2 bg-white text-center">
    <!-- Heading -->
    <p class="uppercase text-sky-600 font-bold tracking-wide text-[14px]">
      Care you can believe in
    </p>
    <h2 class="text-[28px] md:text-[32px] font-bold text-blue-900">
      Our Services
    </h2>

    <!-- Responsive Container -->
    <div class="flex flex-col lg:flex-row items-center justify-between gap-8 px-6 lg:px-16">
      <!-- Left Side - Dynamic Service Cards -->
      <div class="w-full lg:w-1/4 flex flex-col">
        <div
          v-for="(item, index) in limitedServices"
          :key="index"
          class="bg-white p-3 border-t border-l border-r border-[#1F2B6C] flex flex-col items-center transition hover:bg-sky-100 cursor-pointer"
        >
          <router-link :to="`/services/${item.department}`" class="flex flex-col items-center">
            <!-- Font Awesome Icon -->
            <i
              :class="['text-blue-600 mb-2 text-4xl', getIconClass(item.department)]"
            ></i>

            <!-- Department Name -->
            <h3 class="text-lg font-semibold text-[#1F2B6C] mt-1 text-center">
              {{ item.department || "Unknown Department" }}
            </h3>
          </router-link>
        </div>

        <!-- View All Button -->
        <div class="flex justify-center ">
          <router-link to="/Services" class="w-full">
            <button
              class="bg-[#1F2B6C] text-white w-full py-2 font-semibold hover:bg-[#162052] transition"
            >
              View All
            </button>
          </router-link>
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
              Excellence in Every Care
            </li>
            <li class="flex items-center">
              <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
              Trusted 5-Star Healthcare
            </li>
            <li class="flex items-center">
              <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
             Your Health, Our Priority
            </li>
            <li class="flex items-center">
              <span class="w-3 h-3 bg-blue-500 rounded-full mr-2"></span>
              Compassionate Care, Always
            </li>
          </ul>
        </div>

        <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
          we are committed to providing exceptional healthcare with a patient-first approach. Our team of dedicated professionals combines medical expertise with compassion, ensuring that every patient receives personalized care tailored to their needs.
        </p>
        <p class="text-gray-600 mt-4 text-sm md:text-base leading-relaxed">
          We believe in building a legacy of excellence through innovation, advanced technology, and continuous improvement in all aspects of healthcare. From routine check-ups to complex procedures, our goal is to make your experience safe, comfortable, and effective.
        </p>
      </div>

      <!-- Right Side Images -->
      <div class="w-full lg:w-1/4 space-y-4">
        <img
          src="/images/doctor-patient.jpg"
          alt="doctor-patient"
          class="w-full h-48 object-cover rounded-lg shadow-lg"
          loading="lazy"
        />
        <img
          src="/images/doctor-nurses.jpg"
          alt="doctor-nurses"
          class="w-full h-48 object-cover rounded-lg shadow-lg"
          loading="lazy"
        />
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "HomePageServices",
  data() {
    return {
      services: [], // stores all fetched departments
    };
  },
  computed: {
    // Show only first 4 departments
    limitedServices() {
      return this.services.slice(0, 4);
    },
  },
  async mounted() {
    await this.fetchServices();
  },
  methods: {
    async fetchServices() {
      try {
        const res = await fetch(
          "/api/method/healthcare_app.api.service_api.get_services"
        );
        const data = await res.json();
        this.services = data.message || [];
      } catch (err) {
        console.error("Failed to fetch services:", err);
      }
    },

    // Return different Font Awesome icons based on department
    getIconClass(department) {
      if (!department) return "fa-solid fa-hospital";
      const dept = department.toLowerCase();

      if (dept.includes("cardio")) return "fa-solid fa-heart-pulse";
      if (dept.includes("lab") || dept.includes("pathology")) return "fa-solid fa-vials";
      if (dept.includes("radiology")) return "fa-solid fa-x-ray";
      if (dept.includes("dental")) return "fa-solid fa-tooth";
      if (dept.includes("ortho")) return "fa-solid fa-bone";
      if (dept.includes("neuro")) return "fa-solid fa-brain";
      if (dept.includes("emergency")) return "fa-solid fa-truck-medical";
      if (dept.includes("blood")) return "fa-solid fa-droplet";
      if (dept.includes("pediatric")) return "fa-solid fa-baby";
      if (dept.includes("general")) return "fa-solid fa-stethoscope";

      // Default icon
      return "fa-solid fa-hospital";
    },
  },
};
</script>


