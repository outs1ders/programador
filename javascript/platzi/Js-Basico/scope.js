
var nombre = 'David'; // variable global 

function fun(){
    var apellido = 'Ortega'; //variable local
    return `Hola ${nombre} ${apellido}`
}

fun(); //Hola David Ortega

nombre //David
apellido // ERROR
