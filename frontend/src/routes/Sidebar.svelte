<script>
  export let open = false;
</script>

<div class="sidebar">
  <a class="">GitHub</a>
  <a class="">DevPost</a>
  <a class="/app">Nommers</a>
</div>

<style>
  .sidebar {
    right: -100%;
    transition: 0.3s ease-in-out;
  }

  .open {
    right: 0;
  }
</style>
