var frutas = ["mazana", "pera", "fresa", "cereza"];

console.log(frutas); //(4) ["mazana", "pera", "fresa", "cereza"]

console.log(frutas.length); //4

// agregar elementos
var masFrutas = frutas.push("Uvas"); //push: añade elementos al final del arreglo
var nuevaFruta = frutas.unshift("piña"); //unshift: añade elementos al inicio del arreglo

// Eliminar elementos
var ultimo = frutas.pop("Uvas"); //pop: elemina el ultimo elemento o el seleccionado
var primero = frutas.shift(); //shift: elimina el primer elemento de l arreglo

//posicion del elemento
var posicion = frutas.indexOf("pera") //indexOf:traee la posicion de un elemento dentro de un arreglo
console.log(frutas[0]); //manzana

// Recorrer arreglos
var articulos = [
    {nombre: "Bici", costo: 3000},
    {nombre: "Tv", costo: 2500},
    {nombre: "Libro", costo: 320},
    {nombre: "Celular", costo: 3000},
    {nombre: "Laptop", costo: 20000},
    {nombre: "Teclado", costo: 500},
    {nombre: "Aufifonos", costo: 1700}
];

// Flitrar en arreglos
    // filter : crea un nuevo arreglo con los elementos filtrados, retrona todas las coinicidencias
var articulosFiltrados = articulos.filter(function(articulo){
    return articulo.costo <=500;
});

// Mapear arreglos
    // map : crea un nuevo arreglo con el elemnto indicado
var nombreArticulo = articulos.map(function(articulo){
    return articulo.nombre;
});

// Buscar en arreglos
    // find : crea un nuevo arreglo con el elemento que se busca dentro del arreglo, retorna una coincidencia
var BucarArticulo = articulos.find(function(articulo){
    return articulo.nombre === "laptop";
});

// Fitrar en el arreglo
    // forEach : Ejecuta lo que le definamos una vez por cada elemento de nuestro array
articulos.forEach(function(articulo) {
    console.log(articulo.nombre);
});

// Validacion
    //some : envia un true o un false dependiendo si el articulo cumple o no la condicion  
var articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
});