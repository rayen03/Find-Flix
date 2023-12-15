var datatext = document.getElementById("data").innerHTML;
const data = JSON.parse(datatext);
document.getElementById("data").innerHTML="";
for(i=0;i<data.length;i++){
    var newDiv = document.createElement("div");
    const newContent = data[i][1];
    newDiv.textContent = newContent;
    newDiv.classList.add("result_div");
    const currentDiv = document.getElementById("data");
    currentDiv.parentNode.insertBefore(newDiv, currentDiv.previousSibling)
}