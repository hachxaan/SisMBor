function pValidaPlaca(placa) {

    var _parameters = {'placa': placa, 'action': 'searchdata'}
    if (placa.length > 0) {
        _ajax('/getInfoUnidad/', _parameters, function (data) {
            if (data.length > 0) {

                // $("#edtPlaca").addClass('bg-olive');
                $("#edtMotor").val(data[0].motor);
                $("#edtMarca").val(data[0].marca);
                $("#edtModelo").val(data[0].modelo);
                $("#edtChasis").val(data[0].chasis);
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
                // $("#edtPlaca").removeClass('bg-olive');
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
    } else {
        message_error('Ingresa una descripción');
    }


}


$(function () {


});