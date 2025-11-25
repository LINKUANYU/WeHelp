const welcome_msg = document.querySelector('#welcome-msg');

async function fetchData(url, options) {
    const res = await fetch(url, options);
    const ct = res.headers.get('content-type') || '';
    const body = ct.includes('application/json') ? await res.json() : await res.text();
    
    if (!res.ok){
        const err = new Error (`HTTP ${res.status}`)
        err.status = res.status;
        err.payload = body;
        throw err
    }
    return body
}

(async function(){
    try{
        const result = await fetchData("/api/member");
        const name = result.name;
        welcome_msg.textContent = `${name}，歡迎登入系統`;
    } catch (e){
        const err_msg = e?.payload?.detail ||
        (typeof e?.payload === 'string' ? e.payload : '') ||
        e?.message || "發生錯誤，稍後再試";
        alert(err_msg);
    }

})();