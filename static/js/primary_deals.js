// flipkart-primary
$(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'tshirt', store: 'flipkart', req_data: 'primary'}
    })
    .done((res) => {
      console.log("Flipkart primary deal recieved");
      console.log(res);
      console.log(res.data['item_link']);

      const numOfKeys = Object.keys(res.data['offers']).length;
      console.log(numOfKeys);
      var offers = "";
      for(var i=0; i<numOfKeys; ++i){
        var li = "<li>" + res.data['offers'][i] + "</li>";
        offers += li;
      }
      $("#primary_img_flip").attr("src", res.data['img']);
      $("#primary_title_flip").append(res.data['title']);
      $("#primary_rating_flip").append(res.data['rating']);
      $("#primary_rating_count_flip").append(res.data['no_of_ratings']);
      $("#primary_mrp_flip").append(res.data['mrp']);
      $("#primary_price_flip").append(res.data['price']);
      $("#primary_discount_flip").append(res.data['discount']);
      $("#primary_offers_flip").append(offers);
      if(res.data['is_assured']==true) {
        var assured = `<img src="../static/images/fassured 1.png" alt="" class="center assured mb-1">`
        $("#primary_assured_flip").append(assured);
      } else {
        $("#primary_assured_flip").append(`<br>`);
      }
    })
    .fail((err) => {
      console.log('Flipkart primary data Error');
      console.log(err.responseText);
    });
  });
  
  // amazon-primary
  $(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'tshirt', store: 'amazon', req_data: 'primary'}
    })
    .done((res) => {
      console.log("Amazon primary deal recieved");
      console.log(res);
      console.log(res.data['item_link']);

      offers = ""
      for (var key of Object.keys(res.data['offers'])) {
        offers += "<li><b>" + key + "</b> : " + res.data['offers'][key] + "</li>";
        console.log(key + " -> " + res.data['offers'][key])
      }
      
      $("#primary_img_amz").attr("src", res.data['img']);
      $("#primary_title_amz").append(res.data['title']);
      $("#primary_rating_amz").append(res.data['rating']);
      $("#primary_rating_count_amz").append(res.data['no_of_ratings']);
      $("#primary_mrp_amz").append(res.data['mrp']);
      $("#primary_price_amz").append(res.data['price']);
      $("#primary_discount_amz").append(res.data['discount']);
      $("#primary_offers_amz").append(offers);
      if(res.data['type']=="prime") {
        var assured = `<img src="{% static 'images/prime 1.png' %}" alt="" class="center prime">`
        $("#primary_prime_amz").append(assured);
      } else if(res.data['type'] == "fresh") {
        var fresh = `<img src="{% static 'images/amazon fresh.svg' %}" alt="" class="center prime">`
        $("#primary_prime_amz").append(fresh);
      } else {
        $("#primary_prime_amz").append(`<br><br>`);
      }
    })
    .fail((err) => {
      console.log('Amazon error');
      console.log(err.responseText);
    });
  });
  
  // snapdeal-primary
  $(document).ready(function() {
    $.ajax({
      url: 'data',
      type: 'get',
      data: { search: 'tshirt', store: 'snapdeal', req_data: 'primary'}
    })
    .done((res) => {
      console.log("Snapdeal primary deal recieved");
      console.log(res);
      console.log(res.data['item_link']);

      const numOfKeys = Object.keys(res.data['offers']).length;
      console.log(numOfKeys);
      var offers = "";
      for(var i=0; i<numOfKeys; ++i){
        var li = "<li>" + res.data['offers'][i] + "</li>";
        offers += li;
      }

      $("#primary_img_snap").attr("src", res.data['img']);
      $("#primary_title_snap").append(res.data['title']);
      $("#primary_rating_snap").append(res.data['rating']);
      $("#primary_rating_count_snap").append(res.data['no_of_ratings']);
      $("#primary_mrp_snap").append(res.data['mrp']);
      $("#primary_price_snap").append(res.data['price']);
      $("#primary_discount_snap").append(res.data['discount']);
      if(offers!="") {
        var disp = `
            <p class="center">Offers</p>
            <ul id="primary_offers_flip">
                ` + offers + `
            </ul>`;
        $("#primary_offers_snap").append(disp);
      }
    })
    .fail((err) => {
      console.log('error');
      console.log(err.responseText);
    });
  });