<template>
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
  </section>

 
</template>

<script>

export default {
  name: "AppointmentPage",
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
    // -----------------------------
    // Build FormData
    // -----------------------------
    const formData = new FormData();
    formData.append("name1", this.form.name);
    formData.append("email", this.form.email);
    formData.append("gender", this.form.gender);
    formData.append("appointment_type", this.form.appointment_type);
    formData.append("appointment_date", this.form.date);
    formData.append("appointment_time", this.form.time); // HH:MM:SS - HH:MM:SS
    formData.append("practitioner", this.form.doctor);
    formData.append("department", this.form.department);
    formData.append("notes", this.form.message || "");
    formData.append("phone", this.form.phone);
    formData.append("age", this.form.age);

    // -----------------------------
    // API Call
    // -----------------------------
    const response = await fetch(
      "/api/method/healthcare_app.api.Appointment_api.create_appointment",
      {
        method: "POST",
        body: formData
      }
    );

    const data = await response.json();
    console.log("✅ API Response:", data);

    // -----------------------------
    // Normalize response (IMPORTANT)
    // -----------------------------
    const result = data.message || data;

    // -----------------------------
    // SUCCESS
    // -----------------------------
    if (result.status === "success") {
      this.message = {
        text: "✅ Appointment booked successfully!",
        type: "success"
      };
      this.resetForm();
      return;
    }

    // -----------------------------
    // ERROR FROM API
    // -----------------------------
    this.message = {
      text: `❌ Failed to book appointment: ${result.message || "Unknown error"}`,
      type: "error"
    };

  } catch (error) {
    console.error("⚠️ Network/API Error:", error);
    this.message = {
      text: "⚠️ Something went wrong. Please try again.",
      type: "error"
    };
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

