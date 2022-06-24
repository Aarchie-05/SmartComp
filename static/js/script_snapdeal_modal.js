var modalS = document.getElementById("myModalS");
var btnS = document.getElementById("myBtnS");
var spanS = document.getElementsByClassName("closeS")[0];

btnS.onclick = function () {
    modalS.style.display = "block";
}

spanS.onclick = function () {
    modalS.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modalS) {
        modalS.style.display = "none";
    }
}