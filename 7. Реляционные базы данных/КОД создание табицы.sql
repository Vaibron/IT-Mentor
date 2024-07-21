CREATE TABLE Employees (
	EmployeeID SERIAL PRIMARY KEY,
	LastName VARCHAR(50),
	FirstName VARCHAR(50),
	MiddleName VARCHAR(50),
	Position VARCHAR(50),
	Address VARCHAR(100),
	HomePhone VARCHAR(20),
	BirthDate DATE
	);
CREATE TABLE Clients (
	ClientID SERIAL PRIMARY KEY,
	FullName VARCHAR(100),
	Address VARCHAR(100),
	Phone VARCHAR(20)
	);

CREATE TABLE Suppliers (
	SupplierID SERIAL PRIMARY KEY,
	SupplierName VARCHAR(100),
	SupplierRepresentative VARCHAR(100),
	ContactPhone VARCHAR(20),
	Address VARCHAR(100)
	);

CREATE TABLE Deliveries (
	DeliveryID SERIAL PRIMARY KEY,
	SupplierID INT,
	DeliveryDate DATE,
	FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
	);

CREATE TABLE Products (
	ProductID SERIAL PRIMARY KEY,
	DeliveryID INT,
	ProductName VARCHAR(100),
	TechnicalSpecifications VARCHAR(255),
	Description TEXT,
	Image TEXT,
	PurchasePrice DECIMAL(10, 2),
	SalePrice DECIMAL(10, 2),
	FOREIGN KEY (DeliveryID) REFERENCES Deliveries(DeliveryID)
	);


CREATE TABLE Orders (
	OrderID SERIAL PRIMARY KEY,
	EmployeeID INT,
	ProductID INT,
	OrderDate DATE,
	ExecutionDate DATE,
	ClientID INT,
	FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
	FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
	FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
	);
