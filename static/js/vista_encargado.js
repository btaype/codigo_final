function gestionarEventos(){
    data={"solicitud":2};
    fetch("http://localhost:5000/encargadoVista", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.redireccionar) {            
            window.location.href = data.redireccionar;
        } else {
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

}
function crearEvento(){
    data={"solicitud":1};
    fetch("http://localhost:5000/encargadoVista", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.redireccionar) {            
            window.location.href = data.redireccionar;
        } else {
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

}