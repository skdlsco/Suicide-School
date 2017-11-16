function onClick() {
  var id = $("#id").val()
  var password = $("#password").val()
  var passwordCheck = $("#passwordCheck").val()
  if (password != passwordCheck) {
    return;
  }
  $.ajax({
    type: "POST",
    url:"/auth/signup",
    data: {'id' : $("#id").val(), 'password' : $("#password").val()},
    success: function(data) {
      if (data.status == true){
        location.replace("http://soylatte.kr:4102/auth/login")
      }
    },
    error: function(data) {
      console.log(data);
    }
  })
}
