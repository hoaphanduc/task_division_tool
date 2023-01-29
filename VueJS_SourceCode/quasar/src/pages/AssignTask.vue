<template>
    <q-page class="flex flex-center">
      <q-form @submit.prevent="onSubmit" class="rounded q-my-lg flex column">
        <q-select
          outlined
          v-model="form.projectName"
          :options="optionProject"
          class="full-width q-pb-lg"
          label="Project Name"
          :rules="[
            (val) => (val.label && val.label.length > 0) || 'Project Name is required',
            (val) => 
              (val.label && val.label.length <= 30) ||
              'Project name cannot be longer than 30 characters.',
          ]"
        />
        <q-select
        outlined
        class="full-width q-pb-lg"
        v-model="form.pic"
        :options="optionsPic"
        label="PIC"
        :rules="[(val) => val || 'PIC is required']"
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

const HOST = "http://localhost:8000/api/";

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
      const projects = await axios.get(HOST + "projects/?format=json")
      this.optionProject = projects.data.map((item) => {
        return {
          label: item.title,
          value: item.id,
        };
      })
    },

    async getPic() {
      const pics = await axios.get(HOST + "pics/?format=json");
      this.optionsPic = pics.data.map((item) => {
        return {
          label: item.account,
          value: item.id,
        };
      });
    },
    onSubmit() {
      axios
        .post(HOST + "assigntask/", {
          project: this.form.projectName.value,
          pic: this.form.pic.value,
          note: this.form.note,
        })
        .then(() => {
          this.form = "";
        })
        .catch((err) => {
          console.log(err);
        });
    }

  },
  async mounted() {
    this.getProject();
    this.getPic();
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
