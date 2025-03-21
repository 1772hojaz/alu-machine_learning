-- Write a SQL script that creates a trigger that
-- decreases the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS decrease_quantity;

DELIMITER $$
CREATE TRIGGER decrease_quantity
       AFTER INSERT
       ON `orders` FOR EACH ROW
BEGIN
        UPDATE items SET quantity = quantity - new.number
        WHERE items.name=new.item_name;
END $$

DELIMITER ;
