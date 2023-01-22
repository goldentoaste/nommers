<script>
    export let valMaps = {}; // {name:val, ...}
    export let val;

    if (valMaps){
      val = Object.values(valMaps)[0]
    }
    
</script>
<style>
  .selected {
    background-color: red;
  }
</style>


{#each Object.entries(valMaps) as [name, varVal]}
<button on:click={()=>{val = varVal}} class={varVal === val? "selected":""}>
  {name}
</button>
{/each}