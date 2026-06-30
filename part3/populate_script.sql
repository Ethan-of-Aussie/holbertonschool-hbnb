-- DELETE FROM users;
-- DELETE FROM places;
-- DELETE FROM amenities;
-- DELETE FROM place_amenity;

-- DROP TABLE amenities;

-- ALTER TABLE amenities DROP COLUMN place_id;

INSERT INTO users (id, first_name, last_name, email, password, is_admin) VALUES
('9b17d3fd-4e2b-4c9a-b0db-9e3b50e3f001', 'John', 'Doe', 'john@example.com', 'hashed_password_1', 1),
('9b17d3fd-4e2b-4c9a-b0db-9e3b50e3f002', 'Jane', 'Smith', 'jane@example.com', 'hashed_password_2', 0),
('9b17d3fd-4e2b-4c9a-b0db-9e3b50e3f003', 'Alice', 'Brown', 'alice@example.com', 'hashed_password_3', 0);

INSERT INTO places (id, title, description, price, latitude, longitude, user_id) VALUES
(
    'f31a4e7a-1111-4444-8888-aaaaaaaaaaaa',
    'Beach House',
    'Beautiful ocean view',
    250.00,
    -37.8136,
    144.9631,
    '9b17d3fd-4e2b-4c9a-b0db-9e3b50e3f001'
),
(
    'f31a4e7a-2222-4444-8888-bbbbbbbbbbbb',
    'City Apartment',
    'Close to downtown',
    150.00,
    -37.8140,
    144.9650,
    '9b17d3fd-4e2b-4c9a-b0db-9e3b50e3f002'
);

INSERT INTO amenities (id, name) VALUES
("f31a4e7a-1111-3223-8888-aaaaaaaaaaaa", "WIFI"),
("f31a4e7a-1111-4444-8888-avc982vbasdf", "Swimming pool"),
("f31a4e7a-1111-4444-3488-avc982vbasdf", "Air conditioner");

INSERT INTO place_amenity (place_id, amenity_id) VALUES
("f31a4e7a-1111-4444-8888-aaaaaaaaaaaa", "f31a4e7a-1111-3223-8888-aaaaaaaaaaaa"),
("f31a4e7a-2222-4444-8888-bbbbbbbbbbbb", "f31a4e7a-1111-3223-8888-aaaaaaaaaaaa"),
("f31a4e7a-2222-4444-8888-bbbbbbbbbbbb", "f31a4e7a-1111-4444-8888-avc982vbasdf");

SELECT CONCAT(CHAR(10), 'user data ----------------------------', CHAR(10));
SELECT * FROM users;
SELECT CONCAT(CHAR(10), 'place data ----------------------------', CHAR(10));
SELECT * FROM places;
SELECT CONCAT(CHAR(10), 'amenities ----------------------------', CHAR(10));
SELECT * FROM amenities;
SELECT CONCAT(CHAR(10), 'place_amenities ----------------------------', CHAR(10));
SELECT * FROM place_amenity;

PRAGMA table_info(amenities)