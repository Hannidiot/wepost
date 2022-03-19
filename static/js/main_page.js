function load_albums() {
    $.ajax({
        url: "{% url 'vali' %}",
        type = "POST",
        data = {

        },
        // on success
        success: function (response) {
            // update html
            $('#album').html(response)

        },
        // on error
        error: function (response) {
            // alert the error if any error occured
            console.log(response.responseJSON.errors)
        }
    });
}