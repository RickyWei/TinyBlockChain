<template>
  <div>
    <Menu mode="horizontal" :theme="theme1" active-name="1">
      <MenuItem name="1">
        <Icon type="ios-paper" />
        <a href="/balance">Balance</a>
      </MenuItem>
      <MenuItem name="2">
        <Icon type="ios-people" />
        <a href="/checkchain">CheckChain</a>
      </MenuItem>
      <MenuItem name="3">
        <Icon type="ios-stats" />
        <a href="/mine">Mine</a>
      </MenuItem>
      <MenuItem name="4">
        <Icon type="ios-stats" />
        <a href="/transaction">Transaction</a>
      </MenuItem>
      <MenuItem name="5">
        <Icon type="ios-construct" />
        <a href="/about">About</a>
      </MenuItem>
    </Menu>

    <p>Change theme</p>
    <RadioGroup v-model="theme1">
      <Radio label="light"></Radio>
      <Radio label="dark"></Radio>
      <Radio label="primary"></Radio>
    </RadioGroup>
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
