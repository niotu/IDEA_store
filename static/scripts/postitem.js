function postitem() {
  $('#myform').find('.captureInput').each(function() {
    console.log($(this).val());
  });
}