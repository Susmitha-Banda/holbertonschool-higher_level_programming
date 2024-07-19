const { func } = require("prop-types");

let add_item = document.getElementById("add_item");
let my_list = document.querySelector("ul.my_list");

add_item.addEventListener("click", function() {
  const li = document.createElement("li");
  li.appendChild(document.createTextNode("item"));
  my_list.appendChild(li);
})
