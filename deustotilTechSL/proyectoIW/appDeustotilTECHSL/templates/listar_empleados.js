const API = {
    SERVICE_URL: "http://127.0.0.1:8000/api/",
    Proyectos: "proyectos/",
    Tareas: "tareas/",
    Empleados: "empleados/",
    Clientes: "clientes/"
}

let elementoAMostrar = document.getElementById('seleccion_Elemento');
elementoAMostrar.addEventListener('change', event => {
    let elemento = document.getElementById('elemento');
    elemento.textContent = event.target.value
    loadData(event.target.value)
});

function loadData(seleccion_Elemento) {
    let url = API.SERVICE_URL + API[seleccion_Elemento];
    console.log(url);
    fetch(url)
        .then((response) => response.json())
        .then((json) => {
            let list = document.getElementById('list')
            list.innerHTML = '';
            for (let element of json) {
                list.append(crearElemento(element.nombre));
            }
        });
}

function crearElemento(name) {
    let li = document.createElement('li');
    li.textContent = name;
    li.classList = 'list-group-item list-group-item-action';
    return li;
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