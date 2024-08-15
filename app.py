import pandas
import plotly.express as px
import streamlit

streamlit.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


@streamlit.cache_data
def get_data_from_excel():
    df = pandas.read_excel(
            io="supermarkt_sales.xlsx",
            engine="openpyxl",
            sheet_name="Sales",
            skiprows=3,
            usecols="B:R",
            nrows=1000,
        )
    # Add 'hour' column to dataframe
    df["hour"] = pandas.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


df = get_data_from_excel()

# ---- SIDEBAR ----
streamlit.sidebar.header("Filter data Here:")
city = streamlit.sidebar.multiselect(
     "Select the City:",
     options=df["City"].unique(),
     default = df["City"].unique()
)


customer_type = streamlit.sidebar.multiselect(
    "Select the customer type",
    options= df["Customer_type"].unique(),
    default= df["Customer_type"].unique()
)

gender = streamlit.sidebar.multiselect(
    "choose your gender",
    options= df["Gender"].unique(),
    default= df["Gender"].unique()
)


df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

# Check if the dataframe is empty:
if df_selection.empty:
    streamlit.warning("No data available based on the current filter settings!")
    streamlit.stop() # This will halt the app from further execution.

# ---- MAINPAGE ----
streamlit.title(":bar_chart: Sales Dashboard")
streamlit.markdown("##")

total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column , middle_column, right_column  = streamlit.columns(3)

with left_column:
    streamlit.subheader("Total Sales: ")
    streamlit.subheader(f"US ${total_sales:,}")
    
with middle_column:
    streamlit.subheader("Average Rating: ")
    streamlit.subheader(f" {average_rating} {star_rating}")
    
with right_column:
    streamlit.subheader("Average Sales Per Transaction: ")
    streamlit.subheader(f"US ${average_sale_by_transaction}")
    
streamlit.markdown("""-----""")


# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")

# Plotting sales by hour
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
)


fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


left_column, right_column = streamlit.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
streamlit.markdown(hide_st_style, unsafe_allow_html=True)


streamlit.write(df_selection)