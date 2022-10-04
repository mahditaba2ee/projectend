
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
})


function searchclick(){

var searchinput = document.getElementById('inputsearch')
var searchbtn = document.getElementById('searchbtn')
var simple_search = document.getElementById('simple_search')
simple_search.classList.add('active_nav')
var btn_search = document.getElementById('btn-search')

    if(searchinput.style.width==0){
        searchinput.classList.add('searchbtn')
        btn_search.style.display='block'
        // searchinput.style.transition ='1s'
    //    searchinput.style.width='150px'
       return;
       }
       alert(searchinput.value)


    
 
   
}
function all_search(){
    var search_box = document.getElementById('search-box')
    search_box.style.display='block'
}



function search(){
    var searchinput = document.getElementById('inputsearch')
    location.href='/category/search/'+searchinput.value
}
// $("div#content").load("page.html");
function itemclick(btn){
    var slug = btn.dataset.slug
    location.href='/category/search/'+slug
    console.log(data)


    } 
function night_mode_click(btn){
    if(btn.dataset.mode=='night'){
        var helptext = document.getElementsByClassName('help_night')
        color_btn = 'white'
        color_body='black'
        btn.dataset.mode='day'
        helptext[0].innerHTML='روز'

    }
    else{
        window.location = window.location.href;

      

    }
    var body_main = document.getElementById('body_main')
    $('#body_main').fadeIn("slow",function(){
        body_main.style.backgroundColor=color_body

    })
    // body_main.style.opacity=".5"
    btn.classList.add("active_nav")
    var ta = document.getElementsByClassName('night')
    
   
    for (element in ta){
        try{
            ta[element].style.color=color_btn

            
        }

        catch{
            return
        }
    } 
    
}
function btn_login(){
    location.href='/accounts/login'
}
function btn_logout(){
    location.href='/accounts/logout'

}