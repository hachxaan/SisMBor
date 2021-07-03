(function ($) {
    "use strict"
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

                {"data": "id_concepto"},
                {"data": "cve_concepto"},
                {"data": "desc_concepto"},
//                {"data": "desc_categoria"},
                {"data": "precio_venta",
                class: 'all text-right',
                render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')},
                // {"data": "desc_tipo_servicio"},
                {"data": "hora_hombre"},
                // {"data": "desc_periodo_km"},
                {"data": null}

            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/mantenimiento/update/' + row.id_concepto + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/mantenimiento/delete/' + row.id_concepto + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    });




})(jQuery);
