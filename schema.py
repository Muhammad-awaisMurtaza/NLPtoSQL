db_schema_details = """
  Customer:
    ID: Unique ID to identify each row.
    FULL_NAME: Full name of the customer.
    ADDRESS: Location where the customer lives.
    PHONE: Phone number of the customer.
    EMAIL: Email address of the customer.
    CREATED_AT: DateTime stamp when this object was created.

  Products:
    ID: Unique ID to identify each row.
    NAME: Name of the product.
    DESCRIPTION: A short summary of the product.
    PRICE: Amount in dollars needed to purchase this product.
    QUANTITY: Maximum available quantity of this product.
    CREATED_AT: DateTime stamp when this object was created.

  Platforms:
    ID: Unique ID to identify each row.
    NAME: Name of the store/center where the product is purchased from, such as Amazon, eBay, or Walmart.
    CREATED_AT: DateTime stamp when this object was created.

  Promotions:
    ID: Unique ID to identify each row.
    NAME: Short name of the promotion for reference, such as Amazon 50%, eBay 10%, etc.
    PLATFORM_ID: Foreign key that points to the primary key (ID) of the platforms table, indicating which platform this promotion applies to.
    DISCOUNT_PERCENTAGE: An integer value between 0 and 100, indicating the discount percentage.
    START_DATE: DateTime when this promotion becomes available to customers.
    END_DATE: Last date and time when this promotion is valid.
    CREATED_AT: DateTime stamp when this object was created.

  Payment_Card_Details:
    ID: Unique ID to identify each row.
    INTENT_ID: Third-party app key for reference, such as Stripe Intent ID.
    CUSTOMER_ID: Foreign key that points to the primary key (ID) of the customers table, indicating which customer this card information belongs to.
    CARD_NUMBER: 16-digit card number.
    CREATED_AT: DateTime stamp when this object was created.

  Orders:
    ID: Unique ID to identify each row.
    PRODUCT_ID: Foreign key that points to the primary key (ID) of the products table, indicating which product was ordered.
    CUSTOMER_ID: Foreign key that points to the primary key (ID) of the customers table, indicating which customer made the order.
    PLATFORM_ID: Foreign key that points to the primary key (ID) of the platforms table, indicating which platform the order was made on.
    PROMOTION_ID: Foreign key that points to the primary key (ID) of the promotions table, indicating if a discount was applied.
    STATUS: Enum values indicating the status of the order. Possible values are PENDING, CONFIRMED, DELIVERED, CANCELLED.
    QUANTITY: Integer value of how many units of the product were purchased in this order.
    TOTAL_AMOUNT: Total amount the customer needs to pay for this order.
    CREATED_AT: DateTime stamp when this object was created.
  
  Order_Returns:
    ID: Unique ID to identify each row.
    ORDER_ID: Foreign key that points to the primary key (ID) of the orders table, indicating which order was returned.
    REASON_OF_RETURN: Short summary of why this order was returned.
    CREATED_AT: DateTime stamp when this object was created.
"""
