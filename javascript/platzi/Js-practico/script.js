const h1 = document.querySelector('h1');
const input1 = document.querySelector('#calculo1');
const input2 = document.querySelector('#calculo2');
const btn = document.querySelector('#btnCalcular');
const resultdo = document.querySelector('#resultado');
const form = document.querySelector('#form');

btn.addEventListener('click', sumaInputs);

function sumaInputs(event){
   const sumInputs = parseInt(input1.value) + parseInt(input2.value);
   resultdo.innerText = "Resultado: " + sumInputs; 
   console.log(sumInputs);
}

/* solucion 1
form.addEventListener('submit', sumaInputs);

function sumaInputs(event){
   console.log({event});
   event.preventDefault(); //No ejecuta la recarga de pagian del formulario
   const sumInputs = parseInt(input1.value) + parseInt(input2.value);
   resultdo.innerText = "Resultado: " + sumInputs; 
   console.log(sumInputs);
}
*/


/*
btn.addEventListener('click', btnOnClick); //solo se debe de dar el nombre de la funcion a ejecutar
*/
