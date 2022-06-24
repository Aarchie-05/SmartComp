// flipkart-other
  $(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'gowns', store: 'flipkart', req_data: 'other'}
    })
    .done((res) => {
      console.log('Flipkart other deals scrapped')
      var data = JSON.parse(res.data);
      console.log(data);
      var numOfKeys = Object.keys(data['Item URL']).length;
      console.log(numOfKeys);

      for(var i=0;i<numOfKeys;i++) {
        var item = `
        <div class="column1">
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img src="` + data['Image Link'][i] + `" class="card-img" alt="item_img" style="height:300px">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="product-title">` + data['Product Title'][i] + `</p>`;
                            if(data['Rating'][i] != null || data['Reviews Count'][i] != null) {
                            item += `<div class="btn-group product-ratings"
                                style="border-color: red">`;
                                if(data['Rating'][i] != null) {
                                item += `<span class="rating-values">` + data['Rating'][i] + ` <span class="fa fa-star" style="color: green"></span>`;
                                }
                                if(data['Reviews Count'][i] != null) {
                                item += `<span class="seprator"></span>` + data['Reviews Count'][i] + ` Ratings</span>`;
                                }
                            item += `</div>`;
                            } else {
                              item += `<br>`;
                            }
                            item += `<p class="mt-2">
                                <s class="product-mrp">M.R.P: ` + data['MRP'][i] + ` </s>
                                <span class="product-price"
                                    style="color: maroon; font-size: 20px;">` + data['Price'][i] + `</span>&nbsp;
                                <span class="product-discount"
                                    style="color: #558D02">(` + data['Discount %age'][i] + `)</span>
                            </p>`;  
                            if(data['Is_Assured'][i] == "True"){
                            item += `<img src="../static/images/fassured 1.png" alt=""
                                class="assured"><br><br>`;
                            } else {
                            item += `<br>`;
                            }
                            item += `<a type="button" class="btn btn-primary"
                                style="color: white; background-color: #558D02; border-color: #558D02">Compare
                                Deal</a>
                            <a href= "` + data['Item URL'][i] + `" type="button" class="btn btn-outline-info"
                                style="color: #558D02; border-color: #558D02">View on
                                Flipkart</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
        $("#flipkart-other").append(item);
      }
    })
    .fail((err) => {
      console.log('Flipkart other deals error');
      console.log(err.responseText);
    });
  });


  // amazon-other
  $(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'gowns', store: 'amazon', req_data: 'other'}
    })
    .done((res) => {
      console.log('Amazon other deals scrapped')
      var data = JSON.parse(res.data);
      console.log(data);
      var numOfKeys = Object.keys(data['Item URL']).length;
      console.log(numOfKeys);

      for(var i=0;i<numOfKeys;i++) {
        var item = `
        <div class="column1">
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img src="` + data['Image Link'][i] + `" class="card-img" alt="item_img" style="height:300px">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="product-title">` + data['Product Title'][i] + `</p>`;
                            if(data['Rating'][i] != null || data['Reviews Count'][i] != null) {
                            item += `<div class="btn-group product-ratings"
                                style="border-color: red">`;
                                if(data['Rating'][i] != null) {
                                item += `<span class="rating-values">` + data['Rating'][i] + ` <span class="fa fa-star" style="color: green"></span>`;
                                }
                                if(data['Reviews Count'][i] != null) {
                                item += `<span class="seprator"></span>` + data['Reviews Count'][i] + ` Ratings</span>`;
                                }
                            item += `</div>`;
                            } else {
                              item += `<br>`;
                            }
                            item += `<p class="mt-2">
                                <s class="product-mrp">M.R.P: ` + data['MRP'][i] + ` </s>
                                <span class="product-price"
                                    style="color: maroon; font-size: 20px;">` + data['Price'][i] + `</span>&nbsp;
                                <span class="product-discount"
                                    style="color: #558D02">(` + data['Discount %age'][i] + `)</span>
                            </p>`;  
                            if(data['Is_prime'][i] == true || data['Is_fresh'][i]){
                              if(data['Is_prime'][i] == true) {
                                item += `<span><img src="../static/images/prime 1.png" alt=""
                                    class="assured"></span>`;
                              }
                              if(data['Is_fresh'][i] == true) {
                                item += `<span><img src="../static/images/amazon fresh.png" alt=""
                                    class="assured"></span>`;
                              }
                            item += `<br>`;
                            } else {
                            item += `<br>`;
                            }
                            item += `<a type="button" class="btn btn-primary"
                                style="color: white; background-color: #558D02; border-color: #558D02">Compare
                                Deal</a>
                            <a href= "` + data['Item URL'][i] + `" type="button" class="btn btn-outline-info"
                                style="color: #558D02; border-color: #558D02">View on
                                Amazon</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
        $("#amazon-other").append(item);
      }
    })
    .fail((err) => {
      console.log('error');
      console.log(err.responseText);
    });
  });


  
  // snapdeal-other
  $(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'gowns', store: 'snapdeal', req_data: 'other'}
    })
    .done((res) => {
      console.log('Snapdeal other deals scrapped')
      var data = JSON.parse(res.data);
      console.log(data);
      var numOfKeys = Object.keys(data['Item URL']).length;
      console.log(numOfKeys);

      for(var i=0;i<numOfKeys;i++) {
        var item = `
        <div class="column1">
            <div class="card mb-3" style="max-width: 540px;">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <img src="` + data['Image Link'][i] + `" class="card-img" alt="item_img" style="height:300px">
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <p class="product-title">` + data['Product Title'][i] + `</p>`;
                            if(data['Rating'][i] != null || data['Reviews Count'][i] != null) {
                            item += `<div class="btn-group product-ratings"
                                style="border-color: red">`;
                                if(data['Rating'][i] != null) {
                                item += `<span class="rating-values">` + data['Rating'][i] + ` <span class="fa fa-star" style="color: green"></span>`;
                                }
                                if(data['Reviews Count'][i] != null) {
                                item += `<span class="seprator"></span>` + data['Reviews Count'][i] + ` Ratings</span>`;
                                }
                            item += `</div>`;
                            } else {
                              item += `<br>`;
                            }
                            item += `<p class="mt-2">
                                <s class="product-mrp">M.R.P: ` + data['MRP'][i] + ` </s>
                                <span class="product-price"
                                    style="color: maroon; font-size: 20px;">` + data['Price'][i] + `</span>&nbsp;
                                <span class="product-discount"
                                    style="color: #558D02">(` + data['Discount %age'][i] + `)</span>
                            </p>
                            <br>
                            <a type="button" class="btn btn-primary"
                                style="color: white; background-color: #558D02; border-color: #558D02">Compare
                                Deal</a>
                            <a href= "` + data['Item URL'][i] + `" type="button" class="btn btn-outline-info"
                                style="color: #558D02; border-color: #558D02">View on
                                Snapdeal</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>`;
        $("#snapdeal-other").append(item);
      }
    })
    .fail((err) => {
      console.log('error');
      console.log(err.responseText);
    });
  });