var estudiantes = ['David', 'Alejandro', 'Felipe', 'Daniel'];

function saludar(estudiante){
    console.log(`Hola ${estudiante}`);
}

while (estudiantes.length > 0) {
    var estudiante = estudiantes.shift();
    saludar(estudiante);
}