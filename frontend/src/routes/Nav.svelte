<script>
    export let useSideBar = false;
</script>

<div class="header-container">
    <div class="header">
        <div class="header-logo">
            <img src="nommers_logo.svg" alt="Nommers logo" />
        </div>
        <slot />
        <div
            class="header-icon"
            on:mousedown={() => {
                useSideBar = !useSideBar;
            }}
        >
            <img src="icons/menu_open.svg" alt="Menu icon" />
        </div>
    </div>
</div>

<style>
    .header-container {
        position: fixed;
        z-index: 100;
        width: 100vw;
    }

    .header {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: var(--sp-lg);
    }

    .header > div {
        display: flex;
        align-items: center;
    }
</style>
