function guess(element) {
    var num = document.getElementById('number').value;
    element.action = "/guess/" + num;
}