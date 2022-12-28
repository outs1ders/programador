var edad = 18

if (edad === 18){
    console.log("puede votar"); //Hola
} else if (edad > 18){
    console.log("puede vaotar de nuevo");   //soy falso
} else {
    console.log("aun no puedes votar");
}

// operador ternario
condition ? true : false;

var numero = 1;

var resultado = numero === 1 ?  "si es uno" : "No es uno";

// Ejercicio

function piedraPapelTijera(opcion){
    if (opcion == 'piedra') {
        console.log( "Perdiste contra el papel" )
        console.log( "Ganaste contra las tijeras")
    } else if (opcion == 'papel'){
        console.log( "Perdiste contra las tijeras")
        console.log( "Ganaste contra la piedra" )
    } else {
        console.log( "Perdiste contra la piedra")
        console.log( "Ganaste contra el papel")
    }   
}

piedraPapelTijera("piedra")