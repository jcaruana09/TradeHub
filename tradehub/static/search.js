$( document ).ready(function() {
  $("#search").on('click', function() {
    $(".stocks-container").html('');
    $.getJSON("/filter_data", {
      filtervalue: $("input[name='filtervalue']").val(),
    }, function(data) {
      $.each(data.result, function(i) {
        $(".stocks-container").append(`<div class="stock-card"><h5>${data.result[i].name}</h5><a>${data.result[i].symbol}</a></div>`);
      });
    });
    return false;
  });
});