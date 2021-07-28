$(function () {
    $('#btnSeleccionarUnidad').on('click', function (event) {

        // saber registro seleccionado //
        var table = $('#dtBuscador').DataTable();
        var count = table.rows( { selected: true } ).count();
        if (count == 0){
            Swal.fire({
                title: 'Notificación!',
                html: 'Selecciona una unidad',
                icon: 'error'
            }).then(function (result) {

            });
        } else {
            var rowIdx = table.row('.selected').index()
            let placa = $(table.cells(rowIdx, 2).nodes()).text();
            let id_unidad = $(table.cells(rowIdx, 0).nodes()).text();
            let cliente = $(table.cells(rowIdx, 1).nodes()).text();
            $("#edtPlaca").val(placa);
            pValidaPlaca(placa, id_unidad, cliente);
            $("#BuscarUnidadModal").modal('hide');
        }


    });
    $( "#BuscarUnidadModal" ).on('show.bs.modal', function(){

        $('#dtBuscador').DataTable({
            language: {
                url: '../../static/libs/datatables-es.json'
            },
            responsive: true,
            autoWidth: false,
            destroy: true,
            select: {
                style: 'single'
            },
            stripeClasses: [],
            deferRender: true,
            ajax: {
                url: '/unidad/list/',
                type: 'POST',
                beforeSend: function(request) {
                     request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                 },
                data: {
                    "action": "searchdata_buscador",
                    "b_todas": 'b_todas'
                },
                 dataSrc: ""
            },
            columns: [
                {"data": "id_unidad"},
                {"data": "nombre_empresa"},
                {"data": "placa"},
                {"data": "marca"},
                {"data": "modelo"},
                {"data": "motor"},
                {"data": "chasis"}
                // {"data": null}
            ],
            initComplete: function (settings, json) {
            }
        });

    });

});