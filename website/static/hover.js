count = document.getElementsByClassName('imghv').length;  

for (let i = 0; i < count; i++) {


  document.getElementsByClassName("imghv")[i].onmouseover = function() {mouseOverImage()};

  document.getElementsByClassName("imghv")[i].onmouseout = function() {mouseOutImage()};


  function mouseOverImage() {
    document.getElementsByClassName("texthv")[i].style.color = "black";
  }

  function mouseOutImage() {
    document.getElementsByClassName("texthv")[i].style.color = "";
  }
}
