// 確認是否已登入
const params = new URLSearchParams(window.location.search);
const msg = params.get('msg');

if (msg){alert(msg)};

const form_signup = document.querySelector('#signup_form');
const form_login = document.querySelector('#login_form');

async function fetchData(url, options) {
    const res = await fetch(url, options);
    const ct = res.headers.get('content-type') || '';
    const body = ct.includes('application/json') ? await res.json() :await res.text();
    
    // 如果回傳不是2XX，建立一個變數把回傳錯誤訊息存在裡面丟給上一層catch處理
    if (!res.ok){
        const err = new Error (`HTTP ${res.status}`);
        err.status = res.status;
        err.payload = body;
        throw err;
    }
    return body;
}

form_signup.addEventListener('submit',async function(e){
    // 這裏一定要先讓form不送出
    e.preventDefault();
    const name = document.querySelector('#name_signup').value.trim();
    const email = document.querySelector('#email_signup').value.trim();
    const pw = document.querySelector('#pw_signup').value;
    
    if (!name || !email || !pw){
        alert("請輸入完整資訊");
        return
    }
    try{
        const result = await fetchData("/api/signup", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({name, email, pw})
        });
        const msg = document.createElement('div');
        msg.className = "flex mb";
        msg.textContent = result.msg;
        form_signup.append(msg);
    } catch(e) {
        const err_msg = 
        e?.payload?.detail ||
        (typeof e?.payload === "string" ? e.payload : '') ||
        e?.message || "發生錯誤，請稍後再試";
        alert(err_msg);
    }
});


form_login.addEventListener('submit', async function(e){
    e.preventDefault();
    const email = document.querySelector('#email_login').value.trim();
    const pw = document.querySelector('#pw_login').value;
    if (!email || !pw){
        alert("請輸入完整資訊");   
        return
    }

    try{
        const result = await fetchData("/api/login", {
            method: "POST",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({email, pw})
        });
        const name = result.name;

        const msg = document.createElement('div');
        msg.className = "flex mb";
        
        let seconds = 3;
        msg.textContent = `歡迎回來 ${name}，${seconds}秒後為您轉跳`;
        form_login.append(msg);
        
        const timer = setInterval(() => {
            seconds -= 1;
            if (seconds < 0){
                clearInterval(timer);
                window.location.href = "/member"
            } else {
                msg.textContent = `歡迎回來 ${name}，${seconds}秒後為您轉跳`;
            }
        }, 1000)

    } catch (e){
        const err_msg = 
        e?.payload?.detail ||
        (typeof e?.payload === 'string' ? e.payload : '') ||
        e?.message || '發生錯誤，請稍後再試';
        alert(err_msg);
    }

});