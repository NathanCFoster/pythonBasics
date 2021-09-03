function changeAction(element) {
    var num = document.getElementById('number').value;
    element.action = '/add/' + num;
}