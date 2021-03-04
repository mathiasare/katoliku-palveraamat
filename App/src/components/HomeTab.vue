
<template>
      <FlexboxLayout class="root" flexDirection="column">
        <FlexboxLayout id="date-box" backgroundColor="#ffffff" >
          
          <TextView class="date"  :text="currentDate" editable="false"/>
          <Label class="header" :text="name"/>
        </FlexboxLayout>
      </FlexboxLayout>
</template>

<script lang="ts">

//Class component for Home Tab

import  {Vue,Prop, Component } from 'vue-property-decorator'
import Intl from 'intl'
import { dailyContent } from 'store/types';
import { Content } from 'store/types';
import axios from 'axios'

import { knownFolders, Folder, File } from "@nativescript/core/file-system";

@Component
export default class HomeTab extends Vue{

    
    //@Prop() private daily: dailyContent<Content>;
   
    private name:string = "tere";
    //Computed
    get currentDate(){
      let date = new Date();
      let options = {
        day:'numeric',
        month:'numeric',
        year:'numeric'
      };
    return new String(new Intl.DateTimeFormat('et-EE',options).format(date)).toUpperCase();
    }

    
created(){

this.name="eiii"
const [day,month,year] = ["1","1","2021"]    //! use this later: this.currentDate.split(".") 
const ID = this.$store.state.date;


let file = knownFolders.currentApp().getFolder("assets").getFolder("FS").getFolder("2021").getFile("1.json");


/**  const response = await fetch(path);
const json = await response.json() */


let body = JSON.parse(file.readTextSync())

this.name=body.days[0].content.name
  

}
    
    
}
</script>

<style scoped>
.root{
  text-align: center;
}
#date-box{
  margin: 100px;
  padding:20 10 20 10;
  height: auto;
  border-radius: 30px;
  border-width:3px;
  border-color: #000000;
  align-items: center;
  justify-content: space-around;
}

.date{
  font-size: 20;
  text-decoration: none;
  text-align: left;
  border:none;
  background-color:#ffffff;
  overflow-wrap: break-word;
}

.header{
  font-size: 20;
  color: #000000;
  border:none;
  text-decoration: none;
}
</style>