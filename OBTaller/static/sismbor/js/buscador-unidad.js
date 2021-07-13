$(function () {


    $(document).ready(function() {


    });

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
            $("#edtPlaca").val(placa);
            pValidaPlaca(placa);
            $("#BuscarUnidadModal").modal('hide');
        }




    });
    $( "#BuscarUnidadModal" ).on('show.bs.modal', function(){
        b_todas = $(this).data("b_todas");
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
                    "b_todas": b_todas
                },
                 dataSrc: ""
            },
            columns: [
                {"data": "id_unidad"},
                {"data": "id_cliente"},
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
//        $('#dtBuscador tbody').on('click', function () {
//        $('#dtBuscador tbody').on('click', 'td', function () {
//            var table = $('#dtBuscador').DataTable();
//            var colIdx = table.cell(this).index().column;
//            var rowIdx = table.cell(this).index().row;
//            console.log($(this).val(), window.location.pathname)
//            if ($($(this).parent()).hasClass('selected')) {
//                let placa = $(table.cells(rowIdx, 2).nodes()).text();
//                $("#edtPlaca").val(placa);
//                console.log(placa, window.location.pathname)
//                pValidaPlaca(placa);
//                if (window.location.pathname.indexOf('neumaticosadmin') > -1 ) {
//                    pLoadPosicionesDT(placa);
//                }
//                $("#BuscarUnidadModal").modal('hide');
//
//            }
//        });
    });

});