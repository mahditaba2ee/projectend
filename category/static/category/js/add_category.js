

function change_name(value){
    var t =document.getElementById('link')
    t.value=''
    for(ch in value){
        switch (value[ch]){

            case 'ض':t.value+='z' 
            break;
            case 'ص':t.value+='sa'
            break;
            case 'ث':t.value+='se'
            break;
            case 'ق':t.value+='gh'
            break;
            case 'ف':t.value+='f'
            break;
            case 'غ':t.value+='gh'
            break;
            case 'ع':t.value+='aa' 
            break;
            case 'ه':t.value+='h'
            break;
            case 'خ':t.value+='kh'
            break;
            case 'ح':t.value+='he'
            break;
            case 'ج':t.value+='ch'
            break;
            case 'ج':t.value+='cha'
            break;




            case 'ژ':t.value+='zh' 
            break;
            case 'ش':t.value+='sh'
            break;
            case 'س':t.value+='s'
            break;
            case 'ی':t.value+='ye'
            break;
            case 'ب':t.value+='b'
            break;
            case 'ل':t.value+='l'
            break;
            case 'ا':t.value+='a' 
            break;
            case 'ت':t.value+='t'
            break;
            case 'ن':t.value+='n'
            break;
            case 'م':t.value+='m'
            break;
            case 'ک':t.value+='k'
            break;
            case 'گ':t.value+='g'
            break;



            case '‍‍‍ظ':t.value+='z' 
            break;
            case 'ط':t.value+='ta'
            break;
            case 'ز':t.value+='z'
            break;
            case 'ر':t.value+='r'
            break;
            case 'ذ':t.value+='z'
            break;
            case 'د':t.value+='d'
            break;
            case 'پ':t.value+='b' 
            break;
            case 'و':t.value+='o'
            break;
            case 'ن':t.value+='n'
            break;
            case 'م':t.value+='m'
            break;
            case 'ک':t.value+='k'
            break;
            case 'گ':t.value+='g'
            break;
        }
    }
//  document.onkeyup= function(e){
   
//     if(e.key=='ا'){
//         document.getElementById('link').value+='a'
//     }
// if(e.key=='Backspace'){
//     alert('s')
// }

// }

}