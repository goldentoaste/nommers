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

  <a
    href="/home"
    class="body-title secondary-action">Return to home</a
  >
</div>

<style>
  .voting-results {
    display: flex;
    gap: var(--sp-lg);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: var(--sp-lg);
    background-color: var(--secondary-50);
    max-height: calc(100vh - var(--sp-lg) - var(--sp-lg));
    height: calc(100vh - var(--sp-lg) - var(--sp-lg));
  }

  .results-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: var(--sp-sm);
    padding: var(--sp-lg);
    background-color: white;
    overflow: scroll;
    border-radius: var(--sp-sm);
    border: 1px solid var(--secondary-100);
  }

  .secondary-action {
    color: var(--secondary-500);
    background-color: var(--secondary-100);
    width: 100%;
    padding: var(--sp-md) 0;
    border-radius: var(--sp-2xl);
    text-align: center;
    text-decoration: none;
  }

  @media screen and (min-width: 720px) {
    .results-title {
      padding: var(--sp-2xl) var(--sp-lg);
    }

    .secondary-action {
      width: fit-content;
      padding: var(--sp-md);
    }

    .results-container {
      max-width: 720px;
    }
  }
</style>
