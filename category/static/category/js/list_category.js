// function getCookie(name) {
//     var cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         var cookies = document.cookie.split(';');
//         for (var i = 0; i < cookies.length; i++) {
//             var cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// var csrftoken = getCookie('csrftoken');

    

// function csrfSafeMethod(method) {
// // these HTTP methods do not require CSRF protection
// return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }
// $.ajaxSetup({
// beforeSend: function(xhr, settings) {
//     if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//         xhr.setRequestHeader("X-CSRFToken",csrftoken);
//     }
// }
// });

// function likeproduct(btn){
//         var like_number = document.getElementById(btn.dataset.id)
//         $.post('/category/like/',{  
//             id:btn.dataset.id,
//             is_like:btn.dataset.is_like,  

//         },function(data){   
            
//             if (data['status'] == 'like_before'){
//                 message.hidden=false
//                 message.innerHTML='‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍دارای تغییر می باشد عملیات لایک انجام نشد'
//             }
//             else{
//             if (btn.dataset.is_like =='like'){
//                 btn.dataset.is_like ='dislike'
//                 btn.innerHTML='دوست ندارم'
//                 like_number.innerHTML=data['like_number']
//                 message.hidden=false
//                 message.innerHTML='لایک شد'
//             }
//             else {
//                 btn.dataset.is_like ='like'
//                 btn.innerHTML=' دوست دارم'
//                 like_number.innerHTML=data['like_number']
//                 message.hidden=false
//                 message.innerHTML='لایک برداشته شد'


                
//             }}
            
//         })  
    
// }

// function sendproduct(btn){
    
//     var slug=btn.dataset.slug
//     var name = btn.dataset.name
    
//     $.post('/category/card/add/',{

//         slug:slug,
    
//     },function(data){
//         console.log(data)
//         if (data['status']=='ok'){
            
//             message.hidden=false
//             message.innerHTML=name +' '+ 'در سبد خرید ثبت شد'
            
//         }
//       })
    
// }
