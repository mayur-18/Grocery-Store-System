// Define your api here
var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var umoListApiUrl = 'http://127.0.0.1:5000/getUMO';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';

// For product drop in order
var productsApiUrl = 'https://fakestoreapi.com/products';

function callApi(method, url, data) {
    $.ajax({
        method: method,
        url: url,
        data: data
    }).done(function( msg ) {
        window.location.reload();
    });


}

function calculateValue() {
    var total = 0;
    $(".product-item").each(function(index) {
        var qty = parseFloat($(this).find('.product-qty').val());
        var price = parseFloat($(this).find('#product_price').val());
        var itemTotal = parseFloat($(this).find('#item_total').val());

        // Recalculate the item total if quantity is changed or item total is manually entered
        if (isNaN(itemTotal) || itemTotal <= 0) {
            itemTotal = price * qty;
            $(this).find('#item_total').val(itemTotal.toFixed(2));
        } else if (itemTotal !== price * qty) {
            // Reflect manual changes to item_total if different from calculated value
            itemTotal = parseFloat($(this).find('#item_total').val());
        } else {
            itemTotal = price * qty;
        }

        total += itemTotal;
    });
    $("#product_grand_total").val(total.toFixed(2));
}

function orderParser(order) {
    return {
        id : order.id,
        date : order.employee_name,
        orderNo : order.employee_name,
        customerName : order.employee_name,
        cost : parseInt(order.employee_salary)
    }
}

function productParser(product) {
    return {
        id : product.id,
        name : product.employee_name,
        unit : product.employee_name,
        price : product.employee_name
    }
}

function productDropParser(product) {
    return {
        id : product.id,
        name : product.title
    }
}

//To enable bootstrap tooltip globally
// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// });