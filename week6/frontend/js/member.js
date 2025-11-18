const form_msg = document.querySelector('#form_msg');

form_msg.addEventListener('submit', function(e){
    const msg = document.querySelector('#msg').value.trim();
    if (!msg){
        e.preventDefault();
        alert("請輸入留言");
    }
});

const form_delete = document.querySelectorAll('.form_delete');
form_delete.forEach((form) => {
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const ok = window.confirm("確認是否刪除留言");
        if (!ok) return;
        form.submit();
    });
});
