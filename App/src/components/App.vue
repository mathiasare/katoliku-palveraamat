<template>
  <Page>
    <ActionBar android:flat="true">
      <FlexboxLayout justifyContent="center">
        <Label class="title" text="KATOLIKU -|-" />
      </FlexboxLayout>
    </ActionBar>

    <Tabs id="tabs" selectedIndex="0"  v-model="selected">
      <TabStrip>
        <TabStripItem :class="{selected:isSelected(0)}">
              <Image src="~/assets/images/church2.png"></Image>
          <Image src="~/assets/images/church2.png"></Image>
        </TabStripItem>
        <TabStripItem :class="{selected:isSelected(1)}">
          
          <Image src="~/assets/images/cal.png"></Image>
          </TabStripItem>
          <TabStripItem :class="{selected:isSelected(2)}">
            
            <Image src="~/assets/images/bible.png"></Image>
          </TabStripItem>
          <TabStripItem :class="{selected:isSelected(3)}">
            
            <Image src="~/assets/images/wrench.png"></Image>
          </TabStripItem>
      </TabStrip>

      <TabContentItem>
        <GridLayout columns="*" rows="*">
          <HomeTab msg="kodu" :daily="findDaily" />
        </GridLayout>
      </TabContentItem>

      <TabContentItem>
        <GridLayout columns="*" rows="*">
          <CalendarTab msg="Kalender" />
        </GridLayout>
      </TabContentItem>
      <TabContentItem>
        <GridLayout columns="*" rows="*">
          <BookTab msg="Palveraamat" />
        </GridLayout>
      </TabContentItem>
      <TabContentItem>
        <GridLayout columns="*" rows="*">
          <SettingsTab />
        </GridLayout>
      </TabContentItem>
    </Tabs>
  </Page>
</template>

<script lang="ts">
//Root component for the whole App


//Class components
import { Component, Prop, Vue } from "vue-property-decorator";


import HomeTab from "./HomeTab.vue";
import CalendarTab from "./CalendarTab.vue";
import BookTab from "./BookTab.vue";
import SettingsTab from "./SettingsTab.vue";

//Store components

import {dailyContent} from '../../store/types'
import {Content} from '../../store/types'
import store from '../store'
import data from '../../FS/2021/1.json'
import { knownFolders, Folder, File } from "@nativescript/core/file-system";

@Component({
  components: {
    HomeTab,
    CalendarTab,
    BookTab,
    SettingsTab,
  },
})
export default class App extends Vue {
//Properties
  
//Data
  data(){
      return{
          selected:""
        
          
      }
  }
//Methods
isSelected(index){
    if(index==this.$data.selected){
        return true;
    }
}

get findDaily(){
  const identifier = this.$store.state.date;
  const year = "2021";
  const month = "1";
  const path = '../../FS/2021/1.json'
  
  const data = this.getJsonFile(path);
  for (let index = 0; index < data.days.length; index++) {
     const element:dailyContent<Content> = data.days[index];
    if(element.id==identifier){
      return element;
    }
    
  }

return null;
}

getJsonFile (path) {
  let appFolder = knownFolders.currentApp();
  let cfgFile = appFolder.getFile(path);
  cfgFile.readText()
    .then((res) => {

    let data=JSON.parse(res);
        
    
    }).catch((err) => {
        console.log(err.stack);
    });
    return data;
}





}
</script>

<style scoped>
ActionBar {
  background-color: #030214;
  color: #ffffff;
}
TabStrip {
    background-color:#030214 ;
    highlight-color:#ffffff ;
}

.title {
  font-size: 20%;
}

.message {
  vertical-align: center;
  text-align: center;
  font-size: 20;
  color: #333333;
}
.selected{
   
   background-color:#ffffff;
}




</style>
