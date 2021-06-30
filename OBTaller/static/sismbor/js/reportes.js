'use strict';
$(function () {

});
//    function pSetSessionsReportes(id_reporte, fieldsColums, atitulo_reporte){
//        consolo.log('rrrrrrrrrrrrr');
//        consolo.log(atitulo_reporte);
//        consolo.log('ssssssssssssssssss');
//        sessionStorage.setItem('id_reporte', id_reporte);
//        sessionStorage.setItem('columns_reporte', JSON.stringify(fieldsColums));
//        sessionStorage.setItem('titulo_reporte', atitulo_reporte);
//    }

window.onload = function() {

    const cNameDT_Reportes = '#data';

    var id_reporte = sessionStorage.getItem('id_reporte');
    var fieldsColums = JSON.parse( sessionStorage.getItem('fieldsColums'));
    var titulo_reporte =  sessionStorage.getItem('titulo_reporte');
    var filename =  sessionStorage.getItem('filename');


    $(cNameDT_Reportes).DataTable({

        language: {
            url: '../../static/libs/datatables-es_orde-editar.json'
        },
        "destroy": true,
        "processing": true,
        "ordering": true,
        autoWidth: true,
        select: true,
        "scrollX": false,
        paging: false,
//        "language": idioma,
        dom: 'Bfrtip',
        info: false,
        buttons: [
            'copy', {
                extend: 'excel',
                text: 'Excel',
                title: titulo_reporte,
                filename: filename,
            }, {
                extend: 'pdf',
                text: 'PDF',
                orientation: 'landscape',
                title: titulo_reporte,
                filename: filename,
            }, {
                extend: 'print',
                text: 'Imprimir',
                title: titulo_reporte,
                exportOptions: {
                    modifier: {
                        page: 'current'
                    }
                },
            }
        ],
        columns: fieldsColums,
        ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    beforeSend: function (request) {
                        request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    },
                    data: {
                        'action': 'searchdata',
                        'id_reporte' : id_reporte
                    },
                    dataSrc: ""
                },


//        responsive: true,
//        autoWidth: false,
//        destroy: true,
//        select: true,
//        deferRender: true,
//        dom: 'B',
//        ajax: {
//            url: window.location.pathname,
//            type: 'POST',
//            beforeSend: function (request) {
//                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//            },
//            data: {
//                'action': 'searchdata',
//                'id_reporte' : id_reporte
//            },
//            dataSrc: ""
//        },
//        columns: columns_reporte,
//        initComplete: function (settings, json) {
//
//        }
    });
};

