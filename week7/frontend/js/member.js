const welcome_msg = document.querySelector('#welcome-msg');
const search_form = document.querySelector('#searchId-form');
const rename_form = document.querySelector('#rename-form');
const who_search_form = document.querySelector('#whoSearchMe-form');


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
// 取得會員資訊
async function stratup(){
    try{
        const result = await fetchData("/api/member");
        const name = result.name;
        welcome_msg.textContent = `${name}，歡迎登入系統`;
    } catch (e){
        if (e.status === 401){
            const err_msg = e?.payload?.detail || "請先登入";
            window.location.href = '/?msg=' + encodeURIComponent(err_msg);
            return;
        }
        if (e.status === 404){
            const err_msg = e?.payload?.detail || "會員不存在";
            alert(err_msg);
            return;
        }
        const err_msg = 
            e?.payload?.detail ||
            (typeof e?.payload === 'string' ? e.payload : '') ||
            e?.message || "發生錯誤，稍後再試";
        alert(err_msg);
    }

};

// 查詢會員姓名
search_form.addEventListener('submit', async function(e){
    e.preventDefault();

    const search_id_input = document.querySelector('#search-id');
    // parseInt(..., 10)：轉成 10 進位的整數, 不是有效數字則變成NaN
    const search_id = parseInt(search_id_input.value.trim(), 10);
    // 如果是Number型別的NaN
    if (Number.isNaN(search_id) || search_id <= 0){
        alert("請輸入正整數ID");
        return;
    }
    if (!search_id){
        alert("請輸入資料");
        return;
    }

    try{
        const res = await fetchData(`/api/member/${search_id}`);
        // show result <div>
        let search_id_result = search_form.querySelector('.search-id-result');
        if (!search_id_result){
            search_id_result = document.createElement('div');
            search_id_result.className = "flex mb search-id-result";
        }
        // check result data
        let result;
        if (res.data === "null"){
            result = "No Data";
        } else {
            result = `${res.data.name}(${res.data.email})`;
        }
        search_id_result.textContent = result;
        search_form.append(search_id_result);
    } catch (e){
        if (e.status === 401){
            const err_msg = e?.payload?.detail || "請先登入";
            window.location.href = '/?msg=' + encodeURIComponent(err_msg);
            return;
        }
        if (e.status === 404){
            const err_msg = e?.payload?.detail || "會員不存在";
            alert(err_msg);
            return;
        }
        const err_msg = 
            e?.payload?.detail ||
            (typeof e?.payload === 'string' ? e.payload : '') ||
            e?.message || "發生錯誤，稍後再試";
        alert(err_msg);
    }

});

// 修改會員姓名
rename_form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const rename_input = rename_form.querySelector('#rename-input').value.trim();
    if (!rename_input){
        alert("請輸入資料"); 
        return;
    }
    try{
        const result = await fetchData("/api/member", {
            method: "PATCH",
            headers: {"content-type": "application/json"},
            body: JSON.stringify({"new_name": rename_input})
        });
        
        let rename_result = rename_form.querySelector('.rename-result');
        if (!rename_result){
            rename_result = document.createElement('div');
            rename_result.className = "flex mb rename-result";
        }

        if (result.ok === true){
            rename_result.textContent = "更新成功";
            stratup();
        } else {
            rename_result.textContent = "更新失敗";
        }
        rename_form.append(rename_result);
    } catch (e){
        if (e.status === 401){
            const err_msg = e?.payload?.detail || "請先登入";
            window.location.href = '/?msg=' + encodeURIComponent(err_msg);
            return;
        }
        if (e.status === 404){
            const err_msg = e?.payload?.detail || "會員不存在";
            alert(err_msg);
            return;
        }
        const err_msg = 
            e?.payload?.detail ||
            (typeof e?.payload === 'string' ? e.payload : '') ||
            e?.message || "發生錯誤，稍後再試";
        alert(err_msg);
    }  
});

who_search_form.addEventListener('submit', async function (e) {
    e.preventDefault();
    try{
        const result = await fetchData("/api/member/extra/who_search");
        console.log(result);
        result.data.forEach((d) => {
            const timeStr = d.created_at.replace('T', ' ');
            const box = document.createElement('div');
            box.className = "flex mb"
            box.textContent = `${d.name}(${timeStr})`
            who_search_form.append(box);
        }); 
    } catch (e){
        if (e.status === 401){
            const err_msg = e?.payload?.detail || "請先登入";
            window.location.href = '/?msg=' + encodeURIComponent(err_msg);
            return;
        }
        if (e.status === 404){
            const err_msg = e?.payload?.detail || "會員不存在";
            alert(err_msg);
            return;
        }
        const err_msg = 
            e?.payload?.detail ||
            (typeof e?.payload === 'string' ? e.payload : '') ||
            e?.message || "發生錯誤，稍後再試";
        alert(err_msg);
    }
 
});


stratup();