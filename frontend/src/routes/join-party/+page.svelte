<script>
    import { bind } from "svelte/internal";

    import { partyNumber } from "../../votingstates";
    let roomcode = "";

    const joinRoom = ()=>{
        if (!isNaN(roomcode)){
            partyNumber.set(parseInt(roomcode))
            window.location.href = "/lobby"
        }
    }
</script>

<p>type room code here</p>
<input type= "text" bind:value={roomcode}/>
<button on:click={joinRoom}>click here to start</button>
