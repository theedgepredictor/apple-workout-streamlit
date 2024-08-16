import datetime
import json
import os
from typing import List

import pandas as pd
import pyarrow as pa
import re

from data_pipeline.consts import HK_CONSTANTS

def get_dataframe(path: str, columns: List = None):
    """
    Read a DataFrame from a parquet file.

    Args:
        path (str): Path to the parquet file.
        columns (List): List of columns to select (default is None).

    Returns:
        pd.DataFrame: Read DataFrame.
    """
    try:
        return pd.read_parquet(path, engine='pyarrow', dtype_backend='numpy_nullable', columns=columns)
    except Exception as e:
        print(e)
        return pd.DataFrame()

def put_dataframe(df: pd.DataFrame, path: str):
    """
    Write a DataFrame to a parquet file.

    Args:
        df (pd.DataFrame): DataFrame to write.
        path (str): Path to the parquet file.
        schema (dict): Schema dictionary.

    Returns:
        None
    """
    key, file_name = path.rsplit('/', 1)
    if file_name.split('.')[1] != 'parquet':
        raise Exception("Invalid Filetype for Storage (Supported: 'parquet')")
    os.makedirs(key, exist_ok=True)
    df.to_parquet(f"{key}/{file_name}",engine='pyarrow', schema=pa.Schema.from_pandas(df))

def put_json(obj, path: str):
    with open(path, 'w') as f:
        json.dump(obj, f, indent=4, default=str)
    f.close()

def _parse_float(value, default=None):
    if value is None:
        return default

    if value in HK_CONSTANTS:
        return HK_CONSTANTS[value]

    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def _parse_date(value):
    if value is None:
        return None
    if type(value) == datetime.datetime:
        return pd.Timestamp(value)
    return pd.Timestamp(value)


def _clean_string(s):
    if isinstance(s, str):
        return re.sub("[\W_]+", '', s).upper().replace('Â', '')
    else:
        return s


def _parse_source_id(source_name):
    source_id = _clean_string(source_name)
    return source_id


def _parse_device_string(device_string):
    # Split on commas
    components = device_string.split(',')

    # Initialize the dictionary to store key-value pairs
    device_info = {}

    # Initialize variables to hold the key and value
    current_key = None
    current_value = []

    # Process each component
    for component in components:
        # Split on colon to separate key and value
        if ':' in component:
            if current_key is not None:
                # Join the current value parts and store in the dictionary
                device_info[current_key.strip()] = '.'.join(current_value).strip()
            # Split into key and value parts
            key, value = component.split(':', 1)
            current_key = key.replace('&lt;', '').replace('>', '').replace('<', '')
            current_value = [value]
        else:
            # Append the current component to the value list
            current_value.append(component)

    # Store the last key-value pair
    if current_key is not None:
        device_info[current_key.strip()] = ':'.join(current_value).strip()

    return device_info