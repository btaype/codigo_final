function showDocumentNumberField() {
    var select = document.getElementById("documentType");
    var label = document.getElementById("documentNumberLabel");
    var input = document.getElementById("documentNumber");
    if (select.value) {
        label.style.display = "block";
        input.style.display = "block";
        if (select.value === "DNI") {
            label.textContent = "Número de DNI:";
        } else if (select.value === "pasaporte") {
            label.textContent = "Número de Pasaporte:";
        } else if (select.value === "carnet") {
            label.textContent = "Número de Carnet:";
        }
    } else {
        label.style.display = "none";
        input.style.display = "none";
    }
}

function handleSubmit(event) {
    event.preventDefault();
    var formData = new FormData(event.target);
    var data = {
        "nombre": formData.get("nombres"),
        "apellido": formData.get("apellidos"),
        "email": formData.get("email"),
        "telefono": formData.get("telefono"),
        "Contrasena": formData.get("password"),
        "fecha_nacimiento": formData.get("fechaNacimiento"),
        "tipo": formData.get("documentType"),
        "numero": formData.get("documentNumber"),
        "sexo":formData.get("sexo")
    };
    fetch('http://localhost:5000/registro', {
        method: 'POST',
        
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
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