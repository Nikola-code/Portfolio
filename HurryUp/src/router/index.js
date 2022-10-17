import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MainView from "../views/MainView.vue";
import RoomsBielsko from "../components/RoomsBielsko.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/MainView:prop",
      name: "MainView",
      component: MainView,
      props:true
    },
    {
      path: "/RoomsBielsko",
      name: "RoomsBielsko",
      component: RoomsBielsko,
    },
  ],
});

export default router;
