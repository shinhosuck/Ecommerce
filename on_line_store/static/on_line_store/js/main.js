// Nav background image

const navImgSlide = document.querySelector(".nav-img-slide")

const slideImgs = [
    "static/on_line_store/images/img1.jpg",
    "static/on_line_store/images/img2.jpg",
    "static/on_line_store/images/img3.jpg",
]

// index = 1

// function auto_slide(){
//     if (index <= slideImgs.length-1) {
//         setInterval(function(){
//             navImgSlide.style.transition = "all 5s ease-in-out"
//             navImgSlide.style.background = `url(${slideImgs[index]})`
//             navImgSlide.style.minHeight = "70vh"
//             navImgSlide.style.backgroundPosition = "center"
//             navImgSlide.style.backgroundSize = "cover"
//             navImgSlide.style.backgroundRepeat = "no-repeat"
//             navImgSlide.style.backgroundAttachment = "fixed"
//             index+=1
//             if (index > slideImgs.length-1) {
//                 index = 0
//             }
//         }, 4000)
//     }
// }
// auto_slide()