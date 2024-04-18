// app.js
function register() {
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    // Verificar si el correo electrónico contiene el símbolo "@"
    if (!email.includes('@')) {
        alert('Por favor, introduce una dirección de correo electrónico válida.');
        return;
    }

    // Verificar si la contraseña tiene al menos ocho caracteres
    if (password.length < 8) {
        alert('La contraseña debe tener al menos ocho caracteres.');
        return;
    }

    // Continuar con el registro si los datos son válidos
    localStorage.setItem(email, password);
    alert('¡Registro exitoso! Ahora puedes iniciar sesión.');
    window.location.href = 'index.html';
}



function login() {
    const email = document.getElementById('login-email').value;
    const password = document.getElementById('login-password').value;
    const storedPassword = localStorage.getItem(email);
    if (password === storedPassword) {
        localStorage.setItem('session', email);
        alert('Inicio de sesión exitoso.');
        // Redirigir a la página principal de tareas o similar
    } else {
        alert('Error: El correo electrónico o la contraseña no son correctos.');
    }
}

function logout() {
    localStorage.removeItem('session');
    alert('Sesión cerrada correctamente.');
    window.location.href = 'index.html';
}
