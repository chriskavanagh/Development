$(function() {
	
	$('#post-form').submit(function() {
		
		$.ajax({
			type: 'POST',
			url: '/create_post',
			data: {
				'post_text': $('#post-text').val(),
				'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
			},
			success: textSuccess,
			dataType: 'html'
			
	  });
	});    
 });

 
function textSuccess(data, textStatus, jqXHR) {
	$('#text-results').html(data);
}