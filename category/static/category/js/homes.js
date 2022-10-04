var home_nav = document.getElementById('home_nav')
home_nav.classList.add('active_nav')



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
        console.log(this.responseText)
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






let slidindex = 1;
function setslide(input,index){
    
    
    slidindex = index;
    let item = document.getElementById(input)
    let btns =[...document.querySelector('.btns').children]
    btns.forEach((btn)=>{
        btn.classList.remove('active')
    })
    let btnactive = document.getElementById('btn'+slidindex)
    btnactive.classList.add('active')
  
    let slids = [...document.querySelector('.slids').children]
    slids.forEach((element)=>{
        element.classList.remove('active');
    })
    item.classList.add('active')


}
setInterval(()=>{
    slidindex +=1;
    if (slidindex ==4){
        slidindex =1;
    }
    setslide('slid'+slidindex,slidindex)
},10000)

let remingingtime =6980 
function time()
{
    if (remingingtime ==0) return;
    let h = Math.floor(remingingtime/3600)
    let m = Math.floor((remingingtime%3600)/60)
    let s = remingingtime - ((m+h*60)*60)
    document.getElementById('sec').innerHTML=s
    document.getElementById('mini').innerHTML=m
    document.getElementById('hours').innerHTML=h

    


}
setInterval(()=>{
    remingingtime -=1;
    time()
},1000)
