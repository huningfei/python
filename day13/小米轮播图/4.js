 $(function () {

            function next() {

                //筛选选择器
                var img=$(".there-right").find("img");
                console.log(img);

                    for (var i = 0; i < img.length; i++) {
                        if ($("img").eq(i).hasClass("xianshi")) {
                            if (i == 5) {
                                i = -1
                            }
                            $("img").eq(i + 1).addClass("xianshi").siblings().removeClass("xianshi");
                            // $("img").eq(i + 1).addClass("xianshi").siblings().removeClass("xianshi");
                            // $("img").eq(i + 1).attr('class','yincang xianshi');
                             // $('.wrap').attr('class','wrap wrap2');
                            $(".ui-pager-item a").eq(i+1).css('background','white').siblings().css('background','#666');
                           //  $(".ui-pager-item a").eq(i+1).addClass("gradan ui-pager-item a").siblings().removeClass("gradan ui-pager-item a");
                            return


                        }
                    }
            }
            function prev() {
                for (var i = 5; i >= 0; i--) {
                    if ($("img").eq(i).hasClass("xianshi")) {
                        if (i == 0) {
                            i = 6
                        }
                        $("img").eq(i - 1).addClass("xianshi").siblings().removeClass("xianshi");
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