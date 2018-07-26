   // window.onload=function (ev) {
   //             var cart = document.getElementsByClassName('city','wheater')[0];
   //             var cart2=document.getElementsByClassName('wheater')[0];
   //
   //             cart.onmouseover=function () {
   //
   //                 cart2.style.display='block';
   //             };
   //             cart.onmouseout=function () {
   //                 cart2.style.display='none';
   //
   //             };
   //         };

  $(function () {

                $.ajax({

                    url:'https://free-api.heweather.com/s6/weather/forecast?location=beijing&key=7e2f47ead8a94ecab4b9e04f1f8d4a3f',
                    type:'get',
                    success:function (data) {
                        console.log(data.HeWeather6[0]);
                        console.log(data.HeWeather6[0].daily_forecast[0].cond_code_d);
                        $('.left-top .tianqi img').attr('src',"./img/"+data.HeWeather6[0].daily_forecast[0].cond_code_d+'.png');
                        $('.one img').attr('src',"./img/"+data.HeWeather6[0].daily_forecast[0].cond_code_d+'.png');
                        $('.there .day1 img').attr('src',"./img/"+data.HeWeather6[0].daily_forecast[0].cond_code_d+'.png');
                        $('.there .day2 img').attr('src',"./img/"+data.HeWeather6[0].daily_forecast[1].cond_code_d+'.png');
                        $('.there .day3 img').attr('src',"./img/"+data.HeWeather6[0].daily_forecast[2].cond_code_d+'.png');
                        // 日期设置
                        $('.wheater .two .date').text(data.HeWeather6[0].daily_forecast[0].date);//设置第二行日期
                        $('.there .day1 .date').text(data.HeWeather6[0].daily_forecast[0].date);
                        $('.there .day2 .date').text(data.HeWeather6[0].daily_forecast[1].date);
                        $('.there .day3 .date').text(data.HeWeather6[0].daily_forecast[2].date);
                        //设置天气文字
                         $('.there .day1 .wea').text(data.HeWeather6[0].daily_forecast[0].cond_txt_d);
                        $('.there .day2 .wea').text(data.HeWeather6[0].daily_forecast[1].cond_txt_d);
                        $('.there .day3 .wea').text(data.HeWeather6[0].daily_forecast[2].cond_txt_d);
                        //设置温度
                        $('.left-top .tianqi span').text(data.HeWeather6[0].daily_forecast[0].tmp_min+'℃');
                         $('.there .day1 .temp').text(data.HeWeather6[0].daily_forecast[0].tmp_min+'℃');
                         $('.there .day2 .temp_min').text(data.HeWeather6[0].daily_forecast[1].tmp_min );
                         $('.there .day2 .temp_max').text(data.HeWeather6[0].daily_forecast[1].tmp_max+'℃');
                         $('.there .day3 .temp_min').text(data.HeWeather6[0].daily_forecast[2].tmp_min);
                         $('.there .day3 .temp_max').text(data.HeWeather6[0].daily_forecast[2].tmp_max+'℃');

                    },

					error:function (err) {
						console.log(err);
					}


                });
                $.ajax({
                    url:'https://free-api.heweather.com/s6/air/now?parameters?location=beijing&key=7e2f47ead8a94ecab4b9e04f1f8d4a3f',
                    type:'get',
                    success:function (data){
                        console.log(data.HeWeather6[0]);

                    }




                });
               $(function () {
                   $(".wheater.there").click(function () {
                       // location.href="http://www.weather.com.cn/weather/101010100.shtml#7d"
                       window.open("https://www.baidu.com");

                   });
                   $('.left-top').mouseover(function () {
                       $(".wheater").stop().slideDown(500);
                   }).mouseout(function () {

                        $(".wheater").stop().slideUp(500);
                   });
                   $('.wheater').mouseover(function () {
                        $(".wheater").stop().slideDown(500);

                   }).mouseout(function () {

                         $(".wheater").stop().slideUp(500);
                   });


               })
     });