import { writable } from "svelte/store";
import { browser } from '$app/environment';


const storedId = browser? localStorage.getItem("accountId") : null;

export const accountId = writable(storedId)
accountId.subscribe(val=>{
    if (browser) {
    localStorage.setItem("accountId", val);}
})