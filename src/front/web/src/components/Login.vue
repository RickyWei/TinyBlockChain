<template>
  <div>
    <Row>
      <Col span="8"><div></div></Col>
      <Col span="8">
        <div>
          <Form ref="formInline" :model="formInline" :rules="ruleInline">
            <FormItem prop="user">
              <Input
                type="text"
                v-model="formInline.user"
                placeholder="Username"
              >
                <Icon type="ios-person-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>
            <FormItem prop="password">
              <Input
                type="password"
                v-model="formInline.password"
                placeholder="Password"
              >
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>
            <FormItem>
              <Button type="success" @click="handleSubmit"> Signin </Button>
              <Button type="primary" @click="handleRegister"> Register </Button>
            </FormItem>
          </Form>
        </div>
      </Col>
      <Col span="8"><div></div></Col>
    </Row>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {
      formInline: {
        user: "",
        password: "",
      },
      ruleInline: {
        user: [
          {
            required: true,
            message: "Please fill in the user name",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message: "Please fill in the password.",
            trigger: "blur",
          },
          {
            type: "string",
            min: 4,
            message: "The password length cannot be less than 6 bits",
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
        url: " http://192.168.56.101:9999/login",
        data: {
          user: this.formInline.user,
          passwd: this.formInline.password,
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            //login
            window.sessionStorage["sha"] = res.data.sha;
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
