import { writable } from "svelte/store";
export const waiting = "wait";
export const voting = "vote";
export const ending = "end";

export const currentState = writable(waiting)
export const places = writable({})
export const totalmembers = writable(0)
export const finishedMembers = writable(0)
export const results = writable({})


const openWebsocket = (partyid, memberid)=> {
    let socket = new WebSocket(`ws://server3-env.eba-7jgvjkan.us-west-2.elasticbeanstalk.com/ws/${partyid}/${memberid}`)

    socket.onopen = (e)=>{
        console.log("socket opened", e)
    }

    socket.onclose = (e)=>{
        if (e.wasClean){
            console.log("socket closed cleanly")
        }
        else{
            console.log("socket closed forcefully.")
        }
    }

    socket.onerror = (e)=>{
        console.log("socket encountered error", e)
    }

    socket.onmessage = (e) =>{
        data = JSON.parse(e.data)

        msg = data['message']
        
        if (msg.includes("total count")){
            count = parseInt(msg.split(":")[1])

            totalmembers.set(count);
        }
        
        if (msg === "start"){
            currentState.set(voting)
        }

        if (msg.includes("finish")){
            count = parseInt(msg.split(":")[1])

            finishedMembers.set(count)
        }

        if (msg === "fullstop"){
            results.set(data["results"])
        }
    }

    return socket;
}