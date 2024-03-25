<template>
    <router-link type="button" class="btn btn-sm btn-outline-secondary" to="/Warhammer">Warhammer</router-link>
    <div class="container-xxl text-dark text-center">
        <h1>Personnages</h1>
        <p>"campagne_actuelle_nom": {{ player.campagne_actuelle_nom }}</p>
        <p>"nom": {{ player.nom }}</p>
        <p>"race": {{ player.race }}</p>
        <p>"sexe": {{ player.sexe}}</p>
        <p>"vocation": {{ player.vocation }}</p>
        <p>"alignement": {{ player.alignement}}</p>
        <p>age": {{ player.age }}</p>
        <p>"taille": {{ player.taille }}</p>
        <p>"poids": {{ player.poids }}</p>
        <p>"cheveux": {{ player.cheveux }}</p>
        <p>"yeux": {{ player.yeux }}</p>
        <p>"photo_personnage": {{ player.photo_personnage }}</p>
        <p>"point_destin": {{ player.point_destin }}</p>
        <p>"debouches": {{ player.debouches}}</p>
        <p>"point_folie": {{ player.point_folie }}</p>
        <p>"langue": {{ player.langue}}</p>
        <p>"note": {{ player.note }}</p>
        <p>"mort_tuer": {{ player.mort_tue }}</p>
        <p>"date_creation": {{ player.date_creation }}</p>
        <p>"date_update": {{ player.date_update }}</p>
        <p>"joueur": {{ player.joueur }}</p>
        <p>"campagne": {{ player.campagne }}</p>
    </div>
    <div class="container-xxl text-dark text-center">
        <h1>Caracteristiques de Base</h1>
        <div v-for="caracteristique in caracteristiquesBase" :key="caracteristique.id">
            <p>"mouvement": {{ caracteristique.personnage_actuelle_nom }}</p>
            <p>"mouvement": {{ caracteristique.mouvement }}</p>
            <p>"capacite_combat": {{ caracteristique.capacite_combat }}</p>
            <p>"capacité_tir": {{ caracteristique.capacité_tir }}</p>
            <p>"force": {{ caracteristique.force }}</p>
            <p>"endurance": {{ caracteristique.endurance }}</p>
            <p>"point_blessure": {{ caracteristique.point_blessure }}</p>
            <p>"initiative": {{ caracteristique.initiative }}</p>
            <p>"nb_attaque": {{ caracteristique.nb_attaque }}</p>
            <p>"dexterite": {{ caracteristique.dexterite }}</p>
            <p>"commandement": {{ caracteristique.commandement }}</p>
            <p>"intelligence": {{ caracteristique.intelligence }}</p>
            <p>"calme": {{ caracteristique.calme }}</p>
            <p>"force_mentale": {{ caracteristique.force_mentale }}</p>
            <p>"sociabilite": {{ caracteristique.sociabilite }}</p>
        </div>
    </div>
    <div class="container-xxl text-dark text-center">
        <h1>Caracteristiques de Actuelle</h1>
        <div v-for="caracteristique in caracteristiquesActuelle" :key="caracteristique.id">
            <p>"mouvement": {{ caracteristique.personnage_actuelle_nom }}</p>
            <p>"mouvement": {{ caracteristique.mouvement }}</p>
            <p>"capacite_combat": {{ caracteristique.capacite_combat }}</p>
            <p>"capacité_tir": {{ caracteristique.capacité_tir }}</p>
            <p>"force": {{ caracteristique.force }}</p>
            <p>"endurance": {{ caracteristique.endurance }}</p>
            <p>"point_blessure": {{ caracteristique.point_blessure }}</p>
            <p>"initiative": {{ caracteristique.initiative }}</p>
            <p>"nb_attaque": {{ caracteristique.nb_attaque }}</p>
            <p>"dexterite": {{ caracteristique.dexterite }}</p>
            <p>"commandement": {{ caracteristique.commandement }}</p>
            <p>"intelligence": {{ caracteristique.intelligence }}</p>
            <p>"calme": {{ caracteristique.calme }}</p>
            <p>"force_mentale": {{ caracteristique.force_mentale }}</p>
            <p>"sociabilite": {{ caracteristique.sociabilite }}</p>
        </div>
    </div>
</template>

<script>
import api from '@/axiosConfig';

export default {
    name: 'WarhammerPlayer',
    data() {
        return {
            player: '',
            caracteristiquesBase: [],
            caracteristiquesActuelle: [],
        };
    },
    methods: {
        getWarhammerPlayer() {
            const playerId = this.$route.params.id;
            const path = `/warhammer/WarhammerPlayerViewSet/${playerId}/`;
            api.get(path)
            .then((res) => {
                this.player = res.data;
                console.log(this.player)
                this.getWarhammerPlayerCaracteristiqueBase(playerId);
                this.getWarhammerPlayerCaracteristiqueActuelle(playerId);
            })
            .catch((error) => {
                console.error(error);
            });
        },
        getWarhammerPlayerCaracteristiqueBase(playerId) {
            const path = `/warhammer/WarhammerCaracteristiqueBaseViewSet/`;
            const params = {
                player: playerId
            };
            console.log(playerId)
            api.get(path, { params })
            .then((res) => {
                this.caracteristiquesBase = res.data.results;
                console.log(this.caracteristiquesBase)
            })
            .catch((error) => {
                console.error(error);
            });

        },
        getWarhammerPlayerCaracteristiqueActuelle(playerId) {
            const path = `/warhammer/WarhammerCaracteristiqueActuelleViewSet/`;
            const params = {
                player: playerId
            };
            console.log(playerId)
            api.get(path, { params })
            .then((res) => {
                this.caracteristiquesActuelle = res.data.results;
                console.log(this.caracteristiquesActuelle)
            })
            .catch((error) => {
                console.error(error);
            });

        },
        
    },
    created() {
        this.getWarhammerPlayer()

    }
}
</script>