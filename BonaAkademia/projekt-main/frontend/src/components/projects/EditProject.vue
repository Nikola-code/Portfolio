<template>
  <div class="px-8 flex flex-column justify-content-center">
    <div class="field">
      <label for="leader">Kierownik</label>
      <CascadeSelect
        v-model="leader"
        :options="teams"
        optionLabel="name"
        optionGroupLabel="shortcut"
        :optionGroupChildren="['members']"
        placeholder="Wybierz kierownika"
      />
    </div>

    <div class="field">
      <label for="client">Klient</label>
      <Dropdown
        id="client"
        v-model="client"
        :options="clients"
        optionLabel="name"
        optionValue="id"
        placeholder="Wybierz klienta"
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
    <label for="shortcut">Krótka nazwa</label>
    <InputText id="shortcut" type="shortcut" v-model="shortcut" />

    <div class="field">
      <label for="fullName">Pełna nazwa</label>
      <InputText id="fullName" type="fullName" v-model="fullName" />
    </div>

    <div class="field">
      <label for="projectNum">Numer projektu</label>
      <InputText id="projectNum" type="projectNum" v-model="projectNum" />
    </div>

    <Button
      class="w-8 align-self-center bg-indigo-800 border-indigo-800"
      icon="pi pi-check"
      label="Edytuj"
      v-bind:disabled="isEmpty()"
      v-on:click="editProject"
    />
  </div>
</template>

<script setup>
import propertyIsEmpty from "./../../helpers/helpers.js";

import { ref, toRefs, computed, watch } from "vue";

import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Dropdown from "primevue/dropdown";
import CascadeSelect from "primevue/cascadeselect";
import axios from "../../config/axios";
import statuses from "../../consts/statuses.js";

const props = defineProps({
  project: Object,
  visible: Boolean,
  header: String,
});

const { project, visible } = toRefs(props);

const shortcut = ref(project.value.shortcut);
const fullName = ref(project.value.fullName);
const projectNum = ref(project.value.projectNum);
const status = ref(project.value.status);

const leader = ref();
const client = ref();

const teams = ref([]);
const clients = ref([]);

const fetchAdditionalData = () => {
  axios
    .get("/clients/")
    .then((response) => {
      clients.value = response.data;
      client.value = project.value.client.id;
    })
    .catch((err) => console.error(err));

  axios
    .get("/teams-members/")
    .then((response) => {
      teams.value = response.data;
      leader.value = project.value.leader;
    })
    .catch((err) => console.error(err));
};

fetchAdditionalData();

const isEmpty = () => {
  if (
    propertyIsEmpty(shortcut) ||
    propertyIsEmpty(fullName) ||
    propertyIsEmpty(client) ||
    propertyIsEmpty(projectNum) ||
    status.value === undefined ||
    leader.value === undefined
  ) {
    return true;
  } else {
    return false;
  }
};

const emit = defineEmits(["update:visible", "fetchData"]);

const cVisible = computed({
  get: () => visible.value,
  set: (val) => {
    emit("update:visible", val);
  },
});

watch(project, (newVal) => {
  if (newVal) {
    shortcut.value = newVal.shortcut;
    fullName.value = newVal.fullName;
    client.value = newVal.client;
    projectNum.value = newVal.projectNum;
    leader.value = newVal.leader;
    status.value = newVal.status;
  }
});

const editProject = () => {
  axios
    .put(`/projects/${project.value.id}/`, {
      shortcut: shortcut.value,
      fullName: fullName.value,
      client: client.value,
      projectNum: projectNum.value,
      status: status.value,
      leader: leader.value.id,
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
