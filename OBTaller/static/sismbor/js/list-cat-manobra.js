(function ($) {
    "use strict"
    $(function () {
        console.log(window.location.pathname+'js');
        $('#data').DataTable({
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
                {"data": "desc_categoria"},
                {"data": "precio_venta"},
                {"data": "desc_tipo_servicio"},
                {"data": "hora_hombre"},
                {"data": "desc_periodo_km"},
                {"data": null}

            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/manobra/update/' + row.id_concepto + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/manobra/delete/' + row.id_concepto + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    });




})(jQuery);
