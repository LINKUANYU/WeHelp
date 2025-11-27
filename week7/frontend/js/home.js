// 配合未登入使用者嘗試登入轉跳功能page.py
// 檢查網址是否含有msg，有則送出alert
const params = new URLSearchParams(window.location.search);
const msg = params.get('msg');
if (msg){alert(msg)};

// 登入與註冊
const form_signup = document.querySelector('#signup_form');
const form_login = document.querySelector('#login_form');
const show_signup = document.querySelector('#show-signup');
const show_login = document.querySelector('#show-login');
// 註冊
form_signup.addEventListener('submit',async function(e){
    // 這裏一定要先讓form不送出
    e.preventDefault();
    // 取待送出的值
    const name = document.querySelector('#name_signup').value.trim();
    const email = document.querySelector('#email_signup').value.trim();
    const pw = document.querySelector('#pw_signup').value;
    // 前端確認送出資訊完整
    if (!name || !email || !pw){
        alert("請輸入完整資訊");
        return;
    }
    try{
        // 送出API
        const res = await fetchData("/api/signup", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name, email, pw})
        });
        // 沒有錯誤的話顯示結果
        show_signup.textContent = res.msg;
    } catch(e) {
        // 錯誤處理
        const err_msg = handle_api_error(e);
        if (err_msg){
            show_signup.textContent = err_msg;
        }
    }
});

// 登入
form_login.addEventListener('submit', async function(e){
    e.preventDefault();
    const email = document.querySelector('#email_login').value.trim();
    const pw = document.querySelector('#pw_login').value;

    if (!email || !pw){
        alert("請輸入完整資訊");   
        return
    }

    try{
        const res = await fetchData("/api/login", {
            method: "POST",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({email, pw})
        });
        const name = res.name;
        
        let seconds = 3;
        show_login.textContent = `歡迎回來 ${name}，${seconds}秒後為您轉跳`;

        // 計時器，每1000ms執行一次
        const timer = setInterval(() => {
            seconds -= 1;
            if (seconds < 0){
                clearInterval(timer);
                window.location.href = "/member";
            } else {
                show_login.textContent = `歡迎回來 ${name}，${seconds}秒後為您轉跳`;
            }
        }, 1000);

    } catch (e){
        const err_msg = handle_api_error(e, {redirect_on_401 : false});
        if (err_msg){
            show_login.textContent = err_msg;
        }
    }
});