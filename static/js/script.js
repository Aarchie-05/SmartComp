// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function () {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

$(document).ready(function() {
  console.log("here")
//   ajaxPost('/tasks', {type: 'getData'}, function(content){
//     //onSuccess
//     alert(content);
// })
  $.ajax({
    url: '/tasks/',
    data: { type: 'getData' },
    method: 'POST',
  })
  .done((res) => {
    console.log('donezies')
    // getStatus(res.task_id);
  })
  .fail((err) => {
    console.log('error');
    console.log(err);
  });
});


// $(document).ready(function() {
  // const id = out
  // console.log(out)
  // $.ajax({
  //   url: '/',
  //   method: 'GET'
  // })
  // .done((res) => {

  //   const taskStatus = res.task_status;
  //   const taskid = res.task_id;
  //   const taskres = res.task_result;
  //   console.log(taskStatus)
  //   console.log(taskid)
  //   console.log(taskres)

  //   if (taskStatus === 'SUCCESS' || taskStatus === 'FAILURE') return false;
  //   setTimeout(function() {
  //     getStatus(res.task_id);
  //   }, 1000);
  // })
  // .fail((err) => {
  //   console.log(err)
  // });
// });