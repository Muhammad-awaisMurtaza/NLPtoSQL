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

# -- Enum type for order status
# CREATE TYPE order_status AS ENUM ('PENDING', 'CONFIRMED', 'DELIVERED', 'CANCELLED');

# -- Customers table
# CREATE TABLE Customer (
#     ID SERIAL PRIMARY KEY,
#     FULL_NAME TEXT NOT NULL,
#     ADDRESS TEXT,
#     PHONE VARCHAR(15),
#     EMAIL TEXT UNIQUE,
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Products table
# CREATE TABLE Products (
#     ID SERIAL PRIMARY KEY,
#     NAME TEXT NOT NULL,
#     DESCRIPTION TEXT,
#     PRICE NUMERIC(10,2) NOT NULL,
#     QUANTITY INTEGER CHECK (QUANTITY >= 0),
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Platforms table
# CREATE TABLE Platforms (
#     ID SERIAL PRIMARY KEY,
#     NAME TEXT NOT NULL,
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Promotions table
# CREATE TABLE Promotions (
#     ID SERIAL PRIMARY KEY,
#     NAME TEXT NOT NULL,
#     PLATFORM_ID INTEGER REFERENCES Platforms(ID) ON DELETE CASCADE,
#     DISCOUNT_PERCENTAGE INTEGER CHECK (DISCOUNT_PERCENTAGE >= 0 AND DISCOUNT_PERCENTAGE <= 100),
#     START_DATE TIMESTAMP,
#     END_DATE TIMESTAMP,
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Payment Card Details table
# CREATE TABLE Payment_Card_Details (
#     ID SERIAL PRIMARY KEY,
#     INTENT_ID TEXT NOT NULL,
#     CUSTOMER_ID INTEGER REFERENCES Customer(ID) ON DELETE CASCADE,
#     CARD_NUMBER CHAR(16) NOT NULL,
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Orders table
# CREATE TABLE Orders (
#     ID SERIAL PRIMARY KEY,
#     PRODUCT_ID INTEGER REFERENCES Products(ID) ON DELETE SET NULL,
#     CUSTOMER_ID INTEGER REFERENCES Customer(ID) ON DELETE CASCADE,
#     PLATFORM_ID INTEGER REFERENCES Platforms(ID) ON DELETE SET NULL,
#     PROMOTION_ID INTEGER REFERENCES Promotions(ID) ON DELETE SET NULL,
#     STATUS order_status NOT NULL DEFAULT 'PENDING',
#     QUANTITY INTEGER CHECK (QUANTITY > 0),
#     TOTAL_AMOUNT NUMERIC(10,2) CHECK (TOTAL_AMOUNT >= 0),
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# -- Order Returns table
# CREATE TABLE Order_Returns (
#     ID SERIAL PRIMARY KEY,
#     ORDER_ID INTEGER REFERENCES Orders(ID) ON DELETE CASCADE,
#     REASON_OF_RETURN TEXT,
#     CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );


# INSERT INTO Customer (FULL_NAME, ADDRESS, PHONE, EMAIL)
# VALUES
#   ('Awais Murtaza', '123 Main St, Lahore', '03001234567', 'awais@example.com'),
#   ('Ali Khan', '456 Model Town, Karachi', '03111234567', 'ali@example.com'),
#   ('Daem Rizvi', '789 Gulberg, Islamabad', '03211234567', 'daem@example.com'),
#   ('Fahad Iqbal', '321 Faisal Town, Multan', '03331234567', 'fahad@example.com');

# INSERT INTO Products (NAME, DESCRIPTION, PRICE, QUANTITY)
# VALUES
#   ('Laptop', 'High performance laptop', 1200.00, 10),
#   ('Smartphone', 'Latest Android phone', 800.00, 15),
#   ('Headphones', 'Noise cancelling headphones', 150.00, 30),
#   ('Smartwatch', 'Fitness tracker and smartwatch', 200.00, 20);

# INSERT INTO Platforms (NAME)
# VALUES
#   ('Amazon'),
#   ('eBay'),
#   ('Walmart'),
#   ('BestBuy');

# INSERT INTO Promotions (NAME, PLATFORM_ID, DISCOUNT_PERCENTAGE, START_DATE, END_DATE)
# VALUES
#   ('Amazon 20%', 1, 20, '2025-07-01', '2025-07-31'),
#   ('eBay 10%', 2, 10, '2025-07-05', '2025-07-20'),
#   ('Walmart 30%', 3, 30, '2025-07-10', '2025-07-25'),
#   ('BestBuy 15%', 4, 15, '2025-07-01', '2025-07-15');

# INSERT INTO Payment_Card_Details (INTENT_ID, CUSTOMER_ID, CARD_NUMBER)
# VALUES
#   ('pi_1', 1, '1111222233334444'),
#   ('pi_2', 2, '5555666677778888'),
#   ('pi_3', 3, '9999000011112222'),
#   ('pi_4', 4, '3333444455556666');

# INSERT INTO Orders (PRODUCT_ID, CUSTOMER_ID, PLATFORM_ID, PROMOTION_ID, STATUS, QUANTITY, TOTAL_AMOUNT)
# VALUES
#   (1, 1, 1, 1, 'PENDING', 1, 960.00),
#   (2, 2, 2, 2, 'CONFIRMED', 2, 1440.00),
#   (3, 3, 3, 3, 'DELIVERED', 1, 105.00),
#   (4, 4, 4, 4, 'CANCELLED', 1, 170.00),
#   (1, 2, 1, NULL, 'PENDING', 1, 1200.00); -- no promotion

# INSERT INTO Order_Returns (ORDER_ID, REASON_OF_RETURN)
# VALUES
#   (4, 'Product was defective'),
#   (2, 'Wrong product delivered');
