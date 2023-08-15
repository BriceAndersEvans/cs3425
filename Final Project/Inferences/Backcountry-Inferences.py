import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Inferences on climbing shoes from Backcountry

# Read csv for climbing shoes
climbingshoe_df = pd.read_csv('../Modeling/BackcountryClimbing-Shoes.csv')

# Extract the Shoe_Brand, Shoe_Name and Shoe_Price columns from the DataFrame
shoebrands = climbingshoe_df['Shoe_Brand']
shoenames = climbingshoe_df['Shoe_Name']
shoeprices = climbingshoe_df['Shoe_Price']

# Create a violin plot using Matplotlib with colors for each brand
cmap = 'inferno'
plt.violinplot([shoeprices[shoebrands == brand] for brand in np.unique(shoebrands)],
               positions=np.arange(len(np.unique(shoebrands))) + 1,
               showmeans=True,
               showmedians=True,
               showextrema=True,
               widths=0.8)
plt.title('Cost Across Climbing Shoe Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Price')

# Adjust the x-axis labels to prevent overlap
plt.xticks(np.arange(len(np.unique(shoebrands))) + 1, np.unique(shoebrands), rotation=45, ha='right')
plt.show()
plt.savefig("Climbing Shoe Brand Plot.png")

# Inference on average cost of brand of climbing shoes from Backcountry

# Calculate lowest, highest, and average cost
lowest_cost_shoes = shoeprices.min()
highest_cost_shoes = shoeprices.max()
average_cost_shoes = shoeprices.mean()
brand_avg_shoeprice = climbingshoe_df.groupby('Shoe_Brand')['Shoe_Price'].mean()
lowest_cost_shoe = climbingshoe_df.iloc[climbingshoe_df['Shoe_Price'].idxmin()]['Shoe_Name']
lowest_cost_shoebrand = climbingshoe_df.iloc[climbingshoe_df['Shoe_Price'].idxmin()]['Shoe_Brand']
highest_cost_shoe = climbingshoe_df.iloc[climbingshoe_df['Shoe_Price'].idxmax()]['Shoe_Name']
highest_cost_shoebrand = climbingshoe_df.iloc[climbingshoe_df['Shoe_Price'].idxmax()]['Shoe_Brand']

print("Backcountry Climbing Shoes")
print(f"Lowest Cost: ${lowest_cost_shoes} ({lowest_cost_shoe} - {lowest_cost_shoebrand})")
print(f"Highest Cost: ${highest_cost_shoes} ({highest_cost_shoe} - {highest_cost_shoebrand})")
print(f"Average Cost: ${average_cost_shoes:.2f}")

# Create a DataFrame with the lowest, highest, and average cost
stats_df = pd.DataFrame({
    'Statistic': ['Lowest Cost', 'Highest Cost', 'Average Cost'],
    'Brand': [lowest_cost_shoebrand, highest_cost_shoebrand, ''],
    'Shoe Name': [lowest_cost_shoe, highest_cost_shoe, ''],
    'Price': [lowest_cost_shoes, highest_cost_shoes, average_cost_shoes]
})

# Add the brand average prices to the DataFrame
for brand in brand_avg_shoeprice.index:
    stats_df = stats_df.append({
        'Statistic': 'Brand Average Price',
        'Brand': brand,
        'Shoe Name': '',
        'Price': brand_avg_shoeprice[brand]
    }, ignore_index=True)

# Write the DataFrame to a CSV file
stats_df.to_csv('BackcountryClimbing-ShoeStats.csv', index=False)

###################################################
# Inferences on climbing chalkbags from Backcountry

# Read csv for climbing chalkbags
climbingharness_df = pd.read_csv('BackcountryClimbing-Harnesses.csv')

# Extract the Harness_Brand, Harness_Name and Harness_Price columns from the DataFrame
harnessbrands = climbingharness_df['Harness_Brand']
harnessnames = climbingharness_df['Harness_Name']
harnessprices = climbingharness_df['Harness_Price']

# Create a violin plot using Matplotlib with colors for each brand
cmap = 'inferno'
plt.violinplot([harnessprices[harnessbrands == brand] for brand in np.unique(harnessbrands)],
               positions=np.arange(len(np.unique(harnessbrands))) + 1,
               showmeans=True,
               showmedians=True,
               showextrema=True,
               widths=0.8)
plt.title('Cost Across Climbing Harness Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Price')

# Adjust the x-axis labels to prevent overlap
plt.xticks(np.arange(len(np.unique(harnessbrands))) + 1, np.unique(harnessbrands), rotation=45, ha='right')
plt.show()
plt.savefig("Climbing Harness Brand Plot.png")

# Calculate lowest, highest, and average cost
lowest_cost_harnesses = climbingharness_df['Harness_Price'].min()
highest_cost_harnesses = climbingharness_df['Harness_Price'].max()
average_cost_harnesses = climbingharness_df['Harness_Price'].mean()
brand_avg_harnessprice = climbingharness_df.groupby('Harness_Brand')['Harness_Price'].mean()
lowest_cost_harness = climbingharness_df.iloc[climbingharness_df['Harness_Price'].idxmin()]['Harness_Name']
lowest_cost_harnesbrand = climbingharness_df.iloc[climbingharness_df['Harness_Price'].idxmin()]['Harness_Brand']
highest_cost_harness = climbingharness_df.iloc[climbingharness_df['Harness_Price'].idxmax()]['Harness_Name']
highest_cost_harnessbrand = climbingharness_df.iloc[climbingharness_df['Harness_Price'].idxmax()]['Harness_Brand']

print("Backcountry Climbing Harnesses")
print(f"Lowest Cost: ${lowest_cost_harnesses} ({lowest_cost_harness} - {lowest_cost_harness})")
print(f"Highest Cost: ${highest_cost_harnesses} ({highest_cost_harness} - {highest_cost_harnessbrand})")
print(f"Average Cost: ${average_cost_harnesses:.2f}")

# Create a DataFrame with the lowest, highest, and average cost
stats_df = pd.DataFrame({
    'Statistic': ['Lowest Cost', 'Highest Cost', 'Average Cost'],
    'Brand': [lowest_cost_harness, highest_cost_harnessbrand, ''],
    'Harness Price': [lowest_cost_harness, highest_cost_harness, ''],
    'Price': [lowest_cost_harnesses, highest_cost_harnesses, average_cost_harnesses]
})

# Add the brand average prices to the DataFrame
for brand in brand_avg_harnessprice.index:
    stats_df = stats_df.append({
        'Statistic': 'Brand Average Price',
        'Brand': brand,
        'Harness Name': '',
        'Price': brand_avg_harnessprice[brand]
    }, ignore_index=True)

# Write the DataFrame to a CSV file
stats_df.to_csv('BackcountryClimbing-HarnessStats.csv', index=False)

#######################################################
# Inferences on climbing chalkbags from Backcountry

# Read csv for climbing harnesses
climbingchalkbag_df = pd.read_csv('BackcountryClimbing-Chalkbags.csv')

# Inference on plotting the brand and climbing harness cost

# Extract the Chalkbag_Brand, Chalkbag_Name and Chalkbag_Price columns from the DataFrame
cbbrands = climbingchalkbag_df['Chalkbag_Brand']
cbnames = climbingchalkbag_df['Chalkbag_Name']
cbprices = climbingchalkbag_df['Chalkbag_Price']

# Create a violin plot using Matplotlib with colors for each brand
cmap = 'inferno'
plt.violinplot([cbprices[cbbrands == brand] for brand in np.unique(cbbrands)],
               positions=np.arange(len(np.unique(cbbrands))) + 1,
               showmeans=True,
               showmedians=True,
               showextrema=True,
               widths=0.8)
plt.title('Cost Across Climbing Chalkbag Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Price')

# Adjust the x-axis labels to prevent overlap
plt.xticks(np.arange(len(np.unique(cbbrands))) + 1, np.unique(cbbrands), rotation=45, ha='right')
plt.show()
plt.savefig("Climbing Chalk Bags Brand Plot.png")
# Inference on average cost of brand of climbing chalkbag from Backcountry

# Calculate lowest, highest, and average cost
lowest_cost_cb = climbingchalkbag_df['Chalkbag_Price'].min()
highest_cost_cb = climbingchalkbag_df['Chalkbag_Price'].max()
average_cost_cb = climbingchalkbag_df['Chalkbag_Price'].mean()
brand_avg_cbprice = climbingchalkbag_df.groupby('Chalkbag_Brand')['Chalkbag_Price'].mean()
lowest_cost_chalkbag = climbingchalkbag_df.iloc[climbingchalkbag_df['Chalkbag_Price'].idxmin()]['Chalkbag_Name']
lowest_cost_cbbrand = climbingchalkbag_df.iloc[climbingchalkbag_df['Chalkbag_Price'].idxmin()]['Chalkbag_Brand']
highest_cost_chalkbag = climbingchalkbag_df.iloc[climbingchalkbag_df['Chalkbag_Price'].idxmax()]['Chalkbag_Name']
highest_cost_cbbrand = climbingchalkbag_df.iloc[climbingchalkbag_df['Chalkbag_Price'].idxmax()]['Chalkbag_Brand']

print("Backcountry Climbing Chalkbags")
print(f"Lowest Cost: ${lowest_cost_cb} ({lowest_cost_chalkbag} - {lowest_cost_chalkbag})")
print(f"Highest Cost: ${highest_cost_cb} ({highest_cost_chalkbag} - {highest_cost_cbbrand})")
print(f"Average Cost: ${average_cost_cb:.2f}")

# Create a DataFrame with the lowest, highest, and average cost
stats_df = pd.DataFrame({
    'Statistic': ['Lowest Cost', 'Highest Cost', 'Average Cost'],
    'Brand': [lowest_cost_cbbrand, highest_cost_cbbrand, ''],
    'Harness Price': [lowest_cost_chalkbag, highest_cost_chalkbag, ''],
    'Price': [lowest_cost_cb, highest_cost_cb, average_cost_cb]
})

# Add the brand average prices to the DataFrame
for brand in brand_avg_cbprice.index:
    stats_df = stats_df.append({
        'Statistic': 'Brand Average Price',
        'Brand': brand,
        'Chalkbag Name': '',
        'Price': brand_avg_cbprice[brand]
    }, ignore_index=True)

# Write the DataFrame to a CSV file
stats_df.to_csv('BackcountryClimbing-ChalkbagStats.csv', index=False)

#######################################################
# Inferences on climbing chalk from Backcountry

# Read csv for climbing chalk
climbingchalk_df = pd.read_csv('BackcountryClimbing-Chalk.csv')

# Inference on plotting the brand and climbing chalk cost

# Extract the Chalk_Brand, Chalk_Name and Chalk_Price columns from the DataFrame
chalkbrands = climbingchalk_df['Chalk_Brand']
chalknames = climbingchalk_df['Chalk_Name']
chalkprices = climbingchalk_df['Chalk_Price']

# Create a violin plot using Matplotlib with colors for each brand
cmap = 'inferno'
plt.violinplot([chalkprices[chalkbrands == brand] for brand in np.unique(chalkbrands)],
               positions=np.arange(len(np.unique(chalkbrands))) + 1,
               showmeans=True,
               showmedians=True,
               showextrema=True,
               widths=0.8)
plt.title('Cost Across Climbing Chalk Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Price')

# Adjust the x-axis labels to prevent overlap
plt.xticks(np.arange(len(np.unique(chalkbrands))) + 1, np.unique(chalkbrands), rotation=45, ha='right')
plt.show()
plt.savefig("Climbing Shoe Brand Plot.png")

# Inference on average cost of brand of climbing chalk from Backcountry

# Calculate lowest, highest, and average cost
lowest_cost_chalks = climbingchalk_df['Chalk_Price'].min()
highest_cost_chalks = climbingchalk_df['Chalk_Price'].max()
average_cost_chalks = climbingchalk_df['Chalk_Price'].mean()
brand_avg_chalkprice = climbingchalk_df.groupby('Chalk_Brand')['Chalk_Price'].mean()
lowest_cost_chalk = climbingchalk_df.iloc[climbingchalk_df['Chalk_Price'].idxmin()]['Chalk_Name']
lowest_cost_chalkbrand = climbingchalk_df.iloc[climbingchalk_df['Chalk_Price'].idxmin()]['Chalk_Brand']
highest_cost_chalk = climbingchalk_df.iloc[climbingchalk_df['Chalk_Price'].idxmax()]['Chalk_Name']
highest_cost_chalkbrand = climbingchalk_df.iloc[climbingchalk_df['Chalk_Price'].idxmax()]['Chalk_Brand']

print("Backcountry Climbing Chalkbags")
print(f"Lowest Cost: ${lowest_cost_chalks} ({lowest_cost_chalk} - {lowest_cost_chalk})")
print(f"Highest Cost: ${highest_cost_chalks} ({highest_cost_chalk} - {highest_cost_chalkbrand})")
print(f"Average Cost: ${average_cost_chalks:.2f}")

# Create a DataFrame with the lowest, highest, and average cost
stats_df = pd.DataFrame({
    'Statistic': ['Lowest Cost', 'Highest Cost', 'Average Cost'],
    'Brand': [lowest_cost_chalkbrand, highest_cost_chalkbrand, ''],
    'Chalk Price': [lowest_cost_chalk, highest_cost_chalk, ''],
    'Price': [lowest_cost_chalks, highest_cost_chalks, average_cost_chalks]
})

# Add the brand average prices to the DataFrame
for brand in brand_avg_chalkprice.index:
    stats_df = stats_df.append({
        'Statistic': 'Brand Average Price',
        'Brand': brand,
        'Chalk Name': '',
        'Price': brand_avg_chalkprice[brand]
    }, ignore_index=True)

# Write the DataFrame to a CSV file
stats_df.to_csv('BackcountryClimbing-ChalkStats.csv', index=False)

#######################################################
# Inferences on climbing belay devices from Backcountry

# Read csv for climbing belay devices
climbingbelaydevices_df = pd.read_csv('BackcountryClimbing-BelayDevices.csv')

# Inference on plotting the brand and climbing belay device cost

# Extract the Belay_Brand, Belay_Name and Belay_Price columns from the DataFrame
belaybrands = climbingbelaydevices_df['Belaydevice_Brand']
belaynames = climbingbelaydevices_df['Belaydevice_Name']
belayprices = climbingbelaydevices_df['Belaydevice_Price']

# Create a violin plot using Matplotlib with colors for each brand
cmap = 'inferno'
plt.violinplot([belayprices[belaybrands == brand] for brand in np.unique(belaybrands)],
               positions=np.arange(len(np.unique(belaybrands))) + 1,
               showmeans=True,
               showmedians=True,
               showextrema=True,
               widths=0.8)
plt.title('Cost Across Climbing Belay Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Price')

# Adjust the x-axis labels to prevent overlap
plt.xticks(np.arange(len(np.unique(belaybrands))) + 1, np.unique(belaybrands), rotation=45, ha='right')
plt.show()
plt.savefig("Climbing Shoe Belay Plot.png")

# Inference on average cost of brand of climbing harness from Backcountry

# Calculate lowest, highest, and average cost
lowest_cost_belayd = climbingbelaydevices_df['Belaydevice_Price'].min()
highest_cost_belayd = climbingbelaydevices_df['Belaydevice_Price'].max()
average_cost_belayd = climbingbelaydevices_df['Belaydevice_Price'].mean()
brand_avg_belayprice = climbingbelaydevices_df.groupby('Belaydevice_Brand')['Belaydevice_Price'].mean()
lowest_cost_belay = climbingbelaydevices_df.iloc[climbingbelaydevices_df['Belaydevice_Price'].idxmin()][
    'Belaydevice_Name']
lowest_cost_belaybrand = climbingbelaydevices_df.iloc[climbingbelaydevices_df['Belaydevice_Price'].idxmin()][
    'Belaydevice_Brand']
highest_cost_belay = climbingbelaydevices_df.iloc[climbingbelaydevices_df['Belaydevice_Price'].idxmax()][
    'Belaydevice_Name']
highest_cost_belaybrand = climbingbelaydevices_df.iloc[climbingbelaydevices_df['Belaydevice_Price'].idxmax()][
    'Belaydevice_Brand']

print("Backcountry Climbing Belay Devices")
print(f"Lowest Cost: ${lowest_cost_belayd} ({lowest_cost_belay} - {lowest_cost_belay})")
print(f"Highest Cost: ${highest_cost_belayd} ({highest_cost_belay} - {highest_cost_belaybrand})")
print(f"Average Cost: ${average_cost_belayd:.2f}")

# Create a DataFrame with the lowest, highest, and average cost
stats_df = pd.DataFrame({
    'Statistic': ['Lowest Cost', 'Highest Cost', 'Average Cost'],
    'Brand': [lowest_cost_belaybrand, highest_cost_belaybrand, ''],
    'BelayDevice Price': [lowest_cost_belay, highest_cost_belay, ''],
    'Price': [lowest_cost_belayd, highest_cost_belayd, average_cost_belayd]
})

# Add the brand average prices to the DataFrame
for brand in brand_avg_belayprice.index:
    stats_df = stats_df.append({
        'Statistic': 'Brand Average Price',
        'Brand': brand,
        'BelayDevice Name': '',
        'BelayDevice Price': brand_avg_belayprice[brand]
    }, ignore_index=True)

# Write the DataFrame to a CSV file
stats_df.to_csv('BackcountryClimbing-BelayDevicesStats.csv', index=False)

######################
# Results of brand cost across all categories

# Inferences on climbing shoes from Backcountry
climbingshoe_df = pd.read_csv('../Modeling/BackcountryClimbing-Shoes.csv')
shoebrands = climbingshoe_df['Shoe_Brand']
shoeprices = climbingshoe_df['Shoe_Price']

# Inferences on climbing harnesses from Backcountry
climbingharness_df = pd.read_csv('BackcountryClimbing-Harnesses.csv')
harnessbrands = climbingharness_df['Harness_Brand']
harnessprices = climbingharness_df['Harness_Price']

# Combine the climbing shoes and climbing harnesses data
brands = pd.concat([shoebrands, harnessbrands])
prices = pd.concat([shoeprices, harnessprices])
combined_df = pd.DataFrame({'Brand': brands, 'Price': prices})

# Group the combined DataFrame by brand and calculate the mean price for each brand
brand_avg_price = combined_df.groupby('Brand')['Price'].mean()

# Create a bar plot showing the average price of each brand
plt.bar(x=brand_avg_price.index, height=brand_avg_price.values)
plt.title('Average Cost Across Climbing Brands at Backcountry')
plt.xlabel('Brand')
plt.ylabel('Average Price')
plt.xticks(rotation=45, ha='right')
plt.show()
plt.savefig("Average Cost Across Climbing Brands at Backcountry")

############################
# Cumulative Results

# Read csv files for climbing equipment
climbing_shoes_df = pd.read_csv('../Modeling/BackcountryClimbing-Shoes.csv')
climbing_chalk_df = pd.read_csv('BackcountryClimbing-Chalk.csv')
climbing_chalkbag_df = pd.read_csv('BackcountryClimbing-Chalkbags.csv')
climbing_harness_df = pd.read_csv('BackcountryClimbing-Harnesses.csv')
climbing_belay_df = pd.read_csv('BackcountryClimbing-BelayDevices.csv')


# Define a function to calculate the lowest, highest, and average cost for each category
def calculate_stats(df, category):
    lowest_cost = df[category + '_Price'].min()
    lowest_item = df.loc[df[category + '_Price'].idxmin(), category + '_Name']
    lowest_brand = df.loc[df[category + '_Price'].idxmin(), category + '_Brand']
    highest_cost = df[category + '_Price'].max()
    highest_item = df.loc[df[category + '_Price'].idxmax(), category + '_Name']
    highest_brand = df.loc[df[category + '_Price'].idxmax(), category + '_Brand']
    avg_cost = df[category + '_Price'].mean()
    return {'Category': category,
            'Lowest Cost': lowest_cost,
            'Lowest Item': lowest_item,
            'Lowest Brand': lowest_brand,
            'Highest Cost': highest_cost,
            'Highest Item': highest_item,
            'Highest Brand': highest_brand,
            'Average Cost': avg_cost}


# Calculate the stats for each category
shoe_stats = calculate_stats(climbing_shoes_df, 'Shoe')
chalk_stats = calculate_stats(climbing_chalk_df, 'Chalk')
chalkbag_stats = calculate_stats(climbing_chalkbag_df, 'Chalkbag')
harness_stats = calculate_stats(climbing_harness_df, 'Harness')
belay_stats = calculate_stats(climbing_belay_df, 'Belaydevice')

# Create a DataFrame with the stats for each category
stats_df = pd.DataFrame([shoe_stats, chalk_stats, chalkbag_stats, harness_stats, belay_stats])

# Calculate the lowest cost for all categories combined
lowest_combined = stats_df['Lowest Cost'].min()

# Calculate the highest cost for all categories combined
highest_combined = stats_df['Highest Cost'].max()

# Calculate the average cost for all categories combined
avg_combined = stats_df['Average Cost'].mean()

# Create a DataFrame with the items in the lower cost end for each category
lower_cost_df = pd.concat([climbing_shoes_df[climbing_shoes_df['Shoe_Price'] <= shoe_stats['Lowest Cost']],
                           climbing_chalk_df[climbing_chalk_df['Chalk_Price'] <= chalk_stats['Lowest Cost']],
                           climbing_chalkbag_df[climbing_chalkbag_df['Chalkbag_Price'] <= chalkbag_stats['Lowest Cost']],
                           climbing_harness_df[climbing_harness_df['Harness_Price'] <= harness_stats['Lowest Cost']],
                           climbing_belay_df[climbing_belay_df['Belaydevice_Price'] <= belay_stats['Lowest Cost']]])

# Calculate the total sum of all prices at low cost combined
total_price_low_cost = lower_cost_df['Shoe_Price'].sum() + lower_cost_df['Chalk_Price'].sum() + \
                       lower_cost_df['Chalkbag_Price'].sum() + lower_cost_df['Harness_Price'].sum() + \
                       lower_cost_df['Belaydevice_Price'].sum()

# Add a new column to lower_cost_df with the total cost of each item
lower_cost_df['Total_Cost_Low_Cost'] = lower_cost_df['Shoe_Price'] + lower_cost_df['Chalk_Price'] + \
                                       lower_cost_df['Chalkbag_Price'] + lower_cost_df['Harness_Price'] + \
                                       lower_cost_df['Belaydevice_Price']

# Write the DataFrames to CSV files
stats_df.to_csv('concurrent_results.csv', index=False)
lower_cost_df.to_csv('lower_cost_items.csv', index=False)

# Print the total sum of all prices at low cost combined
print("Total sum of all prices at low cost combined: $", total_price_low_cost)

# Calculate the average price of all categories combined
average_price_all_categories = (climbing_shoes_df['Shoe_Price'].mean() +
                                climbing_chalk_df['Chalk_Price'].mean() +
                                climbing_chalkbag_df['Chalkbag_Price'].mean() +
                                climbing_harness_df['Harness_Price'].mean() +
                                climbing_belay_df['Belaydevice_Price'].mean())

# Print the average price of all categories combined
print("Average price of all categories combined: $", average_price_all_categories)
