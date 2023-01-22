<script>
  export let username;
  export let isOwner;
</script>

<div class="lobby-member">
  {username}
  {#if isOwner}
    <img
      src="/placeholder.png"
      alt="Placeholder"
    />
  {/if}
</div>
