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