var button = document.getElementsByClassName("generate-button")[0]
button.onclick = function () {
  var field = document.getElementsByClassName("word-field-content")[0]
  window.location.href = "/" + field.value
}