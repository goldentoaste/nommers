
<script>
  import { accountId } from "../../account";
  let username = "";
  let password= "";

  const signup = ()=>{

    if (username.length == 0 || password.length == 0){
      return;
    }

    fetch('http://server3-env.eba-7jgvjkan.us-west-2.elasticbeanstalk.com/signup/',
    {
      method: 'POST',
      headers:{
        'Accept':'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(
        {
          'username':username,
          'password':password,
          'ppiurl':""
        }
      )
    }).then((res)=>{
      return res.json()
    }).then(
      (res)=>{
        $accountId = res["id"]
        console.log($accountId)
      }
    )

  }
</script>

<div class="login">
  <div class="login-fields">
    <div class="login-text">
      <p class="overline">SIGN UP</p>
      <h3>Take the hassle out of deciding where to eat</h3>
      <p class="body-text">Create a Nommers account today!</p>
    </div>

    <div class="login-inputs">
      <input
        type="text"
        placeholder="Username"
        bind:value={username}
      />

      <input
        type="password"
        placeholder="Password"
        bind:value={password}
      />
    </div>

    <div class="login-actions">
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <div
        class="body-title primary-action"
        on:click={signup}
       >Create account</div
      >
      <a
        class="body-title secondary-action"
        href="/login">Log in</a
      >
    </div>
  </div>
</div>

<style>
  .login {
    height: 100vh;
    max-height: 100vh;
    display: flex;
    align-items: flex-end;
  }

  .login-fields,
  .login-inputs,
  .login-actions {
    display: flex;
    flex-direction: column;
  }

  .login-fields {
    height: fit-content;
    background-color: white;
    border-radius: var(--sp-md);
    justify-content: space-between;
    padding: var(--sp-lg);
  }

  .login-inputs {
    gap: var(--sp-md);
    margin-bottom: var(--sp-xl);
  }

  .login-text {
    margin-bottom: var(--sp-sm);
  }

  .login-actions {
    gap: var(--sp-xs);
  }

  .primary-action,
  .secondary-action {
    width: 100%;
    padding: var(--sp-md) 0;
    border-radius: var(--sp-2xl);
    text-align: center;
    text-decoration: none;
  }

  .primary-action {
    background-color: var(--secondary-500);
    color: white;
  }

  .secondary-action {
    color: var(--secondary-500);
  }
</style>
