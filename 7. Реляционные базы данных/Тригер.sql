CREATE OR REPLACE FUNCTION update_total_value_product()
RETURNS TRIGGER AS $$
BEGIN
    NEW.total_value_product := NEW.saleprice * NEW.quantity;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER trigger_update_total_value_product
BEFORE UPDATE OF quantity ON products
FOR EACH ROW
EXECUTE FUNCTION update_total_value_product();
