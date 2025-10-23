function function1(name){
    // find out pos of the name
    // calculate the distance
    // check section and decide if it needs extra point
    // find the closest and farest
    
    const people = [
        {"name": "悟空", "pos": [0, 0]},
        {"name": "辛巴", "pos": [-3, 3]},
        {"name": "貝吉塔", "pos": [-4, -1]},
        {"name": "特南克斯", "pos": [1, -2]},
        {"name": "佛利沙", "pos": [4, -1]},
        {"name": "丁滿", "pos": [-1, 4]},
    ];
    
    const section1 = ["悟空", "辛巴", "貝吉塔", "特南克斯"];
    const section2 = ["佛利沙", "丁滿"];

    // find name itself and find pos
    const me = people.find(p => p.name === name);
    if (!me) return console.log("No exsist person");
    const POS = me.pos;
    
    // check section
    const check_section = (n) => (section1.includes(n) ? 1 : section2.includes(n) ? 2 : null);

    let target_section = check_section(name);

    // calculate the distance
    const extrapoint = 2;
    const new_list = [];
    for (let i = 0; i < people.length; i++){
        let person = people[i];
        // skip itself
        if (person.name === name){
            continue;
        }
        // distance 
        let distance_raw = Math.abs(person.pos[0] - POS[0]) + Math.abs(person.pos[1] - POS[1]);

        // different section
        const sec = check_section(person.name);
        if (sec !== target_section){
            distance_raw += extrapoint;
        }
        // make new list to put result
        new_list.push({[person.name] : distance_raw});
    }

    // find the closest
    let min = Infinity;
    let min_list = [];
    for (o of new_list){
        const [who, value] = Object.entries(o)[0]
        if (value < min){
            min = value;
            min_list = [who]; // don't use push. new value should overwrite everything.
        }
        else if (value === min){
            min_list.push(who);
        }
    }
    //find the farest
    let max = -Infinity;
    let max_list = [];
    for (o of new_list){
        const [who, value] = Object.entries(o)[0];
        if (value > max){
            max = value;
            max_list = [who];  // don't use push. new value should overwrite everything.
        }
        else if(value === max){
            max_list.push(who);
        }
    }
    console.log("最遠", max_list.join("、"), "; 最近", min_list.join("、"));
    
}

console.log("================Task1================")
function1("辛巴")
function1("悟空")
function1("佛利沙")
function1("特南克斯")


function func2(ss, start, end, criteria){
    // turn criteria into usable element
    // make the selector by criteria condition and put all qulify into result 
    // make the first one of result become best choice

    const[field, op , rawvalue] = criteria.split(/\s*(<=|>=|=)\s*/);
    let value;
    if (field === "r") value = Number(rawvalue);
    else if (field === "c") value = Number(rawvalue);
    else if (field === "name") value = rawvalue;
    else { console.log("Error"); return; }

    // make selector by condition
    let result = []
    for (let i = 0; i < ss.length; i++){
        const v = ss[i][field];
        // if condition is name 
        if (op === "="){
            if (field != "name"){
                return console.log("Error: name can only use '='");
            }
            if (v === value){
                result.push(ss[i]);
            }
        }
        // if condition is "r" or "c"
        if (op === ">="){
            if (Number(v) >= value){
                result.push(ss[i]);
            }
        }
        if (op === "<="){
            if (Number(v) <= value){
                result.push(ss[i]);
            }
        }
    }
    if (result.length === 0){ console.log("Not Found"); return; }
    // copy result and sort it
    let order = [...result];
    if (op === ">="){
        order.sort((a,b) => Number(a[field]) - Number(b[field])); // from small to big
    }
    else if (op === "<="){
        order.sort((a,b) => Number(b[field]) - Number(a[field])); // from big to small
    }
    const bset_choice = order[0];

    // put best choice into schedule
    // if same name in schedule check time avalible
    // if avalible then put best choice in and print out service
    function check_avalible(start, end, booking){
        if (start < booking.end && end > booking.start){
            return false
        }
        return true
    }

    // same service about to be used
    for (let i = 0; i < schedules.length; i++){
        if (bset_choice.name === schedules[i].name){
            if (check_avalible(start, end, schedules[i]) === false){
                console.log("Sorry");
                return
            }
        }
    }
    console.log(bset_choice.name);
    schedules.push({"name": bset_choice.name, "start": start, "end": end});
    return
    
}
    


const services = [
    {"name": "S1", "r": "4.5", "c":"1000"},
    {"name": "S2", "r": "3", "c":"1200"},
    {"name": "S3", "r": "3.8", "c":"800"},
];
schedules = [];
console.log("================Task2================")
func2(services, 15, 17, "c>=800");
func2(services, 11, 13, "r<=4");
func2(services, 10, 12, "name=S3");
func2(services, 15, 18, "r>=4.5");
func2(services, 16, 18, "r>=4");
func2(services, 13, 17, "name=S1");
func2(services, 8, 9, "c<=1500");


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

function func4(sp, stat, n){
    // put passages into car (take differences)
    // find out which car is unavalible and put the number to 100
    // find the fittest car (minimum)
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