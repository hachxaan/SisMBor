$(function () {
    // console.log(window.location.pathname)

    $(document).ready(function() {


    });

    $('#btnSeleccionarUnidad').on('click', function (event) {
        // console.log('Aqui seleccionar');

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
        $('#dtBuscador').DataTable({
            language: {
                url: '../../static/libs/datatables-es.json'
            },
            responsive: true,
            autoWidth: false,
            destroy: true,
        //      buttons: [
        //     {
        //         text: 'Get selected data',
        //         action: function () {
        //             var count = table.rows( { selected: true } ).count();
        //
        //             events.prepend( '<div>'+count+' row(s) selected</div>' );
        //         }
        //     }
        // ]
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
                    action: "searchdata_buscador"
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
    });

});