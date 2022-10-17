<template>
  <div>
    <div class="min-w-screen">
      <DataTable
        :value="teams"
        v-model:selection="selectedTeams"
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
                class="ml-2 bg-indigo-800 border-indigo-800"
                @click="openAddTeam()"
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
        />
        <Column
          field="members.length"
          header="Liczba pracowników"
          class="w-7rem"
          :sortable="true"
        >
        </Column>
        <Column class="w-11rem" :exportable="false">
          <template #body="slotProps">
            <Button
              icon="pi pi-pencil"
              class="p-button-rounded ml-2 bg-indigo-800 border-indigo-800"
              @click="openEditTeam(slotProps.data)"
            />
            <Button
              icon="pi pi-eye"
              class="p-button-rounded ml-2 bg-indigo-400 border-indigo-400"
              @click="openShowTeam(slotProps.data.id)"
            />
          </template>
        </Column>
      </DataTable>
    </div>

    <Dialog
      v-model:visible="teamDialog"
      :draggable="false"
      header="Szczegóły zespołu"
      :modal="true"
      class="p-fluid w-4"
    >
      <AddTeam
        v-model:visible="teamDialog"
        header="Dodaj zespół"
        @fetchData="fetchData"
      />
    </Dialog>

    <Dialog
      v-model:visible="editDialog"
      :draggable="false"
      header="Szczegóły zespołu"
      :modal="true"
      class="p-fluid w-4"
    >
      <EditTeam
        :teams="team"
        v-model:visible="editDialog"
        header="Edytuj zespół"
        @fetchData="fetchData"
      />
    </Dialog>

    <Dialog
      v-model:visible="showDialog"
      :draggable="false"
      header="Podgląd zespołu"
      :modal="true"
      class="p-fluid w-4"
    >
      <Viewer :keys="keys" type="teams-list" :id="id" />
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { FilterMatchMode } from "primevue/api";

import axios from "../../config/axios";

import AddTeam from "./AddTeam.vue";
import EditTeam from "./EditTeam.vue";

import Column from "primevue/column";
import DataTable from "primevue/datatable";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Toolbar from "primevue/toolbar";
import Dialog from "primevue/dialog";
import Viewer from "../Viewer.vue";

const columnsAttributes = [
  {
    field: "shortcut",
    header: "Krótka nazwa",
    class: "w-7rem",
    sortable: true,
  },
  { field: "fullName", header: "Pełna nazwa", class: "w-7rem", sortable: true },
  { field: "leader", header: "Kierownik", class: "w-7rem", sortable: true },
];

const keys = ref([
  { shortcut: "Krótka" },
  { fullName: "Pełna" },
  { leader: "Kierownik" },
  { members: "Pracownicy" },
]);

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const selectedTeams = ref();
const teamDialog = ref(false);
const editDialog = ref(false);
const showDialog = ref(false);
const team = ref({});
const id = ref();

const teams = ref();

axios
  .get("/teams-list/")
  .then((response) => (teams.value = response.data))
  .catch((err) => console.error(err));

const openAddTeam = () => {
  teamDialog.value = true;
};

const openEditTeam = (teamData) => {
  team.value = teamData;
  editDialog.value = true;
};

const openShowTeam = (idData) => {
  id.value = idData;
  showDialog.value = true;
};
</script>
