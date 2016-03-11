$(document).ready(function() {
	var $orders = $('#orders');
	
	$('#add-order').click(function(){
		//console.log('am i called');
		
	$.ajax({
		type: "POST",
		url: "/testing/orders/",
		dataType: "json",
		data: {
			"name": $("#name").val(),
			"drink": $("#drink").val(),
			'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
		},
		success: function(data) {
			$orders.append('<li>name: '+data.name+', drink: '+data.drink+'</li>');
			console.log(data);
			
		   }
	   });
	});
});