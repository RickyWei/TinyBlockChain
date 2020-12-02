<template>
  <div>
    <Navbar></Navbar>
    <Button @click="getchain" style="margin:10px"
      ><Icon type="ios-refresh" />Click to refresh to get chain</Button
    >
    <template>
      <Input
        v-model="value"
        type="textarea"
        :rows="10"
        placeholder="Enter something..."
      />
    </template>
  </div>
</template>


<script>
import Navbar from "./Navbar.vue";

export default {
  components: { Navbar },
  name: "Checkchain",
  data() {
    return {
      value: "",
    };
  },
  methods: {
    getchain() {
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/getchain",
        data: {
          //   sha: window.sessionStorage["sha"],
        },
      })
        .then((res) => {
          //   console.log(res);
          if (res.status == 200) {
            this.content = "";

            for (var i = 0; i < res.data.length; i++) {
              //   console.log(res.data[i]);
              this.value += JSON.stringify(res.data[i]);
              this.value += "\n";
            }
          }
        })
        .catch((err) => {
          this.$Notice.error({
            title: "Notification title",
            desc: err
              ? ""
              : "Here is the notification description. Here is the notification description. ",
          });
        });
    },
  },
};
</script>