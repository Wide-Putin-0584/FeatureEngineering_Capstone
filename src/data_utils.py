import pandas as pd

def construct_hotel_features(df):
    """
    Helper function to engineer custom features for the Hotel Booking dataset.
    This prevents clutter in the main Jupyter Notebook.
    """
    df_fe = df.copy()
    
    # Calculate Ratios
    df_fe['price_per_person'] = df_fe['adr'] / (df_fe['adults'] + df_fe['children'] + 1)
    
    # Calculate Interactions
    df_fe['total_guests'] = df_fe['adults'] + df_fe['children'] + df_fe['babies']
    df_fe['adr_lead_time_interaction'] = df_fe['adr'] * df_fe['lead_time']
    
    return df_fe
