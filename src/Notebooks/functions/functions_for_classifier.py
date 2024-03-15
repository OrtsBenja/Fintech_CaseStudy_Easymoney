def pk_partition_month_extraction(df):
    
    # df['pk_partition_month'] = df['pk_partition'].dt.month_name()
    df.drop('pk_partition', axis='columns', inplace=True)
    
    return df

def convert_entry_date_to_numeric(df):
    
    df['entry_date'] = df['entry_date'].apply(lambda x: x.timestamp()).astype('int')
    
    return df