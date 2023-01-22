<script>
  import ValueButton from "./ValueButton.svelte";
  export let sort_by = "Relevance";
  let sortOpts = ["Relevance", "Distance"];
</script>

{#each sortOpts as s}
  <ValueButton
    value={s}
    on:valChanged={(e) => {
      sort_by = e.val;
    }}
  >
    {s}
  </ValueButton>
{/each}
