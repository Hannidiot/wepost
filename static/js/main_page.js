function load_albums() {
    $.ajax({
        url: "/wepost/explore/albums/",
        type: "get",
        // on success
        success: function (response) {
            // update html
            $("#album").html(response)
        },
        // on error
        error: function (response) {
            // alert the error if any error occured
            console.log(response)
        }
    })
}

function load_most_liked() {
    $.ajax({
        url: "/wepost/trending/most_liked/",
        type: "get",
        // on success
        success: function (response) {
            // update html
            $("#most_liked_album").html(response)
        },
        // on error
        error: function (response) {
            // alert the error if any error occured
            console.log(response)
        }
    })
}