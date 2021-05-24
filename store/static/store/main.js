
document.addEventListener("touchstart", function () { }, true);

// prevent windows scrolling to top on reload
function storePagePosition() {
  var page_y = window.pageYOffset;
  localStorage.setItem("page_y", page_y);
}

window.addEventListener("scroll", storePagePosition);
var currentPageY;

try {
  currentPageY = localStorage.getItem("page_y");

  if (currentPageY === undefined) {
    localStorage.setItem("page_y") = 0;
  }

  window.scrollTo(0, currentPageY);
} catch (e) {
  // no localStorage available
}

// slick carousel 
$('.product-container1').slick({
  // dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 5,
  slidesToScroll: 5,
  nextArrow: $(".next-btn1"),
  prevArrow: $(".prev-btn1"),
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        //   dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      },
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$('.product-container2').slick({
  // dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 5,
  slidesToScroll: 5,
  nextArrow: $(".next-btn2"),
  prevArrow: $(".prev-btn2"),
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        //   dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

$('.product-container3').slick({
  // dots: true,
  infinite: true,
  speed: 500,
  slidesToShow: 5,
  slidesToScroll: 5,
  nextArrow: $(".next-btn3"),
  prevArrow: $(".prev-btn3"),
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        //   dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});

// card slides prev and next buttons

const nextAndPrevButtons = document.querySelectorAll(".slick-arrow")
const productsContainer = document.querySelectorAll(".products-container")



/*
=========
HOME.HTML
=========*/

const bestMatchAndIcons = document.querySelectorAll(".best-match-and-icons")

bestMatchAndIcons.forEach(function(container){
  container.addEventListener("click", function(event){
    event.currentTarget.nextElementSibling.classList.toggle("show-low-and-high")
    const sibling = event.currentTarget.nextElementSibling
    if(sibling.classList.contains("show-low-and-high")){
      event.currentTarget.children[1].style.display = "none"
      event.currentTarget.children[2].style.display = "block"
    }
    else{
      event.currentTarget.children[1].style.display = "block"
      event.currentTarget.children[2].style.display = "none"
    }
  })
})

/*
================
END OF HOME.HTML
================*/


// slide banner images
const images = document.querySelectorAll(".slide-img")
const imgContainer = document.querySelector(".slide-image-container")
const circles = document.querySelectorAll(".circle")
const prevImgBtn = document.querySelector(".prev-img-btn")
const nextImgBtn = document.querySelector(".next-img-btn")


let counter = 0
circles[counter].style.background = "rgb(0, 134, 116)"

prevImgBtn.addEventListener("click", function () {
  counter--
  slide()
})
nextImgBtn.addEventListener("click", function () {
  counter++
  slide()
})

function slide() {
  circles.forEach(function (circle) {
    circle.style.background = "rgb(167, 167, 167)"
  })
  if (counter < 0) {
    counter = images.length - 1
  }
  else if (counter > images.length - 1) {
    counter = 0
  }
  images.forEach(function (img) {
    img.style.transform = `translatex(-${counter * 100}%)`
    img.style.transition = "all 0.5s ease-in-out"
    circles[counter].style.background = "rgb(0, 134, 116)"
  })
}

circles.forEach(function (circle) {
  circle.addEventListener("click", function () {
    const newCircles = [...circles]
    newCircles.forEach(function (newCircle) {
      newCircle.style.background = "rgb(167, 167, 167)"
    })
    counter = newCircles.indexOf(circle)
    images.forEach(function (img) {
      img.style.transform = `translatex(-${counter * 100}%)`
      img.style.transition = "all 0.5s ease-in-out"
      newCircles[counter].style.background = "rgb(0, 134, 116)"
    })

  })
})

function autoSlide() {
  circles.forEach(function (circle) {
    circle.style.background = "rgb(167, 167, 167)"
  })
  if (counter > images.length - 1) {
    counter = 0
  }
  images.forEach(function (img) {
    img.style.transform = `translate(-${counter * 100}%)`
    img.style.transition = "all 1s ease-in-out"
    circles[counter].style.background = "rgb(0, 134, 116)"
  })
  counter++
  setTimeout(autoSlide, 10000)
}
autoSlide()


// show search bar large screen
// show search bar on mobile screen
const searchButton = document.querySelector("#search-button")
const searchContainer = document.querySelector(".search-container")

searchButton.addEventListener("click", function () {
  searchContainer.classList.toggle("show-search-container")
})


// show navitem container on max-width: 790px.
const barsButton = document.querySelector(".bars-button")
const timesBtn = document.querySelector(".times-btn")
const navItemContainer = document.querySelector(".navitem-container")
const navbar = document.querySelector(".navbar")
const navTimesButton = document.querySelector(".nav-times-button")


barsButton.addEventListener("click", function () {
  navItemContainer.classList.toggle("show-navitem-container")
})
window.addEventListener("resize", function () {
  if (window.innerWidth > 835 || window.innerWidth < 835) {
    navItemContainer.classList.remove("show-navitem-container")
    searchContainer.classList.remove("show-search-container")

  } 
})

navTimesButton.addEventListener("click", function(){
  navItemContainer.classList.remove("show-navitem-container")
})

// base.html show side categories and nav menu
// close nav menu
const category = document.querySelector(".category")
const categories = document.querySelector(".categories-and-sub-category-row")
const timesButton = document.querySelector(".times-button")
const accounts = document.querySelector("#accounts")


category.addEventListener("click", function () {
  sideMenu()
})

function sideMenu() {
  categories.classList.toggle("show-categories-and-sub-category-row")
  searchContainer.classList.remove("show-search-container")
  navItemContainer.classList.remove("show-navitem-container")

  timesButton.addEventListener("click", function () {
    categories.classList.remove("show-categories-and-sub-category-row")
  })

  categories.addEventListener("mouseleave", function () {
    categories.classList.remove("show-categories-and-sub-category-row")
  })

}

// search button from  above comment "show search bar"
searchButton.addEventListener("click", function () {
  categories.classList.remove("show-categories-and-sub-category-row")
 
})

navbar.addEventListener("mouseenter", function () {
  categories.classList.remove("show-categories-and-sub-category-row")
 
})

accounts.addEventListener("mouseenter", function () {
  categories.classList.remove("show-categories-and-sub-category-row")
  searchContainer.classList.remove("show-search-container")
  
})

// my_basket.html show/hide basket edit
const editIcon = document.querySelectorAll(".edit-icon")
const editCloseBtn = document.querySelectorAll(".edit-close-btn")
const tableRows = document.querySelectorAll(".table-row")

editIcon.forEach(function (icon) {
  icon.nextElementSibling.classList.remove("show-edit")
  icon.addEventListener("click", function () {
    icon.nextElementSibling.classList.toggle("show-edit")
    tableRows.forEach(function (row) {
      row.addEventListener("mouseleave", function (event) {
        const children = event.currentTarget.children[1]
        const grandKids = children.children[3]
        const grandGrandKids = grandKids.children
        const newGrandGrandKids = [...grandGrandKids]
        newGrandGrandKids.forEach(function (kid) {
          if (kid.classList.contains("show-edit")) {
            kid.classList.remove("show-edit")
          }
        })
      })
    })
  })
})

editCloseBtn.forEach(function (icon) {
  icon.addEventListener("click", function () {
    icon.parentElement.classList.remove("show-edit")
  })
})

// my_orders.html show-order-detail-text
const myOrderDetailText = document.querySelectorAll(".my-order-detail-text")
const orderPriceMobile = document.querySelectorAll(".order-price-mobile")

myOrderDetailText.forEach(function (orderDetail) {
  orderDetail.addEventListener("click", function () {
    const secondChildren = orderDetail.children[1]
    secondChildren.classList.toggle("show-order-price-mobile")

    orderDetail.addEventListener("mouseleave", function () {
      secondChildren.classList.remove("show-order-price-mobile")
    })
  })
})
