$(document).ready(function() {
    $("#about-btn").click( function(event) {

      msgstr = $("#msg").text();
      $("#msg").remove();
      h3 = document.createElement("h3");
      h3.innerHTML = msgstr;
      $(".ouch").append(h3);
    });
    $(".ouch").click( function(event) {
      alert("You clicked me! ouch!");
    });
    $("p").hover( function() {
      $(this).css('color', 'red');
      },
      function() {
      $(this).css('color', 'blue');
      });


});
