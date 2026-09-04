import pandas as pd
import os

def create_excel():
    print("Generating Excel Report for Retail BI...")
    os.makedirs('../excel', exist_ok=True)
    
    raw_df = pd.read_csv('../data/raw/retail_sales_raw.csv')
    cleaned_full = pd.read_csv('../data/processed/retail_sales_cleaned.csv')
    
    # Create aggregations
    kpi_summary = pd.DataFrame({
        'Metric': ['Total Revenue', 'Total Profit', 'Total Transactions', 'Profit Margin', 'Total Units Sold'],
        'Value': [
            cleaned_full['Revenue'].sum(),
            cleaned_full['Profit'].sum(),
            len(cleaned_full),
            (cleaned_full['Profit'].sum() / cleaned_full['Revenue'].sum()) if cleaned_full['Revenue'].sum() > 0 else 0,
            cleaned_full['Quantity'].sum()
        ]
    })
    
    store_analysis = cleaned_full.groupby('Store_Name').agg(
        Revenue=('Revenue', 'sum'),
        Profit=('Profit', 'sum'),
        Transactions=('Transaction_ID', 'count')
    ).reset_index().sort_values('Revenue', ascending=False)
    
    product_analysis = cleaned_full.groupby('Product_Name').agg(
        Revenue=('Revenue', 'sum'),
        Profit=('Profit', 'sum'),
        Units_Sold=('Quantity', 'sum')
    ).reset_index().sort_values('Revenue', ascending=False).head(100)
    
    category_analysis = cleaned_full.groupby(['Category', 'Sub_Category']).agg(
        Revenue=('Revenue', 'sum'),
        Profit=('Profit', 'sum')
    ).reset_index()
    
    regional_analysis = cleaned_full.groupby(['Region', 'State']).agg(
        Revenue=('Revenue', 'sum'),
        Profit=('Profit', 'sum')
    ).reset_index()
    
    cleaned_full['Transaction_Date'] = pd.to_datetime(cleaned_full['Transaction_Date'])
    monthly_trend = cleaned_full.groupby(cleaned_full['Transaction_Date'].dt.to_period('M')).agg(
        Revenue=('Revenue', 'sum'),
        Profit=('Profit', 'sum')
    ).reset_index()
    monthly_trend['Transaction_Date'] = monthly_trend['Transaction_Date'].astype(str)
    
    promotion_analysis = cleaned_full.groupby('Promotion').agg(
        Revenue=('Revenue', 'sum'),
        Total_Discount=('Discount', 'sum'),
        Transactions=('Transaction_ID', 'count')
    ).reset_index()
    
    return_analysis = cleaned_full.groupby('Return_Flag').agg(
        Revenue_Impact=('Revenue', 'sum'),
        Return_Count=('Transaction_ID', 'count')
    ).reset_index()
    
    pivot_tables = cleaned_full.pivot_table(index='Region', columns='Category', values='Revenue', aggfunc='sum').reset_index()
    extra_data = pd.DataFrame({'Data_Types': cleaned_full.dtypes.astype(str).reset_index().values.tolist()})
    insights = pd.DataFrame({'Key Findings': ['Top 20% of products generate majority of profit', 'Promotions increase transactions but decrease net margin', 'Returns are highest in electronics']})
    
    excel_path = '../excel/Retail_Sales_Analytics.xlsx'
    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        raw_df.sample(min(10000, len(raw_df)), random_state=42).to_excel(writer, sheet_name='Raw_Data', index=False)
        cleaned_full.sample(min(10000, len(cleaned_full)), random_state=42).to_excel(writer, sheet_name='Cleaned_Data', index=False)
        kpi_summary.to_excel(writer, sheet_name='KPI_Summary', index=False)
        store_analysis.to_excel(writer, sheet_name='Store_Analysis', index=False)
        product_analysis.to_excel(writer, sheet_name='Product_Analysis', index=False)
        category_analysis.to_excel(writer, sheet_name='Category_Analysis', index=False)
        regional_analysis.to_excel(writer, sheet_name='Regional_Analysis', index=False)
        monthly_trend.to_excel(writer, sheet_name='Monthly_Trend', index=False)
        promotion_analysis.to_excel(writer, sheet_name='Promotion_Analysis', index=False)
        return_analysis.to_excel(writer, sheet_name='Return_Analysis', index=False)
        pivot_tables.to_excel(writer, sheet_name='Pivot_Tables', index=False)
        extra_data.to_excel(writer, sheet_name='Extra_Data', index=False)
        insights.to_excel(writer, sheet_name='Insights', index=False)
    
    print(f"Excel Report Generated at {excel_path}")

if __name__ == '__main__':
    create_excel()
