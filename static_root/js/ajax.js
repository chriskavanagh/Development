$(function(){

    $('#search').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "/articles/search/",    //or 'search/'
            data: { 
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'json'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').append('<li>'+data.title+'</li>');
}




// original code:

/*

$(function(){

    $('#search').keyup(function() {
    
        $.ajax({
            type: "POST",
            url: "search/",
            data: { 
                'search_text' : $('#search').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}

*/