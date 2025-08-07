import pandas as pd
import ipaddress

def extract_time_features(df, purchase_col, signup_col=None):
    df['hour_of_day'] = df[purchase_col].dt.hour
    df['day_of_week'] = df[purchase_col].dt.day_name()
    if signup_col:
        df['time_since_signup'] = (df[purchase_col] - df[signup_col]).dt.total_seconds() / 3600  # in hours
    return df

import ipaddress

def convert_ip_to_int(df, ip_col='ip_address'):
    # Remove decimal point if float, convert to integer
    df['ip_int'] = df[ip_col].astype('int64')
    return df

def merge_ip_country(df, ip_map_df):
    df = df.copy()
    ip_map_df = ip_map_df.copy()

    # Sort the ip map for efficient range searching
    ip_map_df.sort_values('lower_bound_ip_address', inplace=True)

    # Define a function to find country for a single IP
    def find_country(ip):
        match = ip_map_df[
            (ip_map_df['lower_bound_ip_address'] <= ip) &
            (ip_map_df['upper_bound_ip_address'] >= ip)
        ]
        return match['country'].values[0] if not match.empty else 'Unknown'

    df['country'] = df['ip_int'].apply(find_country)
    return df

