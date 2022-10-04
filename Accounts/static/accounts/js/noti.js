

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



function btnsubmit(btn)
{
    var order_id = btn.dataset.id
    
    
    $.post('/category/sendorder/submit/',{
        
        id:order_id,

},function(data){
    if(data['status']== 'ok'){
        window.location.replace('/accounts/notification')

    }
    

})

}

function btnback(btn)
{
    var order_id = btn.dataset.id
    
    
    $.post('/category/sendorder/back/',{
        
        id:order_id,

},function(data){
    if(data['status']== 'ok'){
        window.location.replace('/accounts/notification')

    }
    

})

}



