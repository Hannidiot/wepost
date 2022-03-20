function load_content(user_id, type) {
    $.ajax({
        url: "/accounts/" + user_id + "/" + type + "/",
        type: "get",
        // on success
        success: function (response) {
            // update html
            $("#content").html(response)
            $(".active").removeClass("active")
            $("#" + type + "_page").addClass("active")
        },
        // on error
        error: function (response) {
            // alert the error if any error occured
            console.log(response)
        }
    })
}
