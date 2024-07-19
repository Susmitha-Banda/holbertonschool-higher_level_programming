document.addEventListener("DOMContentLoaded", function(){
   // Select the div with id 'red_header'
   let.redHeaderDiv = document.querySelector("#red_header");
   // Select the header element
   let.header = document.querySelector("#header");
   // Add a click event listener to the redHeaderDiv
   redHeaderDiv.addEventListener("click", function(){
     // Add the 'red' class to the header element
     header.classList.add("red");
   })
})