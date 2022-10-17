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
                optionLabel="shortcut"
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
              } font-bold text-0 px-2 border-round-md`"
              >{{ slotProps.data.team.name }}</span
            >
          </template>
        </Column>

        <Column field="time" header="Godziny" :sortable="true">
          <template #body="slotProps" v-if="editable">
            <InputNumber
              v-model="slotProps.data.time"
              :maxFractionDigits="1"
            />
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
import { ref, toRefs } from "vue";
import { FilterMatchMode } from "primevue/api";
import axios from "../../config/axios";
import colors from "../../consts/colors.js";

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
});

const selectedWorkers = ref([]);
const selectedTeam = ref([]);
const editingRows = ref([]);
const editable = ref(false);

const workersData = ref([]);
const workers = ref([]);
const teams = ref({});

const props = defineProps({
  weekID: Number,
});

const { weekID } = toRefs(props);

const fetchData = () => {
  axios
    .get(`/jobtime-availability/${weekID.value}/`)
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
};

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

const save = () => {
  editable.value = false;

  axios
    .put(`/jobtime-availability/${weekID.value}/`, {
      week_id: weekID.value,
      data: workers.value,
    })
    .catch((err) => {
      console.error(err);
    });
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

fetchData();
</script>
