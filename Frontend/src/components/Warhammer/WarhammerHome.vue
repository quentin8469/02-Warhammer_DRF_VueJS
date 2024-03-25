<template>
    <div class="container-xxl text-dark text-center">
        <h1>LISTE DES CAMPAGNES</h1>
    </div>
    <div class="album py-5 bg-body-tertiary">
        <div class="container">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                <div v-for="campagne in campagnesList" :key="campagne.id"  class="col">
                    <div class="card shadow-sm">
                        <img :src="campagne.image_campagne" class="card-img-top" alt="Image de la campagne">
                        <div class="card-body">
                            <h5 class="card-title">{{ campagne.nom_de_campagne }}</h5>
                            <p class="card-text">{{ campagne.maitre_du_jeu_username }}</p>
                            <p class="card-text">{{ campagne.date_creation }}</p>
                            <p class="card-text">{{ campagne.date_debut }}</p>
                            <p class="card-text">{{ campagne.campagne_etat}}</p>
                            <p class="card-text">{{ campagne.date_end}}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <router-link type="button" class="btn btn-sm btn-outline-secondary" to="/Warhammer">Warhammer</router-link>
                                    <router-link type="button" class="btn btn-sm btn-outline-secondary" to="/jdrmanager">Accueil</router-link>
                                </div>
                                <small class="text-body-secondary"> {{ campagne.date_update }}</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="container-xxl text-dark text-center">
        <h1>LISTE DES JOUEURS</h1>
    </div>
    <div class="container">
        <div class="card-group">
            <div v-for="player in playersList" :key="player.id" class="card">
                <div class="image-container center">
                    <img :src="player.photo_personnage" class="card-img-top player-image" alt="Image du personnage">
                </div>
                <div class="card-body">
                    <h5 class="card-title">{{ player.nom }}</h5>
                    <p class="card-text">{{ player.race }}</p>
                    <p class="card-text">{{ player.sexe }}</p>
                    <p class="card-text">{{ player.vocation}}</p>
                    <p class="card-text">{{ player.campagne_actuelle_nom}}</p>
                    <p class="card-text">{{ player.date_creation}}</p>
                    <router-link type="button" class="btn btn-primary" :to="'/Warhammer/WarhammerPlayerViewSet/' + player.id + '/'">Personnage</router-link>
                </div>
                <div class="card-footer">
                    <small class="text-body-secondary">Last updated {{ player.date_update }}</small> 
                </div>
            </div>
        </div>
    </div>
    <div class="album py-5 bg-body-tertiary">
        <div class="container">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                <div v-for="player in playersList" :key="player.id" class="col">
                    <div class="card shadow-sm">
                        <div class="image-container">
                            <img :src="player.photo_personnage" class="card-img-top player-image" alt="Image du personnage">
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{{ player.nom }}</h5>
                            <p class="card-text">{{ player.race }}</p>
                            <p class="card-text">{{ player.sexe }}</p>
                            <p class="card-text">{{ player.vocation}}</p>
                            <p class="card-text">{{ player.campagne_actuelle_nom}}</p>
                            <p class="card-text">{{ player.date_creation}}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <router-link type="button" class="btn btn-sm btn-outline-secondary" to="/Warhammer">Warhammer</router-link>
                                    <router-link type="button" class="btn btn-sm btn-outline-secondary" to="/jdrmanager">Accueil</router-link>
                                </div>
                                <small class="text-body-secondary">Last updated {{ player.date_update }}</small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import api from '@/axiosConfig';

export default {
    name: 'WarhammerHome',
    data() {
        return {
            campagnesList: '',
            playersList: '',
        };
    },
    methods: {
        getCampagnesList() {
            const path = '/warhammer/WarhammerCampagneViewSet/';
            api.get(path)
                .then((res) => {
                    this.campagnesList = res.data.results;
                    console.log(this.campagnesList)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        getPlayersList() {
            const path = '/warhammer/WarhammerPlayerViewSet/';
            api.get(path)
            .then((res) => {
                this.playersList = res.data.results;
                console.log(this.playersList)
            })
            .catch((error) => {
                console.error(error);
            });

        }
    },
    created() {
        this.getCampagnesList();
        this.getPlayersList()
    }
    
}
</script>
<style scoped>
.image-container {
    width: 200px; /* Largeur souhaitée */
    height: 200px; /* Hauteur souhaitée */
    overflow: hidden; /* Cache toute partie de l'image dépassant de la zone définie */
}

.player-image {
    width: 100%; /* Permet à l'image de remplir complètement le conteneur */
    height: 100%; /* Permet à l'image de remplir complètement le conteneur */
    object-fit: cover; /* Ajuste la taille de l'image sans déformer */
}


</style>