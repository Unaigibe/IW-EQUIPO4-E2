function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_empleados/'
    fetch(url)
        .then((response) => response.json())
        .then((empleados) => {
            crearTablaEmpleados(empleados);
        })
    }

loadData();

function crearEmpleado(dni, nombre, apellido1, apellido2){
    return `
        <tr>
            <td>${dni}</td>
            <td>${nombre}</td>
            <td>${apellido1}</td>
            <td>${apellido2}</td>
        </tr>`;
}

function generarHTMLTablaEmpleados(empleados) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <td>DNI</td>
                    <td>Nombre</td>
                    <td>Primer Apellido</td>
                    <td>Segundo Apellido</td>
                </tr>
            </thead>
            <tbody>
    `;
    for(const empleado of empleados) {
        tabla += crearEmpleado(empleado.dni, empleado.nombre, empleado.apellido1, empleado.apellido2);
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTablaEmpleados(empleados){
    let tabla = generarHTMLTablaEmpleados(empleados);
    document.getElementById('empleados').innerHTML = tabla;
}

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
