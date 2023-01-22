<script>
  import ButtonGroup from "./ButtonGroup.svelte";

  let currentVal;
</script>

<div class="create-party">
  <h4>Create a party</h4>

  <p class="caption-text">Sort by</p>
  <ButtonGroup 
  valMaps={
    {
      "Option A": "AAAA",
      "Option B": "BBBB"
    }
  }
  bind:val={currentVal}
  />
</div>
<p>Curruent Val is {currentVal}</p>

<style>
  .create-party {
    padding: var(--sp-lg);
  }
</style>
