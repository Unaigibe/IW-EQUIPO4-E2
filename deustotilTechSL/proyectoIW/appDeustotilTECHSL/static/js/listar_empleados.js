function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_empleados/'
    fetch(url)
        .then((response) => response.json())
        .then((empleados) => {
            crearTablaEmpleados(empleados);
        })
    }

loadData();

function crearEmpleado(dni, nombre, apellido1, apellido2, id){
    return `
        <tr>
            <td>${dni}</td>
            <td>${nombre}</td>
            <td>${apellido1}</td>
            <td>${apellido2}</td>
            <td><a href="/index/empleado/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
        </tr>`;
}

function generarHTMLTablaEmpleados(empleados) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <th>DNI</th>
                    <th>Nombre</th>
                    <th>Primer Apellido</th>
                    <th>Segundo Apellido</th>
                </tr>
            </thead>
            <tbody>
    `;
    for(const empleado of empleados) {
        tabla += crearEmpleado(empleado.dni, empleado.nombre, empleado.apellido1, empleado.apellido2, empleado.id);
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
