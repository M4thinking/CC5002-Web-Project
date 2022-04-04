
$('#myModal').on('shown.bs.modal', function () {
    $('#agregar-actividad').trigger('focus');
});

let modal = document.getElementById('myModal');

let add = document.getElementById('agregar-actividad');

add.onclick = function (){
    if (1){
        modal.style.display = "block";
    }
    else {
        return false
    }
}

window.onclick = function (event){
    if(event.target === modal){
        modal.style.display = "none";
    }
}

function cerrar(){
    modal.style.display = "none";
}