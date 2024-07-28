# Create Python Virtual Env and activate venv

```sh
python3 -m venv duckdb_env
source duckdb_env/bin/activate  
```

# Install DuckDB in virtual env

```sh
pip install duckdb
pip install pandas
pip install numpy
```

# Gen data with DuckDB and NumPy and save to csv files
Both scripts (DuckDB and NumPy versions) generate the following tables, each with a configurable number of rows:

- "intOne": Integer column with value 1
- "floatOne": Float column with value 1.0
- "intMillion": Integer column with value 1,000,000
- "countryCode": String column with value 'uk'
- "countryName": String column with value 'United Kingdom'
- "dateTimeCol": DateTime column with value '2023-07-28 12:34:56'
- "dateTimeMsCol": DateTime column with millisecond precision, value '2023-07-28 12:34:56.789'
- "dateTimeMsTimeZoneCol": DateTime column with millisecond precision and timezone, value '2023-07-28 12:34:56.789+00:00'
- "dateCol": Date column with value '2023-07-28'
- "unixTimestampCol": Integer column with Unix timestamp value corresponding to '2023-07-28 12:34:56'
- "combined_table": A single table containing all columns from the above tables

For each table, the scripts:

- Generate the data
- Write the table to a CSV file
- Time how long the data generation and export takes
- Check the file sizes

The scripts also create a stats table showing:

- Table name
- Column name
- Number of rows
- Data type
- Sample value
- File size (in bytes and MB)
- Generation time

The stats are displayed in the console and saved to a 'stats.csv' file.

# Usage:

```sh
python generate_tables.py <number_of_rows>  # For DuckDB version
python generate_data_numpy.py <number_of_rows>  # For NumPy version

```

# Example:

```sh
python generate_tables.py 500000
python generate_data_numpy.py 500000
```

# Output

## 100k rows

```sh
$ python generate_tables.py 100000      
Total data generation and export completed in 0.12 seconds

Stats:
                Table             Column   Rows           DataType                         Value  FileSizeBytes  FileSizeMB  GenerationTime
               intOne              value 100000            Integer                             1         200006    0.190741        0.003844
             floatOne              value 100000              Float                           1.0         400006    0.381475        0.006284
           intMillion              value 100000            Integer                       1000000         800006    0.762945        0.004099
          countryCode        countryCode 100000             String                            uk         300012    0.286114        0.004439
          countryName        countryName 100000             String                United Kingdom        1500012    1.430523        0.005342
          dateTimeCol           dateTime 100000           DateTime           2023-07-28 12:34:56        2000009    1.907357        0.004857
        dateTimeMsCol         dateTimeMs 100000         DateTimeMs       2023-07-28 12:34:56.789        2400011    2.288829        0.006003
dateTimeMsTimeZoneCol dateTimeMsTimeZone 100000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00        2700019    2.574939        0.020293
              dateCol               date 100000               Date                    2023-07-28        1100005    1.049047        0.004160
     unixTimestampCol      unixTimestamp 100000      UnixTimestamp                    1690544096        1100014    1.049055        0.008573
       combined_table        All Columns 100000              Mixed                      Multiple       12500104   11.921028        0.053406
```

## 1 million rows

```sh
$ python generate_tables.py 1000000

Total data generation and export completed in 0.35 seconds

Stats:
                Table             Column    Rows           DataType                         Value  FileSizeBytes  FileSizeMB  GenerationTime
               intOne              value 1000000            Integer                             1        2000006    1.907354        0.008971
             floatOne              value 1000000              Float                           1.0        4000006    3.814703        0.018253
           intMillion              value 1000000            Integer                       1000000        8000006    7.629400        0.009616
          countryCode        countryCode 1000000             String                            uk        3000012    2.861034        0.019921
          countryName        countryName 1000000             String                United Kingdom       15000012   14.305126        0.028582
          dateTimeCol           dateTime 1000000           DateTime           2023-07-28 12:34:56       20000009   19.073495        0.015768
        dateTimeMsCol         dateTimeMs 1000000         DateTimeMs       2023-07-28 12:34:56.789       24000011   22.888194        0.017156
dateTimeMsTimeZoneCol dateTimeMsTimeZone 1000000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00       27000019   25.749225        0.034463
              dateCol               date 1000000               Date                    2023-07-28       11000005   10.490422        0.010700
     unixTimestampCol      unixTimestamp 1000000      UnixTimestamp                    1690544096       11000014   10.490431        0.011143
       combined_table        All Columns 1000000              Mixed                      Multiple      125000104  119.209389        0.170610
```

## 10 million rows

```sh
$ python generate_tables.py 10000000

Total data generation and export completed in 3.40 seconds

Stats:
                Table             Column     Rows           DataType                         Value  FileSizeBytes  FileSizeMB  GenerationTime
               intOne              value 10000000            Integer                             1       20000006   19.073492        0.063212
             floatOne              value 10000000              Float                           1.0       40000006   38.146978        0.144395
           intMillion              value 10000000            Integer                       1000000       80000006   76.293951        0.073748
          countryCode        countryCode 10000000             String                            uk       30000012   28.610241        0.185814
          countryName        countryName 10000000             String                United Kingdom      150000012  143.051159        0.318481
          dateTimeCol           dateTime 10000000           DateTime           2023-07-28 12:34:56      200000009  190.734872        0.117632
        dateTimeMsCol         dateTimeMs 10000000         DateTimeMs       2023-07-28 12:34:56.789      240000011  228.881846        0.128901
dateTimeMsTimeZoneCol dateTimeMsTimeZone 10000000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00      270000019  257.492084        0.373003
              dateCol               date 10000000               Date                    2023-07-28      110000005  104.904180        0.093339
     unixTimestampCol      unixTimestamp 10000000      UnixTimestamp                    1690544096      110000014  104.904188        0.105874
       combined_table        All Columns 10000000              Mixed                      Multiple     1250000104 1192.092995        1.792626

```

## 100 million rows

```sh
$ python generate_tables.py 100000000

Total data generation and export completed in 30.41 seconds

Stats:
                Table             Column      Rows           DataType                         Value  FileSizeBytes   FileSizeMB  GenerationTime
               intOne              value 100000000            Integer                             1      200000006   190.734869        0.595624
             floatOne              value 100000000              Float                           1.0      400000006   381.469732        1.430190
           intMillion              value 100000000            Integer                       1000000      800000006   762.939459        0.845525
          countryCode        countryCode 100000000             String                            uk      300000012   286.102306        2.133107
          countryName        countryName 100000000             String                United Kingdom     1500000012  1430.511486        2.675204
          dateTimeCol           dateTime 100000000           DateTime           2023-07-28 12:34:56     2000000009  1907.348641        1.065535
        dateTimeMsCol         dateTimeMs 100000000         DateTimeMs       2023-07-28 12:34:56.789     2400000011  2288.818370        1.299066
dateTimeMsTimeZoneCol dateTimeMsTimeZone 100000000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00     2700000019  2574.920672        2.956486
              dateCol               date 100000000               Date                    2023-07-28     1100000005  1049.041753        0.836481
     unixTimestampCol      unixTimestamp 100000000      UnixTimestamp                    1690544096     1100000014  1049.041761        0.917833
       combined_table        All Columns 100000000              Mixed                      Multiple    12500000104 11920.929054       15.651480
```

## 1 billion rows

```sh
$ python generate_tables.py

Total data generation and export completed in 181.92 seconds

Stats:
      Table      Column       Rows DataType          Value  FileSizeBytes   FileSizeMB  GenerationTime
     intOne       value 1000000000  Integer              1     2000000006  1907.348639        6.330623
   floatOne       value 1000000000    Float       1.000000     4000000006  3814.697271       14.697648
 intMillion       value 1000000000  Integer        1000000     8000000006  7629.394537        7.722529
countryCode countryCode 1000000000   String             uk     3000000012  2861.022961       20.474182
countryName countryName 1000000000   String United Kingdom    15000000012 14305.114758      132.697090
```

# Run Numpy python file

## 1 million rows

```sh
$ python generate_data_numpy.py 1000000

/fastdatagen/generate_data_numpy.py:18: UserWarning: no explicit representation of timezones available for np.datetime64
  data = np.full(num_rows, np.datetime64(value))
/fastdatagen/generate_data_numpy.py:44: UserWarning: no explicit representation of timezones available for np.datetime64
  combined_data[column_name] = np.full(num_rows, np.datetime64(value))
Total data generation and export completed in 8.31 seconds

Stats:
                Table             Column    Rows           DataType                         Value  FileSizeBytes  FileSizeMB  GenerationTime
               intOne              value 1000000            Integer                             1        2000006    1.907354        0.150766
             floatOne              value 1000000              Float                           1.0        4000006    3.814703        0.249334
           intMillion              value 1000000            Integer                       1000000        8000006    7.629400        0.227135
          countryCode        countryCode 1000000             String                            uk        3000012    2.861034        0.161919
          countryName        countryName 1000000             String                United Kingdom       15000012   14.305126        0.335521
          dateTimeCol           dateTime 1000000           DateTime           2023-07-28 12:34:56       20000009   19.073495        0.812785
        dateTimeMsCol         dateTimeMs 1000000         DateTimeMs       2023-07-28 12:34:56.789       24000011   22.888194        0.938323
dateTimeMsTimeZoneCol dateTimeMsTimeZone 1000000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00       24000019   22.888202        0.946716
              dateCol               date 1000000               Date                    2023-07-28       11000005   10.490422        0.482924
     unixTimestampCol      unixTimestamp 1000000      UnixTimestamp                    1690544096       11000014   10.490431        0.245890
       combined_table        All Columns 1000000              Mixed                      Multiple      116000088  110.626305        3.723951
```

## 10 million rows

```sh
$ python generate_data_numpy.py 10000000

/fastdatagen/generate_data_numpy.py:18: UserWarning: no explicit representation of timezones available for np.datetime64
  data = np.full(num_rows, np.datetime64(value))
/fastdatagen/generate_data_numpy.py:44: UserWarning: no explicit representation of timezones available for np.datetime64
  combined_data[column_name] = np.full(num_rows, np.datetime64(value))
Total data generation and export completed in 85.69 seconds

Stats:
                Table             Column     Rows           DataType                         Value  FileSizeBytes  FileSizeMB  GenerationTime
               intOne              value 10000000            Integer                             1       20000006   19.073492        1.415855
             floatOne              value 10000000              Float                           1.0       40000006   38.146978        2.528698
           intMillion              value 10000000            Integer                       1000000       80000006   76.293951        2.136244
          countryCode        countryCode 10000000             String                            uk       30000012   28.610241        1.755775
          countryName        countryName 10000000             String                United Kingdom      150000012  143.051159        3.302832
          dateTimeCol           dateTime 10000000           DateTime           2023-07-28 12:34:56      200000009  190.734872        8.900745
        dateTimeMsCol         dateTimeMs 10000000         DateTimeMs       2023-07-28 12:34:56.789      240000011  228.881846        9.577135
dateTimeMsTimeZoneCol dateTimeMsTimeZone 10000000 DateTimeMsTimeZone 2023-07-28 12:34:56.789+00:00      240000019  228.881854        9.906716
              dateCol               date 10000000               Date                    2023-07-28      110000005  104.904180        5.114390
     unixTimestampCol      unixTimestamp 10000000      UnixTimestamp                    1690544096      110000014  104.904188        2.583011
       combined_table        All Columns 10000000              Mixed                      Multiple     1160000088 1106.262291       38.159972


```