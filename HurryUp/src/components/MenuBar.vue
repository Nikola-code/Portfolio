<template>
  <div class="menuConainer">
    <Menubar :model="items" class="bg-black-alpha-90 flex justify-content-end">
      <template #start>
        <a class="menuItem" href="/">
          <img
            alt="logo"
            src="../assets/img/klepsydra.png"
            class="h-3rem"
            to="/"
          />
        </a>
      </template>
      <template #item="{ item }">
        <a class="text-lg" :href="item.url">
          <i :class="item.icon" class="mr-1" v-if="width <= 960"></i>
          {{ item.label }}
        </a>
      </template>
      <template #end>
        <Button
          label="REZERWACJA"
          class="p-button-outlined border-round-3xl ml-2 text-white rezerwation"
        ></Button>
      </template>
    </Menubar>
  </div>
</template>

<script setup>
import Button from "primevue/button";
import Menubar from "primevue/menubar";

// read screen width function

import { computed, onMounted, onUnmounted, ref } from "vue";

function useBreakpoints() {
  let windowWidth = ref(window.innerWidth);

  const onWidthChange = () => (windowWidth.value = window.innerWidth);
  onMounted(() => window.addEventListener("resize", onWidthChange));
  onUnmounted(() => window.removeEventListener("resize", onWidthChange));

  const type = computed(() => {
    if (windowWidth.value < 550) return "xs";
    if (windowWidth.value >= 550 && windowWidth.value < 1200) return "md";
    if (windowWidth.value >= 1200) return "lg";
    return null;
  });

  const width = computed(() => windowWidth.value);

  return { width, type };
}

const { width, type } = useBreakpoints();

// end of function

const items = [
  {
    label: "POKOJE",
    url: "#Rooms",
    icon: "pi pi-key",
  },
  {
    label: "INFORMACJE",
    url: "#Info",
    icon: "pi pi-info",
  },
  {
    label: "VOUCHERY",
    url: "#vouchery",
    icon: "pi pi-id-card",
  },
  {
    label: "KONTAKT",
    url: "#contakt",
    icon: "pi pi-phone",
  },
];
</script>

<style>

ul > li > a {
  margin: 0 1rem;
}

ul > li > a:hover {
  color: rgb(116, 116, 116);
}

.menuConainer>.p-menubar {
  border: none;
  border-radius: 0;
}

.menuConainer .p-menubar-end {
  margin-left: 0;
  margin-right: 5vw;
}

.menuConainer .p-menubar-start {
  flex-grow: 1;
  margin-left: 5vw;
}

.menuConainer .p-menubar .p-menubar-button:hover {
  background-color: rgb(35, 35, 35);
}

.menuConainer .p-button.p-button-outlined:enabled:hover {
  background-color: rgb(35, 35, 35);
}

@media screen and (max-width: 960px) {
  .menuConainer .p-menubar .p-menubar-root-list {
    background-color: #1a1a1a;
  }

  .p-menuitem {
    text-align: center;
    margin: 2.5rem 0 2.5rem 0;
  }
}
</style>
