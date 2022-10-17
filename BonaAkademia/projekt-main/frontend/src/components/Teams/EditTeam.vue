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
        <InputText
          id="shortcut"
          type="shortcut"
          v-model="shortcut"
          optionValue="id"
        />
      </div>
      <div class="field">
        <label for="fullName">Pełna nazwa</label>
        <InputText
          id="fullName"
          type="fullName"
          v-model="fullName"
          optionValue="id"
        />
      </div>
      <div class="field">
        <label for="status">Pracownicy</label>
        <MultiSelect
          v-model="selectedWorkers"
          :options="workersList"
          optionLabel="name"
          optionValue="id"
          placeholder="Wybierz pracownika"
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
        />
      </div>
      <Button
        class="w-8 align-self-center bg-indigo-800 border-indigo-800"
        icon="pi pi-check"
        label="Akceptuje"
        v-on:click="editTeam"
      />
    </div>
  </Dialog>
</template>

<script setup>
import { ref, toRefs, computed, watch } from "vue";

import Button from "primevue/button";
import InputText from "primevue/inputtext";
import MultiSelect from "primevue/multiselect";
import Dropdown from "primevue/dropdown";
import Dialog from "primevue/dialog";
import axios from "../../config/axios.js";

const props = defineProps({
  teams: Object,
  visible: Boolean,
  header: String,
});

const { teams, visible, header } = toRefs(props);

const shortcut = ref(teams.value.shortcut);
const fullName = ref(teams.value.fullName);
const id = ref(teams.value.id);

const selectedWorkers = ref(teams.value.selectedWorkers);
const selectedLeaders = ref(teams.value.selectedLeaders);

const emit = defineEmits(["update:visible", "fetchData"]);

const cVisible = computed({
  get: () => visible.value,
  set: (val) => {
    emit("update:visible", val);
  },
});

watch(teams, (newVal) => {
  if (newVal) {
    shortcut.value = newVal.shortcut;
    fullName.value = newVal.fullName;
    selectedLeaders.value = newVal.leader;
    selectedWorkers.value = newVal.workers;
  }
});

const editTeam = () => {
  const urlName = "/teams-creation/" + id.value + "/";

  axios
    .put(urlName, {
      id: id.value,
      shortcut: shortcut.value,
      fullName: fullName.value,
      leader: selectedLeaders.value,
      members: selectedWorkers.value,
    })
    .then(() => {
      cVisible.value = false;
      emit("fetchData");
    });
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
</script>
