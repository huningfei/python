   window.onload=function (ev) {
               var cart = document.getElementsByClassName('city','wheater')[0];
               var cart2=document.getElementsByClassName('wheater')[0];

               cart.onmouseover=function () {

                   cart2.style.display='block';
               };
               cart.onmouseout=function () {
                   cart2.style.display='none';

               };
           };

   // $(function () {
   //     var tianqi=$(".left-top");
   //     tianqi.click(function () {
   //          tianqi.mouseover(function () {
   //
   //              // $('.wheater').css("display",'block')
   //              $('.wheater').style.display='block'
   //
   //
   //         });
   //        tianqi.mouseout(function () {
   //
   //             // $('.wheater').css("display",'none')
   //
   //            $('.wheater').style.display='none';
   //
   //          });

      // var tianqi=$(".wheater");
      //   tianqi.mouseover(function () {
      //
      //        $('.wheater').css("display",'block')
      //   });
      //  tianqi.mouseout(function () {
      //       $('.wheater').css("display",'none')
      //
      //
      //  })

   //     })
   //
   //
   // });