function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_tareas/'
    fetch(url)
        .then((response) => response.json())
        .then((tareas) => {
            crearTablaTareas(tareas)
        })
    }

loadData();



function crearTarea(nombre, fecha_inicio, fecha_fin, prioridad){
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
            <td>${fecha_inicio_Formateada}</td>
            <td>${fecha_fin_Formateada}</td>
            <td>${prioridad}</td>
        </tr>`;
}

function generarHTMLTablaTareas(tareas) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <td>Nombre</td>
                    <td>Fecha Inicio</td>
                    <td>Fecha Fin</td>
                    <td>Prioridad</td>
                </tr>
            </thead>
            <tbody>
    `;
    for(const tarea of tareas) {
        tabla += crearTarea(tarea.nombre, tarea.fecha_inicio, tarea.fecha_fin, tarea.prioridad);
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTablaTareas(tareas){
    let tabla = generarHTMLTablaTareas(tareas);
    document.getElementById('tareas').innerHTML = tabla;
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
