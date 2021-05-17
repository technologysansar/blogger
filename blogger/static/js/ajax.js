$(function(){
	$('#search').keyup(function) {

		$.ajax({

			typpe:"POST",
			path: "/article/search/",
			data: {
				'search_text': $('#search').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType : 'html'
		});
	};


});

function searchSuccess(data, textStatus, jqXHR)
{
	$('#search-reasults').html(data);
}