<script>
  /**
   * @type {String}
   */
  export let img_link;

  /**
   * @type {String}
   */
  export let name;

  /**
   * @type {String}
   */
  export let title;

  /**
   * @type {String}
   */
  export let description;

  /**
   * @type {String}
   */
  export let github_link;

  /**
   * @type {String}
   */
  export let linkedin_link;

  /**
   * @type {String}
   */
  export let resume_link;
</script>

<div class="teammate-card">
  <img
    src={img_link}
    alt="Teammate"
  />
  <h4>{name}</h4>
  <h5>{title}</h5>
  <p class="body">{description}</p>
  <div class="teammate-links">
    <a
      class="body-title secondary-button"
      href={github_link}>GitHub</a
    >
    <a
      class="body-title secondary-button"
      href={linkedin_link}>LinkedIn</a
    >
    <a
      class="body-title secondary-button"
      href={resume_link}>Resume</a
    >
  </div>
</div>

<style>
  .teammate-card {
    background-color: white;
    padding: var(--sp-md);
    border-radius: var(--sp-sm);
  }

  .teammate-card > img {
    margin-bottom: var(--sp-md);
  }

  .teammate-card > h4 {
    margin-bottom: var(--sp-2xs);
  }

  .teammate-card > p {
    margin-top: var(--sp-md);
    margin-bottom: var(--sp-lg);
  }

  .teammate-links {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: var(--sp-xs);
  }
</style>
