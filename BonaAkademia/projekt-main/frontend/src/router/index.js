import { createRouter, createWebHistory } from "vue-router";

import Admin from "../views/Admin.vue";
import WeekTable from "../components/weeks/WeekTable.vue";
import WeekProjectPlan from "../components/weeks/WeekProjectPlan.vue"

const routes = [
  { path: "/", name: "Admin", component: Admin },
  {
    path: "/weekTable/:weekID",
    name: "weekTable",
    component: WeekTable,
    props: true,
  },
  {
    path: "/weekProjectPlan/:weekID",
    name: "weekProjectPlan",
    component: WeekProjectPlan,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),

  routes,
});

export default router;
