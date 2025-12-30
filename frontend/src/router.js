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
import ViewProfile from './pages/ViewProfile.vue'
import HomePageServices from './pages/HomePageServices.vue'
import HomePageAppointment from './pages/HomePageAppointment.vue'

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
  path: '/services/:department',
  name: 'SingleServicePage',
  component: SingleServicePage,
  props: true, // allows passing route params as props
},
  {
    path: '/backToTop',
    name: 'BackToTop',
    component: BackToTop,
  },
    {
    path: '/viewProfile/:id',
    name: 'ViewProfile',
    component: ViewProfile,
    props: true,
  },
   {
    path: '/homePageServices',
    name: 'HomePageServices',
    component: HomePageServices,
  },
  {
    path:'/homePageAppointment',
    name:'HomePageAppointment',
    component: HomePageAppointment,
  }
]

let router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
