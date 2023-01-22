<script>
  import { createEventDispatcher } from "svelte";
  // @ts-ignore
  export let value;

  const dispatch = createEventDispatcher();

  let valChanged = () => {
    dispatch("valChanged", {
      // @ts-ignore
      val: value,
    });
  };
</script>

<div>
  <button on:click={valChanged}>
    <slot />
  </button>
</div>
