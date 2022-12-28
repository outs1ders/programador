// Objeto
var miAuto = {
    marca: "Toyota",
    modelo: "Corolla",
    annio: 2020,  //año
    detalleDelAuto: function(){
        console.log(`Auto ${this.modelo} ${this.annio}`);
    }
};

miAuto.marca //Toyota
miAuto.annio //2020
miAuto.detalleDelAuto(); //Auto Corolla 2020

