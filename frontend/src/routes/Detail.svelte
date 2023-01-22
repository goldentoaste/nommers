<script>
  /**
   * @type {String}
   */
  export let img_link;

  /**
   * @type {String}
   */
  export let heading_text;

  /**
   * @type {String}
   */
  export let paragraph_text;
</script>

<div class="detail-content">
  <div class="detail-img">
    <img
      src={img_link}
      alt="Icon representing the detail"
    />
  </div>
  <h4>{heading_text}</h4>
  <p class="body-text">{paragraph_text}</p>
</div>

<style>
  .detail-content > :last-child {
    margin-bottom: 0;
  }

  .detail-content > h4 {
    margin-top: var(--sp-sm);
  }

  @media only screen and (min-width: 800px) {
    .detail-content {
      width: calc(100% / 3);
    }
  }
</style>
