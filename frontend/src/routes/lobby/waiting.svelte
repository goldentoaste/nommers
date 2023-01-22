<script>
    import LobbyMember from "./LobbyMember.svelte";
    import { isOwner, totalmembers } from "../../votingstates";
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher()

    const start = ()=>{
        if (!$isOwner){
            return
        }

        dispatch("start")
    }
  </script>
  
  <div class="lobby">
    <div class="lobby-content">
      <div class="lobby-pin">
        <p class="overline"> LOBBY PIN </p>
        <h1 class="title">405 102</h1>
      </div>
  
     
    </div>
    <div> <h3>There are {$totalmembers} people in the lobby</h3></div>
    <div class="lobby-actions">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div
        class="body-title primary-action" on:click={start}
        >
        {#if $isOwner}
        Start Voting!
        {:else}
        Waiting for host to start
        {/if}
        </div
      >
      <a href=""
        class="body-title secondary-action">Exit party</a
      >
    </div>
  </div>
  
  <style>
    .lobby {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background-color: var(--black-50);
      height: calc(100vh - (var(--sp-lg) * 2));
      padding: var(--sp-lg);
      text-align: center;
    }
  
    .lobby-pin {
      padding-top: var(--sp-lg);
    }
  
    .lobby-members {
      display: block;
      text-align: center;
      padding: var(--sp-md);
      background-color: var(--black-0);
      border-radius: var(--sp-xs);
      border: 1px solid var(--black-100);
    }
  
    .lobby-actions {
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
    .title {
      font-size: 6rem;
      line-height: 1;
      
    }
  </style>
  