$(function () {
    'use strict';
    $('form').on('submit', function (e) {
        console.log('ready...302');
            e.preventDefault();
            console.log('ready...303');
            // var parameters = new FormData(this);
            var placa = $('#edtPlaca').val();
            var kilometraje = $('#kilometraje').val();
            var nombre_entrega = $('#nombre_entrega').val();
            var parameters = {"placa": placa, "kilometraje" : kilometraje, "nombre_entrega": nombre_entrega}
            console.log('parameters: ', parameters)

            _ajax('../stp/insorden/', parameters, function(response){
                 location.href =  '../operacion/';
            });
            // submit_('../stp/insorden/', 'Notificación', '¿Crear nueva orde? Placa: '+placa, parameters, function (response) {
            //     location.href =  '../operacion/';
            // });
        });
    $("#edtPlaca").change(function (e) {
        pValidaPlaca($(this).val());
    });
    $('#btnNuevaUnidadOrden').on('click', function (e) {
        console.log('ready...301');
            location.href =  '../unidad/add/?orden=true';
        });
    $(document).ready(function () {
        console.log('ready...');
        console.log($("#edtPlaca").val());
        console.log('ready...2');
        if ($("#edtPlaca").val() !== '') {
            console.log('pValidaPlaca...');
            pValidaPlaca($("#edtPlaca").val());
        }
        console.log('ready...3');
    });
});

function pValidaPlaca( placa ){

        var _parameters = {'placa' : placa, 'action': 'searchdata'}
        if ( placa.length > 0 ){
            _ajax('getInfoUnidad/', _parameters, function (data) {
                 if (data.length > 0) {

                    $("#edtPlaca").addClass('bg-olive');
                    $("#edtMotor").val(data[0].motor);
                    $("#edtMarca").val(data[0].marca);
                    $("#edtModelo").val(data[0].modelo);
                    $("#edtChasis").val(data[0].chasis);

                    $("#edtUnidad").val(data[0].id_unidad);
                    $("#edtEmpresa").val(data[0].nombre_empresa);
                    $("#edtRup").val(data[0].rup);
                    $("#edtTelefono").val(data[0].telefono_contacto);
                    $("#edtCelular").val(data[0].celular_contacto);
                    $("#edtDireccion").val(data[0].direccion);
                    $("#edtRepresentante").val(data[0].nombre + ' ' + data[0].apellido);
                    $("#edtEmail").val(data[0].correo_electronico);
                    $("#edtKilometraje").focus();

                 } else {
                    $("#edtPlaca").removeClass('bg-olive');
                    $("#edtMotor").val('');
                    $("#edtMarca").val('');
                    $("#edtModelo").val('');
                    $("#edtChasis").val('');


                    $("#edtUnidad").val('');
                    $("#edtEmpresa").val('');
                    $("#edtRup").val('');
                    $("#edtTelefono").val('');
                    $("#edtCelular").val('');
                    $("#edtDireccion").val('');
                    $("#edtRepresentante").val('');
                    $("#edtEmail").val('');
                 }
            });
        } else
        {
            message_error('Ingresa una descripción');
        }
    }