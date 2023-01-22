<script>
  import ButtonGroup from "./ButtonGroup.svelte";
  import { accountId } from "../../account";

  import {
    partyNumber,
    currentState,
    ending,
    finishedMembers,
    places,
    results,
    totalmembers,
    voting,
    waiting,
    isOwner,
  } from "../../votingstates";
  let sort = "prominence",
    price = "3",
    rating = "1",
    hours = false,
    address = "";

  let selected_dining_option = [];
  let selected_offerings = [];

  let dining_options = ["Takeout", "Delivery", "Dine in"];
  let offerings = ["Breakfast", "Brunch", "Lunch", "Dinner", "Vegetarian"];

  const createParty = () => {
    if (address.length == 0) {
      return;
    }
    let params = {
      id: $accountId,
      address: address,
      radius: 15000,
      sortby: sort,
      cost: price,
      keywords: selected_dining_option.concat(selected_offerings),
      rating: 3,
      opennow: hours,
    };

    fetch(
      "http://server3-env.eba-7jgvjkan.us-west-2.elasticbeanstalk.com/makeparty/",
      {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify(params),
      }
    )
      .then((res) => res.json())
      .then((res) => {
        partyNumber.set(res["id"]);
        places.set(JSON.parse(res["response"]));
        isOwner.set(true);
        window.location.href = "/lobby";
      })
      .catch((e) => alert(e));
  };
</script>

<div class="create-party">
  <div class="create-party-input-group">
    <h4>Create a party</h4>
    <div class="input-group">
      <p class="caption-text">Address</p>
      <input
        type="text"
        bind:value={address}
      />
    </div>
    <div class="input-group">
      <p class="caption-text">Sort by</p>
      <ButtonGroup
        bind:val={sort}
        valMaps={{
          Relevance: "prominence",
          Distance: "distance",
        }}
      />
    </div>

    <div class="input-group">
      <p class="caption-text">Price</p>
      <ButtonGroup
        bind:val={price}
        valMaps={{
          $: 1,
          $$: 2,
          $$$: 3,
          $$$$: 4,
        }}
      />
    </div>

    <div class="input-group">
      <p class="caption-text">Rating (at least)</p>
      <ButtonGroup
        bind:val={rating}
        valMaps={{
          Any: 1,
          "2 ★": 2,
          "3 ★": 3,
          "4 ★": 4,
        }}
      />
    </div>

    <div class="input-group">
      <p class="caption-text">Hours</p>
      <ButtonGroup
        bind:val={hours}
        valMaps={{
          Any: false,
          "Open now": true,
        }}
      />
    </div>

    <div class="checkboxes-div">
      <div class="input-group">
        <p class="caption-text">Dining options</p>
        <div class="checkbox-group">
          {#each dining_options as options}
            <label>
              <input
                type="checkbox"
                bind:group={selected_dining_option}
                name="dining_options"
                value={options}
              />
              {options}
            </label>
          {/each}
        </div>
      </div>

      <div class="input-group">
        <p class="caption-text">Offerings</p>
        <div class="checkbox-group">
          {#each offerings as offering}
            <label>
              <input
                type="checkbox"
                bind:group={selected_offerings}
                name="offerings"
                value={offering}
              />
              {offering}
            </label>
          {/each}
        </div>
      </div>
    </div>
  </div>

  <div class="create-party-actions">
    <div
      class="body-title primary-action"
      on:click={createParty}>Create party</div
    >
    <a
      class="body-title secondary-action"
      href="/home">Back to home</a
    >
  </div>
</div>

<style>
  .create-party {
    padding: var(--sp-lg);
    height: calc(100vh - (var(--sp-lg) * 2));
    max-height: calc(100vh - (var(--sp-lg) * 2));
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .input-group,
  .checkboxes-div {
    width: 100%;
  }

  .input-group {
    margin-bottom: var(--sp-md);
  }

  .input-group > .caption-text {
    margin-bottom: var(--sp-2xs);
  }

  .checkboxes-div {
    display: flex;
    flex-direction: row;
  }

  .checkboxes-div > div {
    width: 50%;
  }

  .checkbox-group {
    display: flex;
    flex-direction: column;
  }

  .create-party-actions {
    display: flex;
    width: 100%;
    flex-direction: row-reverse;
    gap: var(--sp-xs);
  }

  .primary-action,
  .secondary-action {
    width: 50%;
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

  @media screen and (min-width: 768px) {
    .create-party {
      padding-left: calc(var(--sp-4xl) * 2);
      padding-right: calc(var(--sp-4xl) * 2);
    }
  }
</style>
