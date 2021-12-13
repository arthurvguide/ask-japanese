// Script for the MENU functionality

// First step collect all elements from the menu

// Getting sushi and sashimi elements
const sushiSashimi = document.getElementsByClassName("sushi-sashimi")[0];
const sushiSashimiView = document.getElementsByClassName("sushi-sashimi-view")[0];

// Getting rice and nodles elements
const riceNoodles = document.getElementsByClassName("rice-noodles")[0];
const riceNoodlesView = document.getElementsByClassName("rice-noodles-view")[0];

// Getting drinks elements
const drinks = document.getElementsByClassName("drinks")[0];
const drinksView = document.getElementsByClassName("drinks-view")[0];

// Getting desserts elements
const desserts = document.getElementsByClassName("desserts")[0];
const dessertsView = document.getElementsByClassName("desserts-view")[0]

// Getting salads elements
const sides = document.getElementsByClassName("sides")[0];
const sidesView = document.getElementsByClassName("sides-view")[0];

/* Second step create events listener
once one menu class is selected, all the others will be undisplayed */

// If salads is selected
sides.addEventListener("click", () => {
    if (sidesView.classList.contains("d-flex") == false){
        sidesView.classList.add("d-flex");
    };

    let allViews = [dessertsView, sushiSashimiView, riceNoodlesView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-flex")){
            value.classList.remove("d-flex");
            value.classList.add("d-none");
        } 
      }
})

// If sushiSashimi is selected
sushiSashimi.addEventListener("click", () => {
    if (sushiSashimiView.classList.contains("d-flex") == false){
        sushiSashimiView.classList.add("d-flex");
    };

    let allViews = [dessertsView, sidesView, riceNoodlesView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-flex")){
            value.classList.remove("d-flex");
            value.classList.add("d-none");
        } 
      };
})

// If riceNodles is selected
riceNoodles.addEventListener("click", () => {
    if (riceNoodlesView.classList.contains("d-flex") == false){
        riceNoodlesView.classList.add("d-flex");
    };
    
    let allViews = [dessertsView, sidesView, sushiSashimiView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-flex")){
            value.classList.remove("d-flex");
            value.classList.add("d-none");
        } 
      };
});

// If drinks is selected
drinks.addEventListener("click", () => {
    if (drinksView.classList.contains("d-flex") == false){
        drinksView.classList.add("d-flex");
    };
    
    let allViews = [dessertsView, sidesView, sushiSashimiView, riceNoodlesView];

     for(let value of allViews) {
        if (value.classList.contains("d-flex")){
            value.classList.remove("d-flex");
            value.classList.add("d-none");
        }
      };
});

// If desserts is selected
desserts.addEventListener("click", () => {
    if (dessertsView.classList.contains("d-flex") == false){
        dessertsView.classList.add("d-flex");
    };
    
    let allViews = [sidesView, sushiSashimiView, drinksView, riceNoodlesView];

     for(let value of allViews) {
        if (value.classList.contains("d-flex")){
            value.classList.remove("d-flex");
            value.classList.add("d-none");
        }
      };
});
