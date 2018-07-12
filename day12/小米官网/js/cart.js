   window.onload=function (ev) {
            var cart = document.getElementsByClassName('topbar-cart')[0];
            var cart2=document.getElementsByClassName('cart-info')[0];

            cart.onmouseover=function () {

                cart2.style.display='block';
            };
            cart.onmouseout=function () {
                cart2.style.display='none';

            };
        }