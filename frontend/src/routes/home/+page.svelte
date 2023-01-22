
<script>
import { accountId } from "../../account";

  const logout = ()=>{
    $accountId = null;

    window.location.href = "/login"
  }
</script>

<div class="home">
  <div class="home-img">
    <img
      src="nommers_logo.svg"
      alt="Nommers logo"
    />
  </div>

  <div class="home-title">
    <h2>Welcome to Nommers!</h2>
    <p class="body-text">Say yes to more food and less stress with Nommers.</p>

    <div class="home-actions">
      <a
        class="body-title primary-action"
        href="/create-party">Create party</a
      >
      <div class="body-title secondary-action">Join party</div>
      
    </div>
  </div>

  <div class="user-information">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div on:click={logout} class="body-title secondary-action">Logout</div>
    <!-- <p class="caption-text">Your username</p>
    <p class="body-title">FatPenguin</p> -->
  </div>
</div>

<style>
  .home {
    padding: var(--sp-lg);
    height: calc(100vh - var(--sp-lg) - var(--sp-lg));
    max-height: calc(100vh - var(--sp-lg) - var(--sp-lg));
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
  }

  .home > div {
    text-align: center;
  }

  .home-title {
    width: 75%;
  }

  .home-title > p {
    padding-bottom: var(--sp-md);
  }

  .home-actions {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--sp-sm);
  }

  .primary-action,
  .secondary-action {
    width: 100%;
    padding: var(--sp-md) 0;
    border-radius: var(--sp-2xl);
    text-align: center;
    text-decoration: none;
  }

  .primary-action {
    background-color: var(--secondary-500);
    color: white;
  }

  .secondary-action {
    color: var(--secondary-500);
    background-color: var(--secondary-100);
  }
</style>
