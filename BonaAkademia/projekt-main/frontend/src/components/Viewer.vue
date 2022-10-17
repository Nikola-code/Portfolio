<template>
  <ul class="list-none">
    <li v-for="key in keys">
      <span
        v-if="!Array.isArray(dataAxios[Object.keys(key)])"
        class="font-medium line-height-4 text-xl"
      >
        {{
          typeof Object.values(key)[0] === "object"
            ? Object.values(key)[0].name
            : Object.values(key)[0]
        }}:
        <span class="text-lg">
          {{
            typeof dataAxios[Object.keys(key)] === "object"
              ? dataAxios[Object.keys(key)].name
              : showStatus(dataAxios[Object.keys(key)])
          }}
        </span>
      </span>

      <span
        v-else
        class="font-medium line-height-4 text-xl flex align-items-center"
      >
        {{ Object.values(key)[0] }}:
        <span v-if="dataAxios[Object.keys(key)].length === 1">
          <ul class="p-1 list-none text-lg">
            <li v-for="item in dataAxios[Object.keys(key)]">
              {{ 
                typeof item === "object"
                  ? item.name
                  : item
              }}
            </li>
          </ul>
        </span>

        <span v-else>
          <ul class="list-disc line-height-2 text-lg pl-4">
            <li v-for="item in dataAxios[Object.keys(key)]">
              {{ item }}
            </li>
          </ul>
        </span>
      </span>
    </li>
  </ul>
</template>

<script setup>
import axios from "../config/axios.js";

import { toRefs, ref } from "vue";

const props = defineProps({
  keys: Array,
  type: String,
  id: Number
});

const { keys, type, id } = toRefs(props);

const dataAxios = ref({});

const getData = () => {
  axios
    .get(`/${type.value}/${id.value}/`)
    .then((response) => {
      dataAxios.value = response.data;
    })
    .catch((err) => {
      console.error(err);
    });
};

getData();

const isBoolean = (data) => {
  if (typeof data === 'boolean') {
    return true;
  }
  return false;
}

const showStatus = (data) => {
  if (isBoolean(data) === false) {
    return data;
  }
  else if (data === true) {
    return 'aktywny';
  }
  return 'nieaktywny';
}
</script>

