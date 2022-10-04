
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

function f(btn,num){
    for(i=1;i<=5;i++){
        document.getElementById('btn'+i).style.color='black'
    }
    for(i=1;i<=num;i++){
        document.getElementById('btn'+i).style.color='yellow'
    }
    
   
}

function m(num){
    for(i=1;i<=num;i++){
        document.getElementById('btn'+i).style.color='black'
        
    }
    
}





var btnsene = document.getElementById('btnsene')
var message = document.getElementById('message')
function sendproduct(){

    var slug=btnsene.dataset.slug
    
    $.post('/category/card/add/',{

        slug:slug,
    
    },function(data){
        console.log(data)
        if (data['status']=='ok'){
            
            message.hidden=false
            message.innerHTML='کالا در سبد خرید ثبت شد'
            
        }
      })
    
}

var commentinput = document.getElementById('commentinput')
var id = ''
function reply(btn){
    commentinput.value='@'+btn.dataset.username+' '
    id = btn.dataset.id

    
}

function commentsumbit(btn){
    var comment=commentinput.value
    var catslug = btn.dataset.catslug
    var productslug = btn.dataset.productslug
    var brandslug = btn.dataset.brandslug
    var productid = btn.dataset.productid
    

    
    
    
    $.post('/category/commentadd/',{
        
        id:id,
        comment:comment,
        productid:productid,
    
    },function(data){
        console.log(data['status'])
        
        window.location.replace('/category/details/product/'+catslug+'/'+brandslug+'/'+productslug)
        
            
            
        
      })
}

function img_change(img){
    var f = img.src
    var first=document.getElementById('img-first')
    img.src = first.src
    first.src = f
    sec.src = first.dataset.src
    

} 


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





function star_click(btn){

    $.post('/category/addstar/',{
        id:btn.dataset.id,
        count:btn.dataset.count,
    },function(data){
        if (data['status']=='notauth'){
            alert('برای ثبت نظر اول لاگین کنید')
        }
        else{
        var username = data['username']
      
        var star_count =Number(data['star'][username])
        for(i=1;i<=star_count;i++){
            

            console.log(star_count)
            document.getElementById('btn'+i).style.color='yellow'
        }
        var star_all = data['star']
        var value_star = (Object.values(star_all))
        var avarage=0
        for(x in value_star){
            avarage+= Number(value_star[x])
        }
        avarage = avarage/value_star.length
        document.getElementById('all-ranking').innerHTML=avarage.toFixed(1)+'<i class="fas fa-star half"></i>'

        for(i=1;i<=5;i++){
            var star = value_star.filter(x => x==i).length
            var width = String((star*100)/value_star.length)+'%'
            c= document.getElementById('rank'+i).style.width=width

    }
    }
    })

}
var product_id = document.getElementById('btn-id-product')
function s(){
    $.post('/category/addstar/',{
       id:product_id.dataset.id,
       count:'start',
    },function(data){
        var username = data['username']
      
        var star_count =Number(data['star'][username])
        for(i=1;i<=star_count;i++){
            console.log(star_count)
            document.getElementById('btn'+i).style.color='yellow'
        }
        var star_all = data['star']
        var value_star = (Object.values(star_all))
        var avarage=0
        for(x in value_star){
            avarage+= Number(value_star[x])
        }
        if (value_star.length ==0){
            avarage = 0
        }
        else{      
            avarage = avarage/value_star.length
    }
        
        document.getElementById('all-ranking').innerHTML=avarage.toFixed(1)+'<i class="fas fa-star half"></i>'
        for(i=1;i<=5;i++){
            var star = value_star.filter(x => x==i).length
            var width = String((star*100)/value_star.length)+'%'
            c= document.getElementById('rank'+i).style.width=width

    }
     
    })
}

function star_leave(){
s()

}
s()


function share(){
    $.post('/category/sharepost/',{

    },function(data){
        document.getElementById('share').innerHTML=data
    })
    
}
var usernames = document.getElementById('usernames')
function username(value){
    if(value==''){
        usernames.style.display='none'

    }
    if(value[0]=='@'){

        if(id==''){

        usernames.innerHTML=''
        $.post('/accounts/usernames',{
            value:value,
        },function(data){
            for (user in data['users']){
                usernames.style.display='block'
                usernames.innerHTML+='<p onclick="usernameclick(this)">'+data['users'][user]+'</p>'
            console.log(data['users'][user])
            }
          console.log(data['users'])
        })

    }
    }
}
function usernameclick(btn){
    commentinput.value='@'+btn.innerHTML+' '
    commentinput.focus()
}