var clickCount = 0;
var maxClicks = 5;

document.getElementById("myButton").addEventListener("click", function() {
  clickCount++;

  if (clickCount === maxClicks) {
    // Obtener la URL de redirección utilizando la etiqueta {% url %}
    var redirectURL = "/pepe/";
    
    // Redirigir al usuario a la URL obtenida
    window.location.href = redirectURL;
  }
});

var clickCount = 0;
var maxClicks = 5;

document.getElementById("myLink").addEventListener("click", function() {
  clickCount++;

  if (clickCount === maxClicks) {
    // Obtener la URL de redirección utilizando la etiqueta {% url %}
    var redirectURL = "/pepe/";

    // Redirigir al usuario a la URL obtenida
    window.location.href = redirectURL;
  }
});