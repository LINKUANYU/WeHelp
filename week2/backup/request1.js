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
