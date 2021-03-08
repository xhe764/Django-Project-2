function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


$(document).ready(function() {
		// JQuery code to be added in here.
		$('#likes').click(function(){
		var catid;
		catid = $(this).attr("data-catid");

    $.get('/rango/like/', {category_id: catid}, function(data){
      likes=Number(data)
      if(!isNaN(likes)){
        $('#like_count').html(data);
        $('#likes').hide();
      }else{
        $('#likes').hide();
        $('#liked').css("display", "block");
        $('#liked').html(data);
      }
    });
	 });

   $('button.addpage').click(function(){

     var page_url, page_title, page_cat, cat_name;
     page_url = $(this).attr("data-url");
     page_title = $(this).attr("data-title");
     page_cat = $(this).attr("data-cat");
     cat_name = $(this).attr("cat-name");
    // data = ;
     $.ajax({
         url: '/rango/add_page_button/', //The "/" at the end is necessary
         beforeSend: function (xhr) {
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
         data: {
           page_url: page_url,
           page_title: page_title,
           page_cat: page_cat,
           cat_name: cat_name
         },
         datatype: 'json',
         type: 'POST',
         error: function(res){
           alert("Error: " + res.status)
         }
       });
   })

   $("#suggestion").keyup(function(){
     var query;
     query = $(this).val();
     //alert("query: " + query)
     $.get("/rango/suggest/", {suggestion: query}, function(data){
       $("#cats").html(data);
     })
   })


})
