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
                            $(".ui-pager-item a").eq(i+1).css('background','red').siblings().css('background','#666');
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

        });