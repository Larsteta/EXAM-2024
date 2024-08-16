# 3. Data Analysis with Pandas (20%)

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('https://raw.githubusercontent.com/NikoStein/pds_data/main/sales.csv')

# Task 3.1: Total Sales per Store for the a given year 
def total_sales_per_store(data,year): 
    # Extract year from Date
    data['Year'] = pd.to_datetime(data['Date']).dt.year 

    # Filter data for year
    dataYear = data[data['Year'] == year] 

    # Group by Store and sum Sales
    totalSalesYear = dataYear.groupby('Store')['Sales'].sum() 

    return totalSalesYear

print("Task 1 results:")
print("-"*100)
print(total_sales_per_store(data, 2014).sample(5))
print("-"*100)

# Task 3.2: Store with the most consistent sales
def store_with_most_consistent_sales(data):
    # Calculate standard deviation of sales for each store
    SalesStdDev = data.groupby('Store')['Sales'].std() 

    # Get the store with the lowest standard deviation, from the index
    store = SalesStdDev.idxmin() 

    # Get the minimum standard deviation value 
    SalesStdDev = SalesStdDev.min()   
    
    # Print the results
    print(f"Store with the most consistent sales: {store}")
    print(f"Lowest standard deviation: {SalesStdDev}")
    
    return store, SalesStdDev 

print("Task 2 results:")
print("-"*100)
store_with_most_consistent_sales(data)
print("-"*100)

# Task 3.3: Monthly Sales Trend
def monthly_sales_trend(data):
    # Extract month from Date
    data['Month'] = pd.to_datetime(data['Date']).dt.to_period('M') 

    # Group by Store and Month and sum Sales
    monthly_sales_trend = data.groupby(['Store', 'Month'])['Sales'].sum().reset_index() 

    # Rename 'Sales' column to 'TotalSales'
    monthly_sales_trend.rename(columns={'Sales': 'TotalSales'}, inplace=True)   

    return monthly_sales_trend

print("Task 3 results:")
print("-"*100)
print(monthly_sales_trend(data).sample(5))
print("-"*100)

# Task 3.4: Sales Distribution by Day of the Week
def salesDistribution_by_day_of_the_week(data):
    # Extract day of the week from Date
    data['DayOfWeek'] = pd.to_datetime(data['Date']).dt.day_name() 

    # Group by DayOfWeek and calculate mean Sales
    salesDistribution = data.groupby('DayOfWeek')['Sales'].mean() 

    # Reorder days of the week
    salesDistribution = salesDistribution.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']) 

    # Plot bar chart
    salesDistribution.plot(kind='bar')
    plt.ylabel('Average Sales') # Set y-axis label
    plt.tight_layout()  # Adjust layout to fit everything
    plt.title('Sales Distribution by Day of the Week') # Set title
    plt.savefig('Sales Distribution by Day of the Week.png') # Save plot

    return salesDistribution

print("Task 4 results:")
print("-"*100)
print(salesDistribution_by_day_of_the_week(data))
print("-"*100)

# Task 3.5: Top 5 Stores
def top_5_stores(data):
    # Group by Store and sum Sales
    totalSales = data.groupby('Store')['Sales'].sum() 

    # Get the top 5 stores
    top5Stores = totalSales.nlargest(5) 

    return top5Stores.index  # Return the store names or IDs

def plot_sales_trend(data, top_stores):
    # Filter the data for the top stores
    topStores = data[data['Store'].isin(top_stores)]

    # Group by Store and Month and sum Sales
    monthlyData = topStores.groupby(['Store', 'Month'])['Sales'].sum().reset_index() 
    
    # Plotting
    plt.figure(figsize=(12, 6))
    
    for store in top_stores:
        store_data = monthlyData[monthlyData['Store'] == store]
        plt.plot(store_data['Month'].astype(str), store_data['Sales'], label=store)
    
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales Trend for Top Stores')
    plt.legend(title='Store')
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to fit everything
    plt.savefig('Monthly_Sales_Trend_for_Top_Stores.png')  # Save plot

print("Task 5 results:")
print("-"*100)
print(f'The top 5 stores are:\n {top_5_stores(data)}')
print("-"*100)

# Plot the sales trend for the top 5 stores
plot_sales_trend(data, top_5_stores(data))











    




