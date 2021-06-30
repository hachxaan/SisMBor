
"use strict"
var cNameDT_NeumaticosAdmin = '#dtNeumaticosAdmin';

function contextMenuCreate(){
    $.contextMenu({
        selector: '.btn-neumatico',
        build : function ($trigger, e) {
                console.log({"e":e})
                var posicion = $(e['target']).data('posicion');
                var id_posicion = $(e['target']).data('id_posicion');
                var sit_code = $(e['target']).data('sit_code');
                var btnInstall = {}
                var btnUninstall = {}
                switch (parseInt(sit_code)) {
                        case 0: {
                                btnInstall =  { name: "Instalar neumático", icon: "fas fa-arrow-up" }
                            break;
                        }
                        case 1: {
                                btnUninstall =  { name: "Desainstalar Neumático", icon: "fas fa-arrow-down" }
                            break;
                        }
                        default:
                            btnInstall = {}
                            btnUninstall = {}
						break;
                }
                return {
                    callback: function (key, options) {
                        if (key=='install'){
                            sessionStorage.setItem("neumaticos_admin-posision", posicion);
                            pAsignaNeumatico();

                        }
                        if (key=='uninstall'){
                            pDesinstalaNeumatico(id_posicion);
                        }
                    },
                    items: {
                        "install": btnInstall,
                        "uninstall": btnUninstall,
                        "status": {
                            name: "Notas",
                            icon: "fas fa-file-alt",
                            items: {
                                "add_nota": { name: "Agregar Nota", icon: "fas fa-folder-plus"},
                                "view_nota": { name: "Ver Notas", icon: "fas fa-folder-open"},
                            }
                        }
                    }
                };
            },
        trigger: 'left',
    });
}

$(function () {
//    location.reload(true);

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

    $('#btnCalculaVidaUtil').on('click', function (event) {
        var km = $('#edtKilometrajeSet').val();
        if (km !== ''){
            if (esEntero(km)) {

                pLoadPosicionesDT($('#edtPlaca').val());
            }
        }



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
                _ajax(window.location.pathname, _parameters, function(response){
                    ajax_reload(cNameDT_NeumaticosAdmin);
                    $('#cbPosicion').prop("disabled", false);
                    $("#edtTxReferencia").val('');
                    $("#folio_asignar").val('');
                    $("#cbNeumaticos").val('0');
                    $("#cbPosicion").val('0');
                    $('#edtNoSerie').val('');
                    $("#AsignaNeumaticoModal").modal('hide');
                });
            }
        }
    });


})

function pDesinstalaNeumatico(id_posicion){
    var _parameters = {'action': 'pDesinstalaNeumatico', 'id_posicion': id_posicion}
    ajax_confirm(window.location.pathname, 'Confirmar', '¿Desinstalar el neumático de la unidad?', _parameters, function(e){
        ajax_reload(cNameDT_NeumaticosAdmin);
    }, 'Si, desisntalar.');
}

function pAsignaNeumatico(){
    var unidad_neumatico = JSON.parse(sessionStorage.getItem("unidad_neumatico"));
    var posision = sessionStorage.getItem("neumaticos_admin-posision");
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
        $('#cbPosicion').removeAttr("disabled")
        $('#cbPosicion').val('0');

        if(posision !== '0') {

            $('#cbPosicion').prop("disabled", true);
            $('#cbPosicion').val(posision);
            posision = 0;
            sessionStorage.setItem("neumaticos_admin-posision", posision);
        }

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

            success:function(response){
//                $('#diagrama').replaceWith($("#diagrama",response))

                console.log('response');
                console.log(response);
            },
            statusCode: {
            200: function(data) {

                sessionStorage.setItem('unidad_neumatico', JSON.stringify(data));
                console.log('data 200');
                console.log(data);
                pLoadDiagrama(data);
            },
          }
        },
        columns: [


                {"data": "cons"},
                {"data": "fh_alta"},
                {"data": "kilometraje"},
                {"data": "vida_util_km"},
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
                        text: '<i class="fa fa-arrow-up" aria-hidden="true"></i> Instalar neumático',
                        className: 'btn-secundary',
                        action: function (e, dt, node, config) {

                            pAsignaNeumatico(0);
                        }

                    }
                ],
        columnDefs: [
            {
                targets: [1],
                render: function (data, type, row) {
                    var fecha = new Date(data)
                    return  fecha.toLocaleDateString()
                }

            },
            {
                targets: [2],
                render: function (data) {
                    return parseFloat(data).toLocaleString('en')
                }

            },
            {
                targets: [3],
                render: function (data, type, row) {
                    var km_current = $('#edtKilometrajeSet').val();
                    var result = 'Falta info.'
                    var km_result = 0
                    if (km_current !== '') {
                       km_result = parseInt(km_current) - parseInt(row['kilometraje'])
                       result = km_result;
                    }
                    return parseFloat(result).toLocaleString('en') +' / '+ parseFloat(data).toLocaleString('en')
                }
            },
            {
                targets: [4],
                render: function (data, type, row) {
                    var km_current = $('#edtKilometrajeSet').val();
                    var result = 'Falta info.'
                    var km_result = 0
                    if (km_current !== '') {
                       km_result = parseInt(km_current) - parseInt(row['kilometraje'])
                       result = km_result;
                    }
                    var vida_util_km = row['vida_util_km']
                    var pct = 100 - ((parseFloat(result) * 100) / parseFloat(vida_util_km));
                    return pct.toLocaleString('en') + '%'
                }
            },
            {
                targets: [1,2,3,4],
                class: 'text-center'
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

    $('.btn-neumatico').removeClass('btn-warning');
    $('.btn-neumatico').addClass('btn-secondary');


    if (data.length > 0){
        for( var num_llanta = 1; num_llanta <= 22;num_llanta++ ){

            $('#llanta-'+num_llanta.toString()).removeClass('btn-warning');
            $('#llanta-'+num_llanta.toString()).addClass('btn-secondary');
            $('#llanta-'+num_llanta.toString()).data('id_posicion', num_llanta);
            $('#llanta-'+num_llanta.toString()).data('sit_code', '0');

        }
        data.forEach(function(rowJSON, r_index) {
            console.log(rowJSON);
//            console.log({'sit_code', rowJSON.sit_code})
//            console.log({'id_posicion', rowJSON.id_posicion})
            $('#llanta-'+rowJSON.cons).removeClass('btn-secondary');
            $('#llanta-'+rowJSON.cons).addClass('btn-warning');
            $('#llanta-'+rowJSON.cons).data('id_posicion', rowJSON.id_posicion);
            $('#llanta-'+rowJSON.cons).data('sit_code', rowJSON.sit_code);

       });
       contextMenuCreate();
    } else {



    }


}


function pValidaPlaca(placa) {
    if (placa.length > 0) {
        var _parameters = {'placa': placa, 'action': 'searchdata', 'owner': 'neumaticos-admin'}
        _ajax('/getInfoUnidad/?_=' + new Date().getTime(), _parameters, function (data) {
            if (data.length > 0) {
                sessionStorage.setItem('placa', data[0].placa);
                if ((data[0].kilometraje_current !== '') && (data[0].kilometraje_current !== null)) {
                    log('(data[0].kilometraje_current !== ) ');
                    log(data[0].kilometraje_current );
                    $('#edtKilometrajeSet').val(data[0].kilometraje_current);
                } else {
                    if ((data[0].kilometraje_ult !== '') && (data[0].kilometraje_ult !== null)){
                        log('(data[0].kilometraje_ult !== )');
                        $('#edtKilometrajeSet').val(data[0].kilometraje_ult);
                    } else {
                        log('0');
                        $('#edtKilometrajeSet').val('0');
                    }
                }



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
                console.log('response: getInfoUnidad/ pLoadPosicionesDT');
                pLoadPosicionesDT(data[0].placa);

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
//    const cPlaca = urlParams.get('placa');
    const cPlaca = sessionStorage.getItem('placa');
//    console.log({'cPlaca':cPlaca})
    if (cPlaca !== null){
        if (cPlaca !== '' ){
            $('#edtPlaca').val(cPlaca);
            pValidaPlaca(cPlaca);

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


//                            var _parameters = {
//                                'action': 'addNoSerie',
//                                'folio': cfolio,
//                                'no_serie': v_NoSerie,
//                                'id_orden_detalle': v_id_orden_detalle
//                            }
//                            _ajax(window.location.pathname, _parameters, function (data) {
//                                ajax_reload(cNameDT_OrdenDetalle);
//                                $("#edtNoSerie").empty()
//                                $("#NoSerieModal").modal('hide');
//                            });

