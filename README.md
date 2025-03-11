# Flight Analytics Dashboard ✈️📊

## Overview
The **Flight Analytics Dashboard** is an interactive web application built using **Streamlit**, **Plotly**, and **MySQL**. It provides insights into flight data, allowing users to:
- Search for flights between cities ✈️  
- Analyze airline frequencies 📊  
- Identify the busiest airports and travel times 📅  
- View top flight routes and average ticket prices 💰  

## Features 🚀
- **Check Flights:** Search for flights based on source and destination.  
- **Analytics Dashboard:**
  - **Pie Chart:** Airline frequency  
  - **Bar Charts:** Busiest airports, daily flight frequency  
  - **Top Routes:** Most frequent flight routes  
  - **Average Ticket Price by Airline**  
  - **Busiest Travel Hours**  

## Tech Stack 🛠️
- **Frontend:** Streamlit  
- **Backend:** MySQL (using `pymysql`)  
- **Visualization:** Plotly  
- **Database Queries:** SQL  

## Installation 🏰️
1. Clone the repository:
  

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MySQL database:**
   - Import the `flights_cleaned.csv` file into a MySQL database.
   - Update **dbhelper.py** with your MySQL credentials.
   
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Database Schema 📂
The `flights_cleaned` table should have the following columns:
- `Source`
- `Destination`
- `Airline`
- `Route`
- `Dep_Time`
- `Duration`
- `Price`
- `Date_Of_Journey`

## Future Enhancements 🔥
- Add **real-time flight tracking**  
- Integrate **machine learning for price prediction**  
- Optimize queries for better performance  



