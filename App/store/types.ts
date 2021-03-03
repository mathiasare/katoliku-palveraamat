//Store types

export interface State{
    daily: dailyContent<Content>
}


//Models
export interface dailyContent<T>{
    id: string,
    date:string[],
    tags:string[],
    liturgicalTime:string,
    content:T,
    mandatory:boolean
}

export interface Content{
    name: string,
    saint: string,
    imageID: string,
    psalmID:string,
    text:string
}