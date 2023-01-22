
<script>

  
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
      />

      <input
        type="password"
        placeholder="Password"
      />
    </div>

    <div class="login-actions">
      <div
        class="body-title primary-action"
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
