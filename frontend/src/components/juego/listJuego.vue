<template lang="html">
    <main>
        <section class="containerJuegos">
            <div class="card" v-for="(juego,index) in juegos">
                <router-link :to="{ name:'detailJuego' , params:{ juegoId: juego.id}}" class="image">
                    <img  v-bind:src="juego.image" alt="" >
                </router-link>
                <div class="info">
                    <h4>{{juego.name}} </h4>
                    <div class="info__description"> 
                        <!-- <h4>{{juego.description }} </h4> -->
                    </div>
                    <div class="info__price">
                        <a :href="'' + `${juego.link_url}`" target="_blank">
                            <img class="info__steam"  src="@/assets/steam.png">
                        </a>
                        <router-link 
                        :to="{ name:'EditJuego' , 
                        params:{ juegoId: juego.id}}" 
                        class="info__title" 
                        style="text-decoration:none;" 
                        v-if="userLogged"
                        >
                            <b-button variant="success" v-show="userLogged.is_staff">Modificar</b-button>
                        </router-link>
                        <h3>${{juego.price}} </h3>
                        
                    </div>
                </div>
            </div>
           
        </section>
    </main>
</template>

<script>
import axios from 'axios'
import auth from "@/logic/auth";
export default {
    name: 'listJuego',
    data() {
        return{
            name : '',
            juegos: [],
        }     
    },
     computed: { //con las computed podemos crear una variable para utilizarela
        userLogged() {
            return auth.getUserLogged();
      },
    },
    methods: {
        getJuegos (){
            // const path = 'http://localhost:8000/api/list-juegos'  url normales que permiten el metodo get/abjo un viewset permite todo
            const path = 'http://localhost:8000/juego/'
            axios.get(path).then((response) => {
                this.juegos = response.data  
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created(){
        this.getJuegos()
    }
        
        
} 
</script>

<style >

body{
    margin: 0;
    padding: 0;
    font-size:16px;

}
main{
    display: block;
    width: 100%;
    height: 100vh;
    font-size: 18px;
}
.containerJuegos{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    height: auto;
}
.card{
    display: flex;
    flex-direction: column;
    width: 18em;
    height: 20em;
    border-radius: 10px ;
    margin: 15px 15px;
}
.image{
    display: flex;
    flex: 1 1;
}
.image img{
    width: 100%;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}
.info{
    display: flex;
    flex: 1 1;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    background: #c0c1f5;
    border-radius: 0 0 10px 10px;
}
.info__title{
    display: flex;
    justify-content: center;
    color: black;
    min-height: 36%;
    text-align: center;
    
    
}
.info__title :hover{
    
    color: rgba(7, 7, 7, 0.534);
    
    
}
.info__description{
    display: flex;
    justify-content: center;

    min-height: 40%;
    width: 95%;
    margin: 0 5px;
    font-size: 6px;

}
.info__price{
    margin: 0px 20px;
    display: flex;
    justify-content: space-between;
  
}
.info__steam{
    height: 35px;
    width: 35px;
}
</style>