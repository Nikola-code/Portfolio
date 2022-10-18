<template>
  <MenuBar />
  <header
    class="text-300 text-center h-15rem mx-auto mt-8 mb-5 align-items-center"
  >
    <h1>Przeżyj niesamowitą przygodę!</h1>
    <p class="mt-4">
      Live escape room to gra, dzięki której przeniesiesz się do innej
      rzeczywistości, a Twoim zadaniem będzie wyjście z tajemniczego pokoju.
      Zbierz ekipę i rezerwuj termin już dziś!
    </p>
  </header>
  <RoomsWroclaw v-if="$route.params.prop === 'wroclaw'" />
  <RoomsBielsko v-if="$route.params.prop === 'bielsko'" />
  <div id="Info">
    <div class="text-300 text-center mx-auto my-8 infoContainer">
      <h2>Ale o co chodzi?</h2>
      <p class="paragraph">
        Escape roomy, zwane także pokojami zagadek, są nową formą rozrywki,
        zdobywającą ogromną popularność nie tylko w Polsce, ale i na całym
        świecie.
      </p>
      <p class="paragraph">
        Wraz ze swoją ekipą trafiacie do tematycznie zaaranżowanego pokoju, z
        którego musicie się wydostać w określonym czasie, rozwiązując zadania,
        jakie dla Was przygotowaliśmy.
      </p>
      <p class="paragraph">
        Każdy pokój posiada zróżnicowany scenariusz oraz unikalne zagadki, które
        zadowolą zarówno wytrawnych graczy, jak i escaperoomowych nowicjuszy.
      </p>
      <p class="paragraph">Zapoznaj się z <a href="#">Regulaminem</a>.</p>
    </div>
  </div>
  <div
    class="flex flex-column justify-content-around align-items-center h-30rem py-8"
  >
    <div>
      <h2 class="mb-4 text-center">Niezapomniana przygoda czeka!</h2>
      <h2 class="text-center">Podejmiesz wyzwanie?</h2>
    </div>
    <Button
      label="REZERWACJA"
      class="p-button-rounded text-black-alpha-70 bg-white text-xl border-900 infoRezerwation"
    />
  </div>
  <div id="vouchery">
    <section class="mx-auto flex flex-column align-items-center">
      <h2 class="my-8 text-center">Szukasz nietypowego prezentu?</h2>
      <div class="h-10rem flex flex-column align-items-center">
        <p>Podaruj bliskim voucher do Hurry Up!</p>
        <p class="text-center">
          Voucher upoważnia do gry w jednym z naszych pokoi, a termin jego
          realizacji wynosi 3 miesiące.
        </p>
      </div>
      <div class="flex justify-content-center infoVouchersContainer">
        <Card>
          <template #title>
            <i class="pi pi-shopping-bag mt-3 text-white text-5xl"></i>
          </template>
          <template #content>
            <p class="mx-auto w-10">
              Zakupu można dokonać w siedzibie naszej firmy
              {{ citys[$route.params.prop].adress }}, po wcześniejszym umówieniu
              się telefonicznie...
            </p>
          </template>
        </Card>
        <Card>
          <template #title>
            <i class="pi pi-send mt-3 text-white text-5xl"></i>
          </template>
          <template #content>
            <p class="mx-auto w-10">
              ...bądź z możliwością przesyłki kurierskiej pod wskazany adres.
            </p>
          </template>
        </Card>
      </div>
      <div class="text-center mt-6 w-9 vouchersContact">
        <p class="m-4">
          W celu zamówienia vouchera prosimy o kontakt telefoniczny
        </p>
        <p class="m-4">
          <i class="pi pi-phone"></i>

          {{ citys[$route.params.prop].number }}
        </p>
        <p class="m-4">bądź mailowy</p>
        <p class="m-4">
          <i class="pi pi-envelope"></i>

          {{ citys[$route.params.prop].mail }}
        </p>
        <p class="m-2">
          Realizacja vouchera wymaga uprzedniej rezerwacji terminu. Cena
          vouchera jest równoznaczna z ceną gry w danym pokoju.
        </p>
      </div>
      <div class="voucherPrices m-8">
        <h2 class="text-center m-6">Cennik voucherów</h2>
        <div class="flex justify-content-around">
          <div v-if="$route.params.prop === 'bielsko'" class="w-4">
            <p>Dowolny pokój</p>
            <p>Łowcy snów</p>
            <p>Zodiak</p>
            <p>Joker</p>
            <p class="mb-6">Posterunek 13</p>
          </div>
          <div v-if="$route.params.prop === 'wroclaw'" class="w-4">
            <p>Dowolny pokój</p>
            <p>Rodzina Addamsów</p>
            <p>Jumanji</p>
            <p class="mb-6">Wioska Smerfów</p>
          </div>
          <div
            v-if="$route.params.prop === 'bielsko'"
            class="w-4 flex flex-column align-items-end"
          >
            <p class="font-bold">150 PLN</p>
            <p class="font-bold">120 PLN</p>
            <p class="font-bold">150 PLN</p>
            <p class="font-bold">150 PLN</p>
            <p class="font-bold mb-6">120 PLN</p>
          </div>
          <div
            v-if="$route.params.prop === 'wroclaw'"
            class="w-4 flex flex-column align-items-end"
          >
            <p class="font-bold">250 PLN</p>
            <p class="font-bold">250 PLN</p>
            <p class="font-bold">180 PLN</p>
            <p class="font-bold mb-6">180 PLN</p>
          </div>
        </div>
      </div>
      <div id="contakt" class="contact pb-6 mb-8">
        <h2 class="text-center m-6">Kontakt</h2>
        <div class="flex justify-content-around contactContainer">
          <div>
            <p>
              <i class="pi pi-envelope mr-2" style="font-size: 1rem"></i>

              {{ citys[$route.params.prop].mail }}
            </p>
            <p>
              <i class="pi pi-phone mr-2" style="font-size: 1rem"></i>

              {{ citys[$route.params.prop].number }}
            </p>
            <p>
              <i class="pi pi-facebook mr-2" style="font-size: 1rem"></i>
              <a
                v-if="$route.params.prop === 'wroclaw'"
                href="http://www.facebook.pl/Wroclawhurryup"
                target="_blank"
                class="underline"
                >facebook</a
              >
              <a
                v-if="$route.params.prop === 'bielsko'"
                href="http://www.facebook.pl/Bielskohurryup"
                target="_blank"
                class="underline"
                >facebook</a
              >
            </p>
          </div>
          <div class="flex flex-column align-items-end">
            <p>
              <i class="pi pi-map-marker" style="font-size: 1rem"></i>
              {{ citys[$route.params.prop].adress }}
            </p>
            <p>
              <a
                v-if="$route.params.prop === 'wroclaw'"
                href="https://goo.gl/maps/pJchJ7hPWkcX2LECA"
                target="_blank"
                class="underline"
                >pokaż na mapie</a
              >
              <a
                v-if="$route.params.prop === 'bielsko'"
                href="https://goo.gl/maps/aqFTVvZGZmeYcGRm7"
                target="_blank"
                class="underline"
                >pokaż na mapie</a
              >
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script setup>
import MenuBar from "../components/MenuBar.vue";
import RoomsWroclaw from "../components/RoomsWroclaw.vue";
import Button from "primevue/button";
import Card from "primevue/card";
import RoomsBielsko from "../components/RoomsBielsko.vue";

const citys = {
  wroclaw: {
    adress: "ul. Ruska 61/6b",
    number: "+48 797 407 743",
    mail: "wroclaw@hurry-up.pl",
  },
  bielsko: {
    adress: "ul. Wzgórze 19/7",
    number: "+48 510 171 107",
    mail: "bielsko@hurry-up.pl",
  },
};
</script>

<style>
#Info {
  padding: 5vh 0 5vh 0;
  background-color: #1a1a1a;
}

.infoContainer {
  width: 60%;
}

.paragraph {
  margin: 5vh;
}

#vouchery {
  background-color: #1a1a1a;
}

.voucherPrices,
.contact {
  border: 1px solid #333333;
  box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.4);
  border-radius: 16px;
  color: white;
  width: 75%;
}

.contact {
  background-color: rgb(50, 50, 50);
}

.p-button.infoRezerwation {
  transition: width 0.5s;
  transition-timing-function: linear;
  width: 20rem;
}

.p-button.infoRezerwation:hover {
  width: 30%;
}

header,
section {
  width: 60%;
}

.infoVouchersContainer > .p-card.p-card.p-component {
    background-color: rgba(26, 26, 26, 0.64);
    text-align: center;
    width: 25rem;
    height: 17rem;
    line-height: 1.5;
  }

  .infoVouchersContainer > .p-card.p-card.p-component p{
    font-size: 1.3rem;
  }

@media screen and (max-width: 1200px) {
  header,
  .infoContainer,
  section,
  .voucherPrices,
  .contact {
    width: 90%;
    margin: 0;
  }

  .contactContainer div>p{
    width: 250px;
  }

  .infoVouchersContainer {
    flex-direction: column;
  }

  #contakt .contactContainer,
  #contakt div div {
    flex-direction: column;
    align-items: center;
  }

  .voucherPrices div > div:first-of-type {
    flex-grow: 2;
    padding-left: 30px;
  }

  .voucherPrices div > div {
    padding-right: 30px;
  }

  .infoVouchersContainer > .p-card.p-card.p-component p{
    font-size: 1rem;
    margin-top: 1.5rem;
  }
}
</style>
