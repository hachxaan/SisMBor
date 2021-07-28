'use strict';
const cNameDT_PeajeDiario = '#dtPeajeDiario';
const cNameDT_PeajeMes = '#dtPeajeMensual';
const cNameDT_PeajeAnual = '#dtPeajeAnual';

const cNameDT_PeajeDiarioAcum = '#dtPeajeDiarioAcum';
const cNameDT_PeajeMesAcum = '#dtPeajeMensualAcum';
const cNameDT_PeajeAnualAcum = '#dtPeajeAnualAcum';

const DataTablesIniciales = {
        destroy: true,
        processing: false,
        ordering: true,
        responsive: false,
        autoWidth: false,
        selected: true,
        scrollY: "300px",
        ScrollX: "100%",
        paging: false,
        dom: 'rtip',
        info: false,
}


function pValidaPlaca(placa, id_unidad, cliente) {
    "use strict"
    if (placa.length > 0) {
        $('#edtPlaca').val(placa);
        $('#edtCliente').val(cliente);

        var fieldsColumsDiario = JSON.parse( sessionStorage.getItem('fieldsColumsDiario'));
        var fieldsColumsMes = JSON.parse( sessionStorage.getItem('fieldsColumsMes'));
        var fieldsColumsAno = JSON.parse( sessionStorage.getItem('fieldsColumsAno'));

        var fieldsColumsDiarioAcum = JSON.parse( sessionStorage.getItem('fieldsColumsDiarioAcum'));
        var fieldsColumsMesAcum = JSON.parse( sessionStorage.getItem('fieldsColumsMesAcum'));
        var fieldsColumsAnoAcum = JSON.parse( sessionStorage.getItem('fieldsColumsAnoAcum'));

        realoadDataDashboardPeaje(cNameDT_PeajeAnual, fieldsColumsAno,'anual', id_unidad, true, '');




    } else {
        message_error('Ingresa una descripción');
    }
}

function pTotales(id_unidad){
    var parameters = {
        "action": 'totales',
        "id_unidad": id_unidad
    }

    submit_with_ajax_action(parameters, function (response) {
        $('#edtAcumulado').val(response['acumulado']);
        $('#edtPromedio').val(response['promedio']);
    });
}

$(function () {
    $('#xxxxxxxxxxxxxxx').on('click', function(e) {
        var placa = $("#xxxxxxxxx").val();
        var id_personal = $("#xxxxxxxxxxx").val();
        var tx_referencia = $("#xxxxxxxxxxx").val();
    });
});

window.onload = function() {
    $(cNameDT_PeajeDiario).DataTable(DataTablesIniciales).clear().draw();
    $(cNameDT_PeajeMes).DataTable(DataTablesIniciales).clear().draw();
    $(cNameDT_PeajeAnual).DataTable(DataTablesIniciales).clear().draw();
    $(cNameDT_PeajeDiarioAcum).DataTable(DataTablesIniciales).clear().draw();
    $(cNameDT_PeajeMesAcum).DataTable(DataTablesIniciales).clear().draw();
    $(cNameDT_PeajeAnualAcum).DataTable(DataTablesIniciales).clear().draw();
}

function reloadGraficaDashboardDiario(tipo, id_unidad, ano_mes, container, titulo){

    var pathData = window.location.pathname + `data/${tipo}/${id_unidad}/${ano_mes}/`;
    $.getJSON( pathData, function (data) {
        Highcharts.chart(container, {
            chart: {
//                    zoomType: zoomType,
//                       type: 'spline',
//                       inverted: false
                    type: 'column'
            },
            title: {
                text: 'Diario',
            },
            subtitle: {
                text: titulo
            },
            xAxis: {
//                reversed: false,
//                type: 'datetime',
                categories: data['dias'],
                crosshair: true
            },
            yAxis: {
                title: {
                    text: 'Soles'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 1.5
                    },
                    lineWidth: 0,
                    states: {
                        hover: {
                            lineWidth: 1.5
                        }
                    },
                    threshold: null,
                },
                spline: {
                    marker: {
                        enable: true
                    },
                        fillColor: {
                            linearGradient: {
                                x1: 0,
                                y1: 0,
                                x2: 0,
                                y2: 1
                            },
                            stops: [
                                [0, Highcharts.getOptions().colors[0]],
                                [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                            ]
                        },
                    marker: {
                        radius: 1.5
                    },
                    lineWidth: .8,
                    states: {
                        hover: {
                            lineWidth: 1.5
                        }
                    },
                    threshold: null,
                }

            },
            series: [
                {

                    name: '',
                    data: data['data']
                }
//                {
//                    type: 'spline',
//                    name: sensor_name,
//                    data: data['data']
//                }
            ],
        });
    });
}


function reloadGraficaDashboardPeajeMensual(tipo, id_unidad, ano, container, titulo) {
//GraficaPromedioAnual
    var pathData = window.location.pathname + `data/${tipo}/${id_unidad}/${ano}/`;

    $.getJSON( pathData,
        function (data) {
            Highcharts.chart(container, {
            chart: { type: 'column' },
            title: { text: titulo },
            subtitle: { text: 'Mensual' },
            xAxis: {
                categories: [
                    'Enero',
                    'Febrero',
                    'Marzo',
                    'Abril',
                    'Mayo',
                    'Junio',
                    'Julio',
                    'Agosto',
                    'Septiembre',
                    'Octubre',
                    'Noviembre',
                    'Diciembre'
                ],
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: { text: 'Promedio (Soles)' }
            },
            legend: { enabled: false },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                    '<td style="padding:0"><b>S./{point.y:.1f}</b></td></tr>',
                footerFormat: '</table>',
                shared: true,
                useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                    borderWidth: 0
                }
            },
            series: [{
                name: '',
                data: data
            },
            ]
        });
    });

}

function realoadDataDashboardPeaje(element, fieldsColums, tipo, id_unidad, select, filtro) {

    var dataTable = $(element).DataTable({
        destroy: true,
        processing: false,
        ordering: true,
        responsive: false,
        autoWidth: false,
        selected: true,
        scrollY: "300px",
        ScrollX: "100%",
        paging: false,
        dom: 'rtip',
        info: false,
        columns: fieldsColums,
        ajax: {
                    url: window.location.pathname,
                    type: 'POST',
                    beforeSend: function (request) {
                        request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    },
                    complete: function (response) {

                        /********************** P R O M E D I O **********************/
                        if (response['responseJSON'].hasOwnProperty('msgInfo')) {
                            message_info(response['responseJSON']['msgInfo']);
                            $(cNameDT_PeajeDiario).DataTable().clear().draw();
                            $(cNameDT_PeajeMes).DataTable().clear().draw();
                            $(cNameDT_PeajeAnual).DataTable().clear().draw();
                            $(cNameDT_PeajeDiarioAcum).DataTable().clear().draw();
                            $(cNameDT_PeajeMesAcum).DataTable().clear().draw();
                            $(cNameDT_PeajeAnualAcum).DataTable().clear().draw();
                            GraficaVacia(GraficaPromedio);
                            GraficaVacia(GraficaAcumulado);
                            $('#edtAcumulado').val('');
                            $('#edtPromedio').val('');
                        } else {

                            if (element == cNameDT_PeajeAnual){

                                pTotales(id_unidad);
                                var ano = dataTable.row('0').data()['ano'];
                                var fieldsColumsMes = JSON.parse( sessionStorage.getItem('fieldsColumsMes'));
                                var fieldsColumsAnoAcum = JSON.parse( sessionStorage.getItem('fieldsColumsAnoAcum'));
                                realoadDataDashboardPeaje(cNameDT_PeajeMes, fieldsColumsMes,'mensual', id_unidad, true, ano);
                                realoadDataDashboardPeaje(cNameDT_PeajeAnualAcum, fieldsColumsAnoAcum,'anual_acum', id_unidad, true, '');
                            }
                            if (element == cNameDT_PeajeMes){
                                var ano_mes = dataTable.row('0').data()['mes'];
                                var fieldsColumsDiario = JSON.parse( sessionStorage.getItem('fieldsColumsDiario'));
                                realoadDataDashboardPeaje(cNameDT_PeajeDiario, fieldsColumsDiario, 'diario', id_unidad, false, ano_mes);
                                reloadGraficaDashboardDiario('diario_promedio',  id_unidad, ano_mes, 'GraficaPromedio', 'Promedio '+ano_mes);
                            }
                            $(element+' tbody').on('click', 'tr', function () {
                                if (element == cNameDT_PeajeMes){
                                    var ano_mes = dataTable.row( this ).data()['mes'];
                                    var fieldsColumsDiario = JSON.parse( sessionStorage.getItem('fieldsColumsDiario'));
                                    realoadDataDashboardPeaje(cNameDT_PeajeDiario, fieldsColumsDiario, 'diario', id_unidad, false, ano_mes);
                                    if( $("#CheckDiarioProm:radio").is(':checked')) {
                                        reloadGraficaDashboardDiario('diario_promedio',  id_unidad, ano_mes, 'GraficaPromedio', 'Promedio '+ano_mes);
                                    } else {
                                        var ano_mes_split = ano_mes.split('-')
                                        var ano = ano_mes_split[0]
                                        reloadGraficaDashboardPeajeMensual('mensual_promedio', id_unidad, ano, 'GraficaPromedio', 'Mensual Promedio ' +ano);
                                    }
                                }
                            } );
                            /********************** A C U M U L A D O **********************/
                            if (element == cNameDT_PeajeAnualAcum){
                                var ano = dataTable.row('0').data()['ano'];
                                var fieldsColumsMesAcum = JSON.parse( sessionStorage.getItem('fieldsColumsMesAcum'));
                                realoadDataDashboardPeaje(cNameDT_PeajeMesAcum, fieldsColumsMesAcum,'mensual_acum', id_unidad, true, ano);

                            }
                            if (element == cNameDT_PeajeMesAcum){
                                var ano_mes = dataTable.row('0').data()['mes'];
                                var fieldsColumsDiarioAcum = JSON.parse( sessionStorage.getItem('fieldsColumsDiarioAcum'));
                                realoadDataDashboardPeaje(cNameDT_PeajeDiarioAcum, fieldsColumsDiarioAcum, 'diario_acum', id_unidad, false, ano_mes);
                                reloadGraficaDashboardDiario('diario_acumulado',  id_unidad, ano_mes, 'GraficaAcumulado', 'Acumulado '+ano_mes);
                            }
                            $(element+' tbody').on('click', 'tr', function () {
                                if (element == cNameDT_PeajeMesAcum){
                                    var ano_mes = dataTable.row( this ).data()['mes'];
                                    var fieldsColumsDiarioAcum = JSON.parse( sessionStorage.getItem('fieldsColumsDiarioAcum'));
                                    realoadDataDashboardPeaje(cNameDT_PeajeDiarioAcum, fieldsColumsDiarioAcum, 'diario_acum', id_unidad, false, ano_mes);
                                    if( $("#CheckDiarioAcum:radio").is(':checked')) {
                                        reloadGraficaDashboardDiario('diario_acumulado',  id_unidad, ano_mes, 'GraficaAcumulado', 'Acumulado '+ano_mes);
                                    } else {
                                        var ano_mes_split = ano_mes.split('-')
                                        var ano = ano_mes_split[0]
                                        reloadGraficaDashboardPeajeMensual('mensual_acumulado', id_unidad, ano, 'GraficaAcumulado', 'Acumulado ' +ano);
                                    }
                                }
                            } );
                        }
                    },
                    data: {
                        'action': 'searchdata',
                        'vista': tipo,
                        'id_unidad': id_unidad,
                        'filtro': filtro
                    },
                    dataSrc: ""
                },
        columnDefs: [
            {
                targets: [0],
                render: function (data, type, row) {
                    if (element == cNameDT_PeajeDiario || element == cNameDT_PeajeDiarioAcum){
                        console.log(data)
                        return data.substring(0,10)
                    } else {
                        return data
                    }
                }
            }
            ],
        initComplete: function (settings, json) {
            console.log('initComplete');
            /* SELECCIONAR EL PRIMERO */
            if (select) {
                dataTable.row(':eq(0)').select();
            }

        }
    });
};


function GraficaVacia(container){

        Highcharts.chart(container, {
            chart: {
                    type: 'column'
            },
            title: {
                text: '',
            },
            subtitle: {
                text: ''
            },
            xAxis: {
//                reversed: false,
//                type: 'datetime',
                categories: [],
                crosshair: true
            },
            yAxis: {
                title: {
                    text: 'Soles'
                }
            },
            legend: {
                enabled: false
            },
            plotOptions: {
                area: {
                    fillColor: {
                        linearGradient: {
                            x1: 0,
                            y1: 0,
                            x2: 0,
                            y2: 1
                        },
                        stops: [
                            [0, Highcharts.getOptions().colors[0]],
                            [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                        ]
                    },
                    marker: {
                        radius: 1.5
                    },
                    lineWidth: 0,
                    states: {
                        hover: {
                            lineWidth: 1.5
                        }
                    },
                    threshold: null,
                },
                spline: {
                    marker: {
                        enable: true
                    },
                        fillColor: {
                            linearGradient: {
                                x1: 0,
                                y1: 0,
                                x2: 0,
                                y2: 1
                            },
                            stops: [
                                [0, Highcharts.getOptions().colors[0]],
                                [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                            ]
                        },
                    marker: {
                        radius: 1.5
                    },
                    lineWidth: .8,
                    states: {
                        hover: {
                            lineWidth: 1.5
                        }
                    },
                    threshold: null,
                }

            },
            series: [
                {

                    name: '',
                    data: []
                }

            ],
        });

}
