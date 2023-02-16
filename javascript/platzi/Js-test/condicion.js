/*
const tipoDeSuscripcion = "Basic";

if (tipoDeSuscripcion == "Free"){
	console.log("Solo puedes tomar los cursos gratis");
} else if (tipoDeSuscripcion == "Basic"){
	console.log("Puedes tomar casi todos los cursos de Platzi durante un mes");
} else if (tipoDeSuscripcion == "Expert"){
	console.log("Puedes tomar casi tomar los cursos de Platzi durante un año");
} else if (tipoDeSuscripcion == "ExpertPlus"){
	console.log("Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año");
}

*/

// just use if

const tipoDeSuscripcion = "Basic";

var suscripcion = ["Free","Basic", "Expert", "ExpertPlus"]

var TypeOfSuscripcion = [
	"Solo puedes tomar los cursos gratis",
	"Puedes tomar casi todos los cursos de Platzi durante un mes",
	"Puedes tomar casi tomar los cursos de Platzi durante un año",
	"Tú y alguien más pueden tomar TODOS los cursos de Platzi durante un año"
]

for (i = 0; i < suscripcion.length; i++){
	if (tipoDeSuscripcion == suscripcion[i]){
		console.log(`${TypeOfSuscripcion[i]}`);
	}
}



