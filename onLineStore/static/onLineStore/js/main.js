// a tag disable default
// const aTags = document.querySelectorAll("a")
// aTags.forEach(function(element){
//     element.addEventListener("click", function(event){

//     })
// })

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
const categoryBtn = document.querySelector(".category-btn")
const categoryBg = document.querySelector(".category-bg")
const closeCatBtn = document.querySelector(".close-cat-btn")
const subCategoryTitle = document.querySelectorAll(".sub-cat-title")

categoryBtn.addEventListener("click", function(){
    categoryBg.classList.toggle("show-category-bg")
})

closeCatBtn.addEventListener("click", function(){
    categoryBg.classList.remove("show-category-bg")
    subCategoryTitle.forEach(function(item){
        item.children[0].classList.remove("show-sub-sub-category")
    })
})

categoryBg.addEventListener("mouseleave", function(event){
    categoryBg.classList.remove("show-category-bg")
        subCategoryTitle.forEach(function(item){
            item.children[0].classList.remove("show-sub-sub-category")
        })
})

// show sub-sub-category
const subCatTitle = document.querySelectorAll(".sub-cat-title")
const subSubCategory = document.querySelectorAll(".sub-sub-category")

subCatTitle.forEach(function(sub_title){
    sub_title.addEventListener("click", function(){
        sub_title.children[0].classList.toggle("show-sub-sub-category")
            subSubCategory.forEach(function(item){
                if(item.parentElement !== sub_title){
                    item.classList.remove("show-sub-sub-category")
                }
            })
        })
    })
