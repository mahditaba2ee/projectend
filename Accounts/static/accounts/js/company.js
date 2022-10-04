

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

var filebu = document.getElementById('filebu')

var message = document.getElementById('message')
function btnshow(btn)
{
    var filebu = document.getElementById('filebu')
    console.log(filebu)
    alert('s')
    var id = btn.dataset.id
    $.post('/accounts/company/sumbit/',{
        
        


},function(data){
    alert('s')
  if (data['status'=='ok']){
    message.hidden=false
    message.innerHTML='درخواست شما ثبت شد '
  }
  if (data['status'=='false']){
    alert('r')
    message.hidden=false
    message.innerHTML='درخواست شما قبلا ثبت شده است یا سرور با خطا مواجه شده است'
  }

})

}