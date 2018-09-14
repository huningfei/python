// {/*<script>*/
// }
//点赞操作
$(".s21").click(function () {
    // 取到点赞操作需要的三个数据
    // 1. 谁 2. 哪篇文章 3. 支持or反对
    var userId = {
    {
        request.user.id
    }
}
    ;  //如果是字符串外面需要加引号
    var reportId = {
    {
        report.id
    }
}
    ;
    var isUp = $(this).hasClass("diggit"); //判断你现在点击的这个有没有这个样式类

    // 往后端发送请求，创建点赞记录
    $.ajax({
        url: "/fault-report/updown/",
        type: 'post',
        data: {
            "user_id": userId,
            "report_id": reportId,
            "is_up": isUp,
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val() // 一定不要忘了
        },
        success: function (res) {
            console.log(res);
            if (res.code === 1) {
                //有错误就展示错误提示
                $("#digg_tips").text(res.msg);
            } else {
                //在页面展示效果
                // 数据库加1
                if (isUp) {
                    // 点赞数+1
                    var $upEle = $("#digg_count");//把找到$digg_count的值赋值给一个变量
                    var oldNum = $upEle.text(); //获取到旧的值
                    $upEle.text(+oldNum + 1); //设置旧的值加1 oldNum默认是字符串前面加+转换成数字
                } else {
                    //反对数加1
                    var $downEle = $("#bury_count");//把找到$digg_count的值赋值给一个变量
                    var oldNum = $downEle.text(); //获取到旧的值
                    $downEle.text(parseInt(oldNum) + 1); //设置旧的值加1 把字符串转换成数字
                }
                //展示成功的提示信息，digg_tips显示文本的类
                $("#digg_tips").text(res.msg);

            }

        }

    })
});
//发表评论
var parentId; //设置一个全局变量
$("#submit-comment").click(function () {
    //需要获取1 文章id  2谁评论的  3 评论的内容
    var reportId = {
    {
        report.id
    }
}
    ;
    var oldcontent = $("#content").val(); //内容

    var content = oldcontent.slice(oldcontent.indexOf("\n") + 1,);//不含用户名的内容
    $.ajax({
        url: "/fault-report/comment/",
        type: "post",
        data: {
            "report_id": reportId,
            "content": content,
            "parent_id": parentId,
            "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
        },
        success: function (res) {
            //接受views里面传过来的res
            console.log(res);
            if (res.code === 0) {
                //评论完之后自动在页面显示评论的内容，用的模板字符串
                //s21={{ res.data.id }} 获取评论的id
                var s = `
                                     <div class="list-group-item">
                <h4 class="list-group-item-heading" s21="${res.data.id}">
                    <span>${res.data.n}楼</span>
                    <span>${res.data.create_time}</span>
                    <span>${res.data.user}</span>
                    <span class="replay pull-right">回复</span>
                </h4>
                <p class="list-group-item-text">
                   ${res.data.content}
                </p>`;
                //将创建好的评论楼 追加到评论列表中
                // 也就是将s字符串追加到 comment-list 下面的 div中
                $(".comment-list>div").append(s);
                //清空评论输入框
                $("#content").val("");
                //清空全局变量
                parentId = undefined;

            }

        }


    })

});
//给回复按钮绑定事件
$(".replay").click(function () {
    $(".comment-list").on("click", ".replay", function () {  //用事件委托这种绑定方式，新评论的显示的回复按钮也就默认绑定了这个效果
        //点击回复按钮，光标聚焦到输入框里面
        //获取回复的用户名
        var replayname = $(this).prev().text();//获取回复按钮上面的那个标签的内容prev是上面的
        console.log(replayname);
        $("#content").focus().text("@" + replayname + "\n"); //获取焦点并把回复的用户名写到里面
        $("#content").val("@" + replayname + "\n").focus();  // 获取焦点
        //只要点击回复按钮，就把全局变量保存为回复评论的id值
        parentId = $(this).parent().attr("s21"); //先找到回复按钮的父标签，就是h4,然后设置s21的值
    })


// </script>