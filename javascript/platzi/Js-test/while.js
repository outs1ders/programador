var i= 0;
while (i < 5){
	console.log("El valor de i es: " + i);
	i++;
}

var i= 10;
while (i > 5){
	console.log("El valor de i es: " + i);
	i--;
}


var answere = false;

while (answere == false){
	var question = prompt("¿Cuanto es 2 + 2?");
	if (question == 2){
		console.log("good")
		break
	}
}



