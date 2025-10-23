// list = [25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17]
function func3(n){
    let list = [];
    list[0] = 25;

    let count1 = -2;
    let count2 = -3;
    let count3 = 1;
    let count4 = 2;

    for (let i = 1; i <= n; i++){
        if (i % 4 === 1){
            list[i] = list[i - 1] + count1;
        }
        else if (i % 4 === 2){
            list[i] = list[i - 1] + count2;
        }
        else if (i % 4 === 3){
            list[i] = list[i - 1] + count3;
        }
        else if (i % 4 === 0){
            list[i] = list[i - 1] + count4;
        }
    }
    console.log(list[n]);
}

console.log("================Task3================")
func3(1);
func3(5);
func3(10);
func3(30);