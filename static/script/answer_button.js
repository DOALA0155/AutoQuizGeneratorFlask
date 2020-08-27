var buttons = document.getElementsByClassName("answer-button")

function click_button(button) {
  var index = button.id
  answer = document.getElementById("answer" + index)
  var button_text = button.getElementsByTagName("span")[0]

  if (answer.classList.contains("answer-content-show")) {

    answer.style.opacity = 0
    answer.classList.remove("answer-content-show")
    button.style.backgroundColor = "rgba(0,206,255,1)"
    button_text.innerHTML = "表示"

  } else {

    answer.style.opacity = 1
    answer.classList.add("answer-content-show")
    button.style.backgroundColor = "rgba(252, 118, 176, 1)"
    button_text.innerHTML = "非表示"

  }
};

for (let i = 0; i < buttons.length; i++) {
  var button = buttons[i]
  button.onclick = function () {
    var button = buttons[i]
    click_button(button)
  }
}