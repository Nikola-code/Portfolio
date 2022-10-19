<template>
  <div
    class="mainContainer h-screen flex flex-column align-content-center overflow-hidden"
  >
    <img
      class="w-2rem align-self-start mt-5 ml-8"
      src="../assets/img/klepsydra.png"
      alt="logo"
    />
    <div class="flex align-items-center justify-content-center flex-grow-1">
      <router-link
        class="flex imgContainer1 border-round-2xl align-items-end justify-content-end w-30rem h-10rem"
        :to="{ params: { prop: 'wroclaw' }, name: 'MainView' }"
      >
        <p class="text-7xl m-5 text-white">
          <span>W</span><span>r</span><span>o</span><span>c</span><span>ł</span
          ><span>a</span><span>w</span>
        </p>
      </router-link>
      <router-link
        class="flex imgContainer2 border-round-2xl align-items-end justify-content-end w-30rem h-10rem"
        :to="{ params: { prop: 'bielsko' }, name: 'MainView' }"
      >
        <p class="text-7xl m-5 text-white">
          <span>B</span><span>i</span><span>e</span><span>l</span><span>s</span
          ><span>k</span><span>o</span><span>-</span><span>B</span><span>i</span
          ><span>a</span><span>ł</span><span>a</span>
        </p>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style>
.imgContainer1 {
  background: linear-gradient(-45deg, #0a0708, #444444);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
  margin-right: 3rem;
  box-shadow: rgba(66, 66, 66, 0.73) 0px 26px 30px -10px, rgba(66, 66, 66, 0.73) 0px 16px 10px -10px;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

p > span {
  transition: opacity 0.5s;
  opacity: 1;
}

p > span:hover {
  opacity: 0;
}

.imgContainer2 {
  background: linear-gradient(-45deg, #444444, #0a0708);
  animation: gradient 15s ease infinite;
  margin-left: 3rem;
  box-shadow: 8px 15px 47px -9px rgba(66, 68, 90, 1);
}

.imgContainer1 > p,
.imgContainer2 > p {
  font-family: "Bree Serif", serif;
}

.mainContainer {
  background-image: url(../assets/img/bgi/andrew-kliatskyi-0gTTqEaAW3g-unsplash.jpg);
  background-position: center center;
  background-size: cover;
  background-repeat: no-repeat;
  font-family: "Bree Serif", serif;
  color: white;
}

@media screen and (max-width: 960px) {
  .mainContainer> div{
    flex-direction: column;
  }

  .imgContainer1, .imgContainer2{
    margin: 2rem 0 2rem 0;
  }
}
</style>
