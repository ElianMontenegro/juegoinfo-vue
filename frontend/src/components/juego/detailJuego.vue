<template lang="html">
    <div class="containerPlay"  :style="{ backgroundImage: `url(${juego.backimage})` }">
        <div class="juegoDifuninado">
            <div class="juego">
                <div class="juegoInfo">
                    <div class="juegoInfo__name">
                    <h2>{{ juego.name}} </h2>
                    
                    </div>
                    <div class="juegoInfo__link">
                            <h4 class="precio">ARS${{ juego.price}} </h4>
                            <a class="boton" :href="'' + `${juego.link_url}`" target="_blank" >Adquirir!</a>
                    </div>
                </div>
                <div class="imageDescrip">
                    <img class="imageDescrip__image" v-bind:src="juego.image" alt="">
                    <p class="imageDescrip__description"> {{ juego.description }}</p>
                </div>
            </div>
        </div>    
    </div>
</template>


<script>
import axios from "axios";
export default {
    data() {
        return {
        juegoId: this.$route.params.juegoId,
        juego: {},
        };
    },
    watch: {  
        '$route'(to){
            this.juegoId = to.params.juegoId
            this.getjuego();
        }
    },
    methods: {
        getjuego() {
            const path = `http://localhost:8000/api/juego/${this.juegoId}`;
            axios.get(path)
                .then((response) => {
                    this.juego = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
    },
    mounted() {
        this.getjuego();
    },
   
    
};
</script>
<style lang="css" scoped>
.containerPlay{
    width: 100%;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    
}
.juegoDifuninado{
    width: 100%;
    height:100%;
    display: flex;
    align-items: center;
    justify-content: center;
    -webkit-backdrop-filter: blur(6px); /* Safari 9+ */
    backdrop-filter: blur(6px); /* Chrome and Opera */
    background-color: rgba(255, 255, 255, 0.5);
}
.juego{
    width: 50%;
    height:30em;
    display: flex;
    border-radius: 10px;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.6);
    color: white;
}
.imageDescrip{
    width: 30em;
    height: 100%;
    border-radius: 0px 10px 10px 0px ;
    display: flex;
    flex-direction: column;
}
.imageDescrip__image{
    flex: 1;
    width: 100%;
    height: 100%;
    object-fit: fill;
    border-radius: 0 10px 0 0;

}

.imageDescrip__description{
    flex: 1;
    width: 100%;
    height: 100%;
    font-size: 1.2em;
    box-sizing: border-box;
    padding: 10px;
    display: flex;
    align-items: center;

}
.juegoInfo{
    width: 30em;
    height: 60%;
    display: flex;
    flex-direction: column;
    text-align: center;
    
}
.juegoInfo__name{
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}
.juegoInfo__link{
    flex: 1;
    display: flex;
    align-items: flex-end;
    justify-content: flex-end;
    padding: 0 20px;
    box-sizing: border-box;
    
}
.precio{
    margin: 2px 6px;
}
.boton{
    background: #6fa720;
    width: 5em;
    height: 2em;
    font-family: "Motiva Sans", Sans-serif;
    border: 0;
    outline: none;
    border-radius: 10px;
    text-decoration: none;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    color: black;
    font-size: 16px;
    font-style: bold;
    font-weight: 500;
}

</style>
