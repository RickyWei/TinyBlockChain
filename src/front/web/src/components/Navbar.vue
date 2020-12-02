<template>
  <div class="nav">
    <Menu mode="horizontal" :theme="theme1" :active-name="$route.name" >
      <MenuItem name="Balance">
        <Icon type="ios-paper" />
        <a href="/balance">balance</a>
      </MenuItem>
      <MenuItem name="Checkchain">
        <Icon type="ios-people" />
        <a href="/checkchain">CheckChain</a>
      </MenuItem>
      <MenuItem name="Mine">
        <Icon type="ios-stats" />
        <a href="/mine">Mine</a>
      </MenuItem>
      <MenuItem name="Transaction">
        <Icon type="ios-stats" />
        <a href="/transaction">Transaction</a>
      </MenuItem>
      <MenuItem name="About">
        <Icon type="ios-construct" />
        <a href="/about">About</a>
      </MenuItem>
    </Menu>
    <div>
    <p>Change theme</p>
    <RadioGroup v-model="theme1">
      <Radio label="light"></Radio>
      <Radio label="dark"></Radio>
      <Radio label="primary"></Radio>
    </RadioGroup>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navebar",
  data() {
    return {
      theme1: "light",
    };
  },
};
</script>

<style scoped>
.nav{
  background-image: linear-gradient(120deg, #e0c3fc 0%, #8ec5fc 100%);
}
</style>
