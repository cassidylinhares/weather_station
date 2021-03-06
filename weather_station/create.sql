CREATE TABLE WEATHER_MEASUREMENT(
   ID BIGINT NOT NULL AUTO_INCREMENT,
   REMOTE_ID BIGINT,
   AIR_TEMPERATURE DECIMAL(6,2) NOT NULL,
   PRESSURE DECIMAL(6,2) NOT NULL,
   HUMIDITY DECIMAL(6,2) NOT NULL,
   CREATED_ON TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( ID )
);
