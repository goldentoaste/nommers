<script>
  import { fly } from "svelte/transition";
  let innerWidth;
  export let open;
</script>

<svelte:window bind:innerWidth />
<div
  class="drawer"
  transition:fly={{
    x: innerWidth,
  }}
>
  <div class="drawer-content">
    <div
      class="header-icon"
      on:click={() => {
        open = false;
      }}
    >
      <img
        src="icons/close_icon.svg"
        alt="Menu icon"
      />
    </div>

    <div class="links">
      <a href="https://github.com/goldentoaste/nommers">GitHub</a>
      <a href="https://devpost.com/software/nommers">DevPost</a>
      <a href="/login">Log in</a>
      <a href="/signup">Sign up</a>
    </div>
  </div>
</div>

<style>
  .drawer {
    z-index: 1000;
    position: fixed;
    top: 0;
    right: 0;
    background-color: var(--primary-100);
    height: 100vh;
    width: 100vw;
    overflow: hidden;
  }

  .drawer-content {
    width: calc(100% - (var(--sp-lg) * 2));
    height: 100%;
    padding: var(--sp-lg);
  }

  .header-icon {
    display: flex;
    justify-content: flex-end;
    margin-bottom: var(--sp-4xl);
  }

  .links {
    text-align: center;
    display: flex;
    flex-direction: column;
    gap: var(--sp-2xl);
  }

  .links > a {
    font-size: 2.5rem; /* 48px */
    line-height: 1;
    font-weight: 600;
    color: black;
  }

  .links > a:visited {
    color: black;
  }
</style>
