<script>
  export let valMaps = {}; // {name:val, ...}
  export let val;
  export let bindGroup;

  if (valMaps) {
    val = Object.values(valMaps)[0];
  }
</script>

{#each Object.entries(valMaps) as [name, varVal]}
  <label>
    <input
      type="checkbox"
      bind:group={bindGroup}
      value={varVal}
    />{name}
  </label>
{/each}

<style>
  .selected {
    background-color: red;
  }
</style>
