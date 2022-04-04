function getData(){
let data = [
    {
        "Inicio": "23-03-2022 12:00",
        "Término": "23-03-2022 18:00",
        "Comuna": "San Francisco",
        "Sector": "Museo Colonial",
        "Tema": "Historia",
        "Nombre organizador": "Consuelo Fernandez",
        "Foto": "img_1_1.jpg",
        "Total Fotos": "5"
    },
    {
        "Inicio": "24-03-2022 12:00",
        "Término": "24-03-2022 18:00",
        "Comuna": "Lo Barnechea",
        "Sector": "Parque Yerba Loca",
        "Tema": "Caminata 15km",
        "Nombre organizador": "Antonia Cordova",
        "Foto": "img_2_1.jpg",
        "Total Fotos": "5"
    },
    {
        "Inicio": "25-03-2022 12:00",
        "Término": "25-03-2022 18:00",
        "Comuna": "Santiago",
        "Sector": "Beauchef 850",
        "Tema": "Carrete",
        "Nombre organizador": "Francisco Saavedra",
        "Foto": "img_3_1.jpg",
        "Total Fotos": "1"
    },
    {
        "Inicio": "26-03-2022 12:00",
        "Término": "26-03-2022 18:00",
        "Comuna": "Vitacura",
        "Sector": "Parque Bicentenario",
        "Tema": "Conversación",
        "Nombre organizador": "Sebastián Guzmán",
        "Foto": "img_4_1.jpg",
        "Total Fotos": "5"
    },
    {
        "Inicio": "27-03-2022 12:00",
        "Término": "27-03-2022 18:00",
        "Comuna": "Providencia",
        "Sector": "Parque Japonés",
        "Tema": "Fotografía",
        "Nombre organizador": "Patricio González",
        "Foto": "img_5_1.jpg",
        "Total Fotos": "5"
    }];
    return data;
}

function cargarTabla() {
    let data = getData();
    let row = 0;
    for (let j in data) {
        if (row >= 5) break;
        document.write('<tr class="fila-tabla" onclick="showEventInfo('+row+')">');
        let val = data[j];
        for (let i in data[j]) {
            let skipKey = false;
            for (let k = 0; k < arguments.length; k++) {
                if (arguments[k] === i) {
                    skipKey = true;
                    break;
                }
            }
            if (skipKey === true) { //Pasar a siguiente key
                continue;
            }
            if ("Foto" === i) {
                document.write('<td id="contenedor-imagen">');
                document.write(
                    '<img id="imagen-tabla" src="../data/images/' + val[i] + '" alt="Logo de la marca" />'
                );
                document.write("</td>");
                break;
            }
            document.write("<td>");
            document.write(val[i]);
            document.write("</td>");
        }
        document.write("</tr>");
        row++;
    }
}

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

function showEventInfo(row) {
    let data = getData();
    document.getElementById('modal-detalle').style.display = "block";

    let fotos = '';
    for(let i = 1; i <= data[row]["Total Fotos"]; i++){
        fotos +='<img class="modal-imagen" src="../data/images/img_'+(row+1)+'_'+i+'.jpg"'+
        ' alt="imagen '+i+'del evento." onclick="abrirImagen(\'img_'+(row+1)+'_'+i+'.jpg\')">';
    }

    document.getElementById('modal-detalle').innerHTML=
        '<div class="modal-content">'+
        '<header class="modal-header">'+
        '<span class="close" onclick="notShowEventInfo()">x</span></header>'+
        '<b>Información del evento</b>'+
        '<div id="contenido-externo" class="modal-cuerpo">'+
            '<b>Inicio: </b>'+ data[row]["Inicio"]+
            '<br><b>Término: </b>'+ data[row]["Término"]+
            '<br><b>Comuna: </b>'+ data[row]["Comuna"]+
            '<br><b>Sector: </b>'+ data[row]["Sector"]+
            '<br><b>Tema: </b>'+ data[row]["Tema"]+
            '<br><b>Nombre del Organizador: </b>'+ data[row]["Nombre organizador"]+
            '<br><b>Fotos: </b><br>'+ fotos +
        '</div>'+
        '<button id="modal-exit" onclick="notShowEventInfo()">Salir</button>'+
        '</div>'
}

function abrirImagen(imageName){
    document.getElementById('zoom-imagen').innerHTML =
    '<div class= modal-content>'+
        '<div><span class="close" onclick="notShowEventInfo(\'zoom-imagen\')">&times; Cerrar</span></div><br><br>' +
        '<img class="modal-imagen" src="../data/images/'+imageName+'"'+' alt="zoom de la imagen del evento.">'+
    '</div>';
    document.getElementById('zoom-imagen').style.display = "block";
}

function notShowEventInfo(modalId = 'modal-detalle') {
       document.getElementById(modalId).style.display = "none";
}
