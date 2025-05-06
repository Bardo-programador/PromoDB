  export async function load({ fetch }) {
	const res = await fetch('http://promodb-api:8000/api/promos');
	const promocoes = await res.json();
	return { promocoes };
}
