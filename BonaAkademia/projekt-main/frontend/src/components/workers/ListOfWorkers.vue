<template>
  <div>
    <div class="min-w-screen">
      <DataTable
        :value="workersList"
        v-model:selection="selectedWorker"
        showGridlines
        dataKey="id"
        :filters="filters"
        responsiveLayout="scroll"
      >
        <template #header>
          <Toolbar class="border-none p-0">
            <template #start>
              <span class="ml-4 p-input-icon-right">
                <InputText
                  v-model="filters['global'].value"
                  placeholder="Wyszukaj..."
                />
                <i class="pi pi-search" />
              </span>
            </template>

            <template #end>
              <Button
                label="Dodaj"
                icon="pi pi-plus"
                class="mr-2 bg-indigo-800 border-indigo-800"
                @click="openAddWorker"
              />
            </template>
          </Toolbar>
        </template>

        <Column
          v-for="value in columnsAttributes"
          :field="value.field"
          :header="value.header"
          :sortable="value.sortable"
          :key="value.field"
          :class="value.class"
        />

        <Column 
          class="w-20rem" 
          field="role" 
          header="Rola" 
          :sortable="true"
          >
          <template #body="slotProps">
            <span
              :class="`${isLeader(slotProps.data.role)} 
              font-bold border-round-md p-1`"
            >
            {{
                slotProps.data.role === "L"
                  ? "kierownik"
                  : slotProps.data.role === "W"
                  ? "pracownik"
                  : "admin"
              }}
            </span>
          </template>
        </Column>

        <Column class="w-16rem" :exportable="false">
          <template #body="slotProps">
            <div class="p-0">
              <Button
                icon="pi pi-pencil"
                class="p-button-rounded bg-indigo-800 border-indigo-800 ml-2"
                @click="openEditWorker(slotProps.data)"
              />
              <Button
                icon="pi pi-eye"
                class="p-button-rounded bg-indigo-400 border-indigo-400 ml-2"
                @click="showWorker(slotProps.data.id)"
              />
              <Button
                icon="pi pi-history"
                class="p-button-rounded bg-red-700 border-red-700 ml-2"
                @click="changeStatus(slotProps.data)"
              />
            </div>
          </template>
        </Column>
      </DataTable>
    </div>

    <Dialog
      v-model:visible="editDialog"
      header="Edytuj pracownika"
      :modal="true"
      :draggable="false"
      class="p-fluid w-4"
    >
      <EditWorker
        v-model:visible="editDialog"
        header="Edytuj pracownika"
        :worker="worker"
        @fetchData="fetchData"
      />
    </Dialog>

    <AddWorker 
      v-model:visible="addDialog"
      header="Dodaj pracownika"
      @fetchData="fetchData"
    />

    <Dialog
      v-model:visible="showDialog"
      header="Podgląd pracownika"
      :modal="true"
      :draggable="false"
      class="p-fluid w-4"
    >
      <Viewer :id="id" :keys="toMap" type="workers" />
    </Dialog>
  </div>
</template>

<script setup>
import axios from "../../config/axios.js";

import { ref } from "vue";
import { FilterMatchMode } from "primevue/api";

import EditWorker from "./EditWorkers.vue";
import AddWorker from "./AddWorker.vue";
import Viewer from "../Viewer.vue";

import Button from "primevue/button";
import Column from "primevue/column";
import DataTable from "primevue/datatable";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";
import Toolbar from "primevue/toolbar";

const addDialog = ref(false);
const editDialog = ref(false);
const showDialog = ref(false);
const id = ref();
const selectedWorker = ref();
const worker = ref({});
const workersList = ref([]);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const toMap = ref([
  { firstName: "Imię" },
  { lastName: "Nazwisko" },
  { email: "Adres email" },
  { team: "Zespół" },
  { role: "Rola w zespole" },
  { workHours: "Etat" },
  { status: "Status" },
]);

const columnsAttributes = [
  { field: "firstName", header: "Imię", class: "w-23rem", sortable: true },
  { field: "lastName", header: "Nazwisko", class: "w-23rem", sortable: true },
  { field: "team.0.name", header: "Zespół", class: "w-23rem", sortable: true },
];

const isLeader = (role) => {
  if (role === "L") {
    return "bg-orange-200";
  }
  else if (role === "W") {
    return "bg-green-200";
  }
  else{
    return "bg-yellow-400";
  }
};

const getWorkers = () => {
  axios
    .get("/workers/")
    .then((response) => {
      workersList.value = response.data;
    })
    .catch((err) => {
      console.error(err);
    });
};

getWorkers();

const fetchData = () => {
  axios
    .get("/workers/")
    .then((response) => (workersList.value = response.data))
    .catch((err) => console.error(err));
};

fetchData();

const openAddWorker = () => {
  addDialog.value = true;
};

const openEditWorker = (workerData) => {
  worker.value = workerData;
  editDialog.value = true;
};

const showWorker = (idData) => {
  id.value = idData;
  showDialog.value = true;
};

const toActive = (workerData) => {
  axios
    .patch(`/workers/${workerData.id}/`, {
      status: true,
    })
    .catch((err) => console.error(err));
};

const toInactive = (workerData) => {
  axios
    .patch(`/workers/${workerData.id}/`, {
      status: false,
    })
    .catch((err) => console.error(err));
};

const changeStatus = (workerData) => {
  if (workerData.status === false) {
    toActive(workerData);
  }
  else {
    toInactive(workerData);
  }
  fetchData();
};
</script>

