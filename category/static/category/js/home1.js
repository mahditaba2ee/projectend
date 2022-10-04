
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
// // alert('s')
// // alert(csrftoken)

// // let slidindex = 1;
// // function setslide(input,index){
    
// //     slidindex = index;
// //     let item = document.getElementById(input)
// //     let btns =[...document.querySelector('.btns').children]
// //     btns.forEach((btn)=>{
// //         btn.classList.remove('active')
// //     })
// //     let btnactive = document.getElementById('btn'+slidindex)
// //     btnactive.classList.add('active')
  
// //     let slids = [...document.querySelector('.slids').children]
// //     slids.forEach((element)=>{
// //         element.classList.remove('active');
// //     })
// //     item.classList.add('active')


// // }
// // setInterval(()=>{
// //     slidindex +=1;
// //     if (slidindex ==4){
// //         slidindex =1;
// //     }
// //     setslide('slid'+slidindex,slidindex)
// // },10000)


// // var searchinput = document.getElementById('inputsearch')
// // var searchbtn = document.getElementById('searchbtn')


// function btnlike(btn){
    
//     // var like_number = document.getElementById(btn.dataset.id)
//     $.post('/category/like/',{  
//         // id:btn.dataset.id,
//         // is_like:btn.dataset.is_like,  
//         csrf_token:csrftoken,

//     },function(data){   
//         console.log(data)
//         // if (data['status'] == 'like_before'){
//         //     message.hidden=false
//         //     message.innerHTML='‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍دارای تغییر می باشد عملیات لایک انجام نشد'
//         // }
//         // else{
//         // if (btn.dataset.is_like =='like'){
//         //     btn.dataset.is_like ='dislike'
//         //     btn.innerHTML='دوست ندارم'
//         //     like_number.innerHTML=data['like_number']
//         //     message.hidden=false
//         //     message.innerHTML='لایک شد'
//         // }
//         // else {
//         //     btn.dataset.is_like ='like'
//         //     btn.innerHTML=' دوست دارم'
//         //     like_number.innerHTML=data['like_number']
//         //     message.hidden=false
//         //     message.innerHTML='لایک برداشته شد'


            
//         // }}
        
//     })  





  
// }
// // function searchclick(){
// //     if(searchinput.style.width==0){
// //         searchinput.style.display='block';
// //         searchinput.style.transition ='1s'
// //        searchinput.style.width='150px'
// //        return;
// //        }
// //        alert(searchinput.value)


    
 
   
// // }
// // let remingingtime =6980 
// // function time()
// // {
// //     if (remingingtime ==0) return;
// //     let h = Math.floor(remingingtime/3600)
// //     let m = Math.floor((remingingtime%3600)/60)
// //     let s = remingingtime - ((m+h*60)*60)
// //     document.getElementById('sec').innerHTML=s
// //     document.getElementById('mini').innerHTML=m
// //     document.getElementById('hours').innerHTML=h

    


// // }
// // setInterval(()=>{
// //     remingingtime -=1;
// //     time()
// // },1000)
