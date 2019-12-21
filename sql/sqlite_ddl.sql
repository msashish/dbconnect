-- noinspection SqlNoDataSourceInspectionForFile

-- noinspection SqlDialectInspectionForFile

CREATE TABLE TEMP (
  n integer,
  t text
);

ATTACH DATABASE ":memory:" as APP_DB;

CREATE TABLE APP_DB.CUSTOMER (
  cust_id integer primary key,
  cust_name text,
  age integer,
  sex text,
  source_system_name text,
  cust_category  text,
  created_ts timestamp
);

CREATE TABLE APP_DB.LOCATION (
  location_id integer primary key,
  location_name text,
  country_code text,
  state_code text,
  city_code text,
  zip_code integer
);

CREATE TABLE APP_DB.CUST_LOCATION (
  cust_location_id integer primary key,
  cust_id integer,
  location_id integer,
  location_type text,
  created_ts timestamp
);
