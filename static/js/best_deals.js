$(document).ready(function(){
    // Amazon Data Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'amazon'}
    })
    .done((res) => {
        console.log('success')
        data = JSON.parse(res.data)
        console.log(data)
        const numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys)
        for(var i=0; i<numOfKeys; ++i){
            var item = `
                    <div class="deal-container" style="height:320px">
                        <a height="100%" href="` + data['Deal Link'][i] + `">
                            <center>
                                <div style="height:180px;">
                                    <img src="` + data['Image Link'][i] + `" style="padding: 40px 40px 20px 40px; max-height:100%; max-width:100%; width: auto; height: auto;" alt="deal-img">
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

    })
    .fail((err) => {
        console.log('amazon best deals error');
        console.log(err.responseText);
    });

    // Snapdeal Data Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'amazon'}
    })
    .done((res) => {
        console.log('success')
        data = JSON.parse(res.data)
        console.log(data)
        const numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys)
        for(var i=0; i<numOfKeys; ++i){
            var item = `
                    <div class="deal-container" style="height:320px">
                        <a height="100%" href="` + data['Deal Link'][i] + `">
                            <center>
                                <div style="height:180px;">
                                    <img src="` + data['Image Link'][i] + `" style="padding: 40px 40px 20px 40px; max-height:100%; max-width:100%; width: auto; height: auto;" alt="deal-img">
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

    })
    .fail((err) => {
        console.log('error');
        console.log(err.responseText);
    });


   
});