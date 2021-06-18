$(function () {
    'use strict';
    const urlParams = new URLSearchParams(window.location.search);
    const cfolio = urlParams.get('folio');
    const cNameDT_Repuestos     = '#dtRepuestos';
    const cNameDT_Mantenimiento = '#dtMantenimiento';
    const cNameDT_ManoObra      = '#dtManoObra';
    const cNameDT_OrdenDetalle  = '#dtOrdenDetalle';

    function pAgregarConceptoOrden(){
        var parameters = {
            "action": 'addsOrden',
            "folio": cfolio
        }

        submit_with_ajax_action(parameters, function (response) {

             //
            if (response['result']['hay_b_nserie_obligatorio']){
                message_error('Se requiere Número de Serie');
                var table = $(cNameDT_OrdenDetalle).DataTable();
                response['result']['sol_serie'].forEach(function(rowJSON, r_index) {
                    var r_id_orden_detalle = rowJSON['id_orden_detalle']
                    table.rows().data().each(function (value, index) {
                        var t_id_orden_detalle= value.id_orden_detalle;
                        if (r_id_orden_detalle == t_id_orden_detalle){
                            var rows = $(cNameDT_OrdenDetalle+' tr');
                            rows.eq(index+1).find('td').eq(6).addClass('bg-danger');
                        }
                    });
                });
            } else {
                ajaxReaod();
            }


        });
    }

    /******************************************************************************************************************/

    /******************************************************************************************************************/
    function pQuitarConcepto(id_orden_detalle) {
        var parameters = {
            "action": 'delItem',
            "folio": cfolio,
            "id_orden_detalle": id_orden_detalle
        }

        submit_with_ajax_action(parameters, function (response) {
            ajaxReaod();
        });
    }

    /******************************************************************************************************************/

    /******************************************************************************************************************/
    function pAgregaConceptoMain(id_concepto, id_tipo_concepto, stock, b_numero_serie, b_personal, b_agrega_conceptos) {
        var id_personal = 0;
        var no_serie = '';

        function pBuscaPersonal() {
            console.log('ajax pBuscaPersonal...');
            pAgregaConcepto();
        }

        function pSolicitaNoSerie() {

            pAgregaConcepto();
        }

        function pAgregaConcepto() {
            var parameters = {
                "action": 'addItem',
                "folio": cfolio,
                "id_concepto": id_concepto,
                "id_tipo_concepto": id_tipo_concepto,
                "id_personal": id_personal,
                "stock": stock,
                "b_numero_serie": b_numero_serie,
                "no_serie": no_serie,
                "b_personal": b_personal,
                "b_agrega_conceptos": b_agrega_conceptos

            }


            submit_with_ajax_action(parameters, function (response) {
                ajaxReaod()
            });
        }

        if (b_personal == 'V') {
            pBuscaPersonal();
        } else {
            if (b_numero_serie = '1') {
                pSolicitaNoSerie();
            } else {
                pAgregaConcepto();
            }
        }
    }

    /******************************************************************************************************************/

    /******************************************************************************************************************/
    function ajaxReaod() {
        ajax_reload(cNameDT_Repuestos);
        ajax_reload(cNameDT_Mantenimiento);
        ajax_reload(cNameDT_ManoObra);
        ajax_reload(cNameDT_OrdenDetalle);
    }

    /******************************************************************************************************************/
    /* TX REFERENCIA */
    /******************************************************************************************************************/
    $("#TxReferenciaModal").on('shown.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var id_orden_detalle = button.data('id_orden_detalle');
        var dato = button.data('dato');
        $(this).find('#id_orden_detalle').val(id_orden_detalle)
        $(this).find('#edtTxReferencia').val(dato)
        $(this).find('#edtTxReferencia').focus();
    });
    $('#btnGuardarTxReferencia').on('click', function (event) {
        var v_tx_referencia = $("#edtTxReferencia").val()
        var v_id_orden_detalle = $('#id_orden_detalle').val()
        var _parameters = {
            'action': 'addTxReferencia',
            'folio': cfolio,
            'tx_referencia': v_tx_referencia,
            'id_orden_detalle': v_id_orden_detalle
        }
        console.log(_parameters)
        if (v_tx_referencia.length > 0) {
            _ajax(window.location.pathname, _parameters, function (data) {

                ajax_reload(cNameDT_OrdenDetalle);
                $("#edtTxReferencia").empty();
                $("#TxReferenciaModal").modal('hide');
            });
        } else {
            message_error_callback('Ingresa una referencia', function (result) {
                $('#edtTxReferencia').focus();
            });
        }
    });

    /******************************************************************************************************************/
    /* NO SERIE */
    /******************************************************************************************************************/
    $("#NoSerieModal").on('shown.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var id_orden_detalle = button.data('id_orden_detalle');
        console.log('DSADSADASDSDASDASDASDAS', id_orden_detalle)
        var dato = button.data('dato');
        $(this).find('#id_orden_detalle').val(id_orden_detalle)
        $(this).find('#edtNoSerie').val(dato)
        $(this).find('#edtNoSerie').focus();
    });
    $('#btnGuardarNoSerie').on('click', function (event) {
        var v_NoSerie = $("#edtNoSerie").val()
        var v_id_orden_detalle = $("#NoSerieModal").find('#id_orden_detalle').val()
        var _parameters = {
            'action': 'addNoSerie',
            'folio': cfolio,
            'no_serie': v_NoSerie,
            'id_orden_detalle': v_id_orden_detalle
        }
        console.log(_parameters)
        if (v_NoSerie.length > 0) {
            _ajax(window.location.pathname, _parameters, function (data) {
                ajax_reload(cNameDT_OrdenDetalle);
                $("#edtNoSerie").empty()
                $("#NoSerieModal").modal('hide');
            });
        } else {
            message_error_callback('Ingresa un número de serie', function (result) {
                $('#edtNoSerie').focus();
            });
        }
    });


    /******************************************************************************************************************/
    /* PERSONAL */
    /******************************************************************************************************************/
    $("#PersonalModal").on('shown.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var id_orden_detalle = button.data('id_orden_detalle');
        var dato = button.data('dato');
        $(this).find('#id_orden_detalle').val(id_orden_detalle)
        $(this).find('#cbPersonal').val(dato)
        // $(this).find('#edtPersonal').focus();
    });
    $('#btnGuardarPersonal').on('click', function (event) {
        var v_Personal = $("#cbPersonal").val()
        var v_id_orden_detalle = $("#PersonalModal").find('#id_orden_detalle').val()
        var _parameters = {
            'action': 'addPersonal',
            'folio': cfolio,
            'id_personal': v_Personal,
            'id_orden_detalle': v_id_orden_detalle
        }
        console.log(_parameters)
        if (v_Personal.length > 0) {
            _ajax(window.location.pathname, _parameters, function (data) {
                ajax_reload(cNameDT_OrdenDetalle);
                $("#PersonalModal").modal('hide');
            });
        } else {
            message_error_callback('Ingresa un número de serie', function (result) {
                // $('#edtPersonal').focus();
            });
        }
    });

    $(document).ready(function ($) {
        // ##########################################################################################
        // R E P U E S T O S
        // ##########################################################################################

        const cColumsRepuestos = [
            {"data": "id_concepto"},
            {"data": "cve_concepto"},
            {"data": "desc_concepto"},
            {
                "data": "precio_venta",
                class: 'all text-right',
                render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')
            },
            {"data": "desc_marca"},
            {"data": "desc_categoria"},
            {"data": "abreb_unidad_medida"},
            {"data": "vida_util_km", class: "none"},
            {"data": "vida_util_hr", class: "none"},
            {"data": "desc_periodo_km", class: "none"},
            {"data": "stock", class: 'all text-center'},
            {"data": null, class: 'all text-center'}
        ];
        ShowOrdeEdita(cColumsRepuestos, ID_REPUESTOS, cNameDT_Repuestos);
        // ##########################################################################################
        // M A N T E N I M I E N T O
        // ##########################################################################################

        const cColumsMantenimiento = [
            {"data": "id_concepto"},
            {"data": "cve_concepto"},
            {"data": "desc_concepto"},
            {
                "data": "precio_venta",
                class: 'all text-right',
                render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')
            },
            {"data": "hora_hombre"},
            {"data": null, class: 'all text-center'}
        ];
        ShowOrdeEdita(cColumsMantenimiento, ID_MANTENIMIENTO, cNameDT_Mantenimiento);
        // ##########################################################################################
        // M A N O   D E   O B R A
        // ##########################################################################################

        const cColumsManoObra = [
            {"data": "id_concepto"},
            {"data": "cve_concepto"},
            {"data": "desc_concepto"},
            {
                "data": "precio_venta",
                class: 'all text-right',
                render: $.fn.dataTable.render.number(',', '.', 2, 'S/.')
            },
            {"data": "hora_hombre"},
            {"data": null, class: 'all text-center'}
        ];
        ShowOrdeEdita(cColumsManoObra, ID_MANO_OBRA, cNameDT_ManoObra);


        function ShowOrdeEdita(columns, aIdTipoConcepto, aNameDataTable) {

            $(aNameDataTable).DataTable({
                language: {
                    url: '../../static/libs/datatables-es_orde-editar.json'
                },
                legend: {
                    display: false
                },
                responsive: true,
                autoWidth: false,
                select: true,
                destroy: true,
                deferRender: true,
                lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
                ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    beforeSend: function (request) {
                        request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    },
                    data: {
                        'action': 'searchdata', 'id_tipo_concepto': aIdTipoConcepto, 'folio': cfolio
                    },
                    dataSrc: ""
                },
                columns: columns,
                dom: 'frtip',
                columnDefs: [
                    {
                        "targets": '0',
                        "createdCell": function (td, cellData, rowData, row, col) {
                            $(td).css('padding-left', '10px')
                        }
                    },
                    {
                        targets: [-1],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            var
                                // buttons  = `<input id="edtKilometraje" type="number" step="1" class="form-control">`;
                                // buttons += '<a href="operacion/ordeneditar/delete/' + row.id_concepto + '/"               class="btn btn-danger btn-xs btn-flat"><i class="fas fa-minus-circle"></i></a> ';
                                buttons = `<a  
                                              data-id_concepto=${row['id_concepto']} 
                                              data-b_numero_serie=${row['b_numero_serie']} 
                                              data-b_personal=${row['b_personal']}  
                                              data-stock=${row['stock']} 
                                              data-b_agrega_conceptos=${row['b_agrega_conceptos']} 
                                              data-id_tipo_concepto=${row['id_tipo_concepto']} 
                                              
                                              type="button" class="btn btn-success btn-xs btn-flat" id="btnAgegarConcepto"><i class="fas fa-plus-circle"></i></a>`;
                            return buttons;
                        }
                    },
                ],
                initComplete: function (settings, json) {
                    $(`${aNameDataTable}  div:last`).addClass('footerSlim');
                    // $(document).on("click", "a[id^=btnAgegarConcepto]", function (event) {
                    $(aNameDataTable).on("click", "a[id^=btnAgegarConcepto]", function (event) {
                        var id_concepto = $(this).data('id_concepto');
                        var id_tipo_concepto = $(this).data('id_tipo_concepto');
                        var stock = $(this).data('stock');
                        var b_numero_serie = $(this).data('b_numero_serie');
                        var b_personal = $(this).data('b_personal');
                        var b_agrega_conceptos = $(this).data('b_agrega_conceptos');

                        pAgregaConceptoMain(id_concepto, id_tipo_concepto, stock, b_numero_serie, b_personal, b_agrega_conceptos);

                    });
                }
            });



        }

        $('#dtOrdenDetalle').DataTable({
            language: {
                url: '../../static/libs/datatables-es_orde-editar.json'
            },
            responsive: true,
            autoWidth: false,
            select: true,
            destroy: true,
            deferRender: true,
            paging: false,
            dom: 'B',
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
            buttons: [
                    {
                        text: 'Agregar conceptos seleecionados a la orden',
                        className: 'ml-1 btn-success',
                        action: function (e, dt, node, config) {
                            pAgregarConceptoOrden();
                        }

                    }
                ],
            ajax: {
                url: window.location.pathname,
                type: 'POST',
                beforeSend: function (request) {
                    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
                data: {
                    'action': 'OrdenDetalle', 'folio': cfolio
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id_orden_detalle"},
                {"data": "desc_tipo_concepto"},
                {"data": "cantidad"},
                {"data": "desc_categoria"},
                {"data": "abreb_unidad_medida"},
                {"data": "desc_concepto"},
                {"data": "no_serie_od"},
                {"data": "nombre_persona"},
                {"data": "tx_referencia"},
                // {"data": "b_numero_serie", className: 'none'},
                {"data": null, class: 'all text-center'}
            ],
            columnDefs: [
                {
                    targets: [6],
                    render: function (data, type, row) {
                        if (!data) {
                            var dato = ''
                        } else {
                            var dato = data
                        }
                        var b_numero_serie = row['b_numero_serie']

                        if (b_numero_serie == 1) {
                            return `<a 
                                        data-toggle="modal" data-target="#NoSerieModal" 
                                        data-dato="${dato}"
                                        class="btn btn-info btn-xs btn-flat" 
                                        data-id_orden_detalle="${row['id_orden_detalle']}" > 
                                        <i class="fas fa-edit"></i></a>  ${dato}`
                        } else
                            return ''
                    }
                },
                {
                    targets: [7],
                    render: function (data, type, row) {

                        if (row['b_personal'] == 'V') {
                            if (!data) {
                                var dato = ''
                                var info = ''

                            } else {
                                var dato = row['id_personal']
                                var info = data
                            }
                            return `<a 
                                        data-toggle="modal" data-target="#PersonalModal" 
                                        data-dato="${dato}"
                                        class="btn btn-info btn-xs btn-flat" 
                                        data-id_orden_detalle="${row['id_orden_detalle']}" > 
                                        <i class="fas fa-edit"></i></a>  ${info}`
                        } else {
                            return ''
                        }

                    }
                },
                {
                    targets: [8],
                    render: function (data, type, row) {
                        if (!data) {
                            var dato = ''
                        } else {
                            var dato = data
                        }
                        return `<a 
                                        data-toggle="modal" data-target="#TxReferenciaModal" 
                                        data-dato="${dato}" 
                                        class="btn btn-info btn-xs btn-flat" 
                                        data-id_orden_detalle="${row['id_orden_detalle']}" > 
                                        <i class="fas fa-edit"></i></a>  ${dato}`

                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var
                            // buttons  = `<input id="edtKilometraje" type="number" step="1" class="form-control">`;
                            // buttons += '<a href="operacion/ordeneditar/delete/' + row.id_concepto + '/"               class="btn btn-danger btn-xs btn-flat"><i class="fas fa-minus-circle"></i></a> ';
                            buttons = `<a  
                                          data-id_orden_detalle=${row['id_orden_detalle']} 
                                        type="button" class="btn btn-danger btn-xs btn-flat" id="btnQuitaConcepto"><i class="fas fa-minus-circle"></i></a>`;
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {
                $(document).on("click", "a[id^=btnQuitaConcepto]", function (event) {
                    var id_orden_detalle = $(this).data('id_orden_detalle');
                    pQuitarConcepto(id_orden_detalle);
                });



            }
        });

    });


});