SELECT seller_id,
       sum(t1.price) AS totalRevenue,
       count(distinct t1.order_id) AS qtdeSalles

FROM tb_order_items AS t1

GROUP BY seller_id