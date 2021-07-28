'use strict';
const cNameDT_UnidadAsignacion = '#dtUnidadAsignacion';

function pValidaPlaca(placa) {
    "use strict"
    if (placa.length > 0) {


        $('#edtPlaca').val(placa);
//        $('#cbPersonal').simulate('mousedown');
        document.getElementById("cbPersonal").size = 5;

    } else {
        message_error('Ingresa una descripción');
    }
}

$(function () {

    $('#btnCrearAsignaUnidad').on('click', function(e) {
        var placa = $("#edtPlaca").val();
        var id_personal = $("#cbPersonal").val();
        var tx_referencia = $("#edtTxReferencia").val();
        // (tx_referencia.length > 0) &&
        if ( (id_personal !== "0") && (placa.length > 0)) {
            var _parameters =  {'placa': placa,
                                'id_personal': id_personal,
                                'tx_referencia' : tx_referencia,
                                'action': 'asigna_personal'}

            fajax(_parameters, function(response){
                $("#edtPlaca").val("");
                $("#cbPersonal").val("0");
                $("#edtTxReferencia").val("");
                ajax_reload(cNameDT_UnidadAsignacion);
                $("#AsignaUnidadModal").modal('hide');
        });

        } else {
            message_error_callback('Ingresa los datos', function (result) {
                $('#edtPlaca').focus();
            });

        }


    });

});

function pAsignaUnidad(){

    $('#AsignaUnidadModal').modal('show');

}

function pEntregaUnidad(id_unidad_asigna){
    var _parameters =  {'id_unidad_asigna': id_unidad_asigna,
                        'action': 'gen_code_asignacion'}
    fajax(_parameters, function(response){
        ajax_reload(cNameDT_UnidadAsignacion);
    });
}

function pRecibeUnidad(id_unidad_asigna){
    var _parameters =  {'id_unidad_asigna': id_unidad_asigna,
                        'action': 'recibe_unidad'}
    fajax(_parameters, function(response){
        ajax_reload(cNameDT_UnidadAsignacion);
    });
}

window.onload = function() {

//    var id_reporte = sessionStorage.getItem('id_reporte');
    var fieldsColums = JSON.parse( sessionStorage.getItem('fieldsColums'));
//    var titulo_reporte =  sessionStorage.getItem('titulo_reporte');
//    var filename =  sessionStorage.getItem('filename');


    $(cNameDT_UnidadAsignacion).DataTable({
//        language: {
//            url: '../../static/libs/datatables-es_orde-editar.json'
//        },
        destroy: true,
        processing: true,
        ordering: true,
        responsive: false,
        autoWidth: false,
        select: true,
        scrollX: false,
        paging: true,
        dom: 'Bfrtip',
        info: false,
        columns: fieldsColums,
        ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    beforeSend: function (request) {
                        request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    },
                    data: {
                        'action': 'searchdata'
//                        'id_reporte' : id_reporte
                    },
                    dataSrc: ""
                },
        buttons: [
                    {
                        text: '<i class="fa fa-plus" aria-hidden="true"></i> Asignar Unidad',
                        className: 'btn-info',
                        action: function (e, dt, node, config) {
                            pAsignaUnidad(0);
                        }
                    }
                ],
        columnDefs: [
            {
                targets: [-1, -2, -3, -4, -5, -6],
                class: 'none',
                "visible": false,
                "searchable": false
            },
            {   targets: [0, 4],
                class: 'text-center'
            },
            {
                targets: [5],
                render: function (data, type, row) {
                    switch (parseInt(row['sit_code'])) {
                        case 0: {
                            return `<span class="col-12 status_table badge badge-warning">${data}</span>`
                            break;
                        }
                        case 1: {
                            return `<span class="col-12 status_table badge badge-info">${data}</span>`
                            break;
                        }
                        case 2: {
                            return `<span class="col-12 status_table badge badge-success">${data}</span>`
                            break;
                        }

                    }
               }
            },
            {   targets: [6],
                class: 'text-center',
                render: function (data, type, row) {
                    switch (parseInt(row['sit_code'])) {
                        case 0: {
                            return `<a data-id_unidad_asigna="${row['id_unidad_asigna']}"
                                        id="btnAsignar" type="button" class="ml-1 pt-1 btn-action-g btn btn-primary col-5">Asignar</a>`
                            break;
                        }
                        default: {
                            return data
                            break;
                        }
                    }
                }
            },
            {   targets: [7],
                class: 'text-center',
                render: function (data, type, row) {
                    switch (parseInt(row['sit_code'])) {
                        case 1: {
                            return `<a data-id_unidad_asigna="${row['id_unidad_asigna']}"
                                        id="btnRecibe" type="button" class="ml-1 pt-1 btn-action-g btn btn-primary c_btn col-5">Recibir</a>`
                            break;
                        }
                        default: {
                            return data
                            break;
                        }
                    }
                }
            },
            {   targets: [8],
                class: 'text-right',
                render: function (data, type, row) {
//                    if (row['total_combustible_n'] > 0) {
                        return `<div class="row pr-3"><label class="col-6 pr-3" >${data}</label> <a
                            href="/unidades/combustible_ticket/?id_unidad_asigna=${row['id_unidad_asigna']}&id_unidad=${row['id_unidad']}"
                            type="button" class="col-6 pt-1 btn btn-outline-info c_btn">Tickets</a></div>`;
//                    } else {
//                        return data
//                    }
                }
            },
            {   targets: [9],
                class: 'text-right',
                render: function (data, type, row) {
//                    if (row['total_peaje_n'] > 0) {
                        return `<div class="row pr-3"><label class="col-6 pr-3" >${data}</label><a
                         href="/unidades/peaje_ticket/?id_unidad_asigna=${row['id_unidad_asigna']}&id_unidad=${row['id_unidad']}"
                         type="button" class="col-6 pt-1 btn btn-outline-info c_btn">Tickets</a></div>`;
//                    } else {
//                        return data
//                    }
                }
            },
            ],
        initComplete: function (settings, json) {
            $(document).on("click", "a[id^=btnAsignar]", function (event) {
                let id_unidad_asigna = $(this).data('id_unidad_asigna');
                pEntregaUnidad(id_unidad_asigna)
            });
            $(document).on("click", "a[id^=btnRecibe]", function (event) {
                let id_unidad_asigna = $(this).data('id_unidad_asigna');
                pRecibeUnidad(id_unidad_asigna)
            });
        }
    });
};

