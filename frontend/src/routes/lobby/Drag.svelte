<script>
    import { spring } from 'svelte/motion';
    import { fly, fade } from 'svelte/transition';
    let restaurantImg = 'placeholder/placeholder.png';
    import { createEventDispatcher } from 'svelte';

    export let imageToken;

    let dispatch = createEventDispatcher();
    const xSize = 400;
    const ySize = 400;

    const xMax = 132;
    const tMax = 10;

    let targets = { x: 0, y: 0, rot: 0 };
    let coords = spring(
        { x: 0, y: 0, rot: 0 },
        {
            stiffness: 0.1,
            damping: 0.7,
        }
    );
    let dragging = false;
    let sign;
    $: sign = $coords.rot > 0 ? 1 : -1;
    $: console.log(sign);

    const drag = (e) => {
        if (e.buttons !== 1 || !dragging) {
            return;
        }
        let x = targets.x + e.movementX;
        let y = targets.y + e.movementY;
        targets = { x: clamp(x, -xMax, xMax), y: y, rot: targets.rot };

        let signX = Math.sign(x);
        let signY = Math.sign(y);

        let magX = Math.min(xMax, Math.max(0, Math.abs(x))) / xMax;

        let ex = signX * ease(magX) * xMax;
        let er = signX * magX * tMax;
        let ey = 0.1 * y;

        let rotated = rotAround(ex + xSize / 2, ey + ySize / 2, ex + xSize / 2, ey + ySize, er);

        coords.set({ x: rotated.x - xSize / 2, y: rotated.y - ySize / 2, rot: er });
    };

    const clamp = (val, min, max) => {
        return Math.max(min, Math.min(max, val));
    };
    const ease = (x) => {
        return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
    };

    const rotAround = (vx, vy, px, py, angle) => {
        let r = d2r(angle);

        let x = vx - px;
        let y = vy - py;

        let cos = Math.cos(r);
        let sin = Math.sin(r);

        return {
            x: px + (x * cos - y * sin),
            y: py + (x * sin + y * cos),
        };
    };

    const d2r = (d) => {
        return d * (Math.PI / 180);
    };

    const getimage = async () => {
       alert(imageToken)
        let res = await fetch(
            `https://maps.googleapis.com/maps/api/place/photo?key=AIzaSyBL_LkbEw80SHtaRjlV3t3KyPqJv_lsgtQ&photo_reference=${imageToken}&maxheight=400&maxwidth=400`
        )
        let blob = await res.blob()

        return  await URL.createObjectURL(blob);
    };
</script>

<div class="container-container">
    <div
        in:fly={{
            y: -30,
            duration: 500,
        }}
        out:fade={{ duration: 500 }}
        id="container"
        style="transform: translate({$coords.x + 0}px,{$coords.y + 0}px) rotate({$coords.rot}deg) ;"
        on:mousedown={() => {
            dragging = true;
        }}
        on:mouseup={() => {
            dragging = false;
        }}
    >
        <div
            style="clip-path: path('
        M0, 15
        q0,-15,15,-15
        h370
        q15,0,15, 15
        v400
        h-400
        z
        ')"
        >
            <div
                style="transform: translate({170 * sign}px , {10 * sign}px)  rotate({-$coords.rot}deg) translate({-170 *
                    sign}px , {-10 * sign}px);"
            >
                {#if Math.abs($coords.rot) > 5}
                    <div
                        id="label"
                        style=" justify-content: {$coords.rot > 0 ? 'end' : 'start'};"
                        transition:fly={{ y: -50, duration: 300 }}
                    >
                        <!--top label-->
                        <p>stuff</p>
                    </div>
                {/if}
            </div>
            <img src={`https://maps.googleapis.com/maps/api/place/photo?key=AIzaSyBL_LkbEw80SHtaRjlV3t3KyPqJv_lsgtQ&photo_reference=${imageToken}&maxheight=400&maxwidth=400`}/>
            <!-- {#await getimage}
            <p>...waiting</p>
        {:then data}
            <img class="container-img" src={data} alt="image" />
        {:catch error}
            <p>An error occurred!</p>
        {/await} -->
        </div>

        <slot></slot>
    </div>
</div>

<svelte:window
    on:mousemove={drag}
    on:mouseup={() => {
        targets.x = 0;
        targets.y = 0;
        coords.set(targets);
        console.log(targets);

        if ($coords.rot > 5) {
            dispatch(
                "yes"
            );
        }
        else if ($coords.rot < -5){
            dispatch(
                "no"
            )
        }
    }}
/>

<style>
    #label > p {
        padding-left: 130px;
        padding-right: 130px;
        padding-bottom: 10px;
        align-self: flex-end;
    }

    #label {
        background: #aaaaaaaa;
        position: absolute;
        width: 900px;
        height: 150px;
        top: -70px;
        left: -100px;
        display: flex;
    }

    #container {
        user-select: none;
        cursor: move;
        border: 1px black solid;
        width: 400px;
        height: 400px;
        border-radius: 15px;
    }

    .container-container {
        display: flex;
        width: 100vw;
        justify-content: space-evenly;
        align-items: baseline;
    }

    img {
        width: calc(100%);
        height: auto;
        pointer-events: none;
        user-select: none;
    }
</style>
