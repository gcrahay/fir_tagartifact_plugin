function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}


$(function() {
	$('#add-tag').on('click', function(e) {
		e.preventDefault();
		ajax_action($(this), add_tag);
	});

	$('#tag_modals').on('click', '#submit-tag', function(e) {
		e.preventDefault();
		submit_tag();
	});
});

function ajax_action(elt, callback) {

	$.ajax({
		url: elt.data('url'),
		headers: {'X-CSRFToken': getCookie('csrftoken')},
	}).success(function(data) {
		callback(data);
	});
}

function add_tag(data) {
	$("#tag_modals").empty();
	$("#tag_modals").html(data);
	$("#addTag").modal('show');
	$("#id_name").focus();
}

function submit_tag () {
	data = $("#tag_form").serialize()

	$.ajax({
		type: 'POST',
		url: $("#tag_form").attr('action'),
		data: data,
		headers: {'X-CSRFToken': getCookie('csrftoken')},
		success: function (msg) {

			if (msg.status == 'success') {
                $("#addTag").modal('hide');
				window.location = window.location;
			}

			else if (msg.status == 'error') {
				html = $.parseHTML(msg.data);
				$("#addTag .modal-body").html($(html).find('.modal-body'));
			}
		}
	})
}