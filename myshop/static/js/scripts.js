$(document).ready(function () {
    var form = $('#form_buying_product');
   form.on('submit',function (e) {
       e.preventDefault();
       var num = $('#number').val();
       console.log(num);
       var submit_btn = $('#submit_btn');
       var product_id = submit_btn.data("product_id");
       var product_name = submit_btn.data("name");
       var product_price = submit_btn.data("price");
       console.log(product_id);
       console.log(product_name);
       console.log(product_price);

       /*var data = {};
       data.product_id = product_id;
       data.num = num;
       var csrf_token = ('#form_buying_product [name="csrfmiddlewaretoken"]').val();
       data["csrfmiddlewaretoken"] = csrf_token;

       var url = form.attr('action');
       $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data) {
               console.log('OK')
           },
           error: function () {
               console.log('error')
           }
       });*/

       $('.basket-items ul').append('<li>'+product_name+', ' + num + 'шт. ' + 'по ' + product_price + 'kzt  ' +
           '<a class="delete-item" href="">x</a>' + '</li>');
   });

   function showingCart() {
       $('.basket-items').toggleClass('hidden');
   }

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingCart();
    });

    $('.basket-container').mouseover(function () {
        showingCart();
    });

    $('.basket-container').mouseout(function () {
        showingCart();
    });

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault()
        $(this).closest('li').remove();
    })

});