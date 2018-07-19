 $(function () {

            function next() {

                //筛选选择器
                var img=$(".lunbo").find("img");
                console.log(img);

                    for (var i = 0; i < img.length; i++) {
                        if ($("img").eq(i).hasClass("hide")) {
                            if (i == 5) {
                                i = -1
                            }
                            $("img").eq(i + 1).addClass("hide").siblings().removeClass("hide");
                            $(".ui-pager-item a").eq(i+1).css('background','white').siblings().css('background','#666');
                           //  $(".ui-pager-item a").eq(i+1).addClass("gradan ui-pager-item a").siblings().removeClass("gradan ui-pager-item a");
                            return


                        }
                    }
            }
            function prev() {
                for (var i = 5; i >= 0; i--) {
                    if ($("img").eq(i).hasClass("hide")) {
                        if (i == 0) {
                            i = 6
                        }
                        $("img").eq(i - 1).addClass("hide").siblings().removeClass("hide");
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