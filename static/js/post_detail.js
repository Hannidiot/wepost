function load_comments(post_id) {
    $.ajax({
        url: "/wepost/post/" + post_id + "/comments/",
        type: "get",
        success: function (response) {
            $("#comment_list").html(response)
        },
        error: function(response) {
            console.log(response)
        }
    })
}

function add_comment() {
    var post_id = $("#post_id").val();
    var content = $("#content").val();
    var token = $("[name='csrfmiddlewaretoken']").val();
    if (content != "") {
        $.ajax({
            url: "/wepost/post/" + post_id + "/add_comment/",
            type: "post",
            data: {
                content: content,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                if (response.status == "success") {
                    add_alert("add comment success!")
                    load_comments(post_id)
                }
                else {
                    add_alert(response.msg)
                }
            },
            error: function (response) {
                console.log(response.responseJSON)
            }
        })
    }
    $("#content").val("");
}
