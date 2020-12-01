import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Checkchain from '../components/Checkchain.vue'
import Transaction from '../components/Transaction.vue'
import Mine from '../components/Mine.vue'
import Balance from '../components/Balance.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: {
            name: 'Login',
        }
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/checkchain',
        name: 'Checkchain',
        component: Checkchain
    },
    {
        path: '/mine',
        name: 'Mine',
        component: Mine
    },
    {
        path: '/transaction',
        name: 'Transaction',
        component: Transaction
    },
    {
        path: '/balance',
        name: 'Balance',
        component: Balance
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../components/About.vue')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router