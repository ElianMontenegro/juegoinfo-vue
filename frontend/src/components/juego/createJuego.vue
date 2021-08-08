<template lang="html">
    <main >
        <section class="container d-flex justify-content-center p-lg-5 mt-5">
                <form @submit="onSubmit" class="col-lg-6 bg-dark p-4 d-flex flex-column rounded-lg "> 
                    <div class="form-group row my-3">
                        <div class="col-sm-12">
                            <input type="text"  placeholder="Name" name="Name" class="form-control" v-model.trim="form.name">
                        </div>
                    </div>
                    <div class="form-group row my-3">
            
                        <div class="col-sm-12">
                            <textarea name="description" class="form-control"  placeholder="Descripcion" rows="3" v-model.trim="form.description"></textarea>
                        </div>
                    </div>
                    <div class="form-group row my-3">
              
                        <div class="col-sm-12">
                            <input type="number"  placeholder="price" name="price" class="form-control" step="any" v-model.trim="form.price">
                        </div>
                    </div>
                    <div class="form-group row my-3">
      
                        <div class="col-sm-12">
                            <input type="text" placeholder="image" name="image" class="form-control " v-model.trim="form.image">
                            
                        </div>
                    </div>
                    <div class="form-group row my-3">
                      
                        <div class="col-sm-12">
                            <input type="text"  placeholder="URL steam" name="link_url" class="form-control" v-model.trim="form.link_url">
                        </div>
                    </div>
                    <div class="form-group row my-3">
                      
                        <div class="col-sm-12">
                            <input type="text"  placeholder="URL background" name="backimage" class="form-control" v-model.trim="form.backimage">
                        </div>
                    </div>
                    <div class="rows my-3">
                        <div class="col-sm-5 text-left">
                            <b-button block  type="submit" variant="primary">  Crear  </b-button> 
                        </div> 
                    </div> 
                </form> 
        </section>
    </main>

</template>

<script>
import swal from 'sweetalert';
import axios from "axios";
export default {
  name: "listJuego",
  data() {
    return {
      form: {
        name: "",
        description: "",
        price: "",
        image: "",
        link_url: "",
        backimage:"",
      },
    };
  },
  methods: {
    onSubmit(evt){
        evt.preventDefault()
        const path = 'http://localhost:8000/juego/';

        axios.post(path, this.form).then((response) => {
            this.form.name = response.data.name;
            this.form.description = response.data.description;
            this.form.price = response.data.price;
            this.form.image = response.data.image;
            this.form.link_url = response.data.link_url;
            this.form.backimage = response.data.backimage;
            console.log(response)
            swal("Juego Creado exitosamente", {
                content: "button",
            })
            .then((value) => {  
                //window.location.replace("http://localhost:8080/books");
                this.$router.push('/'); // no recarga la pag
            });
        })
        .catch((error) => {
            console.log(error);
        });
    },
  },
  created() {
  
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0;
  font-size: 16px;
}
main {
  display: block;
  width: 100%;
  height: 100vh;
  font-size: 18px;
}
