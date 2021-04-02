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
};
const csrftoken = getCookie('csrftoken');


$(document).ready(function() {
		// JQuery code to be added in here.

   $('#likes').click(function(){
     alert("Likes button clicked");
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
       };
     });
   });

   $("#suggestion").keyup(function(){
     var query;
     query = $(this).val();
     //alert("query: " + query)
     $.get("/rango/suggest/", {suggestion: query}, function(data){
       $("#cats").html(data);
     })
   });


})
