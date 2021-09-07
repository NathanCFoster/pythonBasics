function process(element) {
    var name = document.getElementById('name').value;
    var location = document.getElementById('location').value;
    var language = document.getElementById('language').value;
    var comment = document.getElementById('comment').value;
    element.action = "/process/" + name + "/" + location + "/" + language + "/" + comment;
}