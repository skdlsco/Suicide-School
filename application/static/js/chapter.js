function onLoad(ch) {
  $.ajax({
    type: "POST",
    url:"/chapter/getAfter",
    data: {'ch':ch},
    success: function(data) {
      if (data.status == true) {
        $("#after").css("display", "inline")
      }
    },
    error: function(data) {
      console.log(data);
    }
  })
}
