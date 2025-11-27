const welcome_msg = document.querySelector('#welcome-msg');
const search_form = document.querySelector('#searchId-form');
const rename_form = document.querySelector('#rename-form');
const who_search_form = document.querySelector('#whoSearchMe-form');
const show_search_id = document.querySelector('#show-search-id');
const show_rename = document.querySelector('#show-rename');
const show_who_search = document.querySelector('#show-who-search');


// 取得會員資訊
async function startup(){
    try{
        const result = await fetchData("/api/member");
        const name = result.name;
        welcome_msg.textContent = `${name}，歡迎登入系統`;
    } catch (e){
        const err_msg = handle_api_error(e);
        if (err_msg){
            welcome_msg.textContent = err_msg;
        }
    }
}

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

    try{
        const res = await fetchData(`/api/member/${search_id}`);
        if (res.data === "null"){
            show_search_id.textContent = "No Data";
        } else {
            show_search_id.textContent = `${res.data.name}(${res.data.email})`;
        }
    } catch (e){
        const err_msg = handle_api_error(e);
        if (err_msg){
            show_search_id.textContent = err_msg;
        }
    }
});

// 修改會員姓名
rename_form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const rename_input = document.querySelector('#rename-input').value.trim();
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

        if (result.ok === true){
            show_rename.textContent = "更新成功";
            startup();
        } else {
            show_rename.textContent = "更新失敗";
        }
    } catch (e){
        const err_msg = handle_api_error(e);
        if (err_msg){
            show_rename.textContent = err_msg;
        }
    }
});

// 誰查詢了我
who_search_form.addEventListener('submit', async function (e) {
    e.preventDefault();
    try{
        const result = await fetchData("/api/member/extra/who_search");
        show_who_search.innerHTML = "";
        result.data.forEach((d) => {
            const timeStr = d.created_at.replace('T', ' ');
            const box = document.createElement('div');
            box.className = "mb";
            box.textContent = `${d.name}(${timeStr})`;
            show_who_search.append(box);
        }); 
    } catch (e){
        const err_msg = handle_api_error(e);
        if (err_msg){
            show_who_search.textContent = err_msg;
        }
    }
});

startup();