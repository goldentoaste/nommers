<script>
  // @ts-nocheck
  import LogoCloud from "./LogoCloud.svelte";
  import Detail from "./Detail.svelte";
  import Footer from "./Footer.svelte";
  import TeammateCard from "./TeammateCard.svelte";
  import Nav from "./Nav.svelte";
  import Banner from "../Banner.svelte";
  import Sidebar from "./Sidebar.svelte";
  import HeaderImg from "../HeaderImg.svelte";

  let useSideBar = false;

  let innerWidth = 0;
  let innerHeight = 0;

  const what_is_nommers_details = {
    detail_1: {
      img_link: "food_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text:
        "Nommers helps you find the best restaurants for your party. Simply create a lobby by filtering through restaurants based on location, dietary restrictions, and preferences.",
    },
    detail_2: {
      img_link: "food_2.png",
      heading_text:
        "A fun and easy way to decide where you want to eat with friends",
      paragraph_text:
        "After a lobby is created, invite your friends and cast your votes on the restaurants matching the search conditions.",
    },
    detail_3: {
      img_link: "food_3.png",
      heading_text:
        "Eating is better when you're with friends. But where do we want to go?",
      paragraph_text:
        "After the voting period ends, the lobby will be presented with a list of where everyone wants to eat!",
    },
  };

  const who_is_nommers_for_details = {
    detail_1: {
      img_link: "food_4.png",
      heading_text:
        "For friends and family celebrating a special occassion or a night out",
      paragraph_text:
        "Nommers lightens the load of decision making so you can focus on what really matters, whether it's enjoying the company of loved ones or celebrating a special day!",
    },
    detail_2: {
      img_link: "food_5.png",
      heading_text: "For individuals with dietary restrictions",
      paragraph_text:
        "Everyone deserves a spot at the table and a comfortable eating experience. Nommers helps craft a good eating experience for everyone!",
    },
    detail_3: {
      img_link: "food_6.png",
      heading_text: "For indecisive and picky eaters (like yours truly)",
      paragraph_text:
        "Perfect for when you don't know what you want to eat, but you know what you don't want to eat.",
    },
  };

  const teammates_info = {
    christina: {
      img_link: "placeholder/placeholder_1.png",
      name: "Christina Raganit",
      title: "Product Designer",
      description:
        "A second-year student at Simon Fraser University's Interactive Arts and Technology program, Christina likes writing fantasy novels, designing user interfacces, and writing frontend code.",
      github_link: "https://github.com/christinaraganit",
      linkedin_link: "https://www.linkedin.com/in/christinaraganit/",
      resume_link:
        "https://drive.google.com/file/d/1u-gDM-HkO_jH4ls1bodWWji_FmmGQtJk/view",
    },
    ray: {
      img_link: "placeholder/placeholder_1.png",
      name: "Ray Gong",
      title: "Software Developer",
      description:
        "An Honours Computing Science student in University of Alberta, Ray likes playing steampunk-style video games and aspires to be a cat owner of a little menace with an ordinary number of paws.",
      github_link: "https://github.com/goldentoaste",
      linkedin_link: "https://www.linkedin.com/in/rui-gong-733a5122a/",
      resume_link:
        "https://drive.google.com/file/d/1V5yd6lJf6rMY46k5U_qBxDcJBcyBnZv5/view?usp=sharing",
    },
  };
</script>

<svelte:window
  bind:innerHeight
  bind:innerWidth
/>

{#if useSideBar}
  <Sidebar bind:open={useSideBar} />
{/if}
<div class="landing-content">
  <Nav bind:useSideBar />

  <div class="hero-content content-div">
    <div class="hero-img">
      <img
        src="/hero-image.png"
        alt="Introducing Nommers"
      />
    </div>
    <div class="hero-text">
      <h1>Never starve from indecision ever again</h1>
      <p class="subtitle">
        Why waste time deciding where to eat? Let Nommers do the work for you
        and your crew. Download now and let the good times (and great food)
        roll!
      </p>

      <a
        href="/signup"
        class="button-text primary-button">Try Nommers today</a
      >
    </div>
  </div>

  <Banner />

  <div class="what-is-nommers-content content-div">
    <p class="overline">Learn more</p>
    <h2>What is Nommers?</h2>
    <p class="body-text">
      Tired of endless group texts trying to decide where to eat with your
      friends? Look no further! Our app makes it easy for you and your friends
      to pick the perfect restaurant.
    </p>

    <div class="detail-div">
      <Detail
        img_link={what_is_nommers_details.detail_1.img_link}
        heading_text={what_is_nommers_details.detail_1.heading_text}
        paragraph_text={what_is_nommers_details.detail_1.paragraph_text}
      />
      <Detail
        img_link={what_is_nommers_details.detail_2.img_link}
        heading_text={what_is_nommers_details.detail_2.heading_text}
        paragraph_text={what_is_nommers_details.detail_2.paragraph_text}
      />
      <Detail
        img_link={what_is_nommers_details.detail_3.img_link}
        heading_text={what_is_nommers_details.detail_3.heading_text}
        paragraph_text={what_is_nommers_details.detail_3.paragraph_text}
      />
    </div>
  </div>

  <HeaderImg />

  <div class="technologies-used-content center-div content-div">
    <p class="overline">Inspired by a certain someone's indecisiveness</p>
    <h2>Built by a certain product designer who is an indecisive eater...</h2>
    <p class="body-text"
      >...and her backend developer best friend who has to put up with her indecisive eating.</p
    >
    <LogoCloud />
  </div>

  <Banner />

  <div class="who-is-nommers-for-content content-div">
    <p class="overline">CAN'T DECIDE?</p>
    <h2>Say yes to more food and less stress with Nommers</h2>
    <p class="body-text">
      Anyone who wants to make restaurant decision with friends or group can use
      this app. It's perfect for friends or family who are planning a night out,
      a special occasion or just a casual meal together. It can be used by
      people of all ages who are looking for an easy and efficient way to decide
      where to eat. It's also useful for people who like to try new restaurants
      and want recommendations based on their location and preferences.
    </p>

    <div class="detail-div">
      <Detail
        img_link={who_is_nommers_for_details.detail_1.img_link}
        heading_text={who_is_nommers_for_details.detail_1.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_1.paragraph_text}
      />
      <Detail
        img_link={who_is_nommers_for_details.detail_2.img_link}
        heading_text={who_is_nommers_for_details.detail_2.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_2.paragraph_text}
      />
      <Detail
        img_link={who_is_nommers_for_details.detail_3.img_link}
        heading_text={who_is_nommers_for_details.detail_3.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_3.paragraph_text}
      />
    </div>
  </div>

  <HeaderImg />

  <div class="meet-the-team-content center-div content-div">
    <p class="overline">Meet the team</p>
    <h2>The brains behind Nommers.</h2>
    <p class="body-text">
      On the weekend of nwHacks 2023, software developer Ray and product
      designer Christina sought a solution to a serious problem that plagues our
      society: the indecision of where to eat.
    </p>

    <div class="teammates-div">
      <TeammateCard
        img_link={teammates_info.ray.img_link}
        name={teammates_info.ray.name}
        title={teammates_info.ray.title}
        description={teammates_info.ray.description}
        github_link={teammates_info.ray.github_link}
        linkedin_link={teammates_info.ray.linkedin_link}
        resume_link={teammates_info.ray.resume_link}
      />

      <TeammateCard
        img_link={teammates_info.christina.img_link}
        name={teammates_info.christina.name}
        title={teammates_info.christina.title}
        description={teammates_info.christina.description}
        github_link={teammates_info.christina.github_link}
        linkedin_link={teammates_info.christina.linkedin_link}
        resume_link={teammates_info.christina.resume_link}
      />
    </div>
  </div>

  <Banner />

  <div class="content-div center-div cta-div">
    <p class="overline">AVAILABLE NOW</p>
    <h2>Hungry for a better way to decide where to eat?</h2>
    <p class="body-text">Nommers has you covered.</p>
    <a
      href="/signup"
      class="primary-button button-text">Try Nommers today</a
    >
  </div>

  <Footer />
</div>

<style>
  /* all content */
  .content-div {
    padding: var(--sp-lg);
  }

  .detail-div {
    margin-top: var(--sp-xl);
    display: flex;
    flex-direction: column;
    gap: var(--sp-lg);
  }

  .center-div {
    text-align: center;
  }

  /* hero section */
  .hero-content {
    padding-top: calc(48px + (var(--sp-lg) * 3));
  }

  .hero-img {
    width: 100%;
  }

  .hero-img > img {
    width: 100%;
  }

  /* tech used */

  /* teammates div */
  .teammates-div {
    display: flex;
    flex-direction: column;
    gap: var(--sp-lg);
  }

  /* cta */
  .cta-div {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  /*DESKTOP STYLING */
  @media only screen and (min-width: 920px) {
    .hero-content {
      display: flex;
      flex-direction: row-reverse;
      gap: var(--sp-3xl);
      align-items: center;
    }
  }

  @media only screen and (min-width: 800px) {
    .detail-div {
      flex-direction: row;
    }
  }

  .teammates-div {
    flex-direction: row;
  }

  .teammates-card {
    width: 50%;
  }

  .content-div {
    padding: var(--sp-4xl) var(--sp-6xl);
  }

  .hero-content {
    padding-top: calc(48px + var(--sp-4xl) * 2);
  }

  .detail-div {
    gap: var(--sp-2xl);
  }
</style>
