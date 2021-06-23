
function pLoadPosicionesDT(placa){
    'use strict';
    console.log('pLoadPosicionesDT...', window.location.pathname);
    var cNameDT_NeumaticosAdmin = '#dtNeumaticosAdmin';
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
                console.log(',,,,,,,,,,,,,,,,,,,,,,,');
                console.log(data);
                sessionStorage.setItem('unidad_neumatico', JSON.stringify(data));
                pLoadDiagrama(data);
            }
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
//            $(`${aNameDataTable}  div:last`).addClass('footerSlim');
            // $(document).on("click", "a[id^=btnAgegarConcepto]", function (event) {
            $(cNameDT_NeumaticosAdmin).on("click", "a[id^=btnAsignarNeumatico]", function (event) {
//                var id_concepto = $(this).data('id_concepto');
//                var id_tipo_concepto = $(this).data('id_tipo_concepto');
//                var stock = $(this).data('stock');
//                var b_numero_serie = $(this).data('b_numero_serie');
//                var b_personal = $(this).data('b_personal');
//                var b_agrega_conceptos = $(this).data('b_agrega_conceptos');
//
//                pAgregaConceptoMain(id_concepto, id_tipo_concepto, stock, b_numero_serie, b_personal, b_agrega_conceptos);

            });
        }
    });
}


function pLoadDiagrama(data){
    data.forEach(function(rowJSON, r_index) {
        console.log(rowJSON.cons);
        console.log('#option'+rowJSON.cons);
        $('#llanta-'+rowJSON.cons).addClass('btn-secondary');
        $('#llanta-'+rowJSON.cons).addClass('btn-warning');
//        $('#llanta-'+rowJSON.cons).attr

//        var r_id_orden_detalle = rowJSON['id_orden_detalle']
//        table.rows().data().each(function (value, index) {
//        var t_id_orden_detalle= value.id_orden_detalle;
//        if (r_id_orden_detalle == t_id_orden_detalle){
//            var rows = $(cNameDT_OrdenDetalle+' tr');
//            rows.eq(index+1).find('td').eq(6).addClass('bg-danger');
//        }
//        });
    });
}

function pAsignaNeumatico(data){

    var unidad_neumatico = JSON.parse(sessionStorage.getItem("unidad_neumatico"));
    var CountEjes = 22;
    $('#cbPosicion').empty();
    var options = '';
    for( var num_llanta = 1; num_llanta <= CountEjes;num_llanta++ ){
        options += `<option id="op${num_llanta}" value="${num_llanta}">Posición ${num_llanta} </option>`;
    }
    $('#cbPosicion').append(options);
    $.each(unidad_neumatico, function (key, dataset) {
        $('#cbPosicion').find('option').eq(dataset.cons).attr('disabled',"disabled");
        $('#cbPosicion').find('option').eq(dataset.cons).text('Posición '+ dataset.cons + ' (Asiganda)');
        //console.log(dataset.cons);
    });
//    for( var num_llanta = 1, num_llanta<22;num_llanta++ ){
//
//    }
//
//    unidad_neumatico.foreach( function (rowJSON, r_index) {
//
//        console.log(rowJSON);
//    })
    $('#AsignaNeumaticoModal').modal('show');
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



});