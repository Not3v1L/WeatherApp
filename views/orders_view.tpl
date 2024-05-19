%rebase('layout.tpl',orders = orders, title=title, year=year)

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/content/orders.css" />
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    <title>Order Form</title>
</head>
<body>
    <div class="root-container">
        <div class="order-container">
            <div class="order-form-container">
                <h3>Make an order</h3>
                <form action="/orders" method="post">
                     <div class="form-group">
                        <label for="phoneNumber">Phone</label>
                        <div class="text-field-with-hint">
                            <input type="text" class="form-control" id="phoneNumber" name="PHONE_NUMBER" placeholder="Your phone">
                            <div class="tooltip-custom">
                                <span>
                                    <i class="bi bi-info-circle"></i>
                                </span>
                                <span class="tooltiptext">Number has to be in 8-xxx-xx-xx format</span>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="productName">Product name</label>
                        <div class="text-field-with-hint">
                            <input type="text" class="form-control" id="productName" name="PRODUCT_NAME" placeholder="Product name">
                            <div class="tooltip-custom">
                               <span>
                                   <i class="bi bi-info-circle"></i>
                               </span>
                               <span class="tooltiptext">Product name cannot consist only of spaces</span>
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label for="productDescription">Description</label>
                        <div class="text-field-with-hint">
                            <textarea class="form-control no-resize" id="productDescription" name="PRODUCT_DESCRIPTION" rows="5" placeholder="Product description"></textarea>
                            <div class="tooltip-custom">
                               <span>
                                   <i class="bi bi-info-circle"></i>
                               </span>
                               <span class="tooltiptext">Description cannot consist only of spaces</span>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-primary" value="Send">Order</button>
                </form>
            </div>
        </div>
    </div>

    <div class="orders-container">
            <!-- Цикл для вывода данных из JSON файла -->
            % for key in orders:
                <div>
                    <h3>Orders by phone {{key}}</h3>
                    <table class="order-table">
                        <thead>
                            <tr>
                                <th>Order number</th>
                                <th>Product name</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            <!-- Цикл для вывода каждого заказа -->
                            %for index, order in enumerate(orders[key]):
                                <tr>
                                    <!-- Номер заказа (подсчитывается в цикле) -->
                                    <td>{{index+1}}</td>
                                    <!-- Название продукта из JSON -->
                                    <td>{{ order[0] }}</td>
                                    <!-- Описание продукта из JSON -->
                                    <td>{{ order[1] }}</td>
                                </tr>
                            %end
                        </tbody>
                    </table>
                </div>
            % end
     </div>

</body>
</html>

