'use strict';
const cNameDT_UnidadAsignacion = '#dtUnidadTicketCombustible';


function pAgregarTicket(){

    var id_unidad_asigna =  sessionStorage.getItem('id_unidad_asigna');
    var url = 'add/'+id_unidad_asigna+'/';
    location.href = url;

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
//                            if ((sit_code == 0) || (sit_code == 1 )){
                                pAgregarTicket(0);
//                            }

                        }
                    }
                ],
        columnDefs: [
            {   targets: ['_all'],
                class: 'text-center',
            },
            {   targets: [-2],
                render: function (data, type, row) {
                    var buttons = `<a
                                    data-img_ticket=${row['img_ticket']}
                                    type="button" class="btn btn-info btn-xs btn-flat" id="btnVerFoto"><i class="fas fa-ticket-alt"></i></a>`;
                        return buttons;
                }
            },
            ],
        initComplete: function (settings, json) {
            $(document).on("click", "a[id^=btnVerFoto]", function (event) {
                var img_ticket = $(this).data('img_ticket');
                $('#img_ticket').attr('src', `https://img-sismbor.s3.us-east-2.amazonaws.com/${img_ticket}`);
                $('#imgModal').modal('show');
            });

        }
    });
};