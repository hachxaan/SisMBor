(function ($) {
    "use strict"
    const csrftoken = getCookie('csrftoken');
    const urlParams = new URLSearchParams(window.location.search);
    $("#btnResetColumns").on('click', function (e) {
        confirmar_accion('Confirmación', '¿Reiniciar el orden de las columnas?',
            function () {
                var table = $('#data').DataTable();
                table.colReorder.reset();
            });
    });
    /******************************************************************************************************************/
    /******************************************************************************************************************/
    $("#btnCerrarConciliacion").on('click', function (e) {
        const idrenc = urlParams.get('idrenc');
        var parameters = {'idrenc': idrenc};
        ajax_confirm("../cerrarConciliacion/", 'Notificación',
            '¿Cerrar conciliación? La conciliación se pasará a estus Conculiado y revisado.', parameters,
            function (response) {
                location.href = `../cbsres/?idrenc=${response['idrenc']}`;
                return false;
            });
    });
    /******************************************************************************************************************/
    /******************************************************************************************************************/
    $("#btnConciliar").on('click', function () {
        const idrenc = urlParams.get('idrenc');
        var parameters = {'idrenc': idrenc, "sobreescribir": 'false'};
        ajax_confirm("../conciliarSaldos/", 'Notificación',
            '¿Ejecutar el proceso de conciliación?', parameters,
            function (response) {
                if (response.hasOwnProperty('idrenc')) {
                    location.href = `../cbsres/?idrenc=${response['idrenc']}`;
                    return false;
                }
                if (response.hasOwnProperty('existe_info')) {
                    const mensaje = `<label> ${response['existe_info']}</label><p class="m-0">Generado por:</p>  <label class="m-0">Usuairo: <strong> ${response['idusucons']}</strong></label><label>Fecha: <strong> ${response['fechacons']}</strong></label> `
                    ajax_confirm("../conciliarSaldos/", 'Confirmación',
                        mensaje, {'idrenc': idrenc, "sobreescribir": 'true'},
                        function (response) {
                            location.href = `../cbsres/?idrenc=${response['idrenc']}`;
                        });
                    return false;
                }
                if (response.hasOwnProperty('info')) {
                    message_info(response['info'], null, null)
                    return false;
                }
            });
    });
    /******************************************************************************************************************/
    /******************************************************************************************************************/
    $(".getanomes").change(function () {
        var bco = '';
        var cta = '';
        bco = $("#id_codbanco").val();
        cta = $("#id_nrocuenta").val();
        if ((bco != '') && ((cta != ''))) {
            $.ajax({
                method: 'GET',
                beforeSend: function (request) {
                    request.setRequestHeader("X-CSRFToken", csrftoken);
                },
                url: '/getAnoMes',
                data: {'banco': bco, 'cuenta': cta},
                success: function (respons) {
                    if (respons) {
                        $("#id_ano").val(respons.ano);
                        $("#id_mes").val(respons.mes);
                    } else {
                        $("#id_ano").val('2021');
                        $("#id_mes").val('4')
                    }
                },
                error: function (data) {
                }
            });
        }
    });

})(jQuery);
