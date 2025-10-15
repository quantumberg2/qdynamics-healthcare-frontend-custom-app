<template>
  <!-- Banner -->
  <section
    class="mt-8 relative w-full bg-cover h-72"
    style="background-image: url('/images/Appointment.jpg');"
  >
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>
    <div class="relative z-10 flex items-center justify-center h-full text-center px-4">
      <h1 class="text-3xl md:text-5xl lg:text-7xl font-bold text-blue-900">
        Book an Appointment
      </h1>
    </div>
  </section>

  <!-- Form + Schedule -->
  <section
    class="max-w-4xl mx-auto px-4 sm:px-6 py-10 grid grid-cols-1 lg:grid-cols-2 gap-6"
  >
    <!-- Left Column (Form) -->
    <div class="w-full">
      <div class="mb-6 text-center lg:text-left">
        <h2
          class="text-2xl sm:text-3xl lg:text-4xl font-bold text-[#1F2B6C] tracking-wide"
        >
          Book an Appointment
        </h2>
        <p class="text-sm text-gray-700 mt-2">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
          placerat scelerisque tortor ornare ornare. Convallis felis vitae
          tortor augue. Velit nascetur proin massa in. Consequat faucibus
          porttitor enim et.
        </p>
      </div>

      <!-- Form -->
      <div class="bg-[#BFD2F8] text-[#1F2B6C] overflow-hidden">
        <form class="border border-blue-900" @submit.prevent="submitAppointment">
          <div class="grid grid-cols-1 sm:grid-cols-2">
            <input
              v-model="form.name"
              type="text"
              placeholder="Name"
              class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none sm:border-b-0 sm:border-r"
              required
            />

            <select
              v-model="form.gender"
              class="bg-transparent px-3 py-2 focus:outline-none"
              required
            >
              <option value="">Select Gender</option>
              <option>Male</option>
              <option>Female</option>
              <option>Other</option>
            </select>

            <input
              v-model="form.email"
              type="email"
              placeholder="Email"
              class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none sm:border-r"
              required
            />
            <input
              v-model="form.phone"
              type="tel"
              placeholder="Phone"
              class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none"
              required
            />

            <!-- Dynamic Department -->
            <select
              v-model="form.department"
              @change="fetchDoctors"
              class="bg-transparent px-3 py-2 focus:outline-none"
              required
            >
              <option value="">Select Department</option>
              <option
                v-for="dept in departments"
                :key="dept"
                :value="dept"
              >
                {{ dept }}
              </option>
            </select>

            <!-- Dynamic Doctor -->
            <select
              v-model="form.doctor"
              class="bg-transparent px-3 py-2 focus:outline-none sm:border-r"
              required
            >
              <option value="">Select Doctor</option>
              <option
                v-for="doc in doctors"
                :key="doc.name"
                :value="doc.name"
              >
                {{ doc.first_name }} {{ doc.last_name }} ({{ doc.designation || 'Doctor' }})
              </option>
            </select>

            <input
              v-model="form.date"
              type="text"
              placeholder="Date"
              onfocus="(this.type='date')"
              class="bg-transparent placeholder-[#1F2B6C] px-3 py-2 focus:outline-none sm:border-r"
              required
            />
            <input
              v-model="form.time"
              type="text"
              placeholder="Time"
              onfocus="(this.type='time')"
              class="bg-transparent placeholder-[#1F2B6C] px-3 py-2 focus:outline-none"
              required
            />
          </div>

          <!-- Message -->
          <textarea
            v-model="form.message"
            placeholder="Message"
            rows="4"
            class="w-full bg-transparent placeholder-[#1F2B6C] px-3 py-2 outline-none border-none focus:outline-none focus:ring-0"
          ></textarea>

          <!-- Submit -->
          <button
            type="submit"
            class="w-full bg-[#1F2B6C] text-[#BFD2F8] font-bold py-2 hover:bg-blue-400 transition-colors"
          >
            SUBMIT
          </button>
        </form>
      </div>
    </div>

    <!-- Right Column (Schedule Card) -->
    <div class="max-w-xl mx-auto lg:mx-0 bg-[#1F2B6C] text-white shadow-lg p-6 w-full">
      <h2 class="text-4xl lg:text-6xl font-bold text-center mb-4">
        Schedule Hours
      </h2>

      <div class="space-y-3">
        <div
          v-for="(day, index) in schedule"
          :key="index"
          class="flex items-center"
        >
          <span class="w-28">{{ day.day }}</span>
          <span class="border-b border-gray-400 w-6 mx-2 inline-block"></span>
          <span class="w-64 text-right">{{ day.time }}</span>
        </div>
      </div>

      <div class="border-b border-gray-400 my-4"></div>

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
    <iframe
      class="w-full h-full rounded-lg shadow-md"
      src="https://www.google.com/maps?q=No.1376,+2nd+floor,+13th+Cross,+Sarakki+Main+Rd,+1st+Phase,+J.+P.+Nagar,+Bengaluru,+Karnataka+560078&output=embed"
      allowfullscreen=""
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
    ></iframe>
  </section>

  <Contact />
</template>

<script>
import Contact from "./Contact.vue";

export default {
  name: "AppointmentPage",
  components: { Contact },
  data() {
    return {
      departments: [],
      doctors: [],
      form: {
        name: "",
        gender: "",
        email: "",
        phone: "",
        department: "",
        doctor: "",
        date: "",
        time: "",
        message: "",
      },
      schedule: [
        { day: "Monday", time: "09:00 AM - 07:00 PM" },
        { day: "Tuesday", time: "09:00 AM - 07:00 PM" },
        { day: "Wednesday", time: "09:00 AM - 07:00 PM" },
        { day: "Thursday", time: "09:00 AM - 07:00 PM" },
        { day: "Friday", time: "09:00 AM - 07:00 PM" },
        { day: "Saturday", time: "09:00 AM - 07:00 PM" },
        { day: "Sunday", time: "Closed" },
      ],
    };
  },
  methods: {
    // ✅ Get all departments
    async fetchDepartments() {
      try {
        const res = await fetch(
          "/api/method/healthcare_app.api.Appointment_api.get_departments"
        );
        const data = await res.json();

        if (data.message?.status === "success" && Array.isArray(data.message.data)) {
          this.departments = data.message.data.map((dept) => dept.department);
        } else {
          console.error("Error fetching departments:", data.message);
        }
      } catch (e) {
        console.error("Error loading departments:", e);
      }
    },

    // ✅ Get doctors based on department
    async fetchDoctors() {
      if (!this.form.department) {
        this.doctors = [];
        return;
      }
      try {
        const dept = this.form.department.trim();
        const res = await fetch(
          `/api/method/healthcare_app.api.Appointment_api.get_practitioners?department=${encodeURIComponent(
            dept
          )}`
        );
        const data = await res.json();

        if (data.message?.status === "success" && Array.isArray(data.message.data)) {
          this.doctors = data.message.data;
        } else {
          this.doctors = [];
        }
      } catch (e) {
        console.error("Error loading doctors:", e);
      }
    },

    // ✅ Submit appointment form
    async submitAppointment() {
      const payload = {
        patient: this.form.name,
        appointment_date: this.form.date,
        appointment_time: this.form.time,
        department: this.form.department,
        practitioner: this.form.doctor,
        email: this.form.email,
        mobile: this.form.phone,
        gender: this.form.gender,
        notes: this.form.message,
      };

    try {
  const res = await fetch(
    "/api/method/healthcare_app.api.Appointment_api.create_appointment",
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    }
  );
  const data = await res.json();

  if (data.message?.status === "success") {
    console.log("✅ Appointment booked successfully!");
    this.resetForm();
  } else {
    console.error("❌ Failed:", data.message?.message || "Unknown error");
  }
} catch (error) {
  console.error("⚠️ Error submitting form:", error);
}
    },

    resetForm() {
      this.form = {
        name: "",
        gender: "",
        email: "",
        phone: "",
        department: "",
        doctor: "",
        date: "",
        time: "",
        message: "",
      };
      this.doctors = [];
    },
  },
  mounted() {
    this.fetchDepartments();
  },
};
</script>
