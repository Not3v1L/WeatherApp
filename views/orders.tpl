%rebase('layout.tpl', title=title, year=year)

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/content/orders.css" />
    <title>Order Form</title>
</head>
<body>
    <div class="root-container">
        <div class="order-container">
            <div class="order-form-container">
                <h3>Make an order</h3>
                <form action="/order" method="post">
                    <div class="form-group">
                        <label for="productName">Product name</label>
                        <input type="text" class="form-control" id="productName" name="PRODUCT_NAME" placeholder="Product name">
                    </div>
                    <div class="form-group">
                        <label for="productDescription">Description</label>
                        <textarea class="form-control no-resize" id="productDescription" name="PRODUCT_DESCRIPTION" rows="5" placeholder="Описание товара"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="phoneNumber">Phone</label>
                        <input type="text" class="form-control" id="phoneNumber" name="PHONE_NUMBER" placeholder="Your phone">
                    </div>
                    <button type="submit" class="btn btn-primary">Order</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>

