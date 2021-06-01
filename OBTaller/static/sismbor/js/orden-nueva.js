$(function () {
    'use strict';

    $('form').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);
            console.log('parameters: ', parameters)
            submit_with_ajax('../stp/insorden/', 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
                console.log('response: ', response)
                // location.href = '{{ list_url }}';
            });
        });
    // $("#btnCreaOrden").on('click', function (e) {
    //
    //     // if () {
    //     //
    //     // }
    //      Swal.fire({
    //                 title: 'Prueba!',
    //                 html: 'OK',
    //                 icon: 'success'
    //             });
    //
    // })


    $("#edtPlaca").change(function (e) {

        var v_placa = $(this).val()
        var _parameters = {'placa' : v_placa, 'action': 'searchdata'}
        if ( v_placa.length > 0 ){
            _ajax('getInfoUnidad/', _parameters, function (data) {

                 console.log(data);
                 if (data.length > 0) {

                    $("#edtPlaca").addClass('bg-olive');
                    $("#edtMotor").val(data[0].motor);
                    $("#edtMarca").val(data[0].marca);
                    $("#edtModelo").val(data[0].modelo);
                    $("#edtChasis").val(data[0].chasis);


                    $("#id_uniadad").val(data[0].id_uniadad);
                    $("#edtEmpresa").val(data[0].nombre_empresa);
                    $("#edtRup").val(data[0].rup);
                    $("#edtTelefono").val(data[0].telefono_contacto);
                    $("#edtCelular").val(data[0].celular_contacto);
                    $("#edtDireccion").val(data[0].direccion);
                    $("#edtRepresentante").val(data[0].nombre + ' ' + data[0].apellido);
                    $("#edtEmail").val(data[0].correo_electronico);


                 } else {
                    $("#edtPlaca").removeClass('bg-olive');
                 }


             // $('#id_id_tipo_servicio').append(`<option value="${data['id_tipo_servicio']}">${ data['desc_tipo_servicio'] }</option>'`)
                // $('#id_id_tipo_servicio').val(data['id_tipo_servicio'])
                // $("#edtDescTipoServicio").empty()
                // $("#NuevoTipoServicio").modal('hide');
            });
        } else
        {
            message_error('Ingresa una descripción');
        }
    });

});