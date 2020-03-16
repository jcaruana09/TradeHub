$( document ).ready(function() {
  $(".stocks-container input").on('keydown', function() {
    $.getJSON("/filter_data", {
      filterVal: $(".stocks-container input").val(),
    }, function(data) {
      $("#result").text(data.result)
      console.log(data.result)
    });
    return false
  });
});