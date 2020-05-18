function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_clientes/'
    fetch(url)
        .then((response) => response.json())
        .then((clientes) => {
            crearTablaClientes(clientes);
        })
    }

loadData();

function crearCliente(nombre_empresa, nombre_contacto, telf_cliente, id){
    return `
        <tr>
            <td>${nombre_empresa}</td>
            <td>${nombre_contacto}</td>
            <td>${telf_cliente}</td>
            <td class="celdaIconos"><a href="/index/clientes/${id}"><img id="iconoDetalles" src="{% static 'img/iconoDetalles.png' %}"></a>
        </tr>`;
}

function generarHTMLTablaClientes(clientes) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <td>Nombre Empresa</td>
                    <td>Nombre Contacto</td>
                    <td>Telf Contacto</td>
                    <td>Acciones</td>
                </tr>
            </thead>
            <tbody>
    `;
    for(const cliente of clientes) {
        tabla += crearCliente(cliente.nombre_empresa, cliente.nombre_contacto, cliente.telf_cliente, cliente.id);
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTablaClientes(clientes){
    let tabla = generarHTMLTablaClientes(clientes);
    document.getElementById('clientes').innerHTML = tabla;
}






document.getElementById('btn-nuevo-cliente').addEventListener('click', function(event){
    event.preventDefault();
    let formulario = event.currentTarget.parentNode;
    let nuevoCliente = {
        nombre_empresa: formulario.children["nombre_empresa"].value,
        nombre_contacto: formulario.children["nombre_contacto"].value,
        apellido1_contacto: formulario.children["apellido1_contacto"].value,
        apellido2_contacto: formulario.children["apellido2_contacto"].value,
        telf_cliente: formulario.children["telf_cliente"].value,
        email_cliente: formulario.children["email_cliente"].value
    }
    clientes.push(nuevoCliente);
    crearTablaClientes(clientes);
    });


function mostrarForm() {
       document.getElementById('formulario').style.display=''
       document.getElementById('boton').style.display='none'
       document.getElementById('boton_cerrar').style.display=''
       }

function cerrarForm() {
       document.getElementById('formulario').style.display = 'none';
       document.getElementById('boton').style.display=''
       document.getElementById('boton_cerrar').style.display='none'
       }







/*
let elem = document.getElementsByClassName('seleccion');
elem.addEventListener('click', saludar);

function crearEmpleado(dni, nombre, apellido1) {
    return `
        <tr>
            <td>${dni}</td>
            <td>${nombre}</td>
            <td>${apellido1}</td>            
        </tr>`;
}

function crearTablaEmpleados(empleados) {
    let tabla = `
        <tbody>
            <thead>
                <tr>
                    <td>DNI</td>
                    <td>Nombre</td>
                    <td>Apellido</td>
                    <td>Acciones</td>
                </tr>
            </thead>
            <tbody>
    `;

    // Recorrer el listado de tareas para crear una fila por cada tarea
    for (const empleado of empleados) {
        tabla += crearEmpleado(empleado.dni, empleado.nombre, empleado.apellido1);
    }
    tabla += '</tbody></table>'
    return tabla;
}

fetch('http://127.0.0.1:8000/api/empleados/')
    .then((response) => response.json())
    .then((json) => {
        let list = document.getElementById('list')
        list.innerHTML = '';
        for (let element of json) {
            list.append(crearEmpleado(element.name));
        }
    });




let empleado = crearTablaEmpleados(empleados);
document.getElementById('empleados').innerHTML = tabla;




*/
