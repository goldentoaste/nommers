<script>
  import PartyMemberStatus from "./PartyMemberStatus.svelte";
  import Drag from "../lobby/Drag.svelte";

  let restaurantImg = "placeholder/restaurant.jpg";
  let restaurantName = "Chipotle Mexican Grill";
  let restaurantCaption = "Mexican restaurant";
  let starRating = 4.1;
  let dollarRating = "$$";
  let distance = "400m";
  let address = "4700 Kingsway #2200, Burnaby, BC V5H 4M1";
  let description =
    "Fast-food chain offering Mexican fare including design-your-own burritos, tacos, and bowls.";
</script>

<div class="voting-content">
  <div class="exit-button">
    <a href="/home"
      ><img
        src="icons/exit.svg"
        alt="Exit party"
      /> <span>Exit party</span></a
    >
  </div>

  <Drag />
  

  <div class="loader">
    <div class="loader-bar">
      <div class="loading-completed" />
    </div>

    <div class="loader-information">
      <span class="caption-text">12 restaurants remaining</span>
      <span class="overline">75% completed</span>
    </div>
  </div>

  <div class="party-information">
    <div class="party-members">
    
    </div>
    <span class="caption-text">Waiting for 4 others to finish voting...</span>
  </div>
</div>

<style>
  .voting-content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: var(--sp-lg);
  }

  .exit-button {
    display: flex;
    justify-content: center;
  }

  .exit-button > a {
    text-decoration: none;
    display: flex;
    align-items: center;
    width: fit-content;
    gap: var(--sp-2xs);
    padding: var(--sp-xs) var(--sp-md);
    background-color: var(--black-100);
    border-radius: var(--sp-lg);
    border: 1px solid var(--black-200);
  }

  .exit-button > a > img {
    height: var(--sp-lg);
  }

  .voting-content {
    padding: var(--sp-lg);
    height: calc(100vh - (var(--sp-lg) * 2));
    max-height: calc(100vh - (var(--sp-lg) * 2));
  }

  .party-information {
    text-align: center;
    height: fit-content;
  }

  .party-members {
    margin-bottom: var(--sp-2xs);
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: var(--sp-3xs);
  }

  .loader-bar {
    width: 100%;
    height: var(--sp-sm);
    border-radius: var(--sp-lg);
    background-color: var(--green-200);
  }

  .loading-completed {
    width: 85%;
    height: 100%;
    background: var(--green-500);
    border-radius: var(--sp-lg);
  }

  .loader-information {
    margin-top: var(--sp-xs);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .loader-information > .overline {
    margin: 0;
  }

  .restaurant-img-info {
    margin-top: var(--sp-2xs);
  }

  .restaurant-card {
    display: flex;
    gap: var(--sp-xs);
    flex-direction: column;
    justify-content: space-between;
    background-color: var(--black-100);
    border-radius: var(--sp-xs);
    height: 100%;
    padding: var(--sp-lg);
  }

  .restaurant-img {
    color: white;
    padding: var(--sp-lg);
    height: calc(100% - (75px * 2) - var(--sp-md));
    background-size: cover;
    border-radius: var(--sp-sm);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .restaurant-info {
    margin-top: var(--sp-md);
    display: flex;
    flex-direction: column;
    gap: var(--sp-xs);
  }

  .restaurant-info > div {
    display: flex;
    gap: var(--sp-md);
    flex-direction: row;
  }

  .restaurant-info > div > .restaurant-icon {
    width: var(--sp-xl);
    height: auto;
    aspect-ratio: 1/ 1;
  }

  .restaurant-icon > img {
    width: 100%;
  }

  .restaurant-info > div > span {
    width: calc(100% - var(--sp-xl));
    text-overflow: ellipsis;
    overflow: hidden;
    max-height: 75px;
  }
</style>
