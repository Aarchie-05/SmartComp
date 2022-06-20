var modalF = document.getElementById("myModalF");
var btnF = document.getElementById("myBtnF");
var spanF = document.getElementsByClassName("closeF")[0];

btnF.onclick = function () {
    modalF.style.display = "block";
}

spanF.onclick = function () {
    modalF.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modalF) {
        modalF.style.display = "none";
    }
}