

var username = document.getElementById('username')
var password = document.getElementById('password')
var check = document.getElementById('check');
var login = document.getElementById('login')
var phone = document.getElementById('phone')




check.checked=false



function checkbox(){
   
    if (check.value == 1){
        password.type = 'password'
        

        check.value = 0;
        return;
    }
    if (check.value == 0){
        
        password.type = 'text'
        check.value = 1;
        return;
    }
}

function sighon(btn){
    var email = document.getElementById('email')
    var phone = document.getElementById('phone')
    var username = document.getElementById('username')
    var password1 = document.getElementById('password1')
    var password2 = document.getElementById('password2')


    $.post('/accounts/register',{
        email:email.value,
        phone:phone.value,
        username:username.value,
        password1:password1.value,
        password2:password2.value,
    
    },function(data){
        $('#box-form').fadeOut('fast',function(){
            $('#box-form').fadeIn('fast')
            var box_form = document.getElementById('box-form')
            box_form.innerHTML=data
        })
        

        
    }
    )



}
function register(){
    $('#box-form').fadeOut('fast',function(){
        $.get('/accounts/register',function(data){
            $('#box-form').fadeIn('slow')
            var box_form = document.getElementById('box-form')
            box_form.innerHTML=data
    })
        }
    )
    }

function verifycodelogin(){
    var code = document.getElementById("code").value
        $.post('/accounts/verifycode',{
            code:code,
        },function(data){
            console.log(data['code'])
          if (data['code']=='invalid'){
           document.getElementById("message").innerHTML='کد نامعتبر است'
        }  
          if (data['code']=='valid'){
            window.location='/accounts/login'
            
          }  
        })
    }

function phonechanche(btn){
        var valuephone = btn.value
        $.post('/accounts/check/phone/',{
            
            phone:valuephone,
        
        },function(data){
            console.log(data)
            console.log(data['phoneexist'])
            if(data['phoneexist'] =="1"){
                phonehelp.innerHTML="شماره را به صورت صحیح وارد نماید"
    
    
            }
            if(data['phoneexist'] =="0"){
                phonehelp.innerHTML="شماره صحیح است"
                checkphone = true
           
    
            }
            if(data['phoneexist'] =="2"){
                phonehelp.innerHTML="شماره قبلا ثبت نام شده است لطفا با شمار دیگر امتحان کنید"
        
                }
        
        })
        
    
    }

    
function usernamechange(btn){
    var valueusername = btn.value
    console.log(valueusername)
    if (valueusername.length>=5){

    $.post('/accounts/check/username/',{
        
        username:valueusername,
    
    },function(data){
        console.log(data)
        console.log(data['usernameexist'])
        if(data['usernameexist'] =="1"){
            
            usernamehelp.innerHTML = 'نام کاربری نامتعبر است'

        }
        if(data['usernameexist'] =="0"){
            usernamehelp.innerHTML = 'نام کاربری صحیح است'
            checkusername = true
           
       

        }
        if(data['usernameexist'] =="2"){
            usernamehelp.innerHTML = 'نام کاربری قبلا موجود بوده است'
    
    
            }
    
    })}
    else{
        usernamehelp.innerHTML = 'نام کاربری باید 5 لاتین باشد'
        
    }
    

}
