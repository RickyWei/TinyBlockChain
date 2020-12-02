<template>
  <div>
    <Navbar></Navbar>
    
        <div style="margin:10px">
          <Form ref="formInline" :model="formInline" :rules="ruleInline" style="width:60%;margin:auto">
            <FormItem prop="receiver">
              <Input
                type="text"
                v-model="formInline.receiver"
                placeholder="receiver-sha"
              >
                <Icon type="ios-person-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>
            <FormItem prop="amount">
              <Input
                type="text"
                v-model="formInline.amount"
                placeholder="amount"
              >
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>
            <FormItem>
              <Button type="success" @click="handleSubmit">
                DoTransaction</Button
              >
            </FormItem>
          </Form>
        </div>
     
  </div>
</template>
<script>
import Navbar from "./Navbar.vue";

export default {
  components: { Navbar },
  name: "Transaction",
  data() {
    return {
      formInline: {
        receiver: "",
        amount: "",
      },
      ruleInline: {
        receiver: [
          {
            required: true,
            message: "Please fill in the receiver",
            trigger: "blur",
          },
        ],
        amount: [
          {
            required: true,
            message: "Please fill in the amount.",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    handleSubmit() {
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/transaction",
        data: {
          sender: window.sessionStorage["sha"],
          receiver: this.formInline.receiver,
          amount: this.formInline.amount,
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            //login
            // window.sessionStorage["sha"] = res.data.sha;
            // console.log(res);
            // console.log(res.sha);
            // console.log(window.sessionStorage["sha"]);
            this.$router.push({ path: "/Balance" });
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
    handleRegister() {
      this.$router.push({ path: "/Register" });
    },
  },
};
</script>
