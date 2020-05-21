var formulario = document.getElementById("formularioClienteNuevo")
formulario.addEventListener('submit', function(e){
    e.preventDefault();

    var datosClienteNuevo = new FormData(formulario)
    var myFormData = {
    nombre_empresa: datosClienteNuevo.get('nombre_empresa')
    nombre_contacto: datosClienteNuevo.get('nombre_contacto')
    apellido1_contacto: datosClienteNuevo.get('apellido1_contacto')
    apellido2_contacto: datosClienteNuevo.get('apellido2_contacto')
    telf_cliente: datosClienteNuevo.get('telf_cliente')
    email_cliente: datosClienteNuevo.get('email_cliente')
    }

    for(var key in myFormData){
    datosClienteNuevo.append(key, myFormData[key])
    }

    fetch('http://127.0.0.1:8000/index/api_clientes/',{
        method: 'POST',
        body: datosClienteNuevo
    })
    .then((response) =>{
    return response.json()
    })
    .then((data) =>{
    console.log(data)
})
})

