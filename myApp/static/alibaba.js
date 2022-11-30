

$(document).ready(function(){
  $('.likebutton').click(function(){
    $(this).toggleClass('heart')
  })
})


document.querySelector('.odeme').addEventListener('click' , function(){
  document.querySelector('.adres').classList.add('adres1');
})

function displayMenu(){
  var link = document.querySelector(".nav-search");
  link.classList.toggle("responsive")
  link.classList.cssText = "font-size : 10px ; "

  var link1 = document.querySelector(".ekle-btn");
  link1.classList.toggle("responsive")
  link1.classList.cssText = "font-size : 10px ; "

  var link2 = document.querySelector(".dropdown");
  link2.classList.toggle("responsive")
  link2.classList.cssText = "font-size : 10px ; "
  

  var menü = document.getElementById('main-header');
  // if ($(document).width() > 600) {
    
  // }
  menü.style.cssText = "height : 15vh"
 
}


