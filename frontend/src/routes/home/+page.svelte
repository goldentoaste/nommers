<script>
  import { accountId } from "../../account";

  const logout = () => {
    $accountId = null;

    window.location.href = "/login";
  };

  import { bind } from "svelte/internal";

  import { partyNumber } from "../../votingstates";
  let roomcode = "";

  const joinRoom = () => {
    if (!isNaN(roomcode)) {
      partyNumber.set(parseInt(roomcode));
      window.location.href = "/lobby";
    }
  };
</script>

<div class="home">
  <div class="home-img">
    <img
      src="nommers-logo.png"
      alt="Nommers logo"
    />
  </div>

  <div class="home-title">
    <h2>Welcome to Nommers!</h2>
    <p class="body-text">Say yes to more food and less stress with Nommers.</p>

    <div class="home-actions">
      <div class="enter-lobby-code">
        <span class="caption-text">Enter lobby code</span>
        <input
          type="text"
          bind:value={roomcode}
        />
        <a
          class="body-title primary-action"
          on:click={joinRoom}>Join lobby</a
        >
      </div>

      <div class="separator overline">OR</div>

      <a
        class="body-title secondary-action"
        href="/create-party">Create party</a
      >
    </div>
  </div>

  <div class="user-information">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <div
      on:click={logout}
      class="body-title secondary-action">Logout</div
    >
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
    background-color: var(--secondary-50);
  }

  .home > div {
    text-align: center;
  }

  .home-title {
    padding: var(--sp-4xl) var(--sp-2xl);
    background-color: white;
    border-radius: var(--sp-md);
    border: 1px solid var(--secondary-100);
    max-width: 640px;
  }

  .home-title,
  .user-information {
    width: 75%;
  }

  .home-title > p {
    padding-bottom: var(--sp-md);
  }

  .home-actions {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--sp-lg);
  }

  .user-information {
    max-width: 520px;
  }

  .home-actions > .caption-text {
    text-align: left;
  }

  .enter-lobby-code {
    text-align: left;
    display: flex;
    flex-direction: column;
  }

  .enter-lobby-code > input {
    margin-bottom: var(--sp-sm);
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

  .overline {
    margin: 0;
  }

  .separator {
    display: flex;
    align-items: center;
    text-align: center;
    color: var(--secondary-400);
  }

  .separator::before,
  .separator::after {
    content: "";
    flex: 1;
    border-bottom: 1px solid var(--secondary-300);
  }

  .separator:not(:empty)::before {
    margin-right: 0.25em;
  }

  .separator:not(:empty)::after {
    margin-left: 0.25em;
  }
</style>
