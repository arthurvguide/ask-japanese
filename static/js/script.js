// Script for the MENU functionality

// First step collect all elements from the menu

// Getting sushi and sashimi elements
const sushiSashimi = document.getElementsByClassName("sushi-sashimi")[0];
const sushiSashimiView = document.getElementsByClassName("sushi-sashimi-view")[0];

// Getting rice and nodles elements
const riceNodles = document.getElementsByClassName("rice-nodles")[0];
const riceNodlesView = document.getElementsByClassName("rice-nodles-view")[0];

// Getting drinks elements
const drinks = document.getElementsByClassName("drinks")[0];
const drinksView = document.getElementsByClassName("drinks-view")[0];

// Getting desserts elements
const desserts = document.getElementsByClassName("desserts")[0];
const dessertsView = document.getElementsByClassName("desserts-view")[0]

// Getting salads elements
const salads = document.getElementsByClassName("salads")[0];
const saladsView = document.getElementsByClassName("salads-view")[0];

/* Second step create events listener
once one menu class is selected, all the others will be undisplayed */

// If salads is selected
salads.addEventListener("click", () => {
    if (saladsView.classList.contains("d-block") == false){
        saladsView.classList.add("d-block");
    };

    let allViews = [dessertsView, sushiSashimiView, riceNodlesView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-block")){
            value.classList.remove("d-block");
            value.classList.add("d-none");
        } 
      }
})

// If sushiSashimi is selected
sushiSashimi.addEventListener("click", () => {
    if (sushiSashimiView.classList.contains("d-block") == false){
        sushiSashimiView.classList.add("d-block");
    };

    let allViews = [dessertsView, saladsView, riceNodlesView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-block")){
            value.classList.remove("d-block");
            value.classList.add("d-none");
        } 
      };
})

// If riceNodles is selected
riceNodles.addEventListener("click", () => {
    if (riceNodlesView.classList.contains("d-block") == false){
        riceNodlesView.classList.add("d-block");
    };
    
    let allViews = [dessertsView, saladsView, sushiSashimiView, drinksView];

     for(let value of allViews) {
        if (value.classList.contains("d-block")){
            value.classList.remove("d-block");
            value.classList.add("d-none");
        } 
      };
});

// If drinks is selected
drinks.addEventListener("click", () => {
    if (drinksView.classList.contains("d-block") == false){
        drinksView.classList.add("d-block");
    };
    
    let allViews = [dessertsView, saladsView, sushiSashimiView, riceNodlesView];

     for(let value of allViews) {
        if (value.classList.contains("d-block")){
            value.classList.remove("d-block");
            value.classList.add("d-none");
        }
      };
});

// If desserts is selected
desserts.addEventListener("click", () => {
    if (dessertsView.classList.contains("d-block") == false){
        dessertsView.classList.add("d-block");
    };
    
    let allViews = [saladsView, sushiSashimiView, drinksView, riceNodlesView];

     for(let value of allViews) {
        if (value.classList.contains("d-block")){
            value.classList.remove("d-block");
            value.classList.add("d-none");
        }
      };
});

