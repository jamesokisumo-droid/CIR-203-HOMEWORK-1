
import numpy as np
transactions = np.array([
    [120, 150, 100, 90,  200, 170],  
    [80,  110, 95,  130, 160, 140],  
    [200, 220, 210, 230, 250, 240],  
    [50,  60,  55,  70,  65,  75]    
])
print("Transaction volumes (branches × months):\n", transactions)
total_per_branch = np.sum(transactions, axis=1)
print("\nTotal transactions per branch:", total_per_branch)
highest_branch = np.argmax(total_per_branch) + 1
print("Branch with highest total transactions: Branch", highest_branch)
average_monthly = np.mean(transactions)
print("Average monthly transaction volume (all branches):", average_monthly)
reshaped = transactions.reshape(3, 8)
print("Reshaped array (3x8):\n", reshaped)
print("Implication: Reshaping changes structure but not data; branch/month meaning is lost.")