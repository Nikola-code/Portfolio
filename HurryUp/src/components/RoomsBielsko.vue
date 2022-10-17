<template>
  <article id="Rooms">
    <h2 class="RoomsHeader text-300 text-center my-6">Bielsko-Biała pokoje</h2>
    <div
      class="w-10 m-auto flex justify-content-around mb-6 roomsCardsContainer"
    >
      <Card
        @click="
          openModal();
          setN(0);
        "
        class="lowcy cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Łowcy snów
          </p>
        </template>
      </Card>

      <Card
        @click="
          openModal();
          setN(1);
        "
        class="zodiak cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Zodiak
          </p>
        </template>
      </Card>
      <Card
        @click="
          openModal();
          setN(2);
        "
        class="joker cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Joker
          </p>
        </template>
      </Card>
      <Card
        @click="
          openModal();
          setN(3);
        "
        class="posterunek cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Posterunek 13
          </p>
        </template>
      </Card>
    </div>
  </article>
  <Dialog
    header=""
    v-model:visible="displayModal"
    :breakpoints="{ '960px': '75vw', '640px': '90vw' }"
    :style="{ width: '50vw', opacity: 0.98 }"
    :modal="true"
    position="top"
    :draggable="false"
  >
    <template #header class="flex justify-content-center align-items-center">
      <div
        v-if="roomsAray[n].name === 'Łowcy Snów'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center lowcy"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
      <div
        v-if="roomsAray[n].name === 'Zodiak'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center zodiak"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
      <div
        v-if="roomsAray[n].name === 'Joker'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center joker"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
      <div
        v-if="roomsAray[n].name === 'Posterunek 13'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center posterunek"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
    </template>
    <div>
      <p class="roomDescription mt-6 font-bold text-lg">
        {{ roomsAray[n].H1 }}
      </p>
      <p class="roomDescription text-sm">{{ roomsAray[n].p }}</p>
      <p class="roomDescription text-sm">{{ roomsAray[n].p2 }}</p>
    </div>
    <div class="flex justify-content-between mt-8 mx-auto text-lg">
      <div class="">
        <p><i class="pi pi-users mr-2"></i>ilość graczy</p>
        <p><i class="pi pi-hourglass mr-2"></i>czas</p>
        <p><i class="pi pi-calendar mr-2"></i>wiek</p>
        <p><i class="pi pi-star mr-2"></i>poziom trudności</p>
        <p><i class="pi pi-language mr-2"></i>język gry</p>
        <p><i class="pi pi-money-bill mr-2"></i>cena</p>
        <p class="mt-6 font-bold text-sm">{{ roomsAray[n].additionalP }}</p>
      </div>
      <div>
        <p>{{ roomsAray[n].numberOfPlayers }}</p>
        <p>{{ roomsAray[n].time }}</p>
        <p>{{ roomsAray[n].age }}</p>
        <p>{{ roomsAray[n].level }}</p>
        <p>Polski</p>
        <p>{{ roomsAray[n].price }}</p>
      </div>
    </div>
    <template #footer>
      <Button
        label="REZERWACJA"
        class="p-button-rounded w-12 text-xl button"
        autofocus
      />
    </template>
  </Dialog>
</template>

<script setup>
import Card from "primevue/card";
import { ref } from "vue";
import Button from "primevue/button";
import Dialog from "primevue/dialog";

let n = ref();

function setN(m) {
  return (n.value = m);
}

const roomsAray = [
  {
    name: "Łowcy Snów",
    H1: "Bywają takie chwile, w których zasypiamy, sami nawet nie wiedząc kiedy… ",
    p: "Jedyną nadzieją jest wysmerfowanie eliksiru i przechytrzenie złego czarnoksiężnika. Czasu jest niewiele!",
    p2: "Nasze sny to kraina niekończących się możliwości. Niezwykłe podróże, zadziwiające miejsca, wspaniałe przygody - wystarczy tylko zamknąć oczy! Pamiętajmy jednak, że każdy, nawet najpiękniejszy sen, może przemienić się w prawdziwy koszmar… I wtedy rodzi się tylko jedna myśl: „OBUDŹ MNIE!”, jak najszybciej!",
    numberOfPlayers: "2-5",
    time: "60'",
    age: "+0",
    level: "3/5",
    price: "150PLN",
    additionalP: "UWAGA! Pokój wymaga nieco sprawności fizycznej (zalecamy wygodny ubiór) oraz jest nieodpowiedni dla osób z klaustrofobią.",
    url: "../assets/img/josh-hild--0o-SwEnNt0-unsplash.jpg",
  },
  {
    name: "Zodiak",
    H1: "Znany dziennikarz wyruszył śladem seryjnego mordercy, pustoszącego ulice naszego miasta w ostatnich miesiącach. Niestety również po nim słuch zaginął",
    p: "Tajemnice ostatnich morderstw i porwań wciąż pozostają bez odpowiedzi. Czy w naszym mieście znajdą się śmiałkowie, będący w stanie zdemaskować tajemniczego psychopatę, przedstawiającego się jako Zodiak?",
    numberOfPlayers: "3-5",
    time: "60'",
    age: "+16",
    level: "4/5",
    price: "150PLN",
    p2: "",
    additionalP: "",
  },
  {
    name: "Joker",
    H1: "Wpadliście w pułapkę, a nawet o tym nie wiecie... To, co na pozór jest  puste, może skrywać wiele tajemnic…",
    p: "To, co wydaje się proste, często bywa skomplikowane. Wystarczy jeden fałszywy krok, aby znaleźć się w prawdziwych tarapatach! Życie to jedna wielka gra! Why so serious?! HA, HA, HA !",
    p2: "",
    numberOfPlayers: "2-5",
    time: "60'",
    age: "+0",
    level: "5/5",
    price: "120PLN",
    additionalP:"",
    url:"../assets/img/ryunosuke-kikuno-cqtw4QCfbQg-unsplash.jpg"
  },
  {
    name: "Posterunek 13",
    H1: "To dzieje się tylko w najgorszych snach. Jesteście niewinni, a mimo to oskarżono Was o poważne przestępstwo, za które grozi surowa kara. ",
    p: "Jednak dzięki inteligencji i błyskotliwości istnieje sposób, by dowieść swojej niewinności. Potraficie ją wykazać?",
    p2: "",
    numberOfPlayers: "2-5",
    time: "60'",
    age: "+0",
    level: "2/5",
    price: "120PLN",
    additionalP:"",
    url:"../assets/img/ye-jinghan-T5roX1jajzU-unsplash.jpg"
  },
];

const displayModal = ref(false);

const openModal = () => {
  displayModal.value = true;
};
</script>
