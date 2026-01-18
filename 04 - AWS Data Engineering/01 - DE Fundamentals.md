### Data Warehouse
- designed for complex queries and analysis
- data is cleaned, transformed, and loaded (ETL process)
- typically uses a start of snowflake schema
- Optimized for read-heavy operations

### Data Lake
- Can store large volumes of raw data w/o predefined schema
- Data is loaded as-is, no need for pre-processing
- Supports batch, real-time, and stream processing
- Can be queries for data transformation or exploration purposes.

Comparison:
	- Data Warehouse: Schema-on-write (ETL) --> schema defined before writing data
	- Data Lake: Schema-on-read (ELT) --> schema defined at the time of reading data

### AWS Glue 
- automating the ETL pipeline process

