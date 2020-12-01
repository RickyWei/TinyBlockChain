<template>
  <div>
    <Navbar></Navbar>
    <Button @click="registernode"
      ><Icon type="ios-refresh" />register as a node</Button
    >
    <Circle
      :percent="[iscomplete ? 100 : 30]"
      stroke-color="[iscomplete?#5cb85c:#5cb85c]"
    >
      <Icon
        type="[iscomplete?ios-hammer-outline:ios-cog-outline]"
        size="60"
      ></Icon>
    </Circle>
    <Button @click="mine"><Icon type="ios-construct-outline" />mine</Button>
  </div>
</template>


<script>
import Navbar from "./Navbar.vue";

export default {
  components: { Navbar },
  name: "Mine",
  data() {
    return {
      iscomplete: true,
    };
  },
  methods: {
    registernode() {
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/register/node",
        data: {
          sha: window.sessionStorage["sha"],
          ip: "192.168.56.101",
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            window.sessionStorage["uid"] = res.data.uid;
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
    mine() {
      this.iscomplete = false;
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/mine",
        data: {
          uid: window.sessionStorage["uid"],
        },
      })
        .then((res) => {
          //   console.log(res);
          if (res.status == 200) {
            this.iscomplete = true;
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