-- SQL script that creates a trigger that decreases
-- the quantity of an item after adding a new order.

CREATE TRIGGER reset_valid_email
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = FALSE;
    END IF;
END;
