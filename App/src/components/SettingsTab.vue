<template>
  <Label class="message" :text="name"/>
</template>

<script lang="ts">
//Class component for Settings Tab
import  {Vue,Prop, Component } from 'vue-property-decorator'

@Component
export default class SettingsTab extends Vue{
    @Prop() private msg: string;
    data(){
        return{
            //!Example code, remove later
            name:"Siin on mingi muutuja"
        }
    }
}
</script>

<style>

</style>