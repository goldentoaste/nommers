<script>
  import Result from "./Result.svelte";
</script>

<div class="voting-results">
  <div class="results-title">
    <p class="overline">Your results</p>
    <h2>The voting period has ended!</h2>
  </div>

  <div class="results-container">
    <Result
      rank="1"
      restaurant_name="Chipotle Mexican Grill"
      num_of_votes="12"
    />

    <Result
      rank="2"
      restaurant_name="Earl’s Grill and Bar"
      num_of_votes="11"
    />

    <Result
      rank="3"
      restaurant_name="Sushi Garden"
      num_of_votes="11"
    />

    <Result
      rank="4"
      restaurant_name="McDonald's"
      num_of_votes="11"
    />

    <Result
      rank="5"
      restaurant_name="Ramen Danbo"
      num_of_votes="10"
    />

    <Result
      rank="6"
      restaurant_name="Panda Express"
      num_of_votes="10"
    />

    <Result
      rank="7"
      restaurant_name="Popeye's Louisiana Chicken"
      num_of_votes="10"
    />
  </div>
</div>

<style>
  .voting-title {
    height: fit-content;
  }

  .voting-results {
    display: flex;
    gap: var(--sp-lg);
    flex-direction: column;
    text-align: center;
    padding: var(--sp-lg);
    background-color: var(--black-50);
  }

  .results-container {
    display: flex;
    flex-direction: column;
    gap: var(--sp-sm);
  }
</style>
