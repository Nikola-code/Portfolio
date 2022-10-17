<template>
  <div class="Admin">
    <TabView>
      <TabPanel header="Pracownicy">
        <ListOfWorkers />
      </TabPanel>
      <TabPanel header="Zespoły">
        <ListOfTeams />
      </TabPanel>
      <TabPanel header="Projekty">
        <ListOfProjects />
      </TabPanel>
      <TabPanel header="Czas Pracy">
        <ListOfWeeks type ="0"/>
      </TabPanel>
      <TabPanel header="Planowanie">
        <ListOfWeeks type ="1"/>
      </TabPanel>
    </TabView>
  </div>
</template>

<script setup>
import TabView from "primevue/tabview";
import TabPanel from "primevue/tabpanel";

import ListOfWorkers from "../components/workers/ListOfWorkers.vue";
import ListOfProjects from "../components/projects/ListOfProjects.vue";
import ListOfTeams from "../components/Teams/ListOfTeams.vue";
import WeekTable from "../components/weeks/WeekTable.vue";
import WeekProjectPlan from "../components/weeks/WeekProjectPlan.vue";
import WeeksPanel from "../components/Weeks/WeeksPanel.vue";
import ListOfWeeks from "../components/weeks/ListOfWeeks.vue";
</script>

<style>
  .p-tabview .p-tabview-nav li.p-highlight .p-tabview-nav-link{
    border-color: #363885;
    color:#363885; 
  }

  .p-tabview .p-tabview-nav li .p-tabview-nav-link:not(.p-disabled):focus{
    box-shadow: inset 0 0 0 1px white;
  }
</style>
