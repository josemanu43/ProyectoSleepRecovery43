//alternar entre formulario de iniciar sesion y el formulario de registro
document.getElementById('iniciar-sesion-btn').addEventListener('click', function () {
    document.getElementById('formulario-iniciar-sesion').classList.remove('oculto');
    document.getElementById('formulario-registrarse').classList.add('oculto');
});

document.getElementById('registrarse-btn').addEventListener('click', function () {
    document.getElementById('formulario-iniciar-sesion').classList.add('oculto');
    document.getElementById('formulario-registrarse').classList.remove('oculto');
});

//validacionformulario de inicio de sesión
document.getElementById('formulario-iniciar-sesion').addEventListener('submit', function (e) {
    e.preventDefault();
    const correoUsuario = document.getElementById('correo-usuario-iniciar-sesion').value.trim();
    const contrasena = document.getElementById('contrasena-iniciar-sesion').value.trim();

    //funcion para validar un correo electrónico
    function esCorreoValido(correo) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(correo);
    }

    //verificacion de que ambos campos no esten vacíos
    if (!correoUsuario || !contrasena) {
        alert('Todos los campos son obligatorios para iniciar sesión');
        return;
    }

    //verificar si es correo o nombre de usuario
    if (esCorreoValido(correoUsuario)) {
        alert('Inicio de sesión con correo electrónico exitoso');
    } else {
        alert('Inicio de sesión con nombre de usuario exitoso');
    }
});


//validacion del formulario de registro
document.getElementById('formulario-registrarse').addEventListener('submit', function (e) {
    e.preventDefault();
    
    const nombre = document.getElementById('nombre-registrarse').value.trim();
    const correo = document.getElementById('correo-registrarse').value.trim();
    const contrasena = document.getElementById('contrasena-registrarse').value.trim();
    const confirmarContrasena = document.getElementById('confirmar-contrasena-registrarse').value.trim();
    const edad = document.getElementById('edad-registrarse').value;
    const actividadFisica = document.getElementById('actividad-fisica').value;

    if (!nombre || !correo || !contrasena || !confirmarContrasena || !edad || !actividadFisica) {
        alert('Todos los campos son obligatorios para registrarse');
    } else if (contrasena !== confirmarContrasena) {
        alert('Las contraseñas no coinciden');
    } else {
        alert('Registro exitoso');
    }
});

