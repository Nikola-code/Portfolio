<template>
    <div class="px-8 flex flex-column justify-content-center">
      <div class="field">
        <label for="firstName">Imię</label>
        <InputText id="firstName" type="firstName" v-model="firstName" />
      </div>

      <div class="field">
        <label for="lastName">Nazwisko</label>
        <InputText id="lastName" type="lastName" v-model="lastName" />
      </div>

      <div class="field">
        <label for="email">Adres email</label>
        <InputText id="email" type="email" v-model="email" />
      </div>

      <div class="field">
        <label for="team">Zespół</label>
        <Dropdown
          id="team"
          :options="teams"
          v-model="selectedTeam"
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
        class="w-8 align-self-center bg-indigo-800 border-indigo-800"
        label="Edytuj"
        icon="pi pi-check"
        type="submit"
        v-bind:disabled="isEmpty()"
        v-on:click="editWorker"
      />
    </div>
</template>

<script setup>
import axios from "../../config/axios.js";
import propertyIsEmpty from "./../../helpers/helpers.js";
import roles from "../../consts/roles";
import statuses from "../../consts/workerStatuses";

import { ref, toRefs, computed, watch } from "vue";

import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import InputText from "primevue/inputtext";

const props = defineProps({
  worker: Object,
  visible: Boolean,
  header: String,
});

const { worker, visible } = toRefs(props);

const firstName = ref(worker.value.firstName);
const lastName = ref(worker.value.lastName);
const selectedTeam = ref();
const email = ref(worker.value.email);
const selectedRole = ref(worker.value.role);
const status = ref(worker.value.status);

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
    .get("/teams/")
    .then((res) => {
      teams.value = res.data;
      selectedTeam.value = worker.value.team[0].id;
    })
    .catch((err) => {
      console.error(err);
    });
};

getTeams();

const emit = defineEmits(["update:visible", "fetchData"]);

const cVisible = computed({
  get: () => visible.value,
  set: (val) => {
    emit("update:visible", val);
  },
});

watch(worker, (newVal) => {
  if (newVal) {
    firstName.value = newVal.firstName;
    lastName.value = newVal.lastName;
    email.value = newVal.email;
    selectedTeam.value = newVal.team;
    selectedRole.value = newVal.role;
    status.value = newVal.status;
  }
});

const editWorker = () => {
  axios
    .put(`/workers-edit/${worker.value.id}/`, {
      firstName: firstName.value,
      lastName: lastName.value,
      email: email.value,
      team: selectedTeam.value,
      role: selectedRole.value,
      status: status.value,
    })
    .then((res) => {
      cVisible.value = false;
      emit("fetchData");
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

