var estudiantes = ['David', 'Alejandro', 'Felipe', 'Daniel'];

function saludar(estudiante){
    console.log(`Hola ${estudiante}`);
}

for(var i = 0; i < estudiantes.length; i++){
    saludar(estudiantes[i]);
}

for(var estudiante of estudiantes){
    saludar(estudiante);
}


// Ejercicio playground
function solution(estudiantes, deathCount, nuevo) {
    for (var i = 0; i < deathCount; i++){
        estudiantes.pop();
    }
    estudiantes.push(nuevo)
    return estudiantes 
}