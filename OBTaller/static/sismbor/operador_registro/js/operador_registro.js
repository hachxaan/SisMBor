$(function () {

    $(document).on("click", "a[id^=btnVerFoto]", function (event) {
            var img_ticket = $(this).data('img_ticket');
            $('#img_ticket').attr('src', `https://img-sismbor.s3.us-east-2.amazonaws.com${img_ticket}`);
            $('#imgModal').modal('show');
    });

});
