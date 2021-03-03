import Vue from 'vue';
import Vuex from 'vuex';
import {State} from './types'

const state: State = {

    daily: 
        {
            id:'1234',
            date:["1", "1", "2021"],
            tags:['jõuluaeg', 'rõõmus'],
            liturgicalTime:'jõuluaeg',
            content:{
                name:'testimise päev',
                saint: 'pyha loorem',
                imageID: '1',
                psalmID:'2',
                text:'Mingi tekst millel pole v\u00e4ga t\u00e4hendust, aga mis parata.\n'
            },
            mandatory:true
        }
    
   
}
export const dailyContent = {
    state
}
