SELECT 
    c.name AS customer_name,
    p.name AS product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_amount,
    pay.status AS payment_status,
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON p.id = oi.product_id
JOIN payments pay ON pay.order_id = o.id
ORDER BY o.order_date DESC;
