<template>
    <q-page class="flex flex-center">
      <q-form @submit.prevent="onSubmit" class="rounded q-my-lg flex column">
        <q-select
          outlined
          v-model="form.projectName"
          class="full-width q-pb-lg"
          label="Project Name"
          :rules="[
            (val) => (val && val.length > 0) || 'Project Name is required',
            (val) =>
              (val && val.length <= 30) ||
              'Project name cannot be longer than 30 characters.',
          ]"
        />
        <q-select
        outlined
        class="full-width q-pb-lg"
        v-model="form.pic"
        :options="optionsPic"
        label="PIC"
        :rules="[(val) => (val && val.length > 0) || 'PIC is required']"
      />
      <q-input
        v-model="form.note"
        filled
        class="full-width q-pb-lg"
        type="textarea"
        label="Note"
        :rules="[
          (val) => {
            if (val && val.length >= 1000)
              return 'Project name cannot be longer than 1000 characters.';
          },
        ]"
      />
      <q-btn color="primary" label="Submit" type="submit" />
    </q-form>
  </q-page>
</template>
<script>
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent({
  name: "defineComponent",
  data() {
    return {
      form: {
        projectName: "",
        pic: "",
      },
      optionsPic: null,
    };
  },
  methods: {
    async getProject(){
      const projects = await axios.get("http://localhost:3000/projects")
      this.optionProject = projects.data.map((item) => {
        return item.name;
      })
    },
    async getPic() {
      const pics = await axios.get("http://localhost:3000/pics");
      this.optionsPic = pics.data.map((item) => {
        return item.name;
      });
    onSubmit() 
      axios
        .post("http://localhost:3000/projects", this.form)
        .then(() => {
          this.form = "";
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  async mounted() {
    this.getPic();
    this.getProject();
  },
});
</script>
<style lang="scss" scoped>
.rounded {
  border: 1px solid var(--q-primary);
  padding: 20px;
  border-radius: 8px;
  min-width: 420px;
}
</style>
