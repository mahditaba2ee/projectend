
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


function btn_sumbit(btn){
    // alert(btn.dataset.id)
$.post('/category/sendorder/',{

    id : btn.dataset.id,
    
},function(data){
      
    if(data['status']=='not_net'){
        message.hidden=false
        message.innerHTML='اینترنت در دسترس نیست یا ارتباط با سرور برقرار نشده است '
        
        
    }
    if(data['all']==1){
        message.hidden=false
        message.innerHTML=('همه محصولات سبد خرید برای شما است و سبد در بایگانی شما ذخیره شده است')
        
        
    }
    if (data['status']=='ok'){
        window.location.replace('/category/sendorder/')
              
    }
})
}

