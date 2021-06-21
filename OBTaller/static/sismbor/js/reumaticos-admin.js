function pValidaPlaca(placa) {

    var _parameters = {'placa': placa, 'action': 'searchdata', 'owner': 'neumaticos-admin'}
    if (placa.length > 0) {
        _ajax('/getInfoUnidad/', _parameters, function (data) {
            if (data.length > 0) {

                $("#edtMotor").val(data[0].motor);
                $("#edtMarca").val(data[0].marca);
                $("#edtModelo").val(data[0].modelo);
                $("#edtChasis").val(data[0].chasis);
                $("#edtChasis").val(data[0].chasis);


                $("#fh_alta_current").val(data[0].fh_alta_current);
                $("#kilometraje_current").val(data[0].kilometraje_current);
                $("#folio_current").val(data[0].folio_current);
                $("#nombre_entrega_current").val(data[0].nombre_entrega_current);

                $("#fh_salida_ult").val(data[0].fh_salida_ult);
                $("#kilometraje_ult").val(data[0].kilometraje_ult);
                $("#folio_ult").val(data[0].folio_ult);
                $("#nombre_entrega_ult").val(data[0].nombre_entrega_ult);

/*
                $("#edtUnidad").val(data[0].id_unidad);
                $("#edtEmpresa").val(data[0].nombre_empresa);
                $("#edtRup").val(data[0].rup);
                $("#edtTelefono").val(data[0].telefono_contacto);
                $("#edtCelular").val(data[0].celular_contacto);
                $("#edtDireccion").val(data[0].direccion);
                $("#edtRepresentante").val(data[0].nombre + ' ' + data[0].apellido);
                $("#edtEmail").val(data[0].correo_electronico);
                */

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

    $('#btnVerOrden').on('click', function (event) {
        var folio = $("#edtFolio").val();
        if (folio) {
            var prev = '/neumaticosadmin/';
            var placa = $("#edtPlaca").val();
            var kilometraje = $("#kilometraje").val();
            var nombre_entrega = $("#nombre_entrega").val()
            location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
        }

    });
});