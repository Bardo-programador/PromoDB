<script>
    import { onMount } from 'svelte';
	export let name="Samuel";
    let promocoes = []
	onMount(async () => {
	    const response = await fetch ('http://localhost:8000/api/promos');
	    promocoes = await res.json();

	}
</script>

<main>
	<h1>Lista de Promoções!</h1>
	<ul>
	{#each promocoes as promocao}
	<li>{produto.nome}: {produto.preco}</li>
	{/each}
	</ul>
</main>

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