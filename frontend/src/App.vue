<template>
  <div class="container">
    <h1>资产管理</h1>

    <h2>新增资产</h2>
    <input v-model="newAsset.category" placeholder="分类" />
    <input v-model="newAsset.name" placeholder="名称" />
    <input v-model="newAsset.owner" placeholder="负责人" />
    <button @click="addAsset">添加</button>

    <h2>资产列表</h2>
    <table border="1" cellspacing="0" cellpadding="6">
      <thead>
        <tr>
          <th>ID</th>
          <th>分类</th>
          <th>名称</th>
          <th>负责人</th>
          <th>修改时间</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="asset in assets" :key="asset.id">
          <td>{{ asset.id }}</td>
          <td>{{ asset.category }}</td>
          <td>{{ asset.name }}</td>
          <td>{{ asset.owner }}</td>
          <td>{{ asset.date }}</td>
          <td><button @click="deleteAsset(asset.id)">删除</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const assets = ref([]);
const newAsset = ref({
  category: "",
  name: "",
  owner: ""
});

const API_BASE = "http://127.0.0.1:5000/api/assets";

const loadAssets = async () => {
  const res = await axios.get(API_BASE);
  assets.value = res.data;
};

const addAsset = async () => {
  if (!newAsset.value.category || !newAsset.value.name || !newAsset.value.owner) {
    alert("请填写所有字段");
    return;
  }
  await axios.post(API_BASE, newAsset.value);
  newAsset.value.category = "";
  newAsset.value.name = "";
  newAsset.value.owner = "";
  await loadAssets();
};

const deleteAsset = async (id) => {
  await axios.delete(`${API_BASE}/${id}`);
  await loadAssets();
};

onMounted(() => {
  loadAssets();
});
</script>

<style>
.container {
  max-width: 600px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}
input {
  margin: 5px;
}
button {
  margin-left: 5px;
}
table {
  margin-top: 20px;
  width: 100%;
}
</style>
