import pymysql

class DB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='Svini@1995',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('connection established!!!')
        except:
            print("Connection Error")
            
    def fetch_city_names(self):
        self.mycursor.execute("""select Distinct(destination) from flights_cleaned union select distinct(source) from flights.flights_cleaned""")
        data = self.mycursor.fetchall()
        print(data)
        city = []
        for item in data:
            city.append(item[0])
        return city
    # def fetch_all_flights(self, source, dest):
    #     query = """SELECT Airline, Route, Dep_Time, Duration, Price 
    #             FROM flights.flights_cleaned 
    #             WHERE source = %s AND destination = %s"""
    #     self.mycursor.execute(query, (source, dest))
    #     data = self.mycursor.fetchall()
    #     return data
    def fetch_all_flights(self, source, dest, price_range, departure_time):
        """
        Fetch flights based on source, destination, price range, and departure time.
        """
        # Base query
        query = """
            SELECT Airline, Route, Dep_Time, Duration, Price 
            FROM flights_cleaned 
            WHERE source = %s AND destination = %s
        """
        
        # Add price range filter
        query += " AND Price BETWEEN %s AND %s"
        
        # Add departure time filter
        if departure_time == "Morning":
            query += " AND Dep_Time BETWEEN '00:00' AND '12:00'"
        elif departure_time == "Afternoon":
            query += " AND Dep_Time BETWEEN '12:01' AND '18:00'"
        elif departure_time == "Evening":
            query += " AND Dep_Time BETWEEN '18:01' AND '23:59'"
        elif departure_time == "Night":
            query += " AND (Dep_Time BETWEEN '00:00' AND '06:00' OR Dep_Time BETWEEN '23:00' AND '23:59')"
        
        # Execute the query
        self.mycursor.execute(query, (source, dest, price_range[0], price_range[1]))
        data = self.mycursor.fetchall()
        return data
    def fetch_airline_frequency(self):
        airline=[]
        count=[]
        self.mycursor.execute("""SELECT Airline,count(*) from flights_cleaned group by Airline""")
        data=self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            count.append(item[1])
        return airline,count
    def fetch_busiest_airport(self):
        city=[]
        freq=[]
        self.mycursor.execute("""SELECT source,count(*) from (select source from flights_cleaned union all select destination from flights_cleaned) t GROUP BY t.source order by count(*) DESC""")
        data=self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            freq.append(item[1])
        return city,freq
    def fetch_daily_freq(self):
        date=[]
        freq=[]
        self.mycursor.execute("""SELECT Date_Of_Journey,count(*) from flights_cleaned Group by Date_Of_Journey order by count(*) DESC""")
        data=self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            freq.append(item[1])
        return date,freq
    def fetch_total_flights(self):
        self.mycursor.execute("SELECT COUNT(*) FROM flights_cleaned")
        return self.mycursor.fetchone()[0]

    def fetch_avg_price(self):
        self.mycursor.execute("SELECT AVG(Price) FROM flights_cleaned")
        return self.mycursor.fetchone()[0]

    def fetch_top_route(self):
        """
        Fetch the top 10 busiest routes with their flight frequencies.
        Returns:
            routes (list): List of route strings (e.g., "Banglore -> Delhi").
            counts (list): List of integers representing flight frequencies.
        """
        query = """
            SELECT CONCAT(source, ' -> ', destination) AS Route, COUNT(*) AS Frequency
            FROM flights_cleaned
            GROUP BY source, destination
            ORDER BY Frequency DESC
            LIMIT 10
        """
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        
        # Unpack the data into separate lists
        routes = [item[0] for item in data]
        counts = [item[1] for item in data]
        
        return routes, counts
    def fetch_top_routes(self):
        query = """
            SELECT Source, Destination, COUNT(*) as Flight_Count
            FROM flights_cleaned
            GROUP BY Source, Destination
            ORDER BY Flight_Count DESC
            LIMIT 10;
        """
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data

    def fetch_avg_ticket_price(self):
        query = """
            SELECT Airline, AVG(Price) as Avg_Price
            FROM flights_cleaned
            GROUP BY Airline
            ORDER BY Avg_Price DESC;
        """
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        return data

    def fetch_busiest_travel_hours(self):
        query = """
            SELECT HOUR(Dep_Time) as Hour, COUNT(*) as Flight_Count
            FROM flights_cleaned
            GROUP BY Hour
            ORDER BY Flight_Count DESC;
        """
        self.mycursor.execute(query)
        data = self.mycursor.fetchall()
        hours, counts = zip(*data)
        return hours, counts








