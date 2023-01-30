<template>
  <q-page class="flex flex-center">
    <q-form ref="myForm">
  <!-- Your input field -->
</q-form>
    <q-form @submit.prevent="onSubmit" class="rounded q-my-lg flex column">
      <q-input
        outlined
        v-model="form.title"
        class="full-width q-pb-lg"
        label="Project Name"
        :rules="[
          (val) => (val && val.length > 0) || 'Project Name is required',
          (val) =>
            (val && val.length <= 30) ||
            'Project name cannot be longer than 30 characters.',
        ]"
      />
      <div class="row">
        <q-input
          formatModel="string"
          format="YYYY-MM-DD"
          class="q-pb-lg q-mr-sm col"
          v-model="form.start_date"
          outlined
          type="date"
          stack-label
          label="Start Date"
          :rules="[
            (val) => (val && val.length > 0) || 'Start date is required',
          ]"
        />
        <q-input
          formatModel="string"
          format="YYYY-MM-DD"
          class="q-pb-lg col"
          v-model="form.end_date"
          outlined
          type="date"
          stack-label
          label="End Date"
          :rules="[(val) => (val && val.length > 0) || 'End date is required']"
        />
      </div>
      <q-select
        outlined
        class="full-width q-pb-lg"
        v-model="form.status"
        :options="optionsStatus"
        label="Status"
        :rules="[(val) => (val.label && val.label.length > 0) || 'Status is required']"
      />
      <q-input
        outlined
        v-model="form.numberofrequest"
        class="full-width q-pb-lg"
        label="Request Number"
        :rules="[
          (val) => (val && val.length > 0) || 'Request Number is required',
        ]"
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
        title: "",
        start_date: "",
        end_date: "",
        status: "",
        numberofrequest: "",
        note: "",
      },
      optionsStatus: [{
        label: "In Progress",
        value: 2,
      },
      {
        label: "Done",
        value: 0,
      },
      {
        label: "Pending",
        value: 1,
      }],
    };
  },
  methods: {
    onSubmit() {
      axios
        .post("http://localhost:8000/api/addtask/", {
          ...this.form,
          status: this.form.status.value,
        })
        .then(() => {
          this.form.value.reset();
        })
        .catch((err) => {
          console.log(err);
        });
    },
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
