//hoisting

//variables
    // example 1
    console.log(miNombre)
    var miNombre = 'Camilo'; //undefined

    // example 2
    var miApellido = undefined;
    console.log(miApellido);

    miApellido = "Cortez"; //undefined  \n "Cortez"

//funciones
    // example 1
    hey();

    function hey(){
        console.log('Hola' + color)
    }

    var color = "rojo";   //Hola undefined 