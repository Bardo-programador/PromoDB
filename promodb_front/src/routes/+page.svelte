<script>
  export let data;
</script>

<h1>Promoções</h1>
<ul>
  {#each data.promocoes as promo}
    <li>{promo.nome}: {promo.preco}</li>
  {/each}
</ul>


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