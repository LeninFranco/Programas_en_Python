const expresiones = {
    solonum: /^[0-9]+$/,
    soloalpha: /^[0-9a-zA-ZÁÉÍÓÚÑáéíóúñ\s]+$/
}

let formulario = document.getElementById("formulario");
let id = false;
let username = false;
let password = false;

const validarID = (e) => {
    if(expresiones.solonum.test(e.target.value)){
        document.getElementsByName("idSong")[0].classList.remove("is-invalid");
        document.getElementsByName("idSong")[0].classList.add("is-valid");
        id = true;
    }
    else{
        document.getElementsByName("idSong")[0].classList.add("is-invalid");
        document.getElementsByName("idSong")[0].classList.remove("is-valid");
        id = false;
    }
}
document.getElementsByName("idSong")[0].addEventListener('keyup', validarID);
document.getElementsByName("idSong")[0].addEventListener('blur', validarID);

const validarUsername = (e) => {
    if(expresiones.soloalpha.test(e.target.value)){
        document.getElementsByName("name")[0].classList.remove("is-invalid");
        document.getElementsByName("name")[0].classList.add("is-valid");
        username = true;
    }
    else{
        document.getElementsByName("name")[0].classList.add("is-invalid");
        document.getElementsByName("name")[0].classList.remove("is-valid");
        username = false;
    }
}
document.getElementsByName("name")[0].addEventListener('keyup', validarUsername);
document.getElementsByName("name")[0].addEventListener('blur', validarUsername);

const validarPassword = (e) => {
    if(expresiones.soloalpha.test(e.target.value)){
        document.getElementsByName("artist")[0].classList.remove("is-invalid");
        document.getElementsByName("artist")[0].classList.add("is-valid");
        password = true;
    }
    else{
        document.getElementsByName("artist")[0].classList.add("is-invalid");
        document.getElementsByName("artist")[0].classList.remove("is-valid");
        password = false;
    }
}
document.getElementsByName("artist")[0].addEventListener('keyup', validarPassword);
document.getElementsByName("artist")[0].addEventListener('blur', validarPassword);

formulario.addEventListener('submit', (e) => {
    if(!(id & username & password)){
        e.preventDefault();
        alert("Favor de ingresar datos correctos");
    }
});