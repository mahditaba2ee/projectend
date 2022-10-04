
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

    

function csrfSafeMethod(method) {
// these HTTP methods do not require CSRF protection
return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken",csrftoken);
    }
}
});



function usersended(btn){
    var iduser = btn.dataset.iduser
    var idorder = btn.dataset.idorder
    
    $.post('/category/sendorderuser/',{

        iduser : iduser,
        idorder : idorder
    },function(data){
        console.log(data)
        if (data['status']=='ok'){
            
            console.log(data)
            window.location.replace('/category/sendorder/')
            
        }
      })
    
}










var divsend=document.getElementById('send')
function sended(){
    divsend.style.display='none'
}
function sendedenter(){
    divsend.style.display='block'

}


// function checkbox(btn){
    

//     var id=btn.dataset.id
    
    
//     $.post('/category/sendorder/submit/',{

//         id : id,
    
//     },function(data){
//         console.log(data)
//         if (data['status']=='ok'){
            
            
//             window.location.replace('/category/sendorder/')
            
//         }
//       })
    
// }


function send_email(btn){

    
    $.post('/category/send/email/user/',{

        iduser : btn.dataset.id,
    },function(data){
        console.log(data)
        alert(data['status'])
      })



    sendemail
}