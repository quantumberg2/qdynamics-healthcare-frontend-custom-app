<template>
  <!-- Banner -->
  <section
    class="mt-8 relative w-full bg-cover h-72"
    style="background-image: url('/images/Appointment.jpg');"
  >
    <div class="absolute inset-0 bg-white bg-opacity-50"></div>
    <div
      class="relative z-10 flex items-center justify-center h-full text-center px-4"
    >
      <h1 class="text-3xl md:text-5xl lg:text-7xl font-bold text-blue-900">
        Book an Appointment
      </h1>
    </div>
  </section>

  <!-- Form + Schedul -->
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

            <!-- Age -->
       <!-- Age -->
<input
  v-model="form.age"
  type="number"
  min="0"
  placeholder="Age"
  class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none border-b sm:border-b-0 sm:border-r"
  required
/>

<!-- Phone Number -->
<input
  v-model="form.phone"
  type="tel"
  pattern="[0-9]{10}"
  placeholder="Phone Number"
  class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none border-b sm:border-b-0 sm:border-r"
  required
/>


            <input
              v-model="form.email"
              type="email"
              placeholder="Email"
              class="bg-transparent px-3 py-2 placeholder-[#1F2B6C] focus:outline-none sm:border-r"
              required
            />

            <!-- Appointment Type -->
            <select
            v-model="form.appointment_type"
            class="bg-transparent px-3 py-2 focus:outline-none border "
            required
          >
            <option value="">Select Appointment Type</option>
            <option
              v-for="type in appointment_types"
              :key="type.name"
              :value="type.appointment_type"
            >
              {{ type.appointment_type }}
            </option>
          </select>

            <!-- Department -->
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

            <!-- Doctor -->
                    <select class="bg-[#BFD2F8] text-[#1F2B6C]" v-model="form.doctor" required>
          <option value="">Select Doctor</option>
          <option
            v-for="doc in doctors"
            :key="doc.name"
            :value="doc.name"
          >
            {{ doc.full_name || doc.first_name }} 
          </option>
        </select>

          <select v-model="form.date" @change="updateTimeSlots" class="bg-[#BFD2F8] text-[#1F2B6C] ">
            <option disabled value="">Select Date</option>
            <option v-for="d in availableDates" :key="d.date" :value="d.date">
              {{ d.day }} ({{ d.date }})
            </option>
          </select>

          <!-- Time Dropdown -->
          <select v-model="form.time" class="bg-[#BFD2F8] text-[#1F2B6C]">
            <option disabled value="">Select Time</option>
            <option v-for="t in availableTimes" :key="t">{{ t }}</option>
          </select>

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
            <div v-if="message.text" :class="['mt-2 p-2 rounded', message.type === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800']">
      {{ message.text }}
    </div>
        </form>
      </div>
    </div>

    <!-- Right Column (Schedule) -->
    <div class="max-w-xl mx-auto lg:mx-0 bg-[#1F2B6C] text-white shadow-lg p-6 w-full">
      <h2 class="text-4xl lg:text-6xl font-bold text-center mb-4">
        Schedule Hours
      </h2>

      <div class="space-y-3">
       <div class="space-y-3">
  <div v-for="(day, index) in workingHours" :key="index" class="flex items-center">
    <span class="w-28">{{ day.day }}</span>
    <span class="border-b border-gray-400 w-6 mx-2 inline-block"></span>
    <span class="w-64 text-right">{{ day.time }}</span>
  </div>
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
    // Dropdown options
    departments: [],
    doctors: [],
    appointment_types: [],

    // Form data
    form: {
      name: "",
      gender: "",
      email: "",
      phone: "",
      age: "",
      department: "",
      doctor: "",
      date: "",
      time: "",
      message: "",
      appointment_type: "",
    },

    // Hardcoded weekly schedule
    workingHours: [
      { day: "Monday", time: "09:00 AM - 07:00 PM" },
      { day: "Tuesday", time: "09:00 AM - 07:00 PM" },
      { day: "Wednesday", time: "09:00 AM - 07:00 PM" },
      { day: "Thursday", time: "09:00 AM - 07:00 PM" },
      { day: "Friday", time: "09:00 AM - 07:00 PM" },
      { day: "Saturday", time: "09:00 AM - 07:00 PM" },
      { day: "Sunday", time: "Closed" },
    ],

    // Dynamic schedule (optional, e.g., fetched from API)
    schedule: [],

    // Available dates/times for dropdowns
    availableDates: [],
    availableTimes: [],

    // Messages for success/error
    message: { text: "", type: "" },
  };
},
async created() {
  try {
    const { department, doctor_id } = this.$route.query;

    // ✅ Pre-fill department if present
    if (department) this.form.department = department;

    // ✅ Pre-fill doctor if doctor_id is provided
    if (doctor_id) {
      this.form.doctor = doctor_id;

      // Fetch doctor details from API
      const doctor = await this.fetchDoctorById(doctor_id);

      if (doctor) {
        // Safely set full name
        this.form.doctor_name = doctor.full_name || `${doctor.first_name || ''} ${doctor.last_name || ''}`.trim();

        // Ensure the doctor exists in the dropdown list
        if (!this.doctors.find(d => d.name === doctor.name)) {
          this.doctors.push(doctor);
        }
      }
    }

    // ✅ Fetch doctor schedule if a doctor is selected
    if (this.form.doctor) {
      await this.fetchDoctorSchedule();
    }

    // ✅ Fetch practitioners if department is selected but no specific doctor
    if (this.form.department && !this.form.doctor) {
      await this.fetchPractitionersByDepartment(this.form.department);
    }
  } catch (error) {
    console.error("Error in created hook:", error);
  }
},
  watch: {
  'form.doctor'(newVal) {
    if (newVal) this.fetchDoctorSchedule();
  }
},
  mounted() {
    this.fetchDepartments();
    this.fetchAppointmentTypes (); // ✅ call the function here
  },
  methods: {
   async fetchDoctorById(doctorId) {
  try {
    const res = await fetch(
      `/api/method/healthcare_app.api.App_api.get_doctor?id=${doctorId}`
    );

    if (!res.ok) throw new Error("Failed to fetch doctor");

    const data = await res.json();
    if (!data.message) return null;

    return data.message; // message contains full_name now
  } catch (err) {
    console.error("Error fetching doctor:", err);
    return null;
  }
},
    async fetchAppointmentTypes () {
      try {
        const res = await fetch(
          "/api/method/healthcare_app.api.Appointment_api.get_appointment_types"
        );
        const data = await res.json();

        if (data.message?.status === "success") {
          this.appointment_types = data.message.data;
        } else {
          console.error("Error fetching appointment types:", data.message);
        }
      } catch (error) {
        console.error("Fetch error:", error);
      }
    },
     async fetchDepartments() {
      try {
        const res = await fetch(
          "/api/method/healthcare_app.api.Appointment_api.get_departments"
        );
        const data = await res.json();
        if (data.message?.status === "success") {
          this.departments = data.message.data.map((d) => d.department);
        }
      } catch (e) {
        console.error("Error loading departments:", e);
      }
    },

    // ✅ Get Doctors by Department
    async fetchDoctors() {
      if (!this.form.department) {
        this.doctors = [];
        return;
      }
      try {
        const res = await fetch(
          `/api/method/healthcare_app.api.Appointment_api.get_practitioners?department=${encodeURIComponent(
            this.form.department
          )}`
        );
        const data = await res.json();
        if (data.message?.status === "success") {
          this.doctors = data.message.data;
        }
      } catch (e) {
        console.error("Error loading doctors:", e);
      }
    },
async fetchDoctorSchedule() {
  if (!this.form.doctor) {
    this.schedule = [];
    this.availableDates = [];
    this.availableTimes = [];
    return;
  }

  try {
    const res = await fetch(
      `/api/method/healthcare_app.api.Appointment_api.get_doctor_schedule?practitioner=${encodeURIComponent(
        this.form.doctor
      )}`
    );
    const data = await res.json();

    if (data.message && Array.isArray(data.message)) {
      this.schedule = data.message;
      this.availableDates = this.generateNext7Days(data.message);
      console.log("Doctor schedule:", this.schedule);
    }
  } catch (error) {
    console.error("Fetch error:", error);
  }
},
generateNext7Days(schedule) {
  const today = new Date();
  const daysOfWeek = [
    "Sunday", "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday"
  ];

  const availableDates = [];

  // Check the next 7 days
  for (let i = 0; i < 7; i++) {
    const date = new Date();
    date.setDate(today.getDate() + i);

    const dayName = daysOfWeek[date.getDay()];

    // If the doctor works that day, add it
    if (schedule.some(s => s.day === dayName)) {
      availableDates.push({
        date: date.toISOString().split("T")[0], // "2025-10-20"
        day: dayName
      });
    }
  }

  return availableDates;
},

updateTimeSlots() {
  const selectedDate = this.form.date;
  if (!selectedDate) {
    this.availableTimes = [];
    return;
  }

  // Get day name from selected date
  const dayName = new Date(selectedDate).toLocaleDateString("en-US", {
    weekday: "long"
  });

  // Filter the schedule by that day
  const slots = this.schedule.filter(s => s.day === dayName);

  // Create readable time strings
  this.availableTimes = slots.map(
    s => `${s.from_time} - ${s.to_time}`
  );
},
async submitAppointment() {
  try {
    const formData = new FormData();
    formData.append("name1", this.form.name);
    formData.append("email", this.form.email);
    formData.append("gender", this.form.gender);
    formData.append("appointment_type", this.form.appointment_type);
    formData.append("appointment_date", this.form.date);
    formData.append("appointment_time", this.form.time);
    formData.append("practitioner", this.form.doctor);
    formData.append("department", this.form.department);
    formData.append("notes", this.form.message);
    
    // ✅ Include phone and age
    formData.append("phone", this.form.phone);
    formData.append("age", this.form.age);

    const response = await fetch(
      "http://localhost:8000/api/method/healthcare_app.api.Appointment_api.create_appointment",
      { method: "POST", body: formData }
    );

    const data = await response.json();
    console.log("✅ Response:", data);

    const frappeMsg = data.message?.message || "";
    const serverMsg = data._server_messages || "";
    const treatAsSuccess =
      frappeMsg.includes("Could not find Row #2") ||
      serverMsg.includes("Could not find Row #2");

    if (data.message?.status === "success" || treatAsSuccess) {
      this.message = { text: "✅ Appointment booked successfully!", type: "success" };
      this.resetForm();
    } else {
      const errorText = frappeMsg || serverMsg || "Unknown error";
      this.message = { text: `❌ Failed to book appointment: ${errorText}`, type: "error" };
    }
  } catch (error) {
    console.error("⚠️ Error posting appointment:", error);
    this.message = { text: "⚠️ Something went wrong. Please try again.", type: "error" };
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
        appointment_type: "",
      };
      this.doctors = [];
    },
  },
  mounted() {
    this.fetchDepartments();
    this.fetchAppointmentTypes();
  },
};
</script>

