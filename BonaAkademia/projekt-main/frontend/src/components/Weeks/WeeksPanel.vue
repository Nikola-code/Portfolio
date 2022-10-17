<template>
  <div class="card">
    <div class="flex align-items-center mt-6 justify-content-center">
      <div class="px-1">
        <Button
          label="Poprzedni tydzień"
          class="p-button-raised p-button-rounded bg-red-700 border-red-700"
          @click="weekBefore()"
        />
      </div>
      <div>
        <span for="date" class="p-input-icon-right">
          <InputMask
            id="date"
            mask="99/99/9999"
            v-model="val3"
            placeholder="dd.mm.yyyy"
            slotChar="dd.mm.yyyy"
            icon="pi pi-calendar"
            autoclear="true"
          />
          <i class="pi pi-calendar"></i>
        </span>
      </div>
      <div class="px-1">
        <Button
          label="Następny tydzień"
          class="p-button p-button-rounded bg-red-700 border-red-700"
          iconPos="right"
          @click="weekAfter()"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import Button from "primevue/button";
import InputMask from "primevue/inputmask";

const id = ref();
const weekNum = ref();

const weekend = () => {
  id.value = true;
  weekNum.value = {};
};

const weekBefore = () => {};
const weekAfter = () => {};
weekend();

// wyświetlanie daty: --> rok/miesiąc/dzień
</script>
