function add_alert(content) {
    $("#alert_container").append(`
        <div class="alert alert-info alert-dismissible fade show col-sm-8 mt-1" role="alert" id="alert">
           ` + content + `
           <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>`
    );
}

function like(post_id) {
    var token = $("[name='csrfmiddlewaretoken']").val();
    $.ajax({
        url: "/wepost/post/" + post_id + "/like/",
        type: "post",
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            if (response.status == "success") {
                $("#like_img_" + post_id).attr("src", "/static/images/svg/unlike.svg");
                $("#like_img_" + post_id).attr("onclick", "unlike(" + post_id + ")");
                var like_cnt = parseInt($("#like_cnt_" + post_id).text());
                $("#like_cnt_" + post_id).text(like_cnt + 1);
            }
            else {
                add_alert(response.msg)
            }
        },
        error: function (response) {
            add_alert("Please Login first!")
        }
    })
}

function unlike(post_id) {
    var token = $("[name='csrfmiddlewaretoken']").val();
    $.ajax({
        url: "/wepost/post/" + post_id + "/unlike/",
        type: "post",
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            if (response.status == "success") {
                $("#like_img_" + post_id).attr("src", "/static/images/svg/like.svg");
                $("#like_img_" + post_id).attr("onclick", "like(" + post_id + ")");
                var like_cnt = parseInt($("#like_cnt_" + post_id).text());
                $("#like_cnt_" + post_id).text(like_cnt - 1);
            }
            else {
                add_alert(response.msg)
            }
        },
        error: function (response) {
            add_alert("Please Login first!")
        }
    })
}

function follow(user_id) {
    var token = $("[name='csrfmiddlewaretoken']").val();
    $.ajax({
        url: "/accounts/" + user_id + "/follow/",
        type: "post",
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            if (response.status == "success") {
                $("#btn_follow").text("Following");
                $("#btn_follow").removeClass("btn-primary");
                $("#btn_follow").addClass("btn-secondary");
                $("#btn_follow").attr("onclick", "unfollow(" + user_id + ")");
            }
            else {
                add_alert(response.msg)
            }
        },
        error: function (response) {
            add_alert("Please Login first!")
        }
    })
}

function unfollow(user_id) {
    var token = $("[name='csrfmiddlewaretoken']").val();
    $.ajax({
        url: "/accounts/" + user_id + "/unfollow/",
        type: "post",
        data: {
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            if (response.status == "success") {
                $("#btn_follow").text("Follow");
                $("#btn_follow").removeClass("btn-secondary");
                $("#btn_follow").addClass("btn-primary");
                $("#btn_follow").attr("onclick", "follow(" + user_id + ")");
            }
            else {
                add_alert(response.msg)
            }
        },
        error: function (response) {
            add_alert("Please Login first!")
        }
    })
}