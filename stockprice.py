import pandas as pd
import matplotlib.pyplot as plt

# Sample stock price data (Date and Close price)
data_dict = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Close': [150, 155, 157, 160, 162]
}

# Create DataFrame
data = pd.DataFrame(data_dict)

# Convert 'Date' to datetime and set it as index
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Calculate moving average (e.g., over the last 3 days)
data['Moving_Avg'] = data['Close'].rolling(window=3).mean()

# Predict next day's price (we will assume the last moving average is the prediction)
predicted_price = data['Moving_Avg'].iloc[-1]  # This is the moving average on the last available day

# Display the prediction
print(f"Predicted next day's stock price using moving average: ${predicted_price:.2f}")

# Plot the results
plt.figure(figsize=(10, 6))

# Plot real stock prices
plt.plot(data.index, data['Close'], label='Real Prices', color='blue')

# Plot the moving average
plt.plot(data.index, data['Moving_Avg'], label='Moving Average (3-day)', color='orange', linestyle='--')

plt.title('Stock Price Prediction Using Moving Average')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()

# Show plot
plt.show()