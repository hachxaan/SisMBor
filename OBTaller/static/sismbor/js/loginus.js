"use strict"

$(function () {
"use strict"
    $('#btnEntrarOperador').on('click', function(e) {
        var cod_acceso = $('#cod_acceso').val();
        var _parameters =  {'cod_acceso': cod_acceso,
                            'action': 'loginus_oper'};

        lajax(_parameters, function(response) {
            var id_unidad_asigna = response['id_unidad_asigna'];
            var cod_acceso = response['cod_acceso'];
            sessionStorage.setItem('id_unidad_asigna', id_unidad_asigna)
            sessionStorage.setItem('cod_acceso', cod_acceso)
            location.href = '/registro/'
        });
    });
});


function xxx(){
"use strict"

}