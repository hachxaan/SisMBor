$(function () {
    // console.log(window.location.pathname)
    $('#dtBuscador').DataTable({
        language: {
            url: '../../static/libs/datatables-es.json'
        },
        responsive: true,
        autoWidth: false,
        destroy: true,
        select: true,
        deferRender: true,
        ajax: {
            url: '/unidad/list/',
            type: 'POST',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    // beforeSend: function(request) {
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    //     request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    // },
            data: {
                'action': 'searchdata'
            },
            // dataSrc: ""
        },
        columns: [
            {"data": "id_unidad"},
            {"data": "id_cliente"},
            {"data": "placa"},
            {"data": "marca"},
            {"data": "modelo"},
            {"data": "motor"},
            {"data": "chasis"},
            // {"data": null}
        ],
        // columnDefs: [
        //     {
        //         targets: [-1],
        //         class: 'text-center',
        //         orderable: false,
        //         render: function (data, type, row) {
        //             var buttons = '<a href="/unidad/update/' + row.id_unidad + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-select"></i></a> ';
        //             // buttons += '<a href="/unidad/delete/' + row.id_unidad + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
        //             return buttons;
        //         }
        //     },
        // ],
        initComplete: function (settings, json) {

        }
    });

    $('#dtBuscador tbody').on('click', 'td', function () {
        var table = $('#dtBuscador').DataTable();
        var colIdx = table.cell(this).index().column;
        var rowIdx = table.cell(this).index().row;

        if ($($(this).parent()).hasClass('selected')) {
            let placa = $(table.cells(rowIdx, 2).nodes()).text();
            $("#edtPlaca").val(placa);
            pValidaPlaca(placa);
            $("#BuscarUnidadModal").modal('hide');

        }
    });
    $('#btnSeleccionarUnidad').on('click', function (event) {
        // console.log('Aqui seleccionar');

        // saber registro seleccionado //

        $("#BuscarUnidadModal").modal('hide');
    });


});