'use strict';
$(function () {

});

window.onload = function() {

    const cNameDT_Reportes = '#dtUnidadAsignacion';

    var id_reporte = sessionStorage.getItem('id_reporte');
    var fieldsColums = JSON.parse( sessionStorage.getItem('fieldsColums'));
    var titulo_reporte =  sessionStorage.getItem('titulo_reporte');
    var filename =  sessionStorage.getItem('filename');


    $(cNameDT_Reportes).DataTable({
//        language: {
//            url: '../../static/libs/datatables-es_orde-editar.json'
//        },
        "destroy": true,
        "processing": true,
        "ordering": true,
        autoWidth: true,
        select: true,
        "scrollX": false,
        paging: false,
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
                        'id_reporte' : id_reporte
                    },
                    dataSrc: ""
                },


    });
};

