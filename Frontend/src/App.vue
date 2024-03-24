<template>
  <!-- navbar -->
  <nav>
    <div class="container-fluid p-3 bg-dark text-white">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
            <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li><router-link type="button" class="btn btn-primary" to="/jdrmanager">Accueil</router-link></li>
                <li><a href="#" class="nav-link px-2 text-secondary">Mon Profil</a></li>
                <li><a href="#" class="nav-link px-2 text-white">Création de personnage</a></li>
                <li><a href="#" class="nav-link px-2 text-white">Création de campagne</a></li>
            </ul>
            <div class="text-end">
                <a class="btn btn-warning" aria-current="page" href="#">Se déconnecter</a>
                <a class="btn btn-outline-light me-2" aria-current="page" href="#">Se connecter</a>
                <a class="btn btn-outline-light me-2" aria-current="page" href="#">S'inscrire</a>
            </div>
        </div>
    </div>
  </nav>
  <!-- END Header navbar -->
  <RouterView />

  
</template>


<script>
import { RouterView } from "vue-router";

export default {
  name: "App",


}
</script>



<style>

</style>
