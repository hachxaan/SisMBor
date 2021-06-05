$(function () {
    "use strict"
    $('#dataTables4').DataTable({
        // deferRender: true,
        language: {
            url: '../static/libs/datatables-es.json'
        },
        paging: true,
        // colReorder: true,
        // stateSave: true,
        // fixedHeader: true,
        // stripeClasses: [],
        responsive: true,
        // autoWidth: true,
        destroy: true,
        hover: true,
        select: true,
        // dom: '',
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            beforeSend: function (request) {
                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "folio"},
            {"data": "placa"},
            {"data": "desc_status"},
            {"data": "info"},
            {"data": "cliente", name: "cliente"},
            {"data": "cuenta", name: "cuenta", render: $.fn.dataTable.render.number(',', '.', 2, '$')},
            {"data": "fh_registro"},
            {"data": "usu_alta"},
            {"data": "descuento_cuenta"},
            {"data": "id_cliente"},
            {"data": "kilometraje"},
            {"data": "nombre_entrega"},
            {"data": "status"},
            {"data": "modelo"},
            {"data": null},
        ],
        columnDefs: [{
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var EditarTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (parseInt(row['status']) <= 1){ EditarTrabajoEnabled = 'bg-gradient-info'; }
                var IniciaTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (row['status'] == '0'){ IniciaTrabajoEnabled = 'bg-gradient-primary'; }
                var TerminaTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (row['status'] == '1'){ TerminaTrabajoEnabled = 'bg-gradient-success'; }
                var CancelarTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (parseInt(row['status']) <= 1){ CancelarTrabajoEnabled = 'bg-gradient-danger'; }

                if (parseInt(row['status']) <= 1) {
                    var buttons =
                        `<div class="btn-group-lg">
                            <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                <i class="fas fa-briefcase"></i>
                                <span class="sr-only">Toggle Dropdown</span>
                            </button>
                            <div class="dropdown-menu" role="menu" style="">
                                <!-- E D I T A R -->
                                <a data-folio=${ row['folio'] } class="${ EditarTrabajoEnabled } dropdown-item btn-block btn" href="#"><i class="fas fa-edit"></i>Editar</a>
                                <div class="dropdown-divider"></div>
                                <!-- I N I C I A R -->
                                <a data-folio=${ row['folio'] } class="${IniciaTrabajoEnabled} dropdown-item btn-block btn" id="btnIniciaTrabajo"><i class="fas fa-play-circle"></i>Inicia trabajo</a>
                                <!-- T E R M I N R -->
                                <a data-folio=${ row['folio'] } class="${TerminaTrabajoEnabled} dropdown-item btn-block btn" id="btnTerminaTrabajo"><i class="fas fa-check-circle"></i>Termina trabajo</a>
                                <div class="dropdown-divider"></div>
                                <!-- C A N C E L A R -->
                                <a data-folio=${ row['folio'] } class="${CancelarTrabajoEnabled} dropdown-item btn-block btn" id="btnCancelarTrabajo"><i class="fas fa-ban"></i>Cancelar orden</a>
                            </div>
                          </div>`;
                } else {
                     var buttons =
                        `<div class="btn-group-lg">
                            <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                <i class="fas fa-briefcase"></i>
                                <span class="sr-only">Toggle Dropdown</span>
                            </button>
                            <div class="dropdown-menu" role="menu" style="">
                                <!-- DETALLE -->
                                <a data-folio=${ row['folio'] } class="bg-gradient-info dropdown-item btn-block btn"><i class="fas fa-edit"></i>  Detalle</a>
                            </div>
                          </div>`;
                }
                return buttons;
            }
        },
            {
                targets: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                visible: false
            },
            {
                targets: [1],
                render: function (data, type, row) {
                    return `<a href="#" ><i class="mr-3 fas fa-search-plus"></i></a>${data}`
                }
            },
            {
                targets: [2],
                render: function (data, type, row) {

                    switch (row['status']) {
                        case 0: {
                            return `<span class="badge badge-warning">${data}</span>`
                            break;
                        }
                        case 1: {
                            return `<span class="badge badge-info">${data}</span>`
                            break;
                        }
                        case 2: {
                            return `<span class="badge badge-success">${data}</span>`
                            break;
                        }
                        case 3: {
                            return `<span class="badge badge-danger">${data}</span>`
                            break;
                        }
                    }
                    ;


                }
            },

            {
                targets: [3],
                createdCell: function (td, cellData, rowData, row, col) {
                    $(td).css('padding', '0px')
                },
                render: function (data, type, row) {
                    var $elDiv = $('<div></div>');
                    var $Main = $(`<div class="infoMain"></div>`);
                    var $RowD = $('<div class="row elRow"></div>');
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Cliente: </span><a data-id_cliente="${row['id_cliente']}" >${row['cliente']}  </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Entregó: </span><a> ${row['nombre_entrega']}  </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Km Actual: </span><a>${row['kilometraje']}  </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Alta: </span><a> ${row['usu_alta']}  </a></div>`);

                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Modelo: </span><a>${row['modelo']} </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Ult. Serv.: </span><a>   </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Km Anterior: </span><a>  </a></div>`);
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Cuenta: </span><a >${row['cuenta']}</a></div>`);

                    $Main.append($RowD);
                    // $Main.append(`<a>   ${row['cuenta']}  </a>` );

                    $elDiv.append($Main);

                    return $elDiv.clone().html();
                },
            },
        ],

        // columnDefs: [
        //     {
        //         targets: [0, 1, 2, 3, 4],
        //         class: 'text-center pt-4',
        //     },
        //     {
        //         targets: [5],
        //         width: "2%",
        //         class: 'text-center',
        //         render: function (data, type, row) {
        //             var $elDiv = $('<div></div>');
        //             $elDiv.append(
        //                 `<a  style="padding: 2px 7px !important;
        //                             margin-bottom: 2px !important;
        //                             height: 100% !important;
        //                             font-size: large !important;
        //                             color: #727272 !important;
        //                             width: 80%; "
        //                             class="btn btn-block btn-outline-info btn-sm"
        //                             href="cbrbcod/?idrenc=${row.idrenc}">
        //                         <i style="color: #4f4f4f!important;"
        //                                   class="far fa-file-alt mr-2"></i> ${row['recordbco']} </a>`);
        //             return $elDiv.clone().html();
        //         },
        //         "createdCell": function (td, cellData, rowData, row, col) {
        //             $(td).css('padding-bottom', '0px');
        //         }
        //     },
        //     {
        //         targets: [6],
        //         width: "2%",
        //         class: 'text-center',
        //         render: function (data, type, row) {
        //             var $elDiv = $('<div></div>');
        //             $elDiv.append(
        //                 `<a  style="padding: 2px 7px !important;
        //                             margin-bottom: 2px !important;
        //                             height: 100% !important;
        //                             font-size: large !important;
        //                             color: #727272 !important;
        //                             width: 80%; "
        //                             class="btn btn-block btn-outline-info btn-sm"
        //                             href="cbrerpd/?idrenc=${row.idrenc}">
        //                         <i style="color: #4f4f4f!important;"
        //                                   class="far fa-file-alt mr-2"></i> ${row['recorderp']} </a>`);
        //             return $elDiv.clone().html();
        //         },
        //         "createdCell": function (td, cellData, rowData, row, col) {
        //             $(td).css('padding-bottom', '0px');
        //         }
        //     },
        //     {
        //         targets: ['acciones-header'],
        //         class: 'text-center p-0',
        //         orderable: false,
        //         render: function (data, type, row) {
        //             var classBackground = '';
        //             var $elDiv = $('<div></div>');
        //             $elDiv.append('<div></div>');
        //
        //             var CodeStatus = 0;
        //             if (row['recorderp'] === 0 || row['recordbco'] === 0) {
        //                 CodeStatus = 0;
        //             }
        //             if (row['recorderp'] > 0 && row['recordbco'] > 0) {
        //                 if (row['recorderp'] !== row['recordbco']) {
        //                     CodeStatus = 1;
        //                 } else {
        //                     CodeStatus = 2;
        //                 }
        //             }
        //             if (row['status'] == '4') CodeStatus = 4;
        //             var classMain = 'btn btn-app';
        //             var classDetalles = '';
        //             var classEditar = '';
        //             var classConciliar = '';
        //             var classResultados = 'disabled';
        //             var classEliminar = '';
        //             var classIndicador = '';
        //
        //
        //             switch (CodeStatus) {
        //                 case 0: {
        //                     var classBackground = '';
        //
        //                     classDetalles = 'disabled'; //OK
        //                     classConciliar = 'disabled'; //OK
        //                     break;
        //                 }
        //                 case 1: {
        //                     classIndicador = 'callout-warning'; //OK
        //                     break;
        //                 }
        //                 case 2: {
        //                     classIndicador = 'callout-info';
        //                     break;
        //                 }
        //                 case 3: {
        //                     classEditar = 'disabled'; // OK
        //                     // classConciliar = 'disabled'; //OK
        //                     classResultados = ''; //OK
        //                     classEliminar = 'disabled'; //OK
        //                     classIndicador = 'callout-success';
        //                     break;
        //                 }
        //                 case 4: {
        //                     classEditar = 'disabled'; // OK
        //                     // classConciliar = 'disabled'; //OK
        //                     classResultados = ''; //OK
        //                     classEliminar = 'disabled'; //OK
        //                     classIndicador = 'callout-success';
        //
        //                     break;
        //                 }
        //             }
        //             $elDiv.children().addClass('callout m-0 bg-transparent ' + classIndicador);
        //             // ##### EDITAR #####
        //             $elDiv.children().append($(
        //                 `<a class="${classMain}" href="edit/${row.idrenc}/" ><i class="fas fa-edit"></i>Editar</a>`)
        //                 .addClass(classEditar));
        //             // ##### CONCILIAR #####
        //             $elDiv.children().append($(
        //                 `<a class="${classMain}" href="cbsres/?idrenc=${row.idrenc}" ><i class="fas fa-clone"></i>Conciliar</a>`)
        //                 .addClass(classConciliar));
        //             // ##### ELIMINAR #####
        //             $elDiv.children().append($(
        //                 `<a id="btnEliminar${row.idrenc}" class="${classMain}" data-idrenc="${row.idrenc}""><i  class="fas fa-trash-alt"></i>Eliminar</a>`)
        //                 .addClass(classEliminar));
        //             return $elDiv.clone().html();
        //         },
        //     },
        //
        // ],
        // createdRow: function (row, data, dataIndex) {
        //     var classBackground = '';
        //     switch (data['status']) {
        //         case 0:
        //             classBackground = 'bg-default';
        //             break;
        //         case 1:
        //             classBackground = 'bg-paraconciliar';
        //             break;
        //         case 2:
        //             classBackground = 'bg-enconciliacion';
        //             break;
        //         case 3:
        //             classBackground = 'bg-conciliado';
        //             break;
        //         case 4:
        //             classBackground = 'bg-conciliado';
        //             break;
        //     }
        //     $(row).children().addClass(classBackground);
        // },
        initComplete: function (settings, json) {

            $(document).on("click", "a[id^=btnIniciaTrabajo]", function (event) {
                let folio = $(this).data('folio');
                UpdSitStatus(folio, 1)
            });
            $(document).on("click", "a[id^=btnTerminaTrabajo]", function (event) {
                let folio = $(this).data('folio');
                UpdSitStatus(folio, 2)
            });
            $(document).on("click", "a[id^=btnCancelarTrabajo]", function (event) {
                let folio = $(this).data('folio');
                UpdSitStatus(folio, 3)
            });

            // $(document).on("click", "a[id^=btnEliminar]", function (event) {
            //     var idrenc = $(this).data('idrenc');
            //     var parameters = {'idrenc': idrenc, 'index': $(this).data('index')};
            //     ajax_confirm("cbrenca/del/", 'Confirmación',
            //         `¿Eliminar la conciliación ${$(this).data('idrenc')}?`, parameters,
            //         function (response) {
            //             if (response.hasOwnProperty('info')) {
            //                 message_info(response['info'], null, null)
            //                 return false;
            //             }
            //             location.href = '/';
            //             return true;
            //         });
            // });

        }
    });


    // $.fn.dataTable.ext.search.push(
    //     function (settings, searchData, index, rowData, counter) {
    //
    //         if ($('#cbox_conciliados').is(":checked")) {
    //             return (rowData['status'] <= 4)
    //         } else {
    //             return (rowData['status'] <= 3);
    //
    //         }
    //     }
    // );

});

    function UpdSitStatus( folio, status ){
        let parameters = {"folio": folio, "status": status }
        console.log(parameters);
        //?folios=${folio}&statuses=${status}
        submit_with_ajax_json(`../stp/updsitorden/`, 'Notificación', '¿Inician los trabajos de la orden?', parameters, function (response) {
            var table = $('#dataTables4').DataTable();
            table.ajax.reload();
            // location.href =  '../operacion/';
        });
    }