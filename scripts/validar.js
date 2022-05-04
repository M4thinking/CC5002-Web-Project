/* Función que valida los inputs */
error = ""

function validar(){
        let val = valRegion()
        && valComuna()
        && valSector()
        && valNombre()
        && valEmail()
        && valCelular()
        && valContactar()
        && valInicio()
        && valTermino()
        && valDescripción()
        && valTema()
        && valFoto();
        if(!val){
            alert("Existen errores en el formulario.");
        }
        return val;
}

/* Shortcut para obtener datos del formulario */
function getValue(id){
    return document.getElementById(id).value;
}

/* Obligatorio */
function valRegion(){
    let val = getValue("region");
    console.log("Region: "+ val);
    return !(val==="" || val ==="sin-region");
}

/* Obligatorio */
function valComuna(){
    let val = getValue("comuna");
    console.log("Comuna: "+val);
    return !(val==="" || val ==="sin-comuna" || val ==="sin-region");
}

/* Opcional <= 100 caracteres */
function valSector(){
    let val = getValue("sector");
    console.log("Sector: "+val);
    return val==="" || val.length<=100;
}

/* Obligatorio <= 200 caracteres */
function valNombre(){
    let val = getValue("nombre");
    console.log("Nombre: "+val);
    return !(val==="" || val.length>200);
}

/* Obligatorio + formato mail */
function valEmail(){
    let val = getValue("email");
    let regex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/
    console.log("Email: "+val);
    return regex.test(val);
}

/* Opcional ó formato celular Chile */
function valCelular(){
    let val = getValue("celular");
    console.log("Celular: "+val);
    let regex = /\D*([+56]\d [2-9])(\D)(\d{4})(\D)(\d{4})\D*/;
    return val === "" || regex.test(val);
}

/* Opcional, máximo 5, url/id mínimo 4 y máximo 50 caracteres */
function valContactar(){
    let redes = ["Whatsapp", "Telegram", "Twitter", "Instagram", "Facebook", "Tiktok", "Otra"];
    let total = 0;
    for(let i in redes){
        red = redes[i].toLowerCase();
        let check = document.getElementById("check-"+red).checked;
        if(check){
            let val = getValue("contacto-" + red);
            console.log("Contacto de "+red+": "+val);
            if(val.length < 4 || val.length>50) return false;
        }
        total+=check;
    }
    console.log("Cantidad de contactos: "+total);
    if(total > 5) return false;
    return true;
}
/* Obligatorio y cumple aaaa-mm-dd hh:mm */
function valInicio(){
    let val = getValue("dia-hora-inicio");
    console.log("Fecha inicio: "+val);
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    return regex.test(val);
}

/* Opcional y cumple aaaa-mm-dd hh:mm */
function valTermino(){
    let val = getValue("dia-hora-termino");
    console.log("Fecha termino: "+val);
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    return val.length===0 || regex.test(val);
}

/* Opcional, básicamente se valida siempre */
function valDescripción(){
    console.log("Descripción: "+getValue("descripcion-evento"));
    return true;
}

/* Obligatorio al menos 1 tema, "Otro" debe tener entre 3 y 15 caracteres inclusive */
function valTema(){
    let val = getValue("tema");
    console.log("Tema: "+val);
    if (val === "10") {
        let input = getValue("otro-tema");
        console.log("Otro tema: "+input);
        return input.length >= 3 && input.length <= 15; //10 -> Otro
    }
    return val.length !== 0;
}

/* Obligatorio, mínimo 1 máximo 5 fotos */
function valFoto(){
    let count = 0;
    for(let i = 1; i < 5; i++){
        let val = document.getElementById("foto-actividad" + i);
        if(val !== null) {
            count ++;
        }
    }
    console.log("Cantidad de Fotos: "+ count);
    return count >= 1 && count <= 5;
}