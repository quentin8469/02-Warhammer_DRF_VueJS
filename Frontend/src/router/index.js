import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import WarhammerHome from '../components/Warhammer/WarhammerHome.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/jdrmanager',
            name: 'home',
            component: Home
        },
        {
            path: '/Warhammer',
            name: 'WarhammerHome',
            component: WarhammerHome
        },
    ]
})

export default router