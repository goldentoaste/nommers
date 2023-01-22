<script>
  export let voting_complete;
</script>

<div
  class="party-member-status"
  style="background-color: var({voting_complete
    ? '--green-200'
    : '--black-100'})"
>
  {#if voting_complete}
    <img
      src="icons/done.svg"
      alt="Voting done"
    />
  {:else}
    <img
      src="icons/hourglass.svg"
      alt="Voting not done"
    />
  {/if}
</div>

<style>
  .party-member-status {
    width: var(--sp-lg);
    height: auto;
    border-radius: 100%;
    aspect-ratio: 1 / 1;
    display: flex;
    text-align: center;
    padding: var(--sp-2xs);
    align-items: center;
  }

  .party-member-status > img {
    width: 100%;
    text-align: center;
    height: auto;
  }
</style>
