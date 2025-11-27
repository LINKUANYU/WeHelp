// 送API function
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
    // 回傳已解過json的物件
    return body;
}

// 處理錯誤的function
function handle_api_error(e, options){
    // 如果沒有第二個參數，就用空{}
    options = options || {};

    // 如果options.rediret_on_401 為布林值，回傳該布林值，否則預設True
    let redirect_on_401;
    if (typeof options.redirect_on_401 === 'boolean'){
        redirect_on_401 = options.redirect_on_401;
    } else {
        redirect_on_401 = true;
    }
    // 各種不同的錯誤
    if (e.status === 400){
        const err_msg = e?.payload?.detail || "請輸入完整訊息";
        return err_msg;
    }
    if (e.status === 401){
        // 需轉跳首頁
        if (redirect_on_401){
            const err_msg = e?.payload?.detail || "請先登入";
            window.location.href = '/?msg=' + encodeURIComponent(err_msg);
            return;
        // 不需轉跳首頁(在首頁登入時發生錯誤)
        } else {
            const err_msg = e?.payload?.detail || "帳號或密碼輸入錯誤";
            return err_msg;
        }
    }
    if (e.status === 404){
        const err_msg = e?.payload?.detail || "會員不存在";
        return err_msg;
    }
    if (e.status === 409){
        const err_msg = e?.payload?.detail || "已存在email";
        return err_msg;
    }
    if (e.status === 500){
        const err_msg = e?.payload?.detail || "資料庫錯誤，請稍後再試";
        return err_msg;
    }
    const err_msg = 
        e?.payload?.detail ||
        (typeof e?.payload === 'string' ? e.payload : '') ||
        e?.message || "發生錯誤，稍後再試";
    return err_msg;
}

window.fetchData = fetchData;
window.handle_api_error = handle_api_error;