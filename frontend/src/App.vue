<template>
  <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-container>
        <b-navbar-brand :to="{ name: 'listJuego'}">
            <img class="info__steam"  src="@/assets/logoo.png">
        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav v-if="userLogged">
              <b-nav-item :to="{ name: 'createJuego'}" v-show="userLogged.is_staff"> create </b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
                  <div class="d-flex flex-column " style="position:relative;">
                    <b-input size="sm" class="mr-sm-2" placeholder="Search" v-model="kword" ></b-input>
                    <b-list-group style="position:absolute; right:20px; top:30px; z-index:1000" v-if="kword.length > 0">
                      <b-list-group-item 
                      :to="{ name:'detailJuego' , params:{ juegoId: juego.id}}"
                      v-for="juego in buscarjuego"
                      :key="juego.id"
                      >
                      {{ juego.name }}
                      </b-list-group-item>
                    </b-list-group>
                  </div>
                  <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>
            <b-nav-item-dropdown right v-if="userLogged"> 
                <template #button-content>
                  <em>{{userLogged.name}}</em>
                </template>
                <b-dropdown-item href="#">Profile</b-dropdown-item>
                <b-dropdown-item href="#" v-on:click="closeCookie()">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
            <b-nav pills v-show="!userLogged" class="ml-3">
              <b-nav-item active :to="{ name: 'login'}">Log In</b-nav-item>
              <b-nav-item active :to="{ name: 'register'}" class="mx-3">Check In</b-nav-item>
            </b-nav>
          </b-navbar-nav>
        </b-collapse>
      </b-container>
      </b-navbar>
    <router-view/>
  </div>

</template>

<script>
import axios from 'axios'
import Cookies from "js-cookie";
import auth from "@/logic/auth";
export default {
  name: 'App',
  data() {
    return {
      kword:'',
      buscarjuego: [],
    };
  },
  watch: {
    kword: function(val){
      this.BuscarJuegos(val);
    }
  },
  methods:{
    BuscarJuegos(kword){
      const path = 'http://localhost:8000/api/juego/search/?kword=' + kword
      axios.get(path)
      .then((response) => {
        this.buscarjuego = response.data
        console.log(this.buscarjuego)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    closeCookie(){
        Cookies.remove('userLogged');
        this.$router.push('/login');
    }
  },
  computed: { //con las computed podemos crear una variable para utilizarela
      userLogged() {
          return auth.getUserLogged();
          
      },
     
      
  },
  
}
</script>

<style>
#app {
  
  margin: 0;
  padding: 0;
}
</style>
