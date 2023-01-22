<script>
  export let valMaps = {}; // {name:val, ...}
  export let val;

  if (valMaps) {
    val = Object.values(valMaps)[0];
  }
</script>

<div class="button-group">
  {#each Object.entries(valMaps) as [name, varVal]}
    <button
      style="width: calc(100% / {Object.keys(valMaps).length}"
      on:click={() => {
        val = varVal;
      }}
      class={varVal === val ? "selected" : ""}
    >
      {name}
    </button>
  {/each}
</div>

<style>
  .button-group {
    width: 100%;
    border: 1px solid var(--primary-200);
    border-radius: var(--sp-2xs);
  }

  button {
    font-family: "Poppins";
    border: none;
    background-color: white;
    border-radius: var(--sp-2xs);
    padding: var(--sp-xs) var(--sp-sm);
    font-size: 1rem; /* 16px */
    line-height: 1.5rem; /* 24px */
  }

  .selected {
    background-color: var(--secondary-100);
  }
</style>
