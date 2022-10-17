<template>
  <div>
    <Menubar :model="items" class="bg-black-alpha-90 flex justify-content-end">
      <template #start>
        <a class="menuItem" href="/">
          <img
            alt="logo"
            src="../assets/img/klepsydra.png"
            class="my-1 h-2rem"
            to="/"
          />
        </a>
      </template>
      <template #item="{ item }">
        <a class="text-sm" :href="item.url">
          <i :class="item.icon" class="mr-1" v-if="width <= 960"></i>
          {{ item.label }}
        </a>
      </template>
      <template #end>
        <Button
          label="REZERWACJA"
          class="text-sm p-button-outlined border-round-3xl ml-2 text-white rezerwation"
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
*:focus {
  box-shadow: none !important;
}

.logoImg {
  height: 60%;
}

.p-menubar {
  border: none !important;
  border-radius: 0 !important;
}

.p-menubar-end {
  margin-left: 0 !important;
  margin-right: 5vw;
}

.p-menubar-start {
  flex-grow: 1;
  margin-left: 5vw;
}

li > a {
  margin: 0 1rem;
}

li > a:hover {
  color: rgb(116, 116, 116) !important;
}

.p-menubar .p-menubar-button:hover {
  background-color: rgb(35, 35, 35) !important;
}

@media screen and (max-width: 960px) {
  .p-menubar .p-menubar-root-list {
    background-color: #1a1a1a !important;
  }

  .p-menuitem {
    text-align: center;
    margin: 2.5rem 0 2.5rem 0;
  }
}

.rezerwation:enabled:hover {
  background-color: rgb(35, 35, 35) !important;
}
</style>
