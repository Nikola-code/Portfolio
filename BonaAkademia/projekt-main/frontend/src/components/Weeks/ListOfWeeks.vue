<template>
    <div>
        <div class="m-5 flex justify-content-center">
            <Button icon="pi pi-angle-double-left" @click='year--; getWeeks();' class="bg-red-700"/>
            <p class="text-xl align-self-center text-center font-bold w-1 m-2">Rok {{ year }}</p>
            <Button icon="pi pi-angle-double-right" @click='year++; getWeeks();' class="bg-red-700"/>
        </div>
        <Listbox :options="dataRange">
            <template #option="slotProps">
                <div>
                    <h1 class="text-red-700 text-2xl m-6 ml-8">{{slotProps.option.month}}</h1>
                    <ul class="m-3 list-none">
                        <li class='flex flex-column'>
                            <div v-for="(item, index) in slotProps.option.weeks" :key="index" class="flex justify-content-around">
                                <p class="font-bold align-self-center font-medium mx-8 my-3">{{slotProps.option.weeks[index].weekName}}</p>
                                <p class="align-self-center mx-8 my-3">{{slotProps.option.weeks[index].dateStart + " : " + slotProps.option.weeks[index].dateEnd}}</p>
                                <RouterLink v-if="type==='0'" :to="{name: 'weekTable', params: {weekID: slotProps.option.weeks[index].id}}" >
                                    <Button class="h-3rem my-3 bg-indigo-800 block" label='Stwórz harmonogram' /> 
                                </RouterLink>
                                <RouterLink v-if="type==='1'" :to="{name: 'weekProjectPlan', params: {weekID: slotProps.option.weeks[index].id}}" >
                                    <Button class="h-3rem my-3 bg-indigo-800 block" label='Stwórz harmonogram' /> 
                                </RouterLink>
                            </div>
                        </li>
                    </ul>
                </div>
            </template>
        </Listbox>
    </div>
</template>

<script setup>
import { ref, toRefs } from 'vue';
import Listbox from 'primevue/listbox';
import Button from 'primevue/button';
import axios from 'axios';
import { RouterLink } from 'vue-router';

const data = new Date();
const year = ref(data.getFullYear());
const dataRange = ref('');

const props = defineProps({
  type: Number,
});

const { type } = toRefs(props);


const getWeeks = () => {
    axios.get("/weeks-years/" + year.value + "/")
  .then((response) => {
    dataRange.value = response.data;
  });
}

getWeeks();
</script>

<style>
.p-tabview-panels {
    padding: 0 !important
}
</style>
