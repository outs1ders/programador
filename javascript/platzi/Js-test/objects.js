var object = {
	color : "black",
	Height : 300,
	weight : 200
};

function showobject (obj){
	for (var key in obj){
		console.log(obj[key]);
	}
}

showobject(object);
