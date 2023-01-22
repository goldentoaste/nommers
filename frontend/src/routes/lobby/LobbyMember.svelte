<script>
  export let username;
  export let isOwner;
</script>

<div
  class="lobby-member"
  style="background-color: var({isOwner ? '--secondary-100' : '--black-100'})"
>
  <div class="member-info">
    <span>{username}</span>

    <div class="member-icon">
      {#if isOwner}
        <img
          src="/icons/star.svg"
          alt="Lobby owner icon"
        />
      {/if}

      {#if !isOwner}
        <img
          src="/icons/close.svg"
          alt="Remove member icon"
        />
      {/if}
    </div>
  </div>
</div>

<style>
  .lobby-member {
    margin: var(--sp-xs);
    display: inline-block;
    width: fit-content;
    padding: var(--sp-xs) var(--sp-md);
    border-radius: var(--sp-xl);
  }

  .member-info {
    display: inline-flex;
    align-items: center;
    flex-direction: row;
    gap: var(--sp-2xs);
  }

  .member-icon {
    display: flex;
    align-items: center;
    height: var(--sp-md);
    width: auto;
    aspect-ratio: 1/1;
  }

  .member-icon > img {
    height: 100%;
  }
</style>
