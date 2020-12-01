<template>
  <div>
    <Row>
      <Col span="8"><div></div></Col>
      <Col span="8">
        <div>
          <Form
            ref="formValidate"
            :model="formValidate"
            :rules="ruleValidate"
            :label-width="80"
          >
            <FormItem label="Name" prop="name">
              <Input v-model="formValidate.name" placeholder="Enter your name">
                <Icon type="ios-person-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>

            <FormItem label="Passwd" prop="passwd">
              <Input
                v-model="formValidate.passwd"
                placeholder="Enter your password"
              >
                <Icon type="ios-lock-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>

            <FormItem label="E-mail" prop="mail">
              <Input
                v-model="formValidate.mail"
                placeholder="Enter your e-mail"
              >
                <Icon type="ios-mail-outline" slot="prepend"></Icon>
              </Input>
            </FormItem>

            <FormItem>
              <Button type="primary" @click="handleSubmit"> Submit </Button>
              <Button
                @click="handleReset('formValidate')"
                style="margin-left: 8px"
              >
                Reset
              </Button>
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
  name: "Register",
  data() {
    return {
      formValidate: {
        name: "",
        passwd: "",
        mail: "",
      },
      ruleValidate: {
        name: [
          {
            required: true,
            message: "The name cannot be empty",
            trigger: "blur",
          },
        ],
        passwd: [
          {
            required: true,
            message: "The password cannot be empty",
            trigger: "blur",
          },
        ],
        mail: [
          {
            required: false,
            message: "Mailbox cannot be empty",
            trigger: "blur",
          },
          { type: "email", message: "Incorrect email format", trigger: "blur" },
        ],
      },
    };
  },
  methods: {
    handleSubmit() {
      this.axios({
        method: "POST",
        url: " http://192.168.56.101:9999/register/user",
        data: {
          user: this.formValidate.name,
          passwd: this.formValidate.passwd,
        },
      })
        .then((res) => {
          console.log(res);
          if (res.status == 200) {
            //login
            this.$router.push({ path: "/login" });
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
    handleReset(name) {
      this.$refs[name].resetFields();
    },
  },
};
</script>
