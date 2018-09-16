// 设置错误提示
$(function () {
    // $("#submit-btn").click(function () {
    //     // 因为注册功能有头像文件 数据，所以要用FormData对象提交数据
    //     var fd = new FormData();
    //     fd.append("username", $("#id_username").val());
    //     fd.append("phone", $("#id_phone").val());
    //     fd.append("email", $("#id_email").val());
    //     fd.append("csrfmiddlewaretoken", $("[name='csrfmiddlewaretoken']").val());
    //     // avatar头像
    //     fd.append("avatar", $("#id_avatar")[0].files[0]);
    //     $.ajax({
    //         url: "/edit_info/",
    //         type: "post",
    //         data: fd,
    //         contentType: false,
    //         processData: false,
    //         success: function (res) {
    //             if (res.code === 1) {
    //                 $.each(res.error, function (k, v) {
    //                     console.log(k, v[0]);
    //                     {
    //                         // #先找到input标签，下面的那个标签，然后设置错误信息，再找到显示错误标签的父标签，设置has - error
    //
    //                     }
    //                     $("#id_" + k).next().text(v[0]).parent().addClass("has-error");
    //                 })
    //             } else {
    //                 location.href = res.url
    //             }
    //
    //         }
    //     })
    //
    // });

// 给input标签绑定获取焦点就删除错误提示的动作
    $(".register-form input").focus(function () {
        $(this).next().text("").parent().removeClass("has-error");
    });

//头像预览功能
//值发生变化了
    $("#id_avatar").change(function () {
        // 取到用户选中的头像文件
        var fileObj = this.files[0]; //路径
        // 新建一个FileReader对象，从本地磁盘加载文件数据
        var fr = new FileReader();
        fr.readAsDataURL(fileObj);
        // 读取文件是需要时间的
        fr.onload = function () {
            // 找到头像预览的img标签，把它的src属性设置成我读取的用户选中的图片
            $("#avatar-img").attr("src", fr.result)  //结果
        }

    });
});
