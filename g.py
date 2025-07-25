import pandas as pd
import numpy as np
from datetime import datetime

# First, let's load your data and examine the columns
# Replace 'your_data_file.csv' with your actual file path
df = pd.read_csv('uber.csv')

# If you already have loaded data in a different variable name, use that instead
# For example, if your data is in a variable called 'data', uncomment the next line:
# df = data

# Let's examine what columns you have
print("=== EXAMINING YOUR DATA ===")
print("Available columns:")
try:
    print(df.columns.tolist())
    print(f"\nDataFrame shape: {df.shape}")
    print(f"\nFirst few rows:")
    print(df.head())
    
    # Look for timestamp-like columns
    timestamp_cols = []
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['time', 'date', 'pickup', 'dropoff']):
            timestamp_cols.append(col)
    
    print(f"\nPotential timestamp columns found: {timestamp_cols}")
    
    if not timestamp_cols:
        print("\nNo obvious timestamp columns found. Please check your column names.")
        print("Common timestamp column names include: pickup_datetime, dropoff_datetime, timestamp, date, time")
        
except NameError:
    print("ERROR: No DataFrame found!")
    print("Please make sure you have loaded your data into a DataFrame.")
    print("Example ways to load data:")
    print("  df = pd.read_csv('your_file.csv')")
    print("  df = pd.read_excel('your_file.xlsx')")
    print("  df = pd.read_json('your_file.json')")
    print("\nOr if your data is in a different variable, assign it to df:")
    print("  df = your_variable_name")
    print("\n=== CREATING SAMPLE DATA FOR TESTING ===")
    # Create sample data for testing
    np.random.seed(42)
    n_samples = 1000
    
    # Create sample timestamps
    start_date = pd.to_datetime('2024-01-01')
    end_date = pd.to_datetime('2024-12-31')
    random_dates = pd.to_datetime(np.random.randint(start_date.value, end_date.value, n_samples))
    
    df = pd.DataFrame({
        'pickup_datetime': random_dates,
        'fare_amount': np.random.uniform(5, 50, n_samples),
        'passenger_count': np.random.randint(1, 6, n_samples),
        'pickup_longitude': np.random.uniform(-74.1, -73.9, n_samples),
        'pickup_latitude': np.random.uniform(40.6, 40.9, n_samples),
        'dropoff_longitude': np.random.uniform(-74.1, -73.9, n_samples),
        'dropoff_latitude': np.random.uniform(40.6, 40.9, n_samples)
    })
    
    print("Sample data created for demonstration!")
    print(f"Shape: {df.shape}")
    print(df.head())

def create_temporal_features(df, timestamp_col='pickup_datetime'):
    """
    Create analytical features from timestamp columns
    
    Parameters:
    df: pandas DataFrame
    timestamp_col: string, name of the timestamp column
    
    Returns:
    df: DataFrame with new temporal features
    """
    
    # Convert to datetime if not already
    df[timestamp_col] = pd.to_datetime(df[timestamp_col])
    
    # Extract basic time components
    df[f'{timestamp_col}_hour'] = df[timestamp_col].dt.hour
    df[f'{timestamp_col}_day'] = df[timestamp_col].dt.day
    df[f'{timestamp_col}_month'] = df[timestamp_col].dt.month
    df[f'{timestamp_col}_year'] = df[timestamp_col].dt.year
    
    # Day of week (0=Monday, 6=Sunday)
    df[f'{timestamp_col}_dayofweek'] = df[timestamp_col].dt.dayofweek
    
    # Day of week name
    df[f'{timestamp_col}_dayname'] = df[timestamp_col].dt.day_name()
    
    # Weekend indicator
    df[f'{timestamp_col}_is_weekend'] = (df[f'{timestamp_col}_dayofweek'] >= 5).astype(int)
    
    # Peak/off-peak time indicators
    def categorize_time_period(hour):
        """Categorize hours into time periods"""
        if 6 <= hour <= 9:
            return 'morning_peak'
        elif 17 <= hour <= 19:
            return 'evening_peak'
        elif 10 <= hour <= 16:
            return 'midday'
        elif 20 <= hour <= 23:
            return 'evening'
        else:
            return 'night_early_morning'
    
    df[f'{timestamp_col}_time_period'] = df[f'{timestamp_col}_hour'].apply(categorize_time_period)
    
    # Peak hours binary indicator
    df[f'{timestamp_col}_is_peak'] = df[f'{timestamp_col}_time_period'].isin(['morning_peak', 'evening_peak']).astype(int)
    
    # Rush hour indicator (more specific)
    df[f'{timestamp_col}_is_rush_hour'] = (
        ((df[f'{timestamp_col}_hour'] >= 7) & (df[f'{timestamp_col}_hour'] <= 9)) |
        ((df[f'{timestamp_col}_hour'] >= 17) & (df[f'{timestamp_col}_hour'] <= 19))
    ).astype(int)
    
    # Business hours indicator
    df[f'{timestamp_col}_is_business_hours'] = (
        (df[f'{timestamp_col}_hour'] >= 9) & 
        (df[f'{timestamp_col}_hour'] <= 17) & 
        (df[f'{timestamp_col}_dayofweek'] < 5)
    ).astype(int)
    
    return df

# Example usage with your data:
# If you have pickup_datetime and dropoff_datetime columns:

# Create features for pickup time
df = create_temporal_features(df, 'pickup_datetime')

# Create features for dropoff time (if you have this column)
# df = create_temporal_features(df, 'dropoff_datetime')

# Display the new features
print("=== NEW TEMPORAL FEATURES ===")
print("\nSample of new columns:")
temporal_cols = [col for col in df.columns if any(time_keyword in col.lower() 
                for time_keyword in ['hour', 'day', 'month', 'weekend', 'peak', 'rush', 'business'])]
print(df[temporal_cols].head())

print(f"\nTotal new temporal features created: {len(temporal_cols)}")

# Summary statistics for key features
print("\n=== FEATURE SUMMARIES ===")
if 'pickup_datetime_hour' in df.columns:
    print(f"\nHour distribution:")
    print(df['pickup_datetime_hour'].value_counts().sort_index())
    
    print(f"\nDay of week distribution:")
    print(df['pickup_datetime_dayname'].value_counts())
    
    print(f"\nTime period distribution:")
    print(df['pickup_datetime_time_period'].value_counts())
    
    print(f"\nPeak vs Off-peak:")
    print(f"Peak hours: {df['pickup_datetime_is_peak'].sum()} ({df['pickup_datetime_is_peak'].mean()*100:.1f}%)")
    print(f"Off-peak hours: {(1-df['pickup_datetime_is_peak']).sum()} ({(1-df['pickup_datetime_is_peak']).mean()*100:.1f}%)")
    
    print(f"\nWeekend vs Weekday:")
    print(f"Weekend rides: {df['pickup_datetime_is_weekend'].sum()} ({df['pickup_datetime_is_weekend'].mean()*100:.1f}%)")
    print(f"Weekday rides: {(1-df['pickup_datetime_is_weekend']).sum()} ({(1-df['pickup_datetime_is_weekend']).mean()*100:.1f}%)")

# Additional advanced features you might want to create:

def create_advanced_temporal_features(df, timestamp_col='pickup_datetime'):
    """Create more advanced temporal features"""
    
    # Quarter of the year
    df[f'{timestamp_col}_quarter'] = df[timestamp_col].dt.quarter
    
    # Week of year
    df[f'{timestamp_col}_week_of_year'] = df[timestamp_col].dt.isocalendar().week
    
    # Season
    def get_season(month):
        if month in [12, 1, 2]:
            return 'winter'
        elif month in [3, 4, 5]:
            return 'spring'
        elif month in [6, 7, 8]:
            return 'summer'
        else:
            return 'fall'
    
    df[f'{timestamp_col}_season'] = df[f'{timestamp_col}_month'].apply(get_season)
    
    # Time since midnight (in minutes)
    df[f'{timestamp_col}_minutes_since_midnight'] = df[f'{timestamp_col}_hour'] * 60 + df[timestamp_col].dt.minute
    
    # Holiday indicator (you'll need to define holidays for your region)
    # Example for US federal holidays (you can customize this)
    import holidays
    us_holidays = holidays.US()
    df[f'{timestamp_col}_is_holiday'] = df[timestamp_col].dt.date.apply(lambda x: x in us_holidays).astype(int)
    
    return df

# Apply advanced features
print("\n=== CREATING ADVANCED FEATURES ===")
try:
    df = create_advanced_temporal_features(df, 'pickup_datetime')
    print("Advanced temporal features created successfully!")
except ImportError:
    print("Note: Install 'holidays' package for holiday detection: pip install holidays")
except Exception as e:
    print(f"Note: Some advanced features may not be available: {e}")

print("\n=== FINAL FEATURE LIST ===")
all_temporal_cols = [col for col in df.columns if any(keyword in col.lower() 
                    for keyword in ['hour', 'day', 'month', 'year', 'week', 'season', 'peak', 'rush', 'business', 'holiday'])]
print(f"Total temporal features: {len(all_temporal_cols)}")
for col in sorted(all_temporal_cols):
    print(f"  - {col}")




    print("save datasets with new features")

    