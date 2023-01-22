<script>
  export let rank;
  export let restaurant_name;
  export let restaurant_img = "placeholder/placeholder_1.png";
  export let num_of_votes;
</script>

<div class="voting-result">
  <h4 class="rank">#{rank}</h4>

  <div class="result-info">
    <h5>{restaurant_name}</h5>
    <span>{num_of_votes} votes</span>
  </div>
</div>

<style>
  .rank {
    width: 20%;
  }

  .voting-result {
    align-items: center;
    display: flex;
    flex-direction: row;
    gap: var(--sp-md);
    padding: var(--sp-sm);
    background-color: var(--black-50);
    border-radius: var(--sp-xs);
  }

  .voting-result > h4 {
    margin: 0;
  }

  .result-img {
    height: var(--sp-4xl);
    width: auto;
    aspect-ratio: 1 / 1;
  }

  .result-img > img {
    border-radius: var(--sp-xs);
    width: 100%;
  }

  .result-info {
    width: 100%;
    text-align: left;
    display: flex;
    flex-direction: column;
    gap: var(--sp-2xs);
  }
</style>
