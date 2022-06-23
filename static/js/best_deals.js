$(document).ready(function(){
    // Amazon Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'amazon'}
    })
    .done((res) => {
        $("#loading").remove()
        console.log('Amazon Scraped')
        var data = JSON.parse(res.data);
        console.log(data);
        var numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys);

        for(var i=0; i<numOfKeys; ++i){
            var item = `
            <div class="deal-container" style="height:320px">
                <a height="100%" target="_blank" href="` + data['Deal Link'][i] + `">
                    <center>
                        <div style="height:180px;">
                            <img src="` + data['Image Link'][i] + `" loading="lazy" style="padding: 40px 40px 20px 40px; max-height:100%; max-width:100%; width: auto; height: auto;" alt="deal-img">
                        </div>
                        <br/>
                        <div style="padding:0 10px">
                            <span style="color: #558D02; font-weight: 600;">` + data['Offer'][i] + `</span><br/>
                            <p>` + data['Product Title'][i] + `</p>
                        </div>
                    </center>
                </a>    
            </div>`;
            $("#amazon-carousel").append(item);
        }
        $("#amazon-carousel").owlCarousel({
            loop:true,
            margin:25,
            dots:false,
            responsive:{0:{items:1}, 600:{items:3}, 1000:{items:4}}
        });

        if(numOfKeys > 0){
            var header = `<h4 style="margin-bottom: 20px; vertical-align: middle;"><img height="50px" src="../static/images/Amazon logo.png"/> - Deals of the Day</h4>`;
            $("#amazon-carousel").parent().prepend(header)
        } else {
            $("#amazon-carousel").parent().remove()
        }
    })
    .fail((err) => {
        console.log('Amazon Error');
        console.log(err.responseText);
        $("#amazon-carousel").parent().remove()
    });


    //Flipkart Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'flipkart'}
    })
    .done((res) => {
        $("#loading").remove()
        console.log('Flipkart Scraped')
        var data = JSON.parse(res.data);
        console.log(data);
        const numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys);

        for(var i=0; i<numOfKeys; ++i){
            var item = `
            <div class="deal-container" style="height:280px">
                <a height="100%" target="_blank" href="` + data['Deal Link'][i] + `">
                    <center>
                        <div style="height:180px;">
                            <img src="` + data['Image Link'][i] + `" loading="lazy" style="padding: 40px 40px 20px 40px; max-height:100%; max-width:100%; width: auto; height: auto;" alt="deal-img">
                        </div>
                        <br/>
                        <div style="padding:0 10px">
                            <span style="color: #558D02; font-weight: 600;">` + data['Offer'][i] + `</span><br/>
                            <p>` + data['Product Title'][i] + `</p>
                        </div>
                    </center>
                </a>    
            </div>`;
            $("#flipkart-carousel").append(item);
        }
        $("#flipkart-carousel").owlCarousel({
            loop:true,
            margin:25,
            dots:false,
            responsive:{0:{items:1}, 600:{items:3}, 1000:{items:4}}
        });

        if(numOfKeys > 0){
            var header = `<h4 style="margin-bottom: 20px; vertical-align: middle;"><img height="70px" src="../static/images/Flipkart logo.png"/> - Today's Offers</h4>`;
            $("#flipkart-carousel").parent().prepend(header)
        } else {
            $("#flipkart-carousel").parent().remove();
        }

    })
    .fail((err) => {
        console.log('Flipkart Error');
        console.log(err.responseText);
        $("flipkart-carousel").parent().remove();
    });


    
    // Snapdeal Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'snapdeal'}
    })
    .done((res) => {
        $("#loading").remove()
        console.log('Snapdeal Scraped')
        var data = JSON.parse(res.data);
        console.log(data);
        var numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys);
        
        for(var i=0; i<numOfKeys; ++i){
            var item = `
            <div class="deal-container" style="height:420px">
                <a height="100%" target="_blank" href="` + data['Deal Link'][i] + `">
                    <center>
                        <div>
                            <img src="` + data['Image Link'][i] + `" loading="lazy" style="padding: 5px;" alt="deal-img"><br/>
                        </div>
                        <div style="padding:0 10px">
                            <span><del>MRP ` + data['MRP'][i] + `</del> ` + data['Price'][i] + ` <span style="color: #558D02; font-weight: 600;">(` + data['Discount'][i] + `)</span></span><br/>
                            <p>` + data['Product Title'][i] + `</p>
                        </div>
                    </center>
                </a>    
            </div>`;
            $("#snapdeal-carousel").append(item);
        }
        $("#snapdeal-carousel").owlCarousel({
            loop:true,
            margin:25,
            dots:false,
            responsive:{0:{items:1}, 600:{items:3}, 1000:{items:4}}
        });
                
        if(numOfKeys>0){
            var header = `<h4 style="margin-bottom: 20px; vertical-align: middle;"><img height="40px" src="../static/images/snapdeal logo.png"/> - Half Price Store</h4>`;
            $("#snapdeal-carousel").parent().prepend(header)
        } else{
            $("#snapdeal-carousel").parent().remove()
        }

    })
    .fail((err) => {
        console.log('Snapdeal Error');
        console.log(err.responseText);
        $("#snapdeal-carousel").parent().remove()
    });
   

    
});