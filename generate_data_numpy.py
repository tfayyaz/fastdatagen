import numpy as np
import pandas as pd
import time
import os
import argparse
from datetime import datetime, date

def generate_table_and_export(table_name, column_name, data_type, value, num_rows):
    start_time = time.time()
    
    if data_type == 'Integer':
        data = np.full(num_rows, value, dtype=np.int32)
    elif data_type == 'Float':
        data = np.full(num_rows, value, dtype=np.float32)
    elif data_type == 'String':
        data = np.full(num_rows, value, dtype=object)
    elif data_type in ['DateTime', 'DateTimeMs', 'DateTimeMsTimeZone', 'Date']:
        data = np.full(num_rows, np.datetime64(value))
    elif data_type == 'UnixTimestamp':
        data = np.full(num_rows, value, dtype=np.int64)
    
    df = pd.DataFrame({column_name: data})
    df.to_csv(f'{table_name}.csv', index=False)
    
    end_time = time.time()
    generation_time = end_time - start_time
    
    file_size = os.path.getsize(f'{table_name}.csv')
    
    return generation_time, file_size

def generate_combined_table(tables, num_rows):
    start_time = time.time()
    
    combined_data = {}
    for table_name, column_name, data_type, value in tables:
        if data_type == 'Integer':
            combined_data[column_name] = np.full(num_rows, value, dtype=np.int32)
        elif data_type == 'Float':
            combined_data[column_name] = np.full(num_rows, value, dtype=np.float32)
        elif data_type == 'String':
            combined_data[column_name] = np.full(num_rows, value, dtype=object)
        elif data_type in ['DateTime', 'DateTimeMs', 'DateTimeMsTimeZone', 'Date']:
            combined_data[column_name] = np.full(num_rows, np.datetime64(value))
        elif data_type == 'UnixTimestamp':
            combined_data[column_name] = np.full(num_rows, value, dtype=np.int64)
    
    df = pd.DataFrame(combined_data)
    df.to_csv('combined_table.csv', index=False)
    
    end_time = time.time()
    generation_time = end_time - start_time
    
    file_size = os.path.getsize('combined_table.csv')
    
    return generation_time, file_size

def generate_tables_and_export(num_rows):
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
    
    # Export stats to CSV
    stats_df.to_csv('stats.csv', index=False)
    
    print(f"Total data generation and export completed in {total_generation_time:.2f} seconds")
    print("\nStats:")
    print(stats_df.to_string(index=False, float_format=lambda x: f"{x:.6f}"))
    
    print("\nList of all tables:")
    for table in tables:
        print(f"- {table[0]}: {table[1]} ({table[2]})")
    print(f"- combined_table: All Columns (Mixed)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tables with specified number of rows using NumPy")
    parser.add_argument("num_rows", type=int, help="Number of rows to generate in each table")
    args = parser.parse_args()
    
    generate_tables_and_export(args.num_rows)