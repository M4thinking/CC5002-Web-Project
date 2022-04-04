/* Función que valida los inputs */
function validar(){
    console.log(valRegion());
    console.log(valComuna());
    console.log(valSector());
    console.log(valNombre());
    console.log(valEmail());
    console.log(valCelular());
    console.log(valContactar());
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
    /* Validación y reglas: http://en.wikipedia.org/wiki/Email_address#Invalid_email_addresses */
    let regex = /^(?:(?:[\w`~!#$%^&*\-=+;:{}'|,?\/]+(?:(?:\.(?:"(?:\\?[\w`~!#$%^&*\-=+;:{}'|,?\/\.()<>\[\] @]|\\"|\\\\)*"|[\w`~!#$%^&*\-=+;:{}'|,?\/]+))*\.[\w`~!#$%^&*\-=+;:{}'|,?\/]+)?)|(?:"(?:\\?[\w`~!#$%^&*\-=+;:{}'|,?\/\.()<>\[\] @]|\\"|\\\\)+"))@(?:[a-zA-Z\d\-]+(?:\.[a-zA-Z\d\-]+)*|\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\])$/;
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

function valInicio(){
    let val = getValue("dia-hora-inicio");
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    return regex.test(val);
}

function valInicio(){
    let val = getValue("dia-hora-termino");
    let regex = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/;
    return val.length===0 || regex.test(val);
}

function valDescripción(){
    console.log("Descripción: "+getValue("descripcion-evento"));
    return true;
}