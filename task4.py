# Flow-løbenummer: 8
#4. SupplyChainSimulation(30%)


import numpy as np
import matplotlib.pyplot as plt

#Task 5.1:Optimal Production Calculation:

# Constants
costPerUnit = 4
sellingPrice = 15
penaltyPerUnit = 10
meanDemand = 800
maxProduction = 1200


def calculate_profit(production, demand):
    # Calculate profit
    revenue = min(demand, production) * sellingPrice
    productionCost = production * costPerUnit
    salesPenalty = max(demand - production, 0) * penaltyPerUnit
    profit = revenue - productionCost - salesPenalty

    return profit

def simulate_demand(n, λ=800):
    # Simulate n days of demand with an average daily demand of λ
    return np.random.poisson(λ, n) 

def simulate_production(production):
    totalProfit = 0
    n = 1000 # Number of simulations

    # Simulate n days of demand and calculate profit
    for i in range(n):
        demand = simulate_demand(1,800) # Simulate daily demand, average demand is 800
        totalProfit += calculate_profit(production, demand) 
    averageProfit = totalProfit / n
    return averageProfit

def optimal_production():
    
    productionRange = range(1, maxProduction + 1) 
    profits = []

    # Simulate profit for each production quantity
    for p in productionRange:
        averageProfit = simulate_production(p)
        profits.append(averageProfit)

    # Find the index of the maximum profit
    maxProfit = max(profits)   

    # Find the optimal production quantity
    optimalProduction = productionRange[profits.index(maxProfit)]

    return optimalProduction, profits

def plot_profits(productionRange, profits, name):
    # Plot profits
    plt.figure(figsize=(10, 6))
    plt.plot(productionRange, profits, marker='o')
    plt.xlabel('Production Quantity')
    plt.ylabel('Average Profit')
    plt.title('Average Profit vs. Production Quantity')
    plt.grid(True)
    plt.savefig(f'{name}.png')
   


optimalProduction, profits = optimal_production()
print("Task 1 results:")
print("-"*100)
print(f"The optimal production quantity is {optimalProduction} units.")
print("-"*100)

# Plotting results
plot_profits(range(1, maxProduction + 1), profits, 'Task5.1')


#Task 5.2: Increased Production Cost
costPerUnit = 5
optimalProduction, profits = optimal_production() # Calculate optimal production quantity with increased production cost
print("Task 2 results:")
print("-"*100)
print(f"The optimal production quantity with increased production cost to {costPerUnit} is {optimalProduction} units.")
print("-"*100)

# Plotting results
plot_profits(range(1, maxProduction + 1), profits, 'Task5.2')


