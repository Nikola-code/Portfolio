<template>
  <Dialog
    v-model:visible="cVisible"
    :header="header"
    :modal="true"
    :draggable="false"
    class="p-fluid w-4"
  >
    <div class="px-8 flex flex-column justify-content-center">
      <div class="field">
        <label for="shortcut">Krótka nazwa</label>
        <InputText id="shortcut" type="shortcut" v-model="shortcut" />
      </div>

      <div class="field">
        <label for="fullName">Pełna nazwa</label>
        <InputText id="fullName" type="fullName" v-model="fullName" />
      </div>

      <div class="field">
        <label for="status">Pracownicy</label>
        <MultiSelect
          v-model="selectedWorkers"
          :options="workersList"
          optionLabel="name"
          optionValue="id"
          placeholder="Wybierz pracownika"
          id="name"
        />
      </div>
      <div class="field">
        <label for="status">Kierownik</label>
        <Dropdown
          v-model="selectedLeaders"
          :options="leadersList"
          optionLabel="name"
          optionValue="id"
          placeholder="Wybierz kierownika"
          id="leader"
        />
      </div>

      <Button
        class="w-8 align-self-center bg-indigo-800 border-indigo-800"
        icon="pi pi-check"
        label="Akceptuje"
        v-bind:disabled="isEmpty()"
        v-on:click="addTeam()"
      />
    </div>
  </Dialog>
</template>

<script setup>
import propertyIsEmpty from "./../../helpers/helpers.js";

import { ref, toRefs, computed } from "vue";

import Button from "primevue/button";
import InputText from "primevue/inputtext";
import MultiSelect from "primevue/multiselect";
import Dropdown from "primevue/dropdown";
import Dialog from "primevue/dialog";
import axios from "../../config/axios.js";

const props = defineProps({
  visible: Boolean,
  header: String,
});

const { visible, header } = toRefs(props);

const shortcut = ref();
const fullName = ref();
const selectedWorkers = ref();
const selectedLeaders = ref();

const isEmpty = () => {
  if (
    propertyIsEmpty(shortcut) ||
    propertyIsEmpty(fullName) ||
    selectedWorkers.value === undefined ||
    selectedLeaders.value === undefined ||
    workersList.value === undefined
  ) {
    return true;
  } else {
    return false;
  }
};

const workersList = ref([]);

const getTeamsWorkers = () => {
  axios.get("/teams-workers/").then((response) => {
    workersList.value = response.data;
  });
  return workersList;
};

getTeamsWorkers();

const leadersList = ref([]);

const getTeamsLeaders = () => {
  axios.get("/teams-leaders/").then((response) => {
    leadersList.value = response.data;
  });
  return leadersList;
};

getTeamsLeaders();

const emit = defineEmits(["update:visible", "fetchData"]);

const cVisible = computed({
  get: () => visible.value,
  set: (val) => {
    emit("update:visible", val);
  },
});

const addTeam = () => {
  axios
    .post("/teams/", {
      shortcut: shortcut.value,
      fullName: fullName.value,
      leader: selectedLeaders.value,
    })
    .then((response) => {
      console.log(response);
    })
    .catch((err) => {
      console.error(err);
    })
    .finally(() => {
      cVisible.value = false;
      emit("fetchData");
    });
};
</script>
