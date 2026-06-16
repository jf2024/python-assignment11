import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#task2
conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders AS o
JOIN line_items AS l ON o.order_id = l.order_id
JOIN products   AS p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, conn)
print(df)
conn.close()

df["cumulative"] = df["total_price"].cumsum()


plt.plot(df["order_id"], df["cumulative"], color="purple")

plt.title("Cumulative Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.tight_layout()
plt.show()