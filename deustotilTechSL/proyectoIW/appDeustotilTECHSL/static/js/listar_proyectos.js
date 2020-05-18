function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_proyectos/'
    fetch(url)
        .then((response) => response.json())
        .then((proyectos) => {
            crearTablaProyectos(proyectos);
        })
    }

loadData();

function crearProyecto(nombre, cliente, fecha_inicio, fecha_fin){
    var fecha_inicio_Formateada = formato(fecha_inicio);
    function formato(fecha_inicio){
      return fecha_inicio.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }

    var fecha_fin_Formateada = formato(fecha_fin);
    function formato(fecha_fin){
      return fecha_fin.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }
    return `
        <tr>
            <td>${nombre}</td>
            <td>${cliente}</td>
            <td>${fecha_inicio_Formateada}</td>
            <td>${fecha_fin_Formateada}</td>
        </tr>`;
}

function generarHTMLTablaProyectos(proyectos) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <td>Nombre</td>
                    <td>Cliente</td>
                    <td>Fecha Inicio</td>
                    <td>Fecha Fin</td>
                </tr>
            </thead>
            <tbody>
    `;
    for(const proyecto of proyectos) {
        tabla += crearProyecto(proyecto.nombre, proyecto.cliente, proyecto.fecha_inicio, proyecto.fecha_fin);
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTablaProyectos(proyectos){
    let tabla = generarHTMLTablaProyectos(proyectos);
    document.getElementById('proyectos').innerHTML = tabla;
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
