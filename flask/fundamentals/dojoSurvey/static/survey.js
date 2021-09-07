function process(element) {
    var name = document.getElementById('name').value;
    var location = document.getElementById('location').value;
    var language = document.getElementById('language').value;
    var comment = document.getElementById('comment').value;
    var gender = "";
    var icecreams = [];
    var icecream = '';
    if (document.getElementById("gender1").checked == true) {
        gender = "male";
    } else if (document.getElementById("gender2").checked == true) {
        gender = "female";
    } else {
        gender = "other"
    }
    if (document.getElementById("vanilla").checked == true) {
        icecreams.push("vanilla"); 
    } if (document.getElementById("chocolate").checked == true) {
        icecreams.push("chocolate");
    } if (document.getElementById("strawberry").checked == true) {
        icecreams.push("strawberry");
    } if (icecreams.length > 1) {
        for (let index = 0; index < icecreams.length-1; index++) {
            icecream += icecreams[index] + ", ";
        }
        icecream += icecreams[icecreams.length-1];
    }
    element.action = "/process/" + name + "/" + location + "/" + language + "/" + comment + "/" + gender + "/" + icecream;
}