$(function () {
    'use strict';
    $('form').on('submit', function (e) {

            e.preventDefault();
            var placa = $('#edtPlaca').val();
            var kilometraje = $('#kilometraje').val();
            var nombre_entrega = $('#nombre_entrega').val();
            var parameters = {"placa": placa, "kilometraje" : kilometraje, "nombre_entrega": nombre_entrega}


            _ajax('../stp/insorden/', parameters, function(response){
                 location.href =  '../operacion/';
            });

        });
    $("#edtPlaca").change(function (e) {
        pValidaPlaca($(this).val());
    });
    $('#btnNuevaUnidadOrden').on('click', function (e) {
            location.href =  '../unidad/add/?orden=true';
        });
    $(document).ready(function () {
        if ($("#edtPlaca").val() !== '') {

            pValidaPlaca($("#edtPlaca").val());
        }
    });
    $('#btnVerOrden').on('click', function (event) {
        var folio = $("#edtFolio").val();
        if (folio) {
            var prev = '/ordennueva/';
            var placa = $("#edtPlaca").val();
            var kilometraje = $("#kilometraje").val();
            var nombre_entrega = $("#nombre_entrega").val()
            // location.href =  `/ordendetalle/?prev=${prev}&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
            location.href =  `/ordendetalle/?prev=/ordennueva/&folio=${folio}&placa=${placa}&kilometraje=${kilometraje}&nombre_entrega=${nombre_entrega}`;
        }

    });

});

function pValidaPlaca( placa ){

        var _parameters = {'placa' : placa, 'action': 'searchdata'}
        if ( placa.length > 0 ){
            _ajax('/getInfoUnidad/', _parameters, function (data) {
                 if (data.length > 0) {

                    $("#edtPlaca").addClass('bg-success');
                    $("#edtMotor").val(data[0].motor);
                    $("#edtMarca").val(data[0].marca);
                    $("#edtModelo").val(data[0].modelo);
                    $("#edtChasis").val(data[0].chasis);

                    if (data[0].folio) {
                        $("#edtFolio").val(data[0].folio);
                        $("#edtFhUltSer").val(data[0].fh_salida);
                        $("#edtKmUltSer").val(data[0].kilometraje);
                        $("#edtRespUltSer").val(data[0].nombre_entrega);


                    } else {
                        $("#edtFolio").val('');
                        $("#edtFhUltSer").val('');
                        $("#edtKmUltSer").val('');
                        $("#edtRespUltSer").val('');
                    }



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
                    $("#edtPlaca").removeClass('bg-success');
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