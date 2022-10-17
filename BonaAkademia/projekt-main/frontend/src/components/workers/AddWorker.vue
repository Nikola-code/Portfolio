<template>
  <Dialog
    :modal="true"
    :draggable="false"
    class="p-fluid w-4"
    v-model:visible="cVisible"
    :header="header"
  >
    <div class="px-8 flex flex-column justify-content-center">
      <div class="field">
        <label for="firstName">Imię</label>
        <InputText 
          id="firstName" 
          type="firstName" 
          v-model="firstName"
        />
      </div>

      <div class="field">
        <label for="lastName">Nazwisko</label>
        <InputText 
          id="lastName" 
          type="lastName" 
          v-model="lastName" 
        />
      </div>

      <div class="field">
        <label for="email">Adres email</label>
        <InputText 
          id="email" 
          type="email" 
          v-model="email"
        />
      </div>

      <div class="field">
        <label for="team">Zespół</label>
        <Dropdown
          id="team"
          v-model="selectedTeam"
          :options="teams"
          optionLabel="shortcut"
          optionValue="id"
          placeholder="Wybierz zespół"
        />
      </div>

      <div class="field">
        <label for="role">Rola</label>
        <Dropdown
          id="role"
          v-model="selectedRole"
          :options="roles"
          optionLabel="name"
          optionValue="code"
          placeholder="Wybierz rolę"
        />
      </div>

      <div class="field">
        <label for="status">Status</label>
        <Dropdown
          id="status"
          v-model="status"
          :options="statuses"
          optionLabel="name"
          optionValue="code"
          placeholder="Wybierz status"
        />
      </div>

      <Button
        type="submit"
        class="w-8 align-self-center bg-indigo-800 border-indigo-800"
        label="Dodaj"
        icon="pi pi-check"
        v-bind:disabled="isEmpty()"
        v-on:click="addWorker"
      />
    </div>
    </Dialog>
</template>

<script setup>
import axios from "../../config/axios.js";
import propertyIsEmpty from "./../../helpers/helpers.js";
import roles from "../../consts/roles";
import statuses from "../../consts/workerStatuses";

import { ref, toRefs, computed } from "vue";

import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import InputText from "primevue/inputtext";
import Dialog from "primevue/dialog";

const props = defineProps({
  visible: Boolean,
  header: String,
});

const { visible } = toRefs(props);

const firstName = ref();
const lastName = ref();
const email = ref();
const selectedTeam = ref();
const selectedRole = ref();
const status = ref();

const teams = ref([]);

const isEmpty = () => {
  if (
    propertyIsEmpty(firstName) ||
    propertyIsEmpty(lastName) ||
    propertyIsEmpty(email) ||
    selectedTeam.value === undefined ||
    selectedRole.value === undefined ||
    status.value === undefined
  ) {
    return true;
  } else {
    return false;
  }
};

const getTeams = () => {
  axios
    .get('/teams/')
    .then((res) => {
      teams.value = res.data;
    })
    .catch((err) => {
      console.error(err);
    });
}

getTeams();

const emit = defineEmits(["update:visible", "fetchData"]);

const cVisible = computed({
  get: () => visible.value,
  set: (val) => {
    emit("update:visible", val);
  },
});

const clearDialog = () => {
  firstName.value = '';
  lastName.value = '';
  email.value = '';
  selectedTeam.value = undefined;
  selectedRole.value = undefined;
  status.value = undefined;
}

const addWorker = () => {
  axios
    .post('/workers-create/', {
      firstName: firstName.value,
      lastName: lastName.value,
      email: email.value,
      team: selectedTeam.value,
      role: selectedRole.value,
      status: status.value,
      workHours: 0
    })
    .then(res => {
      cVisible.value = false;
      emit("fetchData");
      
    })
    .catch(err => {
      console.error(err)
    })

  clearDialog();
};
</script>

