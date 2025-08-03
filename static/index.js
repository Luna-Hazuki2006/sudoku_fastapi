let casilla = []

let casillas = document.getElementsByClassName('cambiable')

for (const cada of casillas) {
    cada.onclick = () => {
        casilla = cada
        if (['1', '2', '3', '4', '5', '6', '7', '8', '9'].includes(cada.innerText)) {
            casilla.innerHTML = ''
            let input = document.createElement('input')
            input.type = 'number'
            input.min = '1'
            input.max = '9'
            input.step = '1'
            casilla.appendChild(input)
        }
        console.log(casilla);
    }
}

document.onkeyup = (evento) => {
    let info = evento.key
    let datos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if (datos.includes(info)) {
        casilla.innerText = info
    }
}

console.log('holaaaaaaa');
