function handleLogin() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const data = {
        "email": email,
        "contrasena": password
    };

    fetch("http://localhost:5000/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }).then(response => response.json())
        .then(data => {
            // Manejar la respuesta del servidor
            console.log(data);

            // Verificar si hay información de redirección en la respuesta
            if (data.redireccionar) {
                // Redirigir a la página de inicio de sesión
                window.location.href = data.redireccionar;
            } else {
                // Manejar la respuesta según sea necesario
                // ...
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    
}