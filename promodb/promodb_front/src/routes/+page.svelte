<script>
  export let data;
  import Header from './Header.svelte'
  let name = $state("Samuel")
</script>
<Header name={name}/>
<h1>Promoções</h1>
<ul>
  {#each data.promocoes as promo}
    <li>{promo.nome}: {promo.preco}</li>
  {/each}
</ul>
<input type="text" bind:value={name}>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>