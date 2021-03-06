DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tracker;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE tracker (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  symbol TEXT NOT NULL,
  price FLOAT NOT NULL,
  cap FLOAT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
