// // AJAX CODE
// function sendAJAXReq() {
//     var myRequest = new XMLHttpRequest();
//     myRequest.open('GET', 'https://codepen.io/hsoubacadimyweb/pen/eYYWdvm.html');
//     myRequest.onreadystatechange = function () { 
//         if (myRequest.readyState === 4) {
//         document.getElementById('ajax-content').innerHTML = myRequest.responseText;
//         }
//     };
//     myRequest.send();
//     document.getElementById('reveal').style.display = 'none';
// }

$(document).ready(function(){
    $("button").click(function(){
        $(document).ajaxStart(function(){
            $("#wait").css("display", "block");
        });
        $(document).ajaxComplete(function(){
            $("#wait").css("display", "none");
        });
        $("#ajax-content").load("https://i.ibb.co/s5BMyjb/wallpaperbetter.jpg");// رابط اخر
        $("#reveal").css("display", "none");
    });
});
