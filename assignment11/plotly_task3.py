import plotly.express as px
import plotly.data as pldata

#task3
df = pldata.wind(return_type='pandas')

print(df.head(10))
print("----" * 20)
print(df.tail(10))

#print(df['strength'].value_counts())

df["strength"] = (
    df["strength"]
    .str.replace("+", "", regex=False)   
    .str.split("-", n=1).str[0]       
    .astype(float)
)
#print(df['strength'].value_counts())

fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title="Strength vs Frequency Wind", hover_data=["frequency"])

fig.write_html("task3.html", auto_open=True)