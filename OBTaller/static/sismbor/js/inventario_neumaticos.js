$(function () {
    'use strict';

    const cNameDT_Inventario = '#data';
    $(document).ready(function ($) {

        $(cNameDT_Inventario).DataTable({
            language: {
                url: '../../static/libs/datatables-es_orde-editar.json'
            },
            responsive: true,
            autoWidth: false,
            destroy: true,
            select: true,
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

                {"data": 'id_concepto'},
                {"data": "cve_concepto"},
                {"data": "desc_concepto"},
                {"data": "desc_marca"},
                {"data": "desc_categoria"},
                {
                    "data": "precio_compra",
                    "class": "text-right",
                    render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')
                },
                {
                    "data": "precio_venta",
                    "class": "text-right",
                    render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')
                },
                {"data": "bs_numero_serie", class: 'none'},
                {"data": "bs_nserie_obligatorio", class: 'none'},
                {"data": "vida_util_km", class: 'none'},
                {"data": "stock", "class": "text-right"},
                {"data": null}

            ],
            columnDefs: [

                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons  = `<button data-id_concepto="${row['id_concepto']}" data-desc_concepto="${row['desc_concepto']}" type="button" data-toggle="modal" data-target="#EntradaInventarioModal" class="btn btn-success btn-xs btn-flat"><i class="fas fa-plus"></i></button> `;
                            buttons += `<button data-id_concepto="${row['id_concepto']}" data-desc_concepto="${row['desc_concepto']}" type="button" data-toggle="modal" data-target="#SalidaInventarioModal" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-minus"></i></button> `;
                        // buttons += '<a href="/inventario/salida/' + row.id_concepto + '/" type="button" class="ml-3 btn btn-warning btn-xs btn-flat"><i class="fas fa-minus"></i></a>';
                        buttons += '<a href="/inventario_neumaticos/update/' + row.id_concepto + '/" type="button" class="ml-1 btn btn-primary btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });

        // *************************************************************************************************************
        // *****  ENTRADA *****
        // *************************************************************************************************************
        $("#EntradaInventarioModal").on('shown.bs.modal', function (event) {
            $(this).find('#edtCantidad').focus();
            var button = $(event.relatedTarget) // Button that triggered the modal
            var desc_concepto = button.data('desc_concepto')

            $(this).data('id_concepto', button.data('id_concepto'))
            $(this).find('#edtDescripcion').val(desc_concepto)
        });

        $(document).on("click", "input[name^=ingreso_compra]", function (event) {
            var cve_operacion = $(this).data('cve_operacion');

            $('.grupo-compra').attr('hidden', (cve_operacion !== 'COMPRA'));
            $("#EntradaInventarioModal").data('cve_operacion',cve_operacion);

        });

        $('#btnGuardarEntradaInventario').on('click', function (event) {
            var v_cantidad = $("#edtCantidad").val();
            var v_precio = $("#edtPrecio").val();
            var v_cve_operacion = $("#EntradaInventarioModal").data('cve_operacion');
            var v_id_concepto = $("#EntradaInventarioModal").data('id_concepto');
            var v_tx_referencia = $("#edtTxReferencia").val();

            var _parameters =  {'id_concepto': v_id_concepto,
                                'cantidad': v_cantidad,
                                'precio': v_precio,
                                'cve_operacion': v_cve_operacion,
                                'tx_referencia' : v_tx_referencia}

            if ((v_cantidad.length > 0) && (v_cantidad !== "0") && (v_precio.length > 0) && (v_cve_operacion.length > 0)) {
                _ajax('../stp/entradainventario/', _parameters, function(response){
                    $("#EntradaInventarioModal").data('cve_operacion',"");
                    $("#edtPrecio").val('0.00');
                    $("#edtCantidad").val("1");
                    $("#edtTxReferencia").val("")
                    $("#EntradaInventarioModal").data('cve_operacion','');
                    ajax_reload(cNameDT_Inventario);

                    $("#EntradaInventarioModal").modal('hide');

            });

            } else {
                message_error_callback('Ingresa los datos', function (result) {
                    $('#edtDescripcion').focus();
                });

            }


        });

        // *************************************************************************************************************
        // *****  SALIDA  *****
        // *************************************************************************************************************
        $("#SalidaInventarioModal").on('shown.bs.modal', function (event) {
            $(this).find('#edtCantidadS').focus();
            var button = $(event.relatedTarget) // Button that triggered the modal
            var desc_concepto = button.data('desc_concepto')

            $(this).data('id_concepto', button.data('id_concepto'))
            $(this).find('#edtDescripcionS').val(desc_concepto)
        });

        $(document).on("click", "input[name^=salida_inventario]", function (event) {
            var cve_operacion = $(this).data('cve_operacion');
            $("#SalidaInventarioModal").data('cve_operacion',cve_operacion);
        });

        $('#btnGuardarSalidaInventario').on('click', function (event) {
            var v_cantidad = $("#edtCantidadS").val();

            var v_cve_operacion = $("#SalidaInventarioModal").data('cve_operacion');
            var v_id_concepto = $("#SalidaInventarioModal").data('id_concepto');
            var v_tx_referencia = $("#edtTxReferenciaS").val();

            var _parameters =  {'id_concepto': v_id_concepto,
                                'cantidad': v_cantidad,
                                'precio': 0,
                                'cve_operacion': v_cve_operacion,
                                'tx_referencia' : v_tx_referencia}
            if ((v_cantidad.length > 0) && (v_cantidad !== "0") && (v_cve_operacion.length > 0)) {
                _ajax('../stp/salidainventario/', _parameters, function(response){
                    $("#SalidaInventarioModal").data('cve_operacion',"");

                    $("#edtCantidadS").val("1");
                    $("#edtTxReferenciaS").val("")
                    ajax_reload(cNameDT_Inventario);
                    $("#SalidaInventarioModal").data('cve_operacion','');
                    $("#SalidaInventarioModal").modal('hide');

            });

            } else {
                message_error_callback('Ingresa los datos', function (result) {
                    $('#edtDescripcionS').focus();
                });

            }


        });


    });
});