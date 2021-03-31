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

timesButton.addEventListener("click", function(){
    categories.classList.remove("show-categories")
    body.style.overflow = "scroll"
})

function scroll_to_top(){
    document.documentElement.scrollTop = 0;
    categories.classList.toggle("show-categories")
    body.style.overflow = "hidden"
}


// home.html 
const productContentsContainer = document.querySelectorAll(".product-contents-container")
const showMore = document.querySelectorAll(".show-more")

productContentsContainer.forEach(function(container){
    let new_container = [...container.children]
    if (new_container.length > 5){
        let items = new_container.slice(5, new_container.length-1)
        let new_items = [...items]
        new_items.forEach(function(item){
            item.classList.add("hide-product")
            
        })
    }
})

showMore.forEach(function(button){
    button.addEventListener("click", function(event){
        if (event.currentTarget.textContent == "Show less"){
            event.currentTarget.textContent = "Show more"
        }else{
            event.currentTarget.textContent = "Show less"
        }
        let children = event.currentTarget.parentElement.children
        let new_children = [...children]
        let c = new_children.slice(0, new_children.length-1)
        if (c.length > 5){
            let new_c = c.slice(5, c.length)
            new_c.forEach(function(item){
                if(item.classList.contains("hide-product")){
                    item.classList.remove("hide-product")
                }else{
                    item.classList.add("hide-product")
                }
            })
        }
    })
})


