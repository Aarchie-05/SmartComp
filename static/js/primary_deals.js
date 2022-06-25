$(document).ready(function() {

  var url_string = window.location.href;
  var url = new URL(url_string);
  var search_item = url.searchParams.get("search_item");

  // Flipkart
  $.ajax({
    url: 'data',
    type: 'get',
    data: { search: search_item, store: 'flipkart', req_data: 'primary'}
  })
  .done((res) => {
    console.log("Flipkart Primary Deal Scraped");
    $("#flipkart-primary .loading").css({"display":"none"});
    if(res.deal_found == true){
      $("#flipkart-primary .deal-data").css({"display":"block"});
      const numOfKeys = Object.keys(res.data['offers']).length;
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
    } else{
      $("#flipkart-primary .no-deal-found").css({"display":"block"});
    }
  })
  .fail((err) => {
    console.log('Flipkart Primary Deal Error');
    console.log(err.responseText);
    $("#flipkart-primary .loading").css({"display":"none"});
    $("#flipkart-primary .no-deal-found").css({"display":"block"});
  });

  // Amazon
  $.ajax({
    url: 'data',
    type: 'get',
    data: { search: search_item, store: 'amazon', req_data: 'primary'}
  })
  .done((res) => {
    console.log("Amazon Primary Deal Scraped");

    $("#amazon-primary .loading").css({"display":"none"});
    if(res.deal_found == true){
      $("#amazon-primary .deal-data").css({"display":"block"});

      offers = ""
      for (var key of Object.keys(res.data['offers'])) {
        offers += "<li><b>" + key + "</b> : " + res.data['offers'][key] + "</li>";
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
        var assured = `<img src="../static/images/prime 1.png" alt="" class="center prime">`
        $("#primary_prime_amz").append(assured);
      } else if(res.data['type'] == "fresh") {
        var fresh = `<img src="../static/images/amazon fresh.svg" alt="" class="center prime">`
        $("#primary_prime_amz").append(fresh);
      } else {
        $("#primary_prime_amz").append(`<br><br>`);
      }
    } else {
      $("#amazon-primary .no-deal-found").css({"display":"block"});
    }
  })
  .fail((err) => {
    console.log('Amazon Primary Deal Error');
    console.log(err.responseText);
    $("#amazon-primary .loading").css({"display":"none"});
    $("#amazon-primary .no-deal-found").css({"display":"block"});
  });

  // Snapdeal
  $.ajax({
    url: 'data',
    type: 'get',
    data: { search: search_item, store: 'snapdeal', req_data: 'primary'}
  })
  .done((res) => {
    console.log("Snapdeal Primary Deal Scraped");
    $("#snapdeal-primary .loading").css({"display":"none"});
    if(res.deal_found == true){
      $("#snapdeal-primary .deal-data").css({"display":"block"});
      const numOfKeys = Object.keys(res.data['offers']).length;
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
    } else {
      $("#snapdeal-primary .no-deal-found").css({"display":"block"});
    }
  })
  .fail((err) => {
    console.log('Snapdeal Primary Deal Error');
    console.log(err.responseText);
    $("#snapdeal-primary .loading").css({"display":"none"});
    $("#snapdeal-primary .no-deal-found").css({"display":"block"});
  });
});