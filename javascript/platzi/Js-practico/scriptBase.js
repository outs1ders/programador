const h1 = document.querySelector('h1');
const p = document.querySelectorAll('p');
const parrafo = document.querySelector('.parrafo');
const pid = document.querySelector('#pid');
const input = document.querySelector('input');

console.log(input.value)

console.log({
   h1,
   p,
   parrafo,
   pid,
   input,
});

//Modificar HTML desde javascript

h1.innerHTML = 'Perro negro'; //modificar la etiqueta dentro del html (PELIGRO)
h1.innerText = 'Gato blanco'; //modifica el texto de la etiqueta

console.log(h1.getAttribute('pantalla')); //Traer un atributo
h1.setAttribute('pantalla', 'SAMSUNG'); //Modificar atributos

h1.classList.add('verde'); //agrega otra clase a la etiqueta
h1.classList.remove('rojo'); //Elimina una clase de la etiqueta

// h1.classList.toggle('verde'); Es cambiante dependiendo la accion
// h1.classList.contains('verde');  Devuelve unTrue /False

input.value = 456;

//Insertar elementos al HTML

console.log(document.createElement('img'));

const img = document.createElement('img');
img.setAttribute('src','https://static.platzi.com/static/images/conf/logo_black@2x.png');
console.log(img);

pid.innerHTML = '';

pid.append(img);