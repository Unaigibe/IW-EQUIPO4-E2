function loadData(seleccionPrioridad) {
    let url = 'http://127.0.0.1:8000/index/api_tareas/'
    fetch(url)
        .then((response) => response.json())
        .then((tareas) => {
            crearTablaTareas(tareas)
        })
    }

loadData()

function crearTarea(nombre, fecha_inicio, fecha_fin, prioridad, id){
    var fecha_inicio_Formateada = formato(fecha_inicio);
    function formato(fecha_inicio){
      return fecha_inicio.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }

    var fecha_fin_Formateada = formato(fecha_fin);
    function formato(fecha_fin){
      return fecha_fin.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }

    var prioridadTareaSeleccionada = document.getElementById('prioridad_Tareas').value

    if (prioridadTareaSeleccionada == 'Mostrar_todas')
        return `
            <tr>
                <td>${nombre}</td>
                <td>${fecha_inicio_Formateada}</td>
                <td>${fecha_fin_Formateada}</td>
                <td>${prioridad}</td>
                <td><a href="/index/tarea/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
            </tr>`;



    if (prioridadTareaSeleccionada == prioridad)
        return `
        <tr>
            <td>${nombre}</td>
            <td>${fecha_inicio_Formateada}</td>
            <td>${fecha_fin_Formateada}</td>
            <td>${prioridad}</td>
            <td><a href="/index/tarea/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
        </tr>`;}



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
        tabla += crearTarea(tarea.nombre, tarea.fecha_inicio, tarea.fecha_fin, tarea.prioridad, tarea.id);
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
