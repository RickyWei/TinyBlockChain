<template >
  <div >
    <Navbar></Navbar>
    <div style="width:10%;margin:30px auto">
    <Timeline>
        <TimelineItem color="green">发布1.0版本</TimelineItem>
        <TimelineItem color="green">发布2.0版本</TimelineItem>
        <TimelineItem color="red">严重故障</TimelineItem>
        <TimelineItem color="blue">发布3.0版本</TimelineItem>
    </Timeline>
    </div>
  </div>
</template>
<script>
import Navbar from "./Navbar.vue";
    export default {
         components: { Navbar },
    }
</script>
