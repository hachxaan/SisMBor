'use strict';
const cNameDT_UnidadAsignacion = '#dtUnidadTicketCombustible';


function pAgregarTicket(){

    alert('en desarrollo...');
}


window.onload = function() {

//    var id_reporte = sessionStorage.getItem('id_reporte');
    var fieldsColums = JSON.parse( sessionStorage.getItem('fieldsColums'));
//    var titulo_reporte =  sessionStorage.getItem('titulo_reporte');
    var id_unidad_asigna =  sessionStorage.getItem('id_unidad_asigna');
    var sit_code =  sessionStorage.getItem('sit_code');


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
                        'action': 'searchdata',
                        'id_unidad_asigna' : id_unidad_asigna
                    },
                    dataSrc: ""
                },
        buttons: [
                    {
                        text: '<i class="fa fa-plus" aria-hidden="true"></i> Agregar Ticket',
                        className: 'btn-info',
                        action: function (e, dt, node, config) {
                            if ((sit_code == 0) || (sit_code == 1 )){
                                pAgregarTicket(0);
                            }

                        }
                    }
                ],
//        columnDefs: [
//            {
//                targets: [-1, -2, -3, -4, -5, -6],
//                class: 'none',
//                "visible": false,
//                "searchable": false
//            },
//            {   targets: [0, 4],
//                class: 'text-center'
//            },
//            {
//                targets: [5],
//                render: function (data, type, row) {
//                    switch (parseInt(row['sit_code'])) {
//                        case 0: {
//                            return `<span class="col-12 status_table badge badge-warning">${data}</span>`
//                            break;
//                        }
//                        case 1: {
//                            return `<span class="col-12 status_table badge badge-info">${data}</span>`
//                            break;
//                        }
//                        case 2: {
//                            return `<span class="col-12 status_table badge badge-success">${data}</span>`
//                            break;
//                        }
//
//                    }
//               }
//            },
//            {   targets: [6],
//                class: 'text-center',
//                render: function (data, type, row) {
//                    switch (parseInt(row['sit_code'])) {
//                        case 0: {
//                            return `<a data-id_unidad_asigna="${row['id_unidad_asigna']}"
//                                        id="btnAsignar" type="button" class="ml-1 pt-1 btn-action-g btn btn-primary col-5">Asignar</a>`
//                            break;
//                        }
//                        default: {
//                            return data
//                            break;
//                        }
//                    }
//                }
//            },
//            {   targets: [7],
//                class: 'text-center',
//                render: function (data, type, row) {
//                    switch (parseInt(row['sit_code'])) {
//                        case 1: {
//                            return `<a data-id_unidad_asigna="${row['id_unidad_asigna']}"
//                                        id="btnRecibe" type="button" class="ml-1 pt-1 btn-action-g btn btn-primary c_btn col-5">Recibir</a>`
//                            break;
//                        }
//                        default: {
//                            return data
//                            break;
//                        }
//                    }
//                }
//            },
//            {   targets: [8],
//                class: 'text-right',
//                render: function (data, type, row) {
//                    if (row['total_combustible_n'] > 0) {
//                        return `<div class="row pr-3"><label class="col-6 pr-3" >${data}</label> <a href="/unidades/combustible_ticket/?id_unidad_asigna=${row['id_unidad_asigna']}&id_unidad=${row['id_unidad']}" type="button" class="col-6 pt-1 btn btn-outline-info c_btn">Tickets</a></div>`;
//                    } else {
//                        return data
//                    }
//                }
//            },
//            {   targets: [9],
//                class: 'text-right',
//                render: function (data, type, row) {
//                    if (row['total_peaje_n'] > 0) {
//                        return `<div class="row pr-3"><label class="col-6 pr-3" >${data}</label><a type="button" class="col-6 pt-1 btn btn-outline-info c_btn">Tickets</a></div>`;
//                    } else {
//                        return data
//                    }
//                }
//            },
//            ],
        initComplete: function (settings, json) {
//            $(document).on("click", "a[id^=btnAsignar]", function (event) {
//                let id_unidad_asigna = $(this).data('id_unidad_asigna');
//                pEntregaUnidad(id_unidad_asigna)
//            });
//            $(document).on("click", "a[id^=btnRecibe]", function (event) {
//                let id_unidad_asigna = $(this).data('id_unidad_asigna');
//                pRecibeUnidad(id_unidad_asigna)
//            });
        }
    });
};