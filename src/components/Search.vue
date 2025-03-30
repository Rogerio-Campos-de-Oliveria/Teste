<template>
    <div>
        <input v-model="query" @input="search" placeholder="Buscar operadora..." />
        <ul v-if="results.length">
            <li v-for="(item, index) in results" :key="index">
                {{ item.nome }} - {{ item.telefone }} <!-- Substitua com os campos corretos do seu CSV -->
            </li>
        </ul>
        <p v-else>Nenhum resultado encontrado.</p>
    </div>
</template>

<script>
export default {
    data() {
        return {
            query: '',
            results: []
        };
    },
    methods: {
        async search() {
            if (this.query.length > 2) {
                const response = await fetch(`http://localhost:5000/search?query=${this.query}`);
                const data = await response.json();
                this.results = data;
            } else {
                this.results = [];
            }
        }
    }
};
</script>

<style scoped>
/* Adicione o estilo conforme necessário */
</style>