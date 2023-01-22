<script>
    import {
        openWebsocket,
        partyNumber,
        currentState,
        ending,
        finishedMembers,
        isOwner,
        places,
        results,
        totalmembers,
        voting,
        waiting,
    } from '../../votingstates.js';
    import { accountId } from '../../account.js';
    import { onMount } from 'svelte';
    import Waiting from '../lobby/waiting.svelte';
    import Memberstatus from '../lobby/memberstatus.svelte';
    import Voting from '../lobby/voting.svelte';
    /**
   * @type {WebSocket}
   */
    let socket;

    onMount(async () => {

        socket = openWebsocket($partyNumber, $accountId);
    });

    const startVote = ()=>{
      socket.send(JSON.stringify(
        {
          "message":"start"
        }
      ))
    }
</script>


{#if $currentState == waiting}
<Waiting on:start={startVote}></Waiting>
{/if}


{#if $currentState == voting}
<Voting></Voting>
{/if}