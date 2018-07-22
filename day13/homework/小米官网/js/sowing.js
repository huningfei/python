 // $(function () {
 //  //
 //  //            function next() {
 //  //
 //  //                //筛选选择器
 //  //                var img=$(".lunbo").find("img");
 //  //                console.log(img);
 //  //
 //  //                    for (var i = 0; i < $(".there-left img").length; i++) {
 //  //                        if ($(".there-left img").eq(i).hasClass("hide")) {
 //  //                            if (i == 5) {
 //  //                                i = -1
 //  //                            }
 //  //                            $("img").eq(i + 1).addClass("hide").siblings().removeClass("hide");
 //  //                            $(".ui-pager-item a").eq(i+1).css('background','white').siblings().css('background','#666');
 //  //                           //  $(".ui-pager-item a").eq(i+1).addClass("gradan ui-pager-item a").siblings().removeClass("gradan ui-pager-item a");
 //  //                            return
 //  //
 //  //
 //  //                        }
 //  //                    }
 //  //            }
 //  //            function prev() {
 //  //                for (var i = 5; i >= 0; i--) {
 //  //                    if ($(".there-left img").eq(i).hasClass("hide")) {
 //  //                        if (i == 0) {
 //  //                            i = 6
 //  //                        }
 //  //                        $("img").eq(i - 1).addClass("hide").siblings().removeClass("hide");
 //  //                         $(".ui-pager-item a").eq(i-1).css('background','white').siblings().css('background','#666');
 //  //                        return
 //  //                    }
 //  //                }
 //  //            }
 //  //
 //  //            var down = setInterval(next, 3000);
 //  //                $(".ui-next").click(function () {
 //  //                    clearInterval(down);
 //  //                    next();
 //  //                });
 //  //
 //  //                $(".ui-prev").click(function () {
 //  //                    clearInterval(down);
 //  //                    prev();
 //  //                });
 //  //
 //  //        });

  $(function () {
            // function   yuandian() {
            //     for (var i=0;i < $(".gradan .ui-pager-item").length;i++){
            //         if ($(".gradan.ui-pager-item").eq(i).css('background','white'));
            //             $(".ui-pager-item a").eq(i+1).css('background','white').siblings().css('background','#666');
            //             $("img").eq(i).addClass("hide").siblings().removeClass("hide");
            //
            //
            //     }
            //
            // }
            //   $('.gradan').click(function () {
            //       clearInterval(down);
            //       yuandian()
            //
            //    });
            function next() {
                // var img=document.getElementsByClassName('lunbo');

                    for (var i = 0; i < $(".there-right img").length; i++) {
                        if ($(".there-right img").eq(i).hasClass("hide")) {
                            if (i == 5) {
                                i = -1
                            }
                            $(".there-right img").eq(i + 1).addClass("hide").siblings().removeClass("hide");
                            $(".ui-pager-item a").eq(i+1).css('background','white').siblings().css('background','#666');
                           //  $(".ui-pager-item a").eq(i+1).addClass("gradan ui-pager-item a").siblings().removeClass("gradan ui-pager-item a");
                            return


                        }
                    }
            }
            function prev() {
                for (var i = 5; i >= 0; i--) {
                    if ($(".there-right img").eq(i).hasClass("hide")) {
                        if (i == 0) {
                            i = 6
                        }
                        $(".there-right img").eq(i - 1).addClass("hide").siblings().removeClass("hide");
                         $(".ui-pager-item a").eq(i-1).css('background','white').siblings().css('background','#666');
                        return
                    }
                }
            }

            var down = setInterval(next, 3000);
                $(".ui-next").click(function () {
                    clearInterval(down);
                    next();
                });

                $(".ui-prev").click(function () {
                    clearInterval(down);
                    prev();
                });
            $(".round").click(function () {
                $(this).siblings().css("backgroundColor",'#666');//除了自己之外，别的圆点都是灰色的

                $(this).css("backgroundColor", "white");//自己变成白色的
                clearInterval(down);
                for (var i =0; i<$(".gradan .round").length;i++){
                    if ($(".round").eq(i).css("backgroundColor")=="rgb(255, 255, 255)"){
                    // if ($(".round").eq(i).css("backgroundColor","white")){
                        $(".there-right img").eq(i).addClass("hide").siblings().removeClass('hide');
                    }
                }

            })


        });