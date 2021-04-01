// slide images
const images = document.querySelectorAll(".slide-img")
const imgContainer = document.querySelector(".slide-image-container")
const circles = document.querySelectorAll(".circle")

let counter = 0
circles[counter].style.background = "red"

function slide(){
    circles.forEach(function(circle){
         circle.style.background = "rgb(167, 167, 167)"
    })
    if (counter == images.length-1){
        counter = 0
    }
    images.forEach(function(img){
        img.style.transform = `translate(-${counter*100}%)`
        img.style.transition = "all 2s ease-in-out"
        circles[counter].style.background = "red"
    })
    counter ++
    setTimeout(slide, 5000)
}
slide()


// show search bar
const searchButton = document.querySelector("#search-button")
const searchContainer = document.querySelector(".search-container")

searchButton.addEventListener("click", function(){
    searchContainer.classList.toggle("show-search-container")
})


// show navitem container on max-width: 715px.
const barsButton = document.querySelector(".bars-button")
const timesBtn = document.querySelector(".times-btn")
const navItemContainer = document.querySelector(".navitem-container")

barsButton.addEventListener("click", function(){
    navItemContainer.classList.toggle("show-navitem-container")
})
window.addEventListener("resize", function(){
    if (window.innerWidth > 715){
        navItemContainer.classList.remove("show-navitem-container")
        searchContainer.classList.remove("show-search-container")

    }
})


// base.html side categories
const category = document.querySelector(".category")
const categories = document.querySelector(".categories")
const timesButton = document.querySelector(".times-button")
const body = document.querySelector("html body")

category.addEventListener("click", function(){
    scroll_to_top()
})
function scroll_to_top(){
    document.documentElement.scrollTop = 0;
    categories.classList.toggle("show-categories")
    body.style.overflow = "hidden"
}
timesButton.addEventListener("click", function(){
    categories.classList.remove("show-categories")
    body.style.overflow = "scroll"
})
categories.addEventListener("mouseleave", function(){
    categories.classList.remove("show-categories")
})

// // scroll products 
// let counter2 = 0

// const buttonLeft = document.querySelector("#button-left")
// const buttonRight = document.querySelector("#button-right")

// const childrenProduct = buttonLeft.parentElement.parentElement.children[1].children

// const newChildrenProduct = [...childrenProduct]

// buttonRight.addEventListener("click", function(){
//     counter2++
//     scrollProducts()
// })
// buttonLeft.addEventListener("click", function(){
//     counter2--
//     scrollProducts()
// })
// function scrollProducts(){
//     if (counter2 >= newChildrenProduct.length-1){
//         counter2 = 0
//     }
//     else if (counter2 <= 0 ){
//         counter2 = newChildrenProduct.length-1
//     }
//     newChildrenProduct.forEach(function(item){
//         item.style.transform = `translatex(-${counter2*244}px)`
//         item.style.transition = "all 0.3s linear"
//     })
// }