<template>
        <div class="text-center">
            <h1> Bonjour et bienvenue </h1>
        </div>
        <div class="d-inline-flex p-2">
            <div class="card" style="width: 18rem;">
                <img src="/images/base_01.png" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <router-link type="button" class="btn btn-primary" to="/Warhammer">Warhammer</router-link>
                </div>
                <div class="card-footer">
                    <small class="text-body-secondary">Last updated 3 mins ago</small>
                </div>
            </div>
            <div class="card" style="width: 18rem;">
                <img src="/images/cthulhu_defaut_campagne.jpg" class="card-img-top w-75 p-3" alt="...">
                <div class="card-body">
                    <h5 class="card-title">Card title</h5>
                    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
                <div class="card-footer">
                    <small class="text-body-secondary">Last updated 3 mins ago</small>
                </div>
            </div>
        </div>

</template>
<script>

export default{
    name:"Home"
}

</script>

<style scoped>
h1 {
    color: red;
}

</style>