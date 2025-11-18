const form_signup = document.querySelector('#signup_form');
const form_login = document.querySelector('#login_form');

form_signup.addEventListener('submit', function(e){
    const name = document.querySelector('#name_signup').value.trim();
    const email = document.querySelector('#email_signup').value.trim();
    const pw = document.querySelector('#pw_signup').value.trim();
    
    if (!name || !email || !pw){
        e.preventDefault();
        alert("請輸入完整資訊");
    }
});


form_login.addEventListener('submit', function(e){
    const email = document.querySelector('#email_login').value.trim();
    const pw = document.querySelector('#pw_login').value.trim();
    if (!email || !pw){
        e.preventDefault();
        alert("請輸入完整資訊");   
    }

});