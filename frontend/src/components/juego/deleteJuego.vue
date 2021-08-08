<template lang="html">
    <div  class="container">
        <div class="row">
            <div class="col">
                <h2> ¿Estas seguro que deseas eliminar el Juego?</h2> 
                <p>Titulo : {{ element.name }} </p>
            </div>
        </div>
        <div class="row">
            <div class="col">
                <b-button v-on:click="deleteBook"  variant="danger">Si,Borrar</b-button> 
                <b-button class="sm" variant="primary" :to="{ name: 'listJuego'}">
                        No,Volver
                </b-button> 
                </div> 
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import swal from 'sweetalert'
    export default {   
        data() {
            return {
                juegoId: this.$route.params.juegoId,
                element:{
                    name: '',
                }
            }
            
        },
        methods: {
            getJuego (){
                const path = `http://localhost:8000/api/juego/delete/${this.juegoId}`
                axios.get(path).then((response) => {
                    this.element.name = response.data.name
                })
                .catch((error) => {
                    console.log(error)
                })
            },
            deleteBook () {
                // const path = `http://localhost:8000/api/juego/delete/${this.juegoId}`
                const path = `http://localhost:8000/juego/${this.juegoId}`; 
                axios.delete(path).then((response) => {
                    location.href = '/'
                })
                .catch((error) => {
                    console.log(error)
                    swal("No es posible Eliminar el libro", "", "error")
                })
            }, 
        },
        created(){
            this.getJuego()
            
        }
        
        
    } 
</script>
<style lang="css" scoped>

</style>
