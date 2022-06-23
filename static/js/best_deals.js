$(document).ready(function(){
    // Amazon Data Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'amazon'}
    })
    .done((res) => {
        console.log('Amazon Scraped')
        var data = JSON.parse(res.data);
        console.log(data);
        const numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys);
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
        console.log('Amazon Error');
        console.log(err.responseText);
    });

    // Snapdeal Data Scraping
    $.ajax({
        url: 'data',
        type: 'get',
        data: { req_data: 'best-deals', store: 'snapdeal'}
    })
    .done((res) => {
        console.log('Snapdeal Scraped')
        var data = JSON.parse(res.data);
        console.log(data);
        const numOfKeys = Object.keys(data['Deal Link']).length;
        console.log(numOfKeys);
        for(var i=0; i<numOfKeys; ++i){
            var item = `
            <div class="deal-container">
                <a height="100%" href="https://www.amazon.in/stores/page/preview?isPreview=1&isSlp=1&asins=B08N5YD6NF%2CB098XLXDRS%2CB09V1GMW72%2CB094XF92HG%2CB0932LNQ5L%2CB08GG8WCW7%2CB09SQ2KK4B%2CB09QTNZ3QY%2CB09MHTJRWC%2CB09TPHMMFN%2CB09P478FSZ%2CB09V1F446C%2CB09QT9Q2JM%2CB095HZKCGH%2CB0932NQ4CZ%2CB0932MY7RV%2CB09Q3645YF%2CB095Z261FW%2CB09V1G8BQ6%2CB098QB1TPX%2CB09NNBXYLP%2CB09KLYYHHJ%2CB09KGQ1FZ2%2CB09B7YQC5D%2CB09MHVQNBN%2CB09SKV8TXD%2CB09NLS1KZW%2CB09Q35NBG6%2CB09NM2DQ9T%2CB09V1F51SF%2CB0932NLLC5%2CB09NNMYQ3F%2CB09MHTTMNQ%2CB09JN1BMT4%2CB09RX33P36%2CB09M3GP7K6%2CB09P45KHSD%2CB098F7RXYR%2CB097TYRFJJ%2CB08J3D2YHV%2CB09SKTLDK1%2CB09S6V6XN8%2CB09CGRHCSY%2CB09VQ21TW4%2CB09P45KDRY%2CB09LM6CYC4%2CB09MLQPYBF%2CB09RK4H99B%2CB09QC5Y7D4%2CB09JFD5MKT%2CB08HF8Y1YD%2CB09T79X6QD%2CB09NY9BH9V%2CB09S9L66NB%2CB09Q5F1GTP%2CB09CGSC7RF%2CB09GPBVXVJ%2CB09RQLJ41D%2CB09RX285W1%2CB0864KFBNP%2CB09QC4HC7F%2CB09MHT7RPQ%2CB09G9JBTQX%2CB09BRCHW4B%2CB09S6SVHRD%2CB09GVN8D2C%2CB08BD43MZ7%2CB09S3Y2C9F%2CB09MTVR7W6%2CB09JFD8QBL%2CB09MHTFGVK%2CB09MTW7X4D%2CB09QSR2QVG%2CB09S6SGMP2%2CB09S9TVRXL%2CB09MCVK4QR%2CB0933L1RWD%2CB09JZRR376%2CB09S9XXTK5%2CB09SL7GLXW%2CB09C6C12TC%2CB09VGRD512%2CB09F3PY7K2%2CB09NRS37DW%2CB0983RVDPC%2CB09GS14GCK%2CB09FXM3WDR&ref=dlx_deals_gd_dcl_img_0_593ede22_dt_sl15_eb">
                    <center>
                        <img src="https://n4.sdlcdn.com/image/upload/h_258,w_220/Windshield-Glass-Washer-Cleaner-Compact-SDL476592793-1-8792d.jpeg" style="padding: 5px;" alt="deal-img"><br/>
                        <span><del>MRP ₹699</del> ₹159 <span style="color: #558D02; font-weight: 600;">(77% off)</span></span><br/>
                        <p>Clearance Sale - Up to 40000 Off on High Performance Laptops & Desktops</p>
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

    })
    .fail((err) => {
        console.log('Snapdeal Error');
        console.log(err.responseText);
    });
   
});