import { createRouter, createWebHistory } from 'vue-router'
import Home from './pages/Home.vue'
import Footer from './pages/Footer.vue'
import Doctors from './pages/Doctors.vue'
import Contact from './pages/Contact.vue'
import AboutUs from './pages/AboutUs.vue'
import Services from './pages/Services.vue'
import DoctorsList from './pages/DoctorsList.vue'
import ContactUs from './pages/ContactUs.vue'
import AppointmentPage from './pages/AppointmentPage.vue'
import SingleServicePage from './pages/SingleServicePage.vue'
import BackToTop from './pages/BackToTop.vue'
const routes = [
    {
    path: '/',
    name: 'Home',
    component: Home,
  },
     {
    path: '/footer',
    name: 'Footer',
    component: Footer,
  },

    {
    path: '/doctors',
    name: 'Doctors',
    component: Doctors,
  },
     {
    path: '/contact',
    name: 'Contact',
    component: Contact,
  },
   {
    path: '/aboutUs',
    name: 'AboutUs',
    component: AboutUs,
  },
   {
    path: '/services',
    name: 'Services',
    component: Services,
  },
   {
    path: '/doctorsList',
    name: 'DoctorsList',
    component: DoctorsList,
  },
     
  {
    path: '/contactUs',
    name: 'ContactUs',
    component: ContactUs,
  },
   {
    path: '/appointmentPage',
    name: 'AppointmentPage',
    component: AppointmentPage,
  },
   {
    path: '/singleServicePage',
    name: 'SingleServicePage',
    component: SingleServicePage,
  },
  {
    path: '/backToTop',
    name: 'BackToTop',
    component: BackToTop,
  },
]

let router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
