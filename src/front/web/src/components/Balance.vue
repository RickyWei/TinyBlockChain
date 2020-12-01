<template>
  <div>
    <Navbar></Navbar>
    <Poptip title="Balance" v-bind:content="content">
      <Button @click="getbalance"><Icon type="logo-usd" />Click</Button>
    </Poptip>
    <Button @click="getalltransaction"
      ><Icon type="logo-usd" />get all transaction</Button
    >
    <Table border :columns="columns5" :data="data5"></Table>
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";

export default {
  components: { Navbar },
  name: "Balance",
  data() {
    return {
      content: "",
      columns5: [
        {
          title: "Sender",
          key: "sender",
          sortable: true,
        },
        {
          title: "Receiver",
          key: "receiver",
          sortable: true,
        },
        {
          title: "Amount",
          key: "amount",
          sortable: true,
        },
      ],
      data5: [],
    };
  },
  methods: {
    getbalance() {
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/checkbalance",
        data: {
          sha: window.sessionStorage["sha"],
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            this.content = res.data.balance;
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
    getalltransaction() {
      this.axios({
        method: "GET",
        url: " http://192.168.56.101:9999/alltransaction",
        data: {
          // sha: window.sessionStorage["sha"],
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            this.data5 = res.data;
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