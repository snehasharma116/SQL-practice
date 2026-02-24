CREATE TABLE sales (
    order_id INT,
    product_name VARCHAR(50),
    category VARCHAR(50),
    quantity INT,
    price INT,
    city VARCHAR(50)
);

INSERT INTO sales VALUES
(1, 'Laptop', 'Electronics', 2, 50000, 'Delhi'),
(2, 'Phone', 'Electronics', 3, 20000, 'Mumbai'),
(3, 'Shoes', 'Fashion', 5, 2000, 'Delhi'),
(4, 'Watch', 'Fashion', 4, 3000, 'Jaipur'),
(5, 'Tablet', 'Electronics', 1, 30000, 'Mumbai');

SELECT city, SUM(quantity * price) AS total_sales
FROM sales
GROUP BY city;

SELECT category, SUM(quantity) AS total_quantity
FROM sales
GROUP BY category;
