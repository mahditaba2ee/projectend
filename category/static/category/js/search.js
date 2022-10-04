var list_nav = document.getElementById('list_nav')
list_nav.classList.add('active_nav')



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




function btn(btn,type){
    
    if(type=='like'){
        
    const request = new XMLHttpRequest()
    request.open('POST',"/category/like/")
    request.setRequestHeader("X-CSRFToken",csrftoken)
    request.onload = function(){
        const response = JSON.parse(this.responseText)
        if (response['status'] == 'like'){
            btn.dataset.is_like = 'dislike'
            btn.classList.add("active")
        }
        if (response['status'] == 'dislike'){
            btn.dataset.is_like = 'like'
            
            btn.classList.remove('active');
            // var t = document.getElementById('s')
            
        }
    }


    
    const formdata=new FormData()
    formdata.append("id",btn.dataset.id)
    formdata.append("is_like",btn.dataset.is_like)

    request.send(formdata)
    }
}
var times = 0;
function sendproduct(btn){
    
    message.hidden=true

    var slug=btn.dataset.slug
    var name = btn.dataset.name
    var id=btn.dataset.id
    var status = btn.dataset.status
    if (status =='buy'){
    var number = 1

    $.post('/category/card/add/',{

        slug:slug,
        number:number,

    },function(data){
        console.log(data)
        if (data['status']=='ok'){
            btn.classList.add("active")
            var message = document.getElementById('message')
            message.hidden=false
            message.innerHTML=name +' '+ 'در سبد خرید ثبت شد'
            btn.dataset.status = 'sell'

            setInterval(()=>{
                message.hidden=true
            },5000)
        }
      })
    
}
if (status =='sell'){
    $.post('/category/card/remove/',{

        id:id,

    
    },function(data){
        console.log(data)
        if (data['status']=='ok'){
            btn.dataset.status = 'buy'
            btn.classList.remove("active")

        }
      })

}}





