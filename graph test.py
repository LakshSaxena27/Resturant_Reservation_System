import sqlite3
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from collections import Counter

# Connect to your database and get all reservation dates
conn = sqlite3.connect("Customer database.db")
cursor = conn.cursor()
cursor.execute("SELECT Date FROM customer_database")
dates_raw = [row[0] for row in cursor.fetchall()]
conn.close()

# Convert the date strings into Python date objects
date_format = "%Y-%m-%d"  # Change this if your dates are formatted differently
dates = []
for d in dates_raw:
    try:
        dates.append(datetime.strptime(d, date_format).date())
    except Exception:
        print(f"Skipping invalid date: {d}")

# Count how many reservations happen on each date
date_counts = Counter(dates)

# Sort dates for plotting
sorted_dates = sorted(date_counts)
counts = [date_counts[d] for d in sorted_dates]

# Prepare data for the linear regression model
X = np.array([d.toordinal() for d in sorted_dates]).reshape(-1, 1)  # Dates as numbers
y = np.array(counts)  # Reservation counts

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict reservations for the next 28 days after the last date in your data
last_date = sorted_dates[-1]
future_dates = [last_date + timedelta(days=i) for i in range(1, 29)]
future_X = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
predictions = model.predict(future_X)

# Make sure predictions are not negative
predictions = np.clip(predictions, 0, None)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(sorted_dates, counts, label="Historical Reservations", marker='o')
plt.plot(future_dates, predictions, label="Predicted Reservations (Next 4 Weeks)", linestyle='--', marker='x')

plt.title("Reservation Counts: Historical and Predicted")
plt.xlabel("Date")
plt.ylabel("Number of Reservations")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

