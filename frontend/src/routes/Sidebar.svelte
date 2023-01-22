<script>
    import {fly} from "svelte/transition"
    let innerWidth;
    export let open;
</script>

<svelte:window bind:innerWidth />
<div class="drawer"
    transition:fly={{
        x: innerWidth
    }}
>
   <p>content</p>
   <button on:click={()=>{open = false}}> click to close</button>
</div>

<style>
    .drawer {
		position: fixed;
		top: 0;
		right: 0;
		background: #ddd;
		height: 100vh;
		width: 100vw;
		border-left: 1px solid rgba(0, 0, 0, .1);
		box-shadow: -2px 0px 6px -1px rgba(0, 0, 0, 0.1);
	}
</style>
