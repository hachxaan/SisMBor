$(function () {
    'use strict';
    const urlParams = new URLSearchParams(window.location.search);
    const cfolio = urlParams.get('folio');
    const cNameDT_OrdenDetalle  = '#dtOrdenDetalle';


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
                $(cNameDT_OrdenDetalle).DataTable().ajax.reload();
                $("#edtTxReferencia").empty()
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
                $(cNameDT_OrdenDetalle).DataTable().ajax.reload();
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
        console.log('DSADSADASDSDASDASDASDAS', id_orden_detalle)
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
                $(cNameDT_OrdenDetalle).DataTable().ajax.reload();
                // $("#cbPersonal").empty()
                $("#PersonalModal").modal('hide');
            });
        } else {
            message_error_callback('Ingresa un número de serie', function (result) {
                // $('#edtPersonal').focus();
            });
        }
    });

    /******************************************************************************************************************/

    /******************************************************************************************************************/
    function pQuitarConcepto(id_orden_detalle) {
        var parameters = {
            "action": 'delItem',
            "folio": cfolio,
            "id_orden_detalle": id_orden_detalle
        }

        submit_with_ajax_action(parameters, function (response) {
            $(cNameDT_OrdenDetalle).DataTable().ajax.reload();
        });
    }

    $(document).ready(function ($) {

        $(cNameDT_OrdenDetalle).DataTable({
            language: {
                url: '../../static/libs/datatables-es.json'
            },
            responsive: true,
            autoWidth: false,
            select: true,
            destroy: true,
            deferRender: true,
            // paging: true,
            // dom: 'p',
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "All"]],
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
                {"data": null}
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