
import streamlit as st
from dbhelper import DB
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Initialize database connection
db = DB()

# Sidebar navigation with icons
selected = option_menu(
    menu_title=None,
    options=["Home", "Check Flights", "Analytics"],
    icons=["house", "airplane", "bar-chart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Home":
    st.title("Flight Analytics Dashboard")
    st.write("Welcome to the Flight Analytics Dashboard!")
    
    # Key Metrics
    total_flights = db.fetch_total_flights()
    busiest_airport, _ = db.fetch_busiest_airport()
    avg_price = db.fetch_avg_price()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Flights", total_flights)
    col2.metric("Busiest Airport", busiest_airport[0])
    col3.metric("Average Ticket Price", f"${avg_price:.2f}")

elif selected == "Check Flights":
    st.title("Check Flights")
    city = db.fetch_city_names()
    
    col1, col2 = st.columns(2)
    with col1:
        source = st.selectbox("Source", sorted(city))
    with col2:
        dest = st.selectbox("Destination", sorted(city))
    
    price_range = st.slider("Select Price Range", 0, 10000, (0, 5000))
    departure_time = st.selectbox("Departure Time", ["Morning", "Afternoon", "Evening", "Night"])
    
    if st.button("Search"):
        res = db.fetch_all_flights(source, dest, price_range, departure_time)
        st.dataframe(res)

elif selected == "Analytics":
    st.title("Analytics")
    
    # Pie Chart: Airline Frequency
    airline, freq = db.fetch_airline_frequency()
    fig_pie = px.pie(names=airline, values=freq, title="Airline Frequency")
    st.plotly_chart(fig_pie)
    
    # Bar Chart: Busiest Airport
    city, freq1 = db.fetch_busiest_airport()
    fig_bar = px.bar(x=city, y=freq1, title="Busiest Airport", labels={"x": "City", "y": "Count"})
    st.plotly_chart(fig_bar)
    
    # Line Chart: Daily Frequency
    date, freq2 = db.fetch_daily_freq()
    fig_line = px.line(x=date, y=freq2, title="Daily Flight Frequency", labels={"x": "Date", "y": "Count"})
    st.plotly_chart(fig_line)
    
    # Heatmap: Flight Density
    routes, counts = db.fetch_top_route()
    fig_heatmap = go.Figure(data=go.Heatmap(z=counts, x=[r.split(" -> ")[0] for r in routes], y=[r.split(" -> ")[1] for r in routes]))
    fig_heatmap.update_layout(title="Flight Density Heatmap", xaxis_title="Source", yaxis_title="Destination")
    st.plotly_chart(fig_heatmap)

     # Additional Analytics
    st.subheader("Top 10 Flight Routes")
    routes = db.fetch_top_routes()
    st.dataframe(routes)
    
    st.subheader("Average Ticket Price by Airline")
    airline_prices = db.fetch_avg_ticket_price()
    st.dataframe(airline_prices)
    
    st.subheader("Busiest Travel Hours")
    travel_hours = db.fetch_busiest_travel_hours()
    fig = go.Figure(data=[go.Bar(x=travel_hours[0], y=travel_hours[1], marker_color='red')])
    fig.update_layout(title="Busiest Travel Hours", xaxis_title="Hour of Day", yaxis_title="Flight Count", font=dict(size=14), template="plotly_white")
    st.plotly_chart(fig)
