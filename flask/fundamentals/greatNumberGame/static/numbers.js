function guess(element) {
    var num = document.getElementById('number').value;
    element.action = "/guess/" + num;
}

function submitThis(element) {
    var name = document.getElementById('user').value;
    element.action = "/submit/" + name;
    console.log('this user' + name);
}