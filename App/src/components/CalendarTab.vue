<template>
  <Label class="message" :text="msg"/>
</template>

<script lang="ts">

//Class component for Calendar Tab
import  {Vue,Prop, Component } from 'vue-property-decorator'

@Component
export default class CalendarTab extends Vue{
    @Prop() private msg: string;
}
</script>

<style>

</style>