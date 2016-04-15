CREATE TABLE pies(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name           CHAR(100)    NOT NULL,
  price          INT     NOT NULL,
  recipe         TEXT
);

INSERT INTO pies (id, name, price, recipe) VALUES (1, 'Cherry', '1000', 'Take a bunch of cherries, some brandy, etc...'), (2, 'Steak and kidney', '1700', 'Get out your flask of Guinness for this hearty meal ...'), (3, 'Chicken and mushroom', '1350', 'A lovely winter feast with lots of roots ...');
