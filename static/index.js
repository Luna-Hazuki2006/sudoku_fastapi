let casilla = []

let casillas = document.getElementsByClassName('cambiable')

for (const cada of casillas) {
    cada.onclick = () => {
        casilla = cada
        console.log(casilla);
    }
}

document.onkeyup = (evento) => {
    casilla.innerText = evento.key
}

console.log('holaaaaaaa');
