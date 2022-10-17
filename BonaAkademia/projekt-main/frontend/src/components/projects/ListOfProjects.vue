<template>
  <div>
    <div class="min-w-screen">
      <DataTable
        :value="projects"
        showGridlines
        dataKey="id"
        :filters="filters"
        responsiveLayout="scroll"
      >
        <template #header>
          <Toolbar class="p-0 border-none">
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
                class="bg-indigo-800 border-indigo-800 mr-2"
                @click="addProject()"
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

        <Column header="Status" class="w-1rem">
          <template #body="slotProps">
            {{ statuses[slotProps.data.status] }}
          </template>
        </Column>

        <Column class="w-10rem" :exportable="false">
          <template #body="slotProps">
            <div class="p-0">
              <Button
                icon="pi pi-pencil"
                class="p-button-rounded bg-indigo-800 border-indigo-800 ml-2"
                @click="editProject(slotProps.data)"
              />
              <Button
                icon="pi pi-eye"
                class="p-button-rounded bg-indigo-400 border-indigo-400 ml-2"
                @click="showProject(slotProps.data.id)"
              />
              <Button
                icon="pi pi-history"
                class="p-button-rounded bg-red-700 border-red-700 ml-2"
                @click="archiveProject(slotProps.data)"
              />
            </div>
          </template>
        </Column>
      </DataTable>
    </div>

    <AddProject
      v-model:visible="addDialog"
      header="Dodaj projekt"
      @fetchData="fetchData"
    />

    <Dialog
      v-model:visible="editDialog"
      header="Edycja Projektu"
      :modal="true"
      :draggable="false"
      class="p-fluid w-4"
    >
      <EditProject
        :project="project"
        v-model:visible="editDialog"
        @fetchData="fetchData"
      />
    </Dialog>

    <Dialog
      v-model:visible="showDialog"
      header="Podgląd Projektu"
      :modal="true"
      :draggable="false"
      class="p-fluid w-4"
    >
      <Viewer :keys="keys" :id="id" type="projects" />
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { FilterMatchMode } from "primevue/api";

import AddProject from "./AddProject.vue";
import EditProject from "./EditProject.vue";

import Column from "primevue/column";
import DataTable from "primevue/datatable";
import Button from "primevue/button";
import InputText from "primevue/inputtext";
import Toolbar from "primevue/toolbar";
import Dialog from "primevue/dialog";
import axios from "../../config/axios";
import Viewer from "../Viewer.vue";

const statuses = ref({
  A: "aktywny",
  P: "planowany",
  M: "utrzymywany",
  C: "zamknięty",
});

const columnsAttributes = [
  {
    field: "shortcut",
    header: "Krótka nazwa",
    class: "w-9rem",
    sortable: true,
  },
  { field: "fullName", header: "Pełna nazwa", class: "w-9rem", sortable: true },
  { field: "client.name", header: "Klient", class: "w-1rem", sortable: true },
  {
    field: "projectNum",
    header: "Numer projektu",
    class: "w-9rem",
    sortable: true,
  },
  {
    field: "leader.name",
    header: "Kierownik",
    class: "w-1rem",
    sortable: true,
  },
];

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});
const addDialog = ref(false);
const editDialog = ref(false);
const showDialog = ref(false);
const id = ref();
const project = ref({});
const projects = ref([]);

const keys = ref([
  { shortcut: "Krótka nazwa" },
  { fullName: "Pełna nazwa" },
  { projectNum: "Numer projektu" },
  { status: "Status" },
  { members: "Pracownicy" },
  { client: { name: "Klient" } },
  { leader: { name: "Kierownik" } },
]);

const fetchData = () => {
  axios
    .get("/projects/")
    .then((response) => (projects.value = response.data))
    .catch((err) => console.error(err));
};

fetchData();

const archiveProject = (proj) => {
  console.log(proj)

  axios
    .patch(`/projects/${proj.id}/`, {
      status: "C",
    })
    .then((res) => {
      fetchData();
    });
};

const editProject = (proj) => {
  project.value = proj;
  editDialog.value = true;
};

const addProject = () => {
  addDialog.value = true;
};

const showProject = (idData) => {
  id.value = idData;
  showDialog.value = true;
};

</script>
