function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_tareas/'
    fetch(url)
        .then((response) => response.json())
        .then((tareas) => {
            crearTablaTareas(tareas)
        })
    }

loadData();

function crearTarea(nombre, fecha_inicio, fecha_fin, estadoTarea, id){
    var estadoTareaSeleccionado = document.getElementById('estado_Tareas').value
    var fecha_inicio_Formateada = formato(fecha_inicio);
    function formato(fecha_inicio){
      return fecha_inicio.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }

    var fecha_fin_Formateada = formato(fecha_fin);
    function formato(fecha_fin){
      return fecha_fin.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
    }

    if (estadoTareaSeleccionado == estadoTarea)
        return `
        <tr>
            <td>${nombre}</td>
            <td>${fecha_inicio_Formateada}</td>
            <td>${fecha_fin_Formateada}</td>
            <td>${estadoTarea}</td>
            <td class="celdaIconos"><a href="/index/tarea/${id}">Ver más</a>
        </tr>`;


    if (estadoTareaSeleccionado == 'Mostrar_todas')
        return `
            <tr>
                <td>${nombre}</td>
                <td>${fecha_inicio_Formateada}</td>
                <td>${fecha_fin_Formateada}</td>
                <td>${estadoTarea}</td>
                <td class="celdaIconos"><a href="/index/tarea/${id}">Ver más</a>
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
                    <td>Estado</td>
                </tr>
            </thead>
            <tbody>
    `;
    for(const tarea of tareas) {
        tabla += crearTarea(tarea.nombre, tarea.fecha_inicio, tarea.fecha_fin, tarea.estadoTarea, tarea.id);
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
