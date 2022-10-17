<template>
  <div class="mainContainer h-screen flex flex-column align-content-center">
    <img
      class="logo w-2rem align-self-start"
      src="../assets/img/klepsydra.png"
      alt="logo"
    />
    <div class="flex align-items-center justify-content-center flex-grow-1">
      <router-link
        class="flex imgContainer1 border-round-2xl align-items-end justify-content-end w-5 mr-2"
        :to="{params: {prop: 'wroclaw'}, name: 'MainView'}">
        <p class="text-7xl m-5 text-white">Wrocław</p>
      </router-link>
      <router-link
        class="flex imgContainer2 border-round-2xl align-items-end justify-content-end w-5 ml-2"
        :to="{params: {prop: 'bielsko'}, name: 'MainView'}">
      >
        <p class="text-7xl m-5 text-white">Bielsko Biała</p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

</script>

<style>
.imgContainer1,
.imgContainer2 {
  background-image: url(../assets/img/3J.jpg);
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
  height: 90%;
  filter: grayscale(50%);
}

.imgContainer2 {
  background-image: url(../assets/img/2RA.jpg);
}

.imgContainer1 > p,
.imgContainer2 > p {
  font-family: "Bree Serif", serif;
}

.logo {
  margin-left: 6vw;
  margin-top: 4vh;
}
</style>
