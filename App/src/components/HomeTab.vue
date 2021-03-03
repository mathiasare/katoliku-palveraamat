
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


@Component
export default class HomeTab extends Vue{

    //Proprerties
    @Prop() private msg: string;
    @Prop() private daily: dailyContent<Content>;
    

    
    //Computed
    get currentDate(){
      let date = new Date();
      let options = {
        day:'2-digit',
        month:'short'
      };
    return new String(new Intl.DateTimeFormat('et-EE',options).format(date)).toUpperCase();
    }

    get name(){
      if(this.daily==null){
        return "SUVAKAS"
      }else{
        return this.daily.content.name;
      }
      
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