// Get the modal
var modalF = document.getElementById("myModalF");

// Get the button that opens the modal
var btnF = document.getElementById("myBtnF");

// Get the <span> element that closes the modal
var spanF = document.getElementsByClassName("closeF")[0];

// When the user clicks the button, open the modal 
btnF.onclick = function () {
    modalF.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
spanF.onclick = function () {
    modalF.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modalF) {
        modalF.style.display = "none";
    }
}