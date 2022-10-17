<template>
  <div>
    <div>
      <DataTable
        :value="workers"
        v-model:selection="selectedWorkers"
        showGridlines
        dataKey="id"
        :filters="filters"
        responsiveLayout="scroll"
      >
        <template #header>
          <Toolbar class="border-none p-0">
            <template #start>
              <span class="ml-4 h-3rem p-input-icon-right">
                <InputText
                  v-model="filters['global'].value"
                  placeholder="Wyszukaj..."
                />
                <i class="pi pi-search" />
              </span>
            </template>

            <template #end>
              <Dropdown
                class="mr-4 w-14rem h-3rem"
                v-model="selectedTeam"
                :showClear="true"
                @change="changeWorkers()"
                :options="teams"
                optionLabel="name"
                optionValue="id"
                placeholder="Wybierz zespół"
              />

              <Button
                v-if="editable && selectedWorkers.length === 0"
                label="Zapisz"
                :disabled="checkIfFull()"
                icon="pi pi-check"
                class="w-8rem h-3rem bg-red-700 border-red-700"
                @click="save()"
              />
              <Button
                label="Edytuj"
                v-if="!editable"
                icon="pi pi-pencil"
                class="w-8rem h-3rem bg-indigo-800 border-indigo-800"
                @click="makeEditable()"
              />
            </template>
          </Toolbar>
        </template>

        <Column field="name" header="Imię i nazwisko" :sortable="true" />

        <Column header="Zespół" :sortable="true">
          <template #body="slotProps">
            <span
              :class="`bg-${
                colors[slotProps.data.team.id]
              } font-bold text-0 pr-2 pl-2 border-round-md`"
              >{{ slotProps.data.team.name }}</span
            >
          </template>
        </Column>
        <Column header="Projekty" :sortable="true">
          <template #body="slotProps">
            <DataTable
              :value="slotProps.data.projects"
              showGridlines
              dataKey="id"
              headerClass="-my-3 -mx-4 p-0"
              class="-my-3 -mx-4"
              responsiveLayout="scroll"
            >
              <Column field="projName">
                <template #body="slotProps">
                  <span
                    :class="`bg-${
                      colors[slotProps.data.id]
                    } font-bold text-0 pr-2 pl-2 border-round-md`"
                    >{{ slotProps.data.shortcut }}</span
                  >
                </template>
              </Column>

              <Column field="time"
                ><template #body="slotProps" v-if="editable">
                  <InputNumber
                    v-model="slotProps.data.time"
                    :maxFractionDigits="1"
                  />
                </template>
                ></Column
              >

              <Column field="time" v-if="editable"
                ><template #body="slotProps">
                  <Button
                    icon="pi pi-trash"
                    class="p-button-rounded bg-red-300 border-red-300 ml-2"
                    @click="slotProps.data.time = 0"
                  />
                </template>
                ></Column
              >

              <template #footer v-if="editable">
                <Dropdown
                  id="client"
                  v-model="project"
                  :options="projects"
                  optionLabel="shortcut"
                  optionValue="id"
                  placeholder="Wybierz projekt"
                  class="mr-3 w-14rem h-3rem"
                />

                <Button
                  label="Dodaj projekt"
                  :disabled="checkIfFull()"
                  icon="pi pi-check"
                  class="ml-3 w-8rem h-3rem bg-indigo-300 border-indigo-300"
                  @click="addProject(slotProps.data.projects)"
                ></Button>
              </template>
            </DataTable>
            <span class="m-5 font-semibold">
              <p />
              <p />
              <p />
              <span v-if = "pojectsSum(slotProps.data.projects) > slotProps.data.time" class="bg-red-300 p-1 font-semibold"> Lącznie: {{ pojectsSum(slotProps.data.projects) }} </span>
              <span v-else class="bg-green-300 p-1 font-semibold"> Lącznie: {{ pojectsSum(slotProps.data.projects) }} </span>
              <p />
              Dyspozycyjność: {{ slotProps.data.time }}
            </span>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script setup>
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import InputText from "primevue/inputtext";
import Toolbar from "primevue/toolbar";
import InputNumber from "primevue/inputnumber";
import Button from "primevue/button";
import Dropdown from "primevue/dropdown";
import { ref, toRefs, computed } from "vue";
import { FilterMatchMode } from "primevue/api";
import axios from "../../config/axios";
import colors from "../../consts/colors";

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const selectedWorkers = ref([]);
const selectedTeam = ref([]);
const editingRows = ref([]);
const editable = ref(false);

const workersData = ref([]);
const workers = ref([]);
const projects = ref([]);
const project = ref({});
const teams = ref({});

const props = defineProps({
  weekID: Number,
});

const { weekID } = toRefs(props);

console.log(weekID);

const fetchData = () => {
  axios
    .get(`/planning/week/${weekID.value}/`)
    .then((response) => {
      workersData.value = response.data;
      workers.value = workersData.value;
    })
    .catch((err) => console.error(err));

  axios
    .get("/teams/")
    .then((response) => {
      teams.value = response.data;
    })
    .catch((err) => console.error(err));

  axios
    .get("/projects-shortlist/")
    .then((response) => {
      projects.value = response.data;
    })
    .catch((err) => console.error(err));
};

fetchData();
const changeWorkers = () => {
  if (selectedTeam.value === null) {
    workers.value = workersData.value;
  } else {
    workers.value = [];
    for (let worker of workersData.value) {
      if (worker.team.id === selectedTeam.value) {
        workers.value.push(worker);
      }
    }
  }
};

const addProject = (workerProjData) => {
  console.log(workerProjData);
  const tmpProj = ref();

  for (const proj of projects.value) {
    if (proj.id === project.value) {
      tmpProj.value = proj;
      tmpProj.value.time = 0;
      break;
    }
  }
  console.log(tmpProj.value);
  if (!projectWasAdded(workerProjData, project.value)) {
    workerProjData.push(tmpProj.value);
  }
};

const projectWasAdded = (projs, proj) => {
  for (const p of projs) {
    if (p.id == proj) {
      return true;
    }
  }

  return false;
};

const save = () => {
  editable.value = false;

  for (const worker of workers.value) {
    for (const proj of worker.projects) {
      if (proj.time == 0) {
        worker.projects.splice(
          worker.projects.findIndex((a) => a.id === proj.id),
          1
        );
        continue;
      }
    }
  }

  console.log(workers.value);

  axios
    .put(`/workers-projects/${weekID.value}/`, {
      week_id: weekID.value,
      data: workers.value,
    })
    .then((res) => {
      console.log("tu");
    })
    .catch((err) => {
      console.error(err);
    });
};

const pojectsSum = (projs) => {
  const sum = ref(0);
  for (const p of projs) {
    sum.value = sum.value + p.time;
  }

  return sum.value;
};

const makeEditable = () => {
  editingRows.value = workers.value;
  editable.value = true;
};

const checkIfFull = () => {
  for (let worker of workers.value) {
    if (worker.time === null) {
      return true;
    } else {
      return false;
    }
  }
};
</script>

<style>
li.title {
  list-style-type: none;
  margin-left: 0;
  padding-left: 0;
}

ul {
  list-style-position: inside;
}
</style>
