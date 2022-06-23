// flipkart-primary
$(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'dress', store: 'amazon', req_data: 'primary'}
    })
    .done((res) => {
      console.log(res)
      // getStatus(res.task_id);
    })
    .fail((err) => {
      console.log('error');
      console.log(err.responseText);
    });
  });
  
  // // amazon-primary
  // $(document).ready(function() {
  //   $.ajax({
  //     url: 'data',
  //     type: 'get',
  //     data: { search: 'shampoo', store: 'amazon', req_data: 'primary'}
  //   })
  //   .done((res) => {
  //     console.log(res)
  //     // getStatus(res.task_id);
  //   })
  //   .fail((err) => {
  //     console.log('error');
  //     console.log(err.responseText);
  //   });
  // });
  
  // // snapdeal-primary
  // $(document).ready(function() {
  //   $.ajax({
  //     url: 'data',
  //     type: 'get',
  //     data: { search: 'shampoo', store: 'snapdeal', req_data: 'primary'}
  //   })
  //   .done((res) => {
  //     console.log(res)
  //     // getStatus(res.task_id);
  //   })
  //   .fail((err) => {
  //     console.log('error');
  //     console.log(err.responseText);
  //   });
  // });