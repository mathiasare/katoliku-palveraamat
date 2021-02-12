<template>
  <Label class="message" :text="msg"/>
</template>

<script lang="ts">
//Class component for PrayerBook Tab
import  {Vue,Prop, Component } from 'vue-property-decorator'

@Component
export default class BookTab extends Vue{
    @Prop() private msg: string;
}
</script>

<style>

</style>