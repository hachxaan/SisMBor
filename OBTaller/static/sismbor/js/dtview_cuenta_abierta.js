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
        dom: '<"status_filter">flrtip',
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
                if (parseInt(row['status']) <= 1) {
                    EditarTrabajoEnabled = 'bg-gradient-info';
                }
                var IniciaTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (row['status'] == '0') {
                    IniciaTrabajoEnabled = 'bg-gradient-primary';
                }
                var TerminaTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (row['status'] == '1') {
                    TerminaTrabajoEnabled = 'bg-gradient-success';
                }
                var CancelarTrabajoEnabled = 'disabled bg-gradient-secundary';
                if (parseInt(row['status']) <= 1) {
                    CancelarTrabajoEnabled = 'bg-gradient-danger';
                }

                if (parseInt(row['status']) <= 1) {
                    var buttons =
                        `<div class="btn-group-lg">
                            <button type="button" class="btn btn-success dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                                <i class="fas fa-briefcase"></i>
                                <span class="sr-only">Toggle Dropdown</span>
                            </button>
                            <div class="dropdown-menu" role="menu" style="">
                                <!-- E D I T A R -->
                                <a data-folio=${row['folio']} class="${EditarTrabajoEnabled} dropdown-item btn-block btn" id="btnEditaTrabajo"><i class="fas fa-plus"></i>Agregar Conceptos</a>
                                <div class="dropdown-divider"></div>
                                <!-- I N I C I A R -->
                                <a data-folio=${row['folio']} class="${IniciaTrabajoEnabled} dropdown-item btn-block btn" id="btnIniciaTrabajo"><i class="fas fa-play-circle"></i>Inicia trabajo</a>
                                <!-- T E R M I N R -->
                                <a data-folio=${row['folio']} class="${TerminaTrabajoEnabled} dropdown-item btn-block btn" id="btnTerminaTrabajo"><i class="fas fa-check-circle"></i>Termina trabajo</a>
                                <div class="dropdown-divider"></div>
                                <!-- C A N C E L A R -->
                                <a data-folio=${row['folio']} class="${CancelarTrabajoEnabled} dropdown-item btn-block btn" id="btnCancelarTrabajo"><i class="fas fa-ban"></i>Cancelar orden</a>
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
                                <a data-folio=${row['folio']} class="bg-gradient-info dropdown-item btn-block btn" id="btnDetalle"><i class="fas fa-edit"></i>  Detalle</a>
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

                    return `<a href="ordendetalle/?folio=${row['folio']}"  ><i class="mr-3 fas fa-search-plus"></i></a>${data}`
                }
            },
            {
                targets: [2],
                render: function (data, type, row) {

                    switch (parseInt(row['status'])) {
                        case 0: {
                            return `<span class="status_table badge badge-warning">${data}</span>
                                    <br><span class="fh_info"> ${row['fh_registro']}</span>`
                            break;
                        }
                        case 1: {
                            return `<span class="status_table badge badge-info">${data}</span>
                                    <br><span class="fh_info"> ${row['fh_inicio']}</span>`
                            break;
                        }
                        case 2: {
                            return `<span class="status_table badge badge-success">${data}</span>
                                    <br><span class="fh_info"> ${row['fh_salida']}</span>`
                            break;
                        }
                        case 3: {
                            return `<span class="status_table badge badge-danger">${data}</span>
                                    <br><span class="fh_info"> ${row['fh_cancela']}</span>`
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
                    $RowD.append(`<div class="col-lg-4 col-md-4 col-sm-12"><span> Conceptos: </span><a >${row['no_conceptos']}</a></div>`);

                    $Main.append($RowD);
                    // $Main.append(`<a>   ${row['cuenta']}  </a>` );

                    $elDiv.append($Main);

                    return $elDiv.clone().html();
                },
            },
        ],

        initComplete: function (settings, json) {

            $(document).on("click", "a[id^=btnEditaTrabajo]", function (event) {
                let folio = $(this).data('folio');
                location.href = `ordeneditar/?folio=${folio}`;
            });

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
            $(document).on("click", "a[id^=btnDetalle]", function (event) {
                let folio = $(this).data('folio');
                location.href = `ordendetalle/?folio=${folio}`
            });

            $(".status_filter").html(`<div class="filtros-status"></div>`);


        }
    });

    $('.filtros').on('change', function (event) {
        ajax_reload('dataTables4');
        if ($(this).is(":checked")) var valor = '1'; else var valor =  '0';
        setParametro( '../parametros/', $(this).data('cve_parametro'), valor);
    });

    $.fn.dataTable.ext.search.push(
        function (settings, searchData, index, rowData, counter) {
            var EnProceso, Terminados, Cancelados = false;
            EnProceso = $('#chkEnProceso').is(":checked")  && (parseInt(rowData['status']) < 2) ;
            Terminados = $('#chkTerminados').is(":checked")  && (parseInt(rowData['status']) == 2) ;
            Cancelados = $('#chkCancelados').is(":checked")  && (parseInt(rowData['status']) == 3) ;
            return EnProceso || Terminados || Cancelados;

        }
    );

});

function UpdSitStatus(folio, status) {
    let parameters = {"folio": folio, "status": status}
    console.log(parameters);
    //?folios=${folio}&statuses=${status}
    submit_with_ajax_json(`../stp/updsitorden/`, 'Notificación', '¿Inician los trabajos de la orden?', parameters, function (response) {
        var table = $('#dataTables4').DataTable();
        table.ajax.reload();
        // location.href =  '../operacion/';
    });
}