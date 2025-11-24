const form_signup = document.querySelector('#signup_form');
const form_login = document.querySelector('#login_form');

form_signup.addEventListener('submit',async function(e){
    // 這裏一定要先讓form不送出
    e.preventDefault();
    const name = document.querySelector('#name_signup').value.trim();
    const email = document.querySelector('#email_signup').value.trim();
    const pw = document.querySelector('#pw_signup').value.trim();
    
    if (!name || !email || !pw){
        e.preventDefault();
        alert("請輸入完整資訊");
        return
    }
    const res = await fetch("/api/signup", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email, pw})
    });
    // response 還沒做完
    const data = await res.json();
    console.log(data);
});


form_login.addEventListener('submit', function(e){
    const email = document.querySelector('#email_login').value.trim();
    const pw = document.querySelector('#pw_login').value.trim();
    if (!email || !pw){
        e.preventDefault();
        alert("請輸入完整資訊");   
    }

});