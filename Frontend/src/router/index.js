import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import WarhammerHome from '../components/Warhammer/WarhammerHome.vue'
import WarhammerPlayer from '@/components/Warhammer/WarhammerPlayer.vue'

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
        {
            path: '/Warhammer/WarhammerPlayerViewSet/:id/',
            name: 'WarhammerPlayer',
            component: WarhammerPlayer
        },
    ]
})

export default router