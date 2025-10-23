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

