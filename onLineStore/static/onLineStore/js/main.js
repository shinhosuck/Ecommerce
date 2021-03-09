// navbar
const flexContainer = document.querySelector(".flex-container")
const toggleBtn = document.querySelector(".toggle-btn")
const closeBtn = document.querySelector(".close-btn")

toggleBtn.addEventListener("click", function(){
    flexContainer.classList.add("show-flex-container")
    flexContainer.classList.remove("flex-container")
    closeBtn.style.display = "block"
    toggleBtn.style.display = "none"
})
closeBtn.addEventListener("click", function(){
    flexContainer.classList.remove("show-flex-container")
    flexContainer.classList.add("flex-container")
    closeBtn.style.display = "none"
    toggleBtn.style.display = "block"
})

window.addEventListener("resize", function(){
    if(window.innerWidth < 670){
        flexContainer.classList.remove("show-flex-container")
        flexContainer.classList.add("flex-container")
        closeBtn.style.display = "none"
        toggleBtn.style.display = "block"
    }else{
        toggleBtn.style.display = "none"
    }
})

// slider
const images = document.querySelectorAll(".img")
const prevBtn = document.querySelector(".prev-btn")
const nextBtn = document.querySelector(".next-btn")
const dots = document.querySelectorAll(".dot") 

counter = 0


dots[counter].classList.add("dot-color")

nextBtn.addEventListener("click", function(){
    dots[counter].classList.remove("dot-color")
    counter++
    dots[counter].classList.add("dot-color")
    slider()
})

prevBtn.addEventListener("click", function(){
    dots[counter].classList.remove("dot-color")
    counter--
    dots[counter].classList.add("dot-color")
    slider()
})


function slider(){
    if(counter == 2){
        prevBtn.disabled = false
        nextBtn.disabled = true
        counter = 2
    }
    else if(counter <= 0){
            nextBtn.disabled = false
            prevBtn.disabled = true
            counter = 0
        }
    else{
        prevBtn.disabled = false
        nextBtn.disabled = false
    }
    images.forEach(function(img){
        img.style.transform = `translatex(-${counter*100}%)`
    })
}

// show categories
const categoryBg = document.querySelector(".category-bg")
const categoryBtn = document.querySelector(".cat-btn")
const overLayColor = document.querySelector(".overlay-color")
const closeCatBtn = document.querySelector(".close-cat-btn")


categoryBtn.addEventListener("click", function(){
    categoryBg.classList.add("show-category-bg")
    overLayColor.classList.add("show-overlay-color")
    categoryBg.classList.remove("category-bg")
    
})

closeCatBtn.addEventListener("click", function(){
    categoryBg.classList.remove("show-category-bg")
    overLayColor.classList.remove("show-overlay-color")
    categoryBg.classList.add("category-bg")
})