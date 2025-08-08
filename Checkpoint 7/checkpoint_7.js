// Cree una función JS que acepte 4 argumentos. 
// Suma los dos primeros argumentos, luego los dos segundos y multiplícalos. 
// Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". 
// Si es más pequeño, la consola registra "¡El número es menor que 50!"

function operarNumeros(a, b, c, d) {
  const suma1 = a + b;
  const suma2 = c + d;
  const resultado = suma1 * suma2;

  if (resultado > 50) {
    console.log("¡El número es mayor que 50!");
  } else {
    console.log("¡El número es menor que 50!");
  }
}