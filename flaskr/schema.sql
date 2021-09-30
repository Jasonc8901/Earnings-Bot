DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS EarningsDate;

CREATE TABLE Company (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  name TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE EarningsDate (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  company_id INTEGER PRIMARY KEY AUTOINCREMENT,
  quarter INTEGER PRIMARY KEY AUTOINCREMENT,
  earnings_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (company_id) REFERENCES Company (id)
);