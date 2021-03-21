const category = document.querySelector(".category")
const categories = document.querySelector(".categories")
const timesButton = document.querySelector(".times-button")

category.addEventListener("click", function(){
    categories.classList.toggle("show-categories")
})

timesButton.addEventListener("click", function(){
    categories.classList.remove("show-categories")
})

categories.addEventListener("mouseleave", function(){
    categories.classList.remove("show-categories")
})