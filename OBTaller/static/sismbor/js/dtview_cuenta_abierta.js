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
        autoWidth: true,
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
            // {"data": "cliente", name: "cliente"},
            // {"data": "cuenta", name: "cuenta", render: $.fn.dataTable.render.number(',', '.', 2, '$')},
            {"data": "marca", class: 'none'},
            {"data": "modelo", class: 'none'},
            {"data": "motor", class: 'none'},
            {"data": "chasis", class: 'none'},
            {"data": "cliente", class: 'none'},
            {"data": "fh_registro", class: 'none'},
            {"data": "fh_inicio", class: 'none'},
            {"data": "fh_salida", class: 'none'},
            {"data": "usu_alta", class: 'none'},
            // {"data": "descuento_cuenta"},
            // {"data": "id_cliente"},
            // {"data": "kilometraje"},
            // {"data": "nombre_entrega"},
            // {"data": "status"},
            // {"data": "modelo"},
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
                                <a data-folio=${row['folio']} 
                                    data-kilometraje=${row['kilometraje']}
                                    data-placa=${row['placa']}
                                    data-modelo=${row['modelo']}
                                    data-nombre_entrega=${row['nombre_entrega']}
                                    data-row_num=${row['row_num']}
                                    class="${EditarTrabajoEnabled} dropdown-item btn-block btn" id="btnEditaTrabajo"><i class="fas fa-plus"></i>Agregar Conceptos</a>
                                <!-- N E U M A T I C O S -->
                                <a data-placa=${row['placa']}
                                    class="${EditarTrabajoEnabled} dropdown-item btn-block btn" id="btnNeumaticosAdmin"><i class="fas fa-plus"></i>Neumáticos</a>
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
                                <!-- N E U M A T I C O S -->
                                <a data-placa=${row['placa']}
                                    class="bg-gradient-info dropdown-item btn-block btn" id="btnNeumaticosAdmin"><i class="fas fa-plus"></i>Neumáticos</a>
                            </div>

                          </div>`;
                }
                return buttons;
            }
        },
            // {
            //     targets: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            //     visible: false
            // },
            {
                targets: [0],
                class: 'pl-5 pt-3',
            },
            {
                targets: [1],
                render: function (data, type, row) {
                    var folio = row.folio;
                    var prev = '/operacion/';
                    // RASTREO AQUI PORTI
                    var placa = row.placa;
                    var kilometraje = '';
                    var nombre_entrega = '';
                    return `<a href="/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}" ><i class="mr-3 fas fa-search-plus"></i></a>${data}`
                }
            },
            {
                targets: [2],
                class: 'pb-0',
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
                class: 'pt-2',
                createdCell: function (td, cellData, rowData, row, col) {
                    $(td).css('padding', '0px')
                },
                render: function (data, type, row) {
                    var $elDiv = $('<div></div>');
                    var $Main = $(`<div class="infoMain"></div>`);
                    var $RowD = $('<div class="row elRow"></div>');
                    $RowD.append(`<div class="col-xl-3 col-lg-6 col-md-6 col-sm-12"><span> Conceptos: </span><a >${row['no_conceptos']}</a></div>`);
                    $RowD.append(`<div class="col-xl-3 col-lg-6 col-md-6 col-sm-12"><span> Cuenta: </span><a >${row['cuenta_formato']}</a></div>`);
                    $RowD.append(`<div class="col-xl-3 col-lg-6 col-md-6 col-sm-12"><span> Km Anterior: </span><a> ${row['km_anterior']}   </a></div>`);
                    $RowD.append(`<div class="col-xl-3 col-lg-6 col-md-6 col-sm-12"><span> Km Actual: </span><a>${row['kilometraje']}  </a></div>`);
                    $RowD.append(`<div class="col-xl-4 col-lg-6 col-md-6 col-sm-12"><span> Entregó: </span><a> ${row['nombre_entrega']}  </a></div>`);
                    $RowD.append(`<div class="col-xl-4 col-lg-6 col-md-6 col-sm-12"><span> Ult. Serv: </span><a> ${row['fh_ultimo_servicio']}    </a></div>`);


                    $Main.append($RowD);
                    // $Main.append(`<a>   ${row['cuenta']}  </a>` );

                    $elDiv.append($Main);

                    return $elDiv.clone().html();
                },
            },
        ],

        initComplete: function (settings, json) {

            $(document).on("click", "a[id^=btnEditaTrabajo]", function (event) {
                var folio = $(this).data('folio');
                var prev = '/operacion/';
                var placa = $(this).data('placa');
                var kilometraje = $(this).data('kilometraje');
                var modelo = $(this).data('modelo');
                var nombre_entrega = $(this).data('nombre_entrega');
                var nombre_empresa = $(this).data('nombre_empresa');
                var row_num = $(this).data('row_num');
                location.href = `/ordeneditar/?prev=${prev}&prev_old=&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}&modelo=${modelo}&row_num=${row_num}&nombre_empresa=${nombre_empresa}`


            });

            $(document).on("click", "a[id^=btnNeumaticosAdmin]", function (event) {
                var placa = $(this).data('placa');
                sessionStorage.setItem('placa', placa);
                location.href = `/neumaticosadmin/`


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

                let prev = '/operacion/';
                location.href = `ordendetalle/?folio=${folio}&prev=${prev}&placa=&nombre_entrega=&modelo=&nom_empresa=&kilometraje=`
            });

            $(".status_filter").html(`<div class="filtros-status"></div>`);

            UnblockUI_();
        }
    });

    $('.filtros').on('change', function (event) {
        ajax_reload('#dataTables4');
        if ($(this).is(":checked")) var valor = '1'; else var valor = '0';
        setParametro($(this).data('cve_parametro'), valor);
    });

    $.fn.dataTable.ext.search.push(
        function (settings, searchData, index, rowData, counter) {
            var EnProceso, Terminados, Cancelados = false;
            EnProceso = $('#chkEnProceso').is(":checked") && (parseInt(rowData['status']) < 2);
            Terminados = $('#chkTerminados').is(":checked") && (parseInt(rowData['status']) == 2);
            Cancelados = $('#chkCancelados').is(":checked") && (parseInt(rowData['status']) == 3);
            // console.log({"EnProceso": EnProceso})
            // console.log({"Terminados": Terminados})
            // console.log({"Cancelados": Cancelados})

            return EnProceso || Terminados || Cancelados;

        }
    );

});

function UpdSitStatus(folio, status) {
    let parameters = {"folio": folio, "status": status}
    submit_with_ajax_json(`../stp/updsitorden/`, 'Notificación', '¿Inician los trabajos de la orden?', parameters, function (response) {
        var table = $('#dataTables4').DataTable();
        table.ajax.reload();
        // location.href =  '../operacion/';
    });
}