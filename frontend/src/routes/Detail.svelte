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
</style>
