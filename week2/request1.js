function function1(name){
    people = [
        {"name": "悟空", "pos": [0, 0]},
        {"name": "辛巴", "pos": [-3, 3]},
        {"name": "貝吉塔", "pos": [-4, -1]},
        {"name": "特南克斯", "pos": [1, -2]},
        {"name": "佛利沙", "pos": [4, -1]},
        {"name": "丁滿", "pos": [-1, 4]},
    ];
    
    let section1 = ["悟空", "辛巴", "貝吉塔", "特南克斯"];
    let section2 = ["佛利沙", "丁滿"];
    // calculate the differences of input name and each name
    for (let i = 0; i < people.length; i++){
        if (people[i].name == name){
            POS = people[i].pos;
            break;
        }
    }
    // check section
    function section(name){
        for (let i = 0; i < section1.length; i++){
            if (section1[i] === name){
                return 1;
            }
        }
        for (let i = 0; i < section2.length; i++){
            return 2;
        }
        return console.log("Not Found");
    }

    let target_section = section(name);
    let new_list = [];
    for (let i = 0; i < people.length; i++){
        if (people[i].name == name){
            continue;
        }
        else if (section(people[i].name) === target_section){
            distance_raw = Math.abs(people[i].pos[0] - POS[0]) + Math.abs(people[i].pos[1] - POS[1]);
        }
        else if (section(people[i].name) != target_section){
            distance_raw = Math.abs(people[i].pos[0] - POS[0]) + Math.abs(people[i].pos[1] - POS[1]) + 2;
        }
        new_list.push({[people[i].name] : distance_raw})
    }

    let min = Infinity;
    let min_list = [];
    for (o of new_list){
        [name, value] = Object.entries(o)[0]
        if (value < min){
            min = value;
            min_list = [name];
        }
        else if (value === min){
            min_list.push(name);
        }
    }
    let max = -Infinity;
    let max_list = [];
    for (o of new_list){
        [name, value] = Object.entries(o)[0];
        if (value > max){
            max = value;
            max_list = [name];
        }
        else if(value === max){
            max_list.push(name);
        }
    }
    console.log("最遠", max_list.join("、"), "; 最近", min_list.join("、"));

    // check every name if they are  in the same section with input name

    // find the farest and closest one and print
    
}

console.log("================Task1================")
function1("辛巴")
function1("悟空")
function1("佛利沙")
function1("特南克斯")
