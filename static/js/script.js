var modal = document.getElementById("myModal");
var btn = document.getElementById("myBtn");
var span = document.getElementsByClassName("close")[0];
btn.onclick = function () {
    modal.style.display = "block";
}
span.onclick = function () {
    modal.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
function closeDeal(store){
    $('.deal:has(' + '#' + store + '-primary)').hide();
    $('#' + store + '-checkbox').prop('checked', false);
}
function toggleDeal(store){
    const state = $('#' + store + '-checkbox').prop('checked')
    $('#' + store + '-checkbox').prop('checked', !state);
    if(state){
        $('.deal:has(' + '#' + store + '-primary)').hide();
    } else {
        $('.deal:has(' + '#' + store + '-primary)').show();
    }
}


