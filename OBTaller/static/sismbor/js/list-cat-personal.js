$(function () {

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
            {"data": "id_personal"},
            {"data": "nombre"},
            {"data": "apellido"},
            {"data": "cve_usu_alta"},
            {"data": "fh_registro"},
            {"data": null},




        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/personal/update/' + row.id_personal + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/personal/delete/' + row.id_personal + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});