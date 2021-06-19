$(function () {
    // console.log(window.location.pathname);
    $('#data').DataTable({
        language: {
                url: '../../static/libs/datatables-es.json'
            },  
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id_cliente"},
            {"data": "rup"},
            {"data": "nombre_empresa"},
            {"data": "nombre"},
            {"data": "telefono_contacto"},
            {"data": "celular_contacto"},
            {"data": "correo_electronico", class: 'none'},
            {"data": "direccion", class: 'none'},
            {"data": "cve_usu_alta", class: 'none'},
            {"data": "fh_registro", class: 'none'},
            {"data": null},




        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/cliente/update/' + row.id_cliente + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/cliente/delete/' + row.id_cliente + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});