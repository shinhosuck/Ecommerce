// navbar
// const navItem = document.querySelector(".nav-item-container")
// const navRight = document.querySelector(".navbar-right")
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


counter = 0


nextBtn.addEventListener("click", function(){
    counter++
    console.log(counter)
    slider()
})

prevBtn.addEventListener("click", function(){
    counter--
    console.log(counter)
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



