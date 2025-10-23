function func4(sp, stat, n){
    // for loop put passage into car(difference), if meet car unavailable continue
    // renew the min and record the ans each loop
    // finish loop print result
    if (sp.length !== stat.length){
        return console.log("Error: sp and stat length not equal");
    }
    const len = sp.length

    let min = Infinity;
    let ans = -1;
    for (let i = 0; i < len; i++){
        if (stat[i] === "1") continue;
        let diff = Math.abs(sp[i] - n);
        if (diff <= min){
            min = diff;
            ans = i;
        }
    }
    if (ans === -1) return console.log("Error: Not found");
    console.log(ans);
}


console.log("================Task4================")
func4([3, 1, 5, 4, 3, 2], "101000", 2);
func4([1, 0, 5, 1, 3], "10100", 4);
func4([4, 6, 5, 8], "1000", 4);