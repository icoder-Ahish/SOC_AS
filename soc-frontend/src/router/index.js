import { createRouter, createWebHistory } from 'vue-router'

import loginPage from '../components/loginPage.vue'
// import homePage from '../components/homePage.vue'

// import homeView from '@/views/HomeView.vue'
import homeView from '@/views/DashBoard.vue'


const routes = [
  {
    name: 'login',
    path: '/',
    component: loginPage
  },
  {
    name: 'home',
    path: '/home',
    component: homeView
  },
  // {
  //   name: 'home',
  //   path: '/home',
  //   component: homePage
  // },

]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  linkExactActiveClass: 'text-yellow-500'
})



// Create the router guard
router.beforeEach((to, from, next) => {
  const allowedPaths = ['/', ];

  if (allowedPaths.includes(to.path)) {
   
    next();
  } else {
   
   
    const user_id = sessionStorage.getItem('user_id')
    const username = sessionStorage.getItem('username')

    if ( user_id || username) {
      
      next();
    } else {
      next('/');
    }
  }
});


export default router
