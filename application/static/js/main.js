var bgIndex = 0;
var input = document.getElementsByTagName('input');

$(function(){
    $("#bg3").css('display', 'inline')
    setTimeout(function(){
      $("#bg3").fadeOut(2000);
      $("#bg1").fadeIn(2000);
      setInterval(bgChange, 4000)
    }, 2000)
})
function bgChange (){

    switch (bgIndex % 3) {
        case 0:
            $("#bg1").fadeOut(2000);
            $("#bg2").fadeIn(2000);
            break;
        case 1:
            $("#bg2").fadeOut(2000);
            $("#bg3").fadeIn(2000);
            break;
        case 2:
            $("#bg3").fadeOut(2000);
            $("#bg1").fadeIn(2000);
            break;
    }

    bgIndex++;
}
