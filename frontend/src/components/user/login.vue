<template lang="html">
    <div class="all">
        <div class="conteinerLogin">  
            <div class="login">
                <form class="form" @submit.prevent="loginNormal">          
                    <input class="form__input" type="email" placeholder="Email" v-model.trim="user.email_or_username" required>
                    <input class="form__input" type="password" placeholder="Ingrese la contraseña" v-model.trim="user.password" required>
                    
                    <button class="form__button" type="submit"  value="loginNormal"> Check in </button>
                </form>
                <div class="google"> 
                    <button v-on:click="login()"  type="submit" variant="danger" class="google__button">
                        <img class="google__icon" src="@/assets/google.png">  Registrarse con gmail 
                    </button> 
                </div>              
            </div>        
        </div>  
    </div>
</template>

<script>
// Firebase App (the core Firebase SDK) is always required and must be listed first
import firebase from "firebase/app";
// If you are using v7 or any earlier version of the JS SDK, you should import firebase using namespace import
// import * as firebase from "firebase/app"

// Add the Firebase products that you want to use
import "firebase/auth";
import "firebase/firestore";
import axios from "axios";
import auth from "@/logic/auth";


// Your web app's Firebase configuration
export default {
    name: 'login',
    data (){
        return {
            
            user: {
                email_or_username:'',
                password:''
            },   
        } 
    },
    methods: {
      
        loginNormal(){
            const path = 'http://127.0.0.1:8000/api/login/'
            axios.post(path ,this.user)
                .then((response) => { 
                    this.user.email_or_username = response.data.email;
                    this.user.password =  response.data.password
                    auth.setUserLogged(response.data.user);     
                    this.$router.push('/'); // no recarga la pag  
                    location. reload()
                                    
                })
                .catch((error) => {
                    console.log(error);
                });
            
        },

     
    }
}
</script>

<style scoped>
body{
    margin: 0;
    padding: 0;
}
.all{
    font-size: 18px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
    background-color: rgb(230, 230, 230);
}
.conteinerLogin{
    display: flex;
    width:20em;
    height:30em;
    background-color: rgba(0, 0, 0, 0.5);
    justify-content: center;
    align-items: center;
    border-radius:10px ;
}
.login{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width:17em;
    height:27em;
    
}
.form{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 15em;
    height: 20rem;
    background-color: rgba(0, 0, 0, 0.1);
    border: 1px solid gray;
    border-radius:10px ;
}
.form__input{
    margin: 0.7rem  0;
    width: 90%;
    outline: 0;
    border: 0;
    border-bottom: 1px solid white;
    background-color: transparent;
    color: white;

}
.form__input::placeholder{
    color: white;
    font-size: 16px;
} 
.form__button{
    width: 12em;
    height: 1.8em;
    font-size: 16px;
    border: 0;
    margin-top: 3px;
    background-color: #44B78B;
    border-radius: 5px;
}  

.google{
    display: flex;
    width: 14em;
    height: 6em;
    align-items: flex-end;
}
.google__button{
    width: 100%;
    height: 2.3em;
    border-radius:5px;
    background-color: white;
    border: 1px solid rgb(190, 190, 190);
}
.google__icon{
    height: 25px;
    width: 25px;
}

.errors{
    list-style: none;
    background-color: red;
    border-radius:10px;
    width: 15.4em;
    height: 1.5em;
    font-size: 14px;
    margin: 0;
    text-align: center;
 
}
.errors__erorr{

    color: white;

}

</style>>
