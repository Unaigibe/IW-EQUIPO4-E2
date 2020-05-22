function loadDataTareas() {
    let url = 'http://127.0.0.1:8000/index/api_tareas/'
    fetch(url)
        .then((response) => response.json())
        .then((tareas) => {
            crearTablaTareas(tareas)
        })
    }

function formato(fecha){
  return fecha.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
  }

function limpiarTabla(){
document.getElementById("tareas").innerHTML=""
  }


function crearTarea(nombre, fecha_inicio, fecha_fin, prioridad, id){

    limpiarTabla()

    var fecha_inicio_Formateada = formato(fecha_inicio)
    var fecha_fin_Formateada = formato(fecha_fin)
    var prioridadTareaSeleccionada = document.getElementById('prioridad_Tareas').value

    if (prioridadTareaSeleccionada == "Mostrar_todas")
        return `
            <tr>
                <td>${nombre}</td>
                <td>${fecha_inicio_Formateada}</td>
                <td>${fecha_fin_Formateada}</td>
                <td>${prioridad}</td>
                <td><a href="/index/tarea/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
            </tr>`;

    else if (prioridadTareaSeleccionada == prioridad)
        return `
        <tr>
            <td>${nombre}</td>
            <td>${fecha_inicio_Formateada}</td>
            <td>${fecha_fin_Formateada}</td>
            <td>${prioridad}</td>
            <td><a href="/index/tarea/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
        </tr>`;

        return ""}

function generarHTMLTablaTareas(tareas) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <th>Nombre</th>
                    <th>Fecha Inicio</th>
                    <th>Fecha Fin</th>
                    <th>Prioridad</th>
                </tr>
            </thead>
            <tbody>
    `;
    for(const tarea of tareas) {
        tabla += crearTarea(tarea.nombre, tarea.fecha_inicio, tarea.fecha_fin, tarea.prioridad, tarea.id);
        let htmlTarea = crearTarea(tarea.nombre, tarea.fecha_inicio, tarea.fecha_fin, tarea.prioridad, tarea.id);
        console.log("HTML para la tarea con ID "+tarea.id+": "+htmlTarea);
    }
    tabla += '</tbody></table>'
    return tabla;
}

function crearTablaTareas(tareas){
    let tabla = generarHTMLTablaTareas(tareas);
    document.getElementById('tareas').innerHTML = tabla;
}

loadDataTareas()

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
