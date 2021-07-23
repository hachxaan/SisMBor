$(function () {

    $(document).on("click", "a[id^=btnVerFoto]", function (event) {
            var img_ticket = $(this).data('img_ticket');
            $('#img_ticket').attr('src', `../${img_ticket}`);
            $('#imgModal').modal('show');
    });



});