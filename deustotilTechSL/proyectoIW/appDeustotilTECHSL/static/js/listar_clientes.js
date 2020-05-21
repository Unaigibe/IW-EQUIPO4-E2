function loadData() {
    let url = 'http://127.0.0.1:8000/index/api_clientes/'
    fetch(url)
        .then((response) => response.json())
        .then((clientes) => {
            crearTablaClientes(clientes);
        })
    }

function crearCliente(nombre_empresa, nombre_contacto, telf_cliente, id){
    return `
        <tr>
            <td>${nombre_empresa}</td>
            <td>${nombre_contacto}</td>
            <td>${telf_cliente}</td>
            <td><a href="/index/cliente/${id}"><img id="iconoDetalles" src='/static/img/iconoDetalles.png'></a></td>
        </tr>`;
}

function generarHTMLTablaClientes(clientes) {
    let tabla = `
        <table id="tabla" class="tablaListas">
            <thead>
                <tr>
                    <th>Empresa</th>
                    <th>Nombre Contacto</th>
                    <th>Telf Contacto</th>
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

loadData();


