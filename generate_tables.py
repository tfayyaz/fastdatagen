import duckdb
import time
import os
import pandas as pd
from datetime import datetime, date
import argparse

def generate_table_and_export(table_name, column_name, data_type, value, num_rows):
    start_time = time.time()
    
    if data_type == 'Integer':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT {value}::INTEGER AS {column_name} FROM range({num_rows})")
    elif data_type == 'Float':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT {value}::FLOAT AS {column_name} FROM range({num_rows})")
    elif data_type == 'String':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT '{value}' AS {column_name} FROM range({num_rows})")
    elif data_type == 'DateTime':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT '{value}'::TIMESTAMP AS {column_name} FROM range({num_rows})")
    elif data_type == 'DateTimeMs':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT '{value}'::TIMESTAMP(3) AS {column_name} FROM range({num_rows})")
    elif data_type == 'DateTimeMsTimeZone':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT '{value}'::TIMESTAMP WITH TIME ZONE AS {column_name} FROM range({num_rows})")
    elif data_type == 'Date':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT '{value}'::DATE AS {column_name} FROM range({num_rows})")
    elif data_type == 'UnixTimestamp':
        conn.execute(f"CREATE TABLE {table_name} AS SELECT {value}::BIGINT AS {column_name} FROM range({num_rows})")
    
    conn.execute(f"COPY {table_name} TO '{table_name}.csv' (HEADER, DELIMITER ',')")
    
    end_time = time.time()
    generation_time = end_time - start_time
    
    file_size = os.path.getsize(f'{table_name}.csv')
    
    return generation_time, file_size

def generate_combined_table(tables, num_rows):
    start_time = time.time()
    
    # Create the combined table
    columns = []
    for table_name, column_name, data_type, value in tables:
        if data_type == 'Integer':
            columns.append(f"{value}::INTEGER AS {column_name}")
        elif data_type == 'Float':
            columns.append(f"{value}::FLOAT AS {column_name}")
        elif data_type == 'String':
            columns.append(f"'{value}' AS {column_name}")
        elif data_type == 'DateTime':
            columns.append(f"'{value}'::TIMESTAMP AS {column_name}")
        elif data_type == 'DateTimeMs':
            columns.append(f"'{value}'::TIMESTAMP(3) AS {column_name}")
        elif data_type == 'DateTimeMsTimeZone':
            columns.append(f"'{value}'::TIMESTAMP WITH TIME ZONE AS {column_name}")
        elif data_type == 'Date':
            columns.append(f"'{value}'::DATE AS {column_name}")
        elif data_type == 'UnixTimestamp':
            columns.append(f"{value}::BIGINT AS {column_name}")
    
    columns_str = ", ".join(columns)
    conn.execute(f"CREATE TABLE combined_table AS SELECT {columns_str} FROM range({num_rows})")
    
    conn.execute("COPY combined_table TO 'combined_table.csv' (HEADER, DELIMITER ',')")
    
    end_time = time.time()
    generation_time = end_time - start_time
    
    file_size = os.path.getsize('combined_table.csv')
    
    return generation_time, file_size

def generate_tables_and_export(num_rows):
    global conn
    conn = duckdb.connect(database=':memory:', read_only=False)
    
    total_start_time = time.time()
    
    # Generate tables
    tables = [
        ('intOne', 'value', 'Integer', 1),
        ('floatOne', 'value', 'Float', 1.0),
        ('intMillion', 'value', 'Integer', 1000000),
        ('countryCode', 'countryCode', 'String', 'uk'),
        ('countryName', 'countryName', 'String', 'United Kingdom'),
        ('dateTimeCol', 'dateTime', 'DateTime', '2023-07-28 12:34:56'),
        ('dateTimeMsCol', 'dateTimeMs', 'DateTimeMs', '2023-07-28 12:34:56.789'),
        ('dateTimeMsTimeZoneCol', 'dateTimeMsTimeZone', 'DateTimeMsTimeZone', '2023-07-28 12:34:56.789+00:00'),
        ('dateCol', 'date', 'Date', '2023-07-28'),
        ('unixTimestampCol', 'unixTimestamp', 'UnixTimestamp', int(datetime(2023, 7, 28, 12, 34, 56).timestamp()))
    ]
    
    stats = []
    for table_name, column_name, data_type, value in tables:
        generation_time, file_size = generate_table_and_export(table_name, column_name, data_type, value, num_rows)
        stats.append({
            'Table': table_name,
            'Column': column_name,
            'Rows': num_rows,
            'DataType': data_type,
            'Value': str(value),
            'FileSizeBytes': file_size,
            'FileSizeMB': file_size / (1024 * 1024),
            'GenerationTime': generation_time
        })
    
    # Generate combined table
    combined_generation_time, combined_file_size = generate_combined_table(tables, num_rows)
    stats.append({
        'Table': 'combined_table',
        'Column': 'All Columns',
        'Rows': num_rows,
        'DataType': 'Mixed',
        'Value': 'Multiple',
        'FileSizeBytes': combined_file_size,
        'FileSizeMB': combined_file_size / (1024 * 1024),
        'GenerationTime': combined_generation_time
    })
    
    total_end_time = time.time()
    total_generation_time = total_end_time - total_start_time
    
    # Create stats DataFrame
    stats_df = pd.DataFrame(stats)
    
    # Create stats table in DuckDB from the DataFrame
    conn.execute("CREATE TABLE stats AS SELECT * FROM stats_df")
    conn.execute("COPY stats TO 'stats.csv' (HEADER, DELIMITER ',')")
    
    print(f"Total data generation and export completed in {total_generation_time:.2f} seconds")
    print("\nStats:")
    print(stats_df.to_string(index=False, float_format=lambda x: f"{x:.6f}"))
    
    print("\nList of all tables:")
    for table in tables:
        print(f"- {table[0]}: {table[1]} ({table[2]})")
    print(f"- combined_table: All Columns (Mixed)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tables with specified number of rows")
    parser.add_argument("num_rows", type=int, help="Number of rows to generate in each table")
    args = parser.parse_args()
    
    generate_tables_and_export(args.num_rows)