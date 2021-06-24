
"use strict"
var cNameDT_NeumaticosAdmin = '#dtNeumaticosAdmin';
$(function () {

    $('#cbNeumaticos').on('change', function(e) {

        if ( $(this).find(':selected').data('b_numero_serie') == 1) {
            $('.grupo-b_nserie_obligatorio').show();
        } else {$('.grupo-b_nserie_obligatorio').hide();}

    });

    $('#btnNuevaOrden').on('click', function(e) {

        var placa = $('#edtPlaca').val();
        sessionStorage.setItem('prev_ordennueva', `/neumaticosadmin/?placa=${placa}`);
        location.href = `/ordennueva/?placa=${placa}`;

    });


    $("#AsignaNeumaticoModal").on('shown.bs.modal', function (event) {
        folio_current = $('#folio_current').val();
        $(this).find('#folio_asignar').val(folio_current);

        if ( folio_current == '') {
            $('#btnNuevaOrden').show();
        } else {$('#btnNuevaOrden').hide();}
//        $(this).data('id_concepto', button.data('id_concepto'))
//        $(this).find('#edtDescripcion').val(desc_concepto)
    });


    $('#btnGuardarAsignaNeumatico').on('click', function (event) {

        var v_folio_asignar = $("#folio_asignar").val();
        var v_tx_referencia = $("#edtTxReferencia").val();

        if (folio_asignar.length == 0) {
            message_error_callback('Se requiere de una order de taller activa.', function (result) {
                $('#btnNuevaOrden').focus();
            });
        } else {
            var v_id_concepto = $("#cbNeumaticos").val();

            if (v_id_concepto == '0'){

                message_error_callback('Se requiere seleccionar un neumático..', function (result) {
                    $('#cbNeumaticos').focus();
                });

            } else {

                var v_posicion = $("#cbPosicion").val();
                if (v_posicion == '0'){

                    message_error_callback('Se requiere seleccionar una posición..', function (result) {
                        $('#cbPosicion').focus();
                    });

                } else {
                    var v_no_serie = '';
                    if ($('#cbNeumaticos').find(':selected').data('b_numero_serie') == 1){
                        v_no_serie = $('#edtNoSerie').val();
                        if ($('#cbNeumaticos').find(':selected').data('b_nserie_obligatorio') == 1){
                            if (v_no_serie.length == 0) {
                                message_error_callback('El numero de serie es obligatorio.', function (result) {
                                    $('#edtNoSerie').focus();
                                });
                            }
                        }
                    }
                }
                var _parameters =  {'action': 'setNeumaticoAsignacion',
                                    'folio': v_folio_asignar,
                                    'posicion': v_posicion,
                                    'id_concepto': v_id_concepto,
                                    'no_serie': v_no_serie,
                                    'tx_referencia' : v_tx_referencia}
                console.log(_parameters);
                _ajax(window.location.pathname, _parameters, function(response){
                    ajax_reload(cNameDT_NeumaticosAdmin);

                    $("#edtTxReferencia").val('');
                    $("#folio_asignar").val('');
                    $("#cbNeumaticos").val('0')
                    $('#cbNeumaticos').val('0')
                    $('#edtNoSerie').val('');
                    $("#AsignaNeumaticoModal").modal('hide');

                });

            }


        }




    });


})

function pAsignaNeumatico(data){
    var unidad_neumatico = JSON.parse(sessionStorage.getItem("unidad_neumatico"));
    if (unidad_neumatico !== []) {
        var CountEjes = 22;
        $('#cbPosicion').empty();
        $('.grupo-b_nserie_obligatorio').hide();

        var options = '<option class="select2" value="0">Seleccionar una posición...</option>';
        for( var num_llanta = 1; num_llanta <= CountEjes;num_llanta++ ){
            options += `<option id="op${num_llanta}" value="${num_llanta}">Posición ${num_llanta} </option>`;
        }
        $('#cbPosicion').append(options);
        $.each(unidad_neumatico, function (key, dataset) {
            $('#cbPosicion').find('option').eq(dataset.cons).attr('disabled',"disabled");
            $('#cbPosicion').find('option').eq(dataset.cons).text('Posición '+ dataset.cons + ' (Asiganda)');
            //console.log(dataset.cons);
        });
        var _parameters = {'action': 'getNeumaticosStock'}
        _ajax(window.location.pathname, _parameters, function (data) {
            var options = '<option value="0">Seleccionar un neumático...</option>';
            $('#cbNeumaticos').empty();
            $.each(data, function (key, dataset) {
                var disable = (dataset.stock <= 0 ) ? 'disabled' : '';
                options += `<option ${disable}
                            data-b_numero_serie=${dataset.b_numero_serie}
                            data-b_nserie_obligatorio=${dataset.b_nserie_obligatorio}
                            data-b_personal=${dataset.b_personal}
                            id="opn${dataset.id_concepto}"
                            value="${dataset.id_concepto}">${dataset.desc_marca} / ${dataset.desc_concepto} (Stock: ${dataset.stock}) </option>`;
            });
            $('#cbNeumaticos').append(options);
        });
        $('#AsignaNeumaticoModal').modal('show');
    }

}

function pLoadPosicionesDT(placa){

    console.log('pLoadPosicionesDT...', window.location.pathname);
    console.log('cNameDT_NeumaticosAdmin...', cNameDT_NeumaticosAdmin);
    var _parameters = {'placa': placa, 'action': 'searchdata', 'owner': 'neumaticos-admin'}
    $(cNameDT_NeumaticosAdmin).DataTable({
        language: {
            url: '../../static/libs/datatables-es_orde-editar.json'
        },
        legend: {
            display: false
        },
        responsive: true,
        autoWidth: true,
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
            data: _parameters,
            dataSrc: "",
            statusCode: {
            200: function(data) {

                sessionStorage.setItem('unidad_neumatico', JSON.stringify(data));
                pLoadDiagrama(data);
            },
          }
        },
        columns: [

                {"data": "cons"},
                {"data": "fh_alta"},
                {"data": "kilometraje"},
                {"data": "no_serie", class: 'all text-center'},
                {"data": "desc_concepto", class: 'none'},
                {"data": "desc_marca", class: 'none'},
                {"data": "tx_referencia", class: 'none'},
                {"data": null}

            ],
        dom: 'Bfrtip',
        buttons: [
                    {
                        text: 'Asignar neumático',
                        className: 'btn-secundary',
                        action: function (e, dt, node, config) {

                            pAsignaNeumatico(0);
                        }

                    }
                ],
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
                    if (row.posicion){
                        var
                            // buttons  = `<input id="edtKilometraje" type="number" step="1" class="form-control">`;
                            // buttons += '<a href="operacion/ordeneditar/delete/' + row.id_concepto + '/"               class="btn btn-danger btn-xs btn-flat"><i class="fas fa-minus-circle"></i></a> ';
                            buttons = `<button
    //                                      data-id_concepto=${row['id_concepto']}
    //                                      data-b_numero_serie=${row['b_numero_serie']}
    //                                      data-b_personal=${row['b_personal']}
    //                                      data-stock=${row['stock']}
    //                                      data-b_agrega_conceptos=${row['b_agrega_conceptos']}
    //                                      data-id_tipo_concepto=${row['id_tipo_concepto']}

                                          type="button" class="btn btn-warning btn-xs btn-flat" id="btnAsignarNeumatico"><i class="fas fa-sync-alt"></i></button>`;
                    } else {
                        var buttons = '';
                    }

                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            console.log('initComplete...');
//            $(`${aNameDataTable}  div:last`).addClass('footerSlim');
            // $(document).on("click", "a[id^=btnAgegarConcepto]", function (event) {
//            $(cNameDT_NeumaticosAdmin).on("click", "a[id^=btnAsignarNeumatico]", function (event) {
//                var id_concepto = $(this).data('id_concepto');
//                var id_tipo_concepto = $(this).data('id_tipo_concepto');
//                var stock = $(this).data('stock');
//                var b_numero_serie = $(this).data('b_numero_serie');
//                var b_personal = $(this).data('b_personal');
//                var b_agrega_conceptos = $(this).data('b_agrega_conceptos');
//
//                pAgregaConceptoMain(id_concepto, id_tipo_concepto, stock, b_numero_serie, b_personal, b_agrega_conceptos);

//            });
        }
    });
}


function pLoadDiagrama(data){

    if (data.length > 0){
        data.forEach(function(rowJSON, r_index) {
            $('#llanta-'+rowJSON.cons).removeClass('btn-secondary');
            $('#llanta-'+rowJSON.cons).addClass('btn-warning');

       });
    } else {
        console.log('sin registros');
        $('.btn-neumatico').removeClass('btn-warning');
        $('.btn-neumatico').addClass('btn-secondary');

    }


}


function pValidaPlaca(placa) {


    if (placa.length > 0) {
        var _parameters = {'placa': placa, 'action': 'searchdata', 'owner': 'neumaticos-admin'}
        _ajax('/getInfoUnidad/', _parameters, function (data) {
            if (data.length > 0) {

                // $("#edtPlaca").addClass('bg-olive');
                $("#edtMotor").val(data[0].motor);
                $("#edtMarca").val(data[0].marca);
                $("#edtModelo").val(data[0].modelo);
                $("#edtChasis").val(data[0].chasis);
                $("#edtChasis").val(data[0].chasis);


                $("#fh_alta_current").val(data[0].fh_alta_current);
                $("#kilometraje_current").val(data[0].kilometraje_current);
                $("#folio_current").val(data[0].folio_current);
                $("#nombre_entrega_current").val(data[0].nombre_entrega_current);

                $("#fh_salida_ult").val(data[0].fh_salida_ult);
                $("#kilometraje_ult").val(data[0].kilometraje_ult);
                $("#folio_ult").val(data[0].folio_ult);
                $("#nombre_entrega_ult").val(data[0].nombre_entrega_ult);

            } else {
                $("#edtMotor").val('');
                $("#edtMarca").val('');
                $("#edtModelo").val('');
                $("#edtChasis").val('');

                $("#edtUnidad").val('');
                $("#edtEmpresa").val('');
                $("#edtRup").val('');
                $("#edtTelefono").val('');
                $("#edtCelular").val('');
                $("#edtDireccion").val('');
                $("#edtRepresentante").val('');
                $("#edtEmail").val('');
            }
        });
    } else {
        message_error('Ingresa una descripción');
    }
}

$(function () {
    'use strict';
    const urlParams = new URLSearchParams(window.location.search);
    const cPlaca = urlParams.get('placa');
    console.log({'cPlaca':cPlaca})
    if (cPlaca !== null){
        if (cPlaca !== '' ){
        pValidaPlaca(cPlaca);
        pLoadPosicionesDT(cPlaca);
    }
    }


    $('#btnVerOrden_ult').on('click', function (event) {
        var folio = $("#folio_ult").val();
        if (folio) {
            var prev = '/neumaticosadmin/';
            var placa = $("#edtPlaca").val();
            var kilometraje = $("#kilometraje_current").val();
            var nombre_entrega = $("#nombre_entrega_current").val()
            // location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
            location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
        }

    });


    $('#btnVerOrden_current').on('click', function (event) {
        var folio = $("#folio_current").val();
        if (folio) {
            var prev = '/neumaticosadmin/';
            var placa = $("#edtPlaca").val();
            var kilometraje = $("#kilometraje_current").val();
            var nombre_entrega = $("#nombre_entrega_current").val()
            // location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
            location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
        }

    });



});



