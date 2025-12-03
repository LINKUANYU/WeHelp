
console.log("JS腳本開始執行");
console.log("⭐DOM的建立狀態 =", document.readyState);
// 網頁載入狀態：loading -> 還沒建立完整DOM, interactive -> DOM建立完，img/css/外部資源還沒


// 試著抓底部標記
const bottom = document.querySelector('.bottom');

if (bottom) {
  console.log("✅找到 .bottom：HTML 已經解析到底部了");
} else {
  console.log("❌找不到 .bottom：HTML 還在解析中（readyState = loading）");
}


console.log("JS腳本執行結束");
