<script>
  import ButtonGroup from "./ButtonGroup.svelte";

  let sort, price, rating, hours;

  let selected_dining_option = [];
  let selected_offerings = [];

  let dining_options = ["Takeout", "Delivery", "Dine in"];
  let offerings = ["Breakfast", "Brunch", "Lunch", "Dinner", "Vegetarian"];
</script>

<div class="create-party">
  <div class="create-party-input-group">
    <h4>Create a party</h4>

    <div class="input-group">
      <p class="caption-text">Sort by</p>
      <ButtonGroup
        bind:val={sort}
        valMaps={{
          Relevance: "Relevance",
          Distance: "Distance",
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
          Any: 1,
          "Open now": 2,
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
    <a class="body-title primary-action">Create party</a>
    <a class="body-title secondary-action">Back to home</a>
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
</style>
