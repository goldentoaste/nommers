<script>
  // @ts-nocheck
  import LogoCloud from "./LogoCloud.svelte";
  import Detail from "./Detail.svelte";
  import Footer from "./Footer.svelte";
  import TeammateCard from "./TeammateCard.svelte";
  import Nav from "./Nav.svelte";

  let open = false;

  const what_is_nommers_details = {
    detail_1: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
    },
    detail_2: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
    },
    detail_3: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
    },
  };

  const who_is_nommers_for_details = {
    detail_1: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
    },
    detail_2: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
    },
    detail_3: {
      img_link: "placeholder/placeholder_1.png",
      heading_text: "Save time and enjoy more of your night out",
      paragraph_text: "Phasellus mattis euismod dolor, in ultricies metus.",
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
      resume_link: "",
    },
  };
</script>

<div class="landing-content">
  <Nav />

  <div class="hero-content content-div">
    <div class="hero-img" />
    <div class="hero-text">
      <h1>Never starve from indecision ever again</h1>
      <p class="subtitle"
        >Why waste time deciding where to eat? Let Nommers do the work for you
        and your crew. Download now and let the good times (and great food)
        roll!</p
      >
    </div>
    <a
      href="/app"
      class="button-text primary-button">Try Nommers today</a
    >
  </div>

  <div class="landing-header" />

  <div class="what-is-nommers-content content-div">
    <p class="overline">Learn more</p>
    <h2>What is Nommers?</h2>
    <p class="body-text"
      >Tired of endless group texts trying to decide where to eat with your
      friends? Look no further! Our app makes it easy for you and your friends
      to pick the perfect restaurant.</p
    >

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

  <div class="technologies-used-content center-div content-div">
    <p class="overline">Technologies used</p>
    <h2>Built by an indecisive eater...</h2>
    <p class="body-text"
      >...and the friend who has to put up with her indecisive eating.</p
    >
    <LogoCloud />
  </div>

  <div class="who-is-nommers-for-content content-div">
    <p class="overline">CAN'T DECIDE?</p>
    <h2>Made for indecisive foodies, by indecisive foodies</h2>
    <p class="body-text"
      >Tired of endless group texts trying to decide where to eat with your
      friends? Look no further! Our app makes it easy for you and your friends
      to pick the perfect restaurant.</p
    >

    <div class="detail-div">
      <Detail
        img_link={who_is_nommers_for_details.detail_1.img_link}
        heading_text={who_is_nommers_for_details.detail_1.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_1.paragraph_text}
      />
      <Detail
        img_link={who_is_nommers_for_details.detail_2.img_link}
        heading_text={who_is_nommers_for_details.detail_1.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_1.paragraph_text}
      />
      <Detail
        img_link={who_is_nommers_for_details.detail_3.img_link}
        heading_text={who_is_nommers_for_details.detail_1.heading_text}
        paragraph_text={who_is_nommers_for_details.detail_1.paragraph_text}
      />
    </div>
  </div>

  <div class="meet-the-team-content center-div content-div">
    <p class="overline">Meet the team</p>
    <h2>The brains behind Nommers.</h2>
    <p class="body-text"
      >On the weekend of nwHacks 2023, software developer Ray and product
      designer Christina sought a solution to a serious problem that plagues our
      society: the indecision of where to eat.</p
    >

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

  <div class="content-div center-div cta-div">
    <p class="overline">AVAILABLE NOW</p>
    <h3>Hungry for a better way to decide where to eat?</h3>
    <p class="body-text">Nommers has you covered.</p>
    <a
      href=""
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
</style>
