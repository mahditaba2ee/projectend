var cart_nav = document.getElementById('cart_nav')
cart_nav.classList.add('active_nav')



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



var lable_total_price = document.getElementById(('lable_total_price'))

function separate(Number) 
{
Number+= '';
Number= Number.replace(',', '');
x = Number.split('.');
y = x[0];
z= x.length > 1 ? '.' + x[1] : '';
var rgx = /(\d+)(\d{3})/;
while (rgx.test(y))
y= y.replace(rgx, '$1' + ',' + '$2');
return y+ z;
}


function sendproduct(btn){
    var value =btn.value
    if (value>9){
        btn.value =9
        value=9
    }
    if (value<1){
        btn.value =1
        value=1
    }
    
    
   
    $.post('/category/card/add/',{
        
        slug:btn.dataset.slug,
        number:value,
        

    },function(data){

        if (data['status']=='ok'){
            var cart = data['cart_value']
            var totla_price=0
            for (product in cart){
                price = (cart[product]['number']*cart[product]['price'])
                totla_price+=price
                var price = document.getElementById('labal'+product).innerHTML=separate(price)
                
            }
            lable_total_price.innerHTML= separate(totla_price)
            
            
        }
      })
    
}
