function auto(marca, modelo, annio){
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}

// crear nuevo objeto
var AutoNuevo = new auto("Tesla", "model x", 2021);
var AutoNuevo2 = new auto("Tesla", "model 3", 2020);


function solution(car) {
    car.licensePlate === undefined ? car.drivingLicense = false : car.drivingLicense = true;
    return car
}

