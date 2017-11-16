function onClick() {
  $.ajax({
    type: "POST",
    url:"/auth/login",
    data: {'id' : $("#id").val(), 'password' : $("#password").val()},
    success: function(data) {
      if (data.status == true){
        location.replace("http://soylatte.kr:4102/chapter")
      }else{
        alert("로그인 실패")
      }
    },
    error: function(data) {
      console.log(data);
    }
  })
}
