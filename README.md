# Sales Dashboard with Streamlit

This project is a dynamic and interactive sales dashboard built using Python, Streamlit, Pandas, and Plotly. The dashboard allows users to visualize sales data, filter it by various categories, and explore key metrics such as total sales, average rating, and sales distribution by product line and time.

## Features

- **Interactive Filtering**: Filter sales data by city, customer type, and gender through an easy-to-use sidebar.
- **Key Performance Indicators (KPIs)**: Display of total sales, average rating, and average sales per transaction.
- **Sales by Product Line**: Horizontal bar chart showcasing the total sales by each product line.
- **Sales by Hour**: Visualization of sales distribution throughout the day, helping to identify peak sales hours.
- **Responsive Design**: The dashboard layout is designed to be responsive and adapts to different screen sizes.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/sales-dashboard.git
    cd sales-dashboard
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## File Structure

- `app.py`: The main script that runs the Streamlit application.
- `supermarkt_sales.xlsx`: The Excel file containing sales data.
- `requirements.txt`: The file listing all required Python packages for this project.

## Usage

After running the app, open your web browser and navigate to the local URL provided by Streamlit (typically `http://localhost:8501`). From there, you can use the sidebar to filter data based on city, customer type, and gender, and explore the sales data through the interactive charts.

## Customization

You can customize the dashboard by modifying the code in `app.py`. For example, you can:

- Add new filters or charts.
- Adjust the layout to better fit your needs.
- Integrate additional datasets to enhance the dashboard's functionality.

## Dependencies

- Python 3.x
- Streamlit
- Pandas
- Plotly

These dependencies are listed in `requirements.txt` and can be installed with `pip install -r requirements.txt`.

## Screenshots

![Sales Dashboard](Dashboard)

## Contact

For any questions or feedback, please reach out to:

- **Email**: [samarthmathur199@gmail.com](mailto:samarthmathur199@gmail.com)

