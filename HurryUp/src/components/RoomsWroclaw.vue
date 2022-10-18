<template>
  <article id="Rooms">
    <h2 class="RoomsHeader text-300 text-center my-6">Wrocławskie Pokoje</h2>
    <div
      class="w-10 m-auto flex justify-content-around mb-6 roomsCardsContainer"
    >
      <Card
        @click="
          openModal();
          setN(0);
        "
        class="smerfy cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Wioska Smerfów
          </p>
        </template>
      </Card>

      <Card
        @click="
          openModal();
          setN(1);
        "
        class="jumanji cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Jumanji
          </p>
        </template>
      </Card>
      <Card
        @click="
          openModal();
          setN(2);
        "
        class="addamsi cursor-pointer"
      >
        <template #title>
          <p class="text-2xl scale text-center transition-duration-400">
            Rodzina Addamsów
          </p>
        </template>
      </Card>
    </div>
  </article>
  <Dialog
    header=""
    v-model:visible="displayModal"
    :breakpoints="{ '960px': '75vw', '640px': '90vw' }"
    :modal="true"
    position="top"
    :draggable="false"
  >
    <template #header class="flex justify-content-center align-items-center">
      <div
        v-if="roomsAray[n].name === 'Wioska Smerfów'"
        class="h-10rem w-full overflow-hidden smerfy flex justify-content-center align-items-center"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
      <div
        v-if="roomsAray[n].name === 'Jumanji'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center jumanji"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
      <div
        v-if="roomsAray[n].name === 'Rodzina Addamsów'"
        class="h-10rem w-full overflow-hidden flex justify-content-center align-items-center addamsi"
      >
        <h2>
          {{ roomsAray[n].name }}
        </h2>
      </div>
    </template>
    <div>
      <p class="roomDescription mt-6 font-bold text-lg">{{ roomsAray[n].H1 }}</p>
      <p class="roomDescription">{{ roomsAray[n].p }}</p>
      <p class="roomDescription">{{ roomsAray[n].p2 }}</p>
    </div>
    <div class="flex justify-content-between mt-8 mx-auto text-lg">
      <div class="">
        <p><i class="pi pi-users mr-2"></i>ilość graczy</p>
        <p><i class="pi pi-hourglass mr-2"></i>czas</p>
        <p><i class="pi pi-calendar mr-2"></i>wiek</p>
        <p><i class="pi pi-star mr-2"></i>poziom trudności</p>
        <p><i class="pi pi-language mr-2"></i>język gry</p>
        <p><i class="pi pi-money-bill mr-2"></i>cena</p>
        <p class="mt-6 font-bold">{{ roomsAray[n].additionalP }}</p>
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
        class="p-button-rounded w-12 text-xl button text-black-alpha-70"
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
    name: "Wioska Smerfów",
    H1: "Smerfom grozi wielkie niebezpieczeństwo! Gargamel odnalazł drogę do ich Wioski.",
    p: "Jedyną nadzieją jest wysmerfowanie eliksiru i przechytrzenie złego czarnoksiężnika. Czasu jest niewiele!",
    p2: "Pokój Wioska Smerfów zabierze Was do baśniowej krainy, w której stawicie czoła smerfowym zadaniom i spróbujecie przechytrzyć Gargamela. Smerfna zabawa gwarantowana!",
    numberOfPlayers: "2-5",
    time: "60'",
    age: "+0",
    level: "4/5",
    price: "170PLN",
    additionalP: "",
    url: "../assets/img/2RA.jpg",
  },
  {
    name: "Jumanji",
    H1: "Istnieją gry, których lepiej nie zaczynać... Pełne niebezpieczeństw, pułapek i niedokończonych historii.",
    p: "Jedną z takich gier jest JUMANJI, która teraz trafia w Wasze ręce. Czy będziecie na tyle odważni, by stawić czoła zagadkom i ukończyć grę? Czy zdołacie uwolnić Alana Parrisha, który został wchłonięty przez JUMANJI?",
    numberOfPlayers: "2-5",
    time: "60'",
    age: "+0",
    level: "4/5",
    price: "170PLN",
    p2: "GRA SIĘ ZACZYNA... dum dum dum dum dum…",
    additionalP: "",
  },
  {
    name: "Rodzina Addamsów",
    H1: "To już 25 lat odkąd wujaszek Fester zaginął…",
    p: "Wy natomiast, jako kochająca Rodzina, zrobicie wszystko, aby go odnaleźć!… I poskładać do kupy… Dosłownie!",
    p2: "",
    numberOfPlayers: "2-4",
    time: "90'",
    age: "+16",
    level: "3/5",
    price: "250PLN",
    additionalP:
      "UWAGA! Pokój wymaga nieco sprawności fizycznej (zalecamy wygodny ubiór) oraz jest nieodpowiedni dla osób z klaustrofobią.",
  },
];

const displayModal = ref(false);

const openModal = () => {
  displayModal.value = true;
};
</script>
