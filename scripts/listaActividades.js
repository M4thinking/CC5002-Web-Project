function fecha(id, horas_extra = 0) {
    date = new Date();
    date.setHours(date.getHours() + horas_extra);
    year = date.getFullYear();
    month = date.getMonth() + 1;
    day = date.getDate();
    hour = date.getHours();
    minute = date.getMinutes();

    if (month < 10) {
        month = "0" + month;
    }
    if (day < 10) {
        day = "0" + day;
    }
    if (hour < 10) {
        hour = "0" + hour;
    }
    if (minute < 10) {
        minute = "0" + minute;
    }
    document.getElementById(id).value = year + "-" + month + "-" + day + " " + hour + ":" + minute;
}

// Al cliquear fuera del modal o zoom, este se cierra
var modal = document.getElementById("modal-detalle");
var zoom = document.getElementById("zoom-imagen");
window.onclick = function(event) {
    if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == zoom) {
    zoom.style.display = "none";
  }
}

// cerrar modal o zoom con botón
function cerrar(context) {
    if (context == "zoom"){
        zoom.style.display = "none";
    }
    else if (context == "modal"){
        modal.style.display = "none";
    }
}

function abrirImagen(imageRoute){
    document.getElementById('zoom-imagen').innerHTML =
    '<div class= modal-content>'+
        '<div><span class="close" onclick="cerrar('+"\'zoom\'"+')">&times; Cerrar</span></div><br><br>' +
        '<img class="modal-imagen" src="/'+imageRoute+'"'+' alt="zoom de la imagen del evento.">'+
    '</div>';
    document.getElementById('zoom-imagen').style.display = "block";
}