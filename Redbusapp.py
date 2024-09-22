# import libraries
import pandas as pd
import pymysql
import cryptography
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# Andhra bus
list_A=[]
df_apsrtc=pd.read_csv("df_apsrtc.csv")
for i,r in df_apsrtc.iterrows():
    list_A.append(r["bus_route_name"])

# Telugana bus
list_T=[]
df_tsrtc=pd.read_csv("df_tsrtc.csv")
for i,r in df_tsrtc.iterrows():
    list_T.append(r["bus_route_name"])

# Kerala bus
list_K=[]
df_ksrtc=pd.read_csv("df_ksrtc.csv")
for i,r in df_ksrtc.iterrows():
    list_K.append(r["bus_route_name"])

# Goa bus
list_G=[]
df_ktcl=pd.read_csv("df_ktcl.csv")
for i,r in df_ktcl.iterrows():
    list_G.append(r["bus_route_name"])

# Rajastan bus
list_R=[]
df_rsrtc=pd.read_csv("df_rsrtc.csv")
for i,r in df_rsrtc.iterrows():
    list_R.append(r["bus_route_name"])

# South Bengal bus
list_SB=[]
df_sbstc=pd.read_csv("df_sbstc.csv")
for i,r in df_sbstc.iterrows():
    list_SB.append(r["bus_route_name"])

# Haryana bus
list_H=[]
df_hrtc=pd.read_csv("df_hrtc.csv")
for i,r in df_hrtc.iterrows():
    list_H.append(r["bus_route_name"])

# UP bus
list_UP=[]
df_upsrtc=pd.read_csv("df_upsrtc.csv")
for i,r in df_upsrtc.iterrows():
    list_UP.append(r["bus_route_name"])

# Punjab bus
list_P=[]
df_pepsu=pd.read_csv("df_pepsu.csv")
for i,r in df_pepsu.iterrows():
    list_P.append(r["bus_route_name"])

# Bihar bus
list_B=[]
df_bsrtc=pd.read_csv("df_bsrtc.csv")
for i,r in df_bsrtc.iterrows():
    list_B.append(r["bus_route_name"])

# Setting up the Streamlit page
st.set_page_config(layout="wide")

# Creating a sidebar menu with options
web = option_menu(
    menu_title="onlineBus",  # Title of the menu
    options=["Home", "States and Routes"],  # List of options in the menu
    icons=["house", "map"],  # List of icons corresponding to the options (optional)
    menu_icon="cast",  # Icon for the menu (optional)
    default_index=0,  # Default selected option
    orientation="horizontal"  # Orientation of the menu
)
# Home page setting
if web == "Home":
    # st.image("t_500x300.jpg",width=200)
    st.title("Redbus Data Scrapping with selenium & Dynamic Filltering using streamlit")
    st.subheader(":blue[Domain] Transporation")
    st.subheader(":blue[ojective:]")
    st.markdown(" The 'Redbus Data Scrapping and Filltering  with streamlit Application' aims to revolutionize the transportation industry by providing a comperhensive solution")
    st.subheader(":blue[Overview:]")
    st.markdown("Selenium:selenium is a tool used fro automating web browsers.It is comonly used for web scrapping witn involves  extracting data from websites.Selenium")
    st.markdown('''Pandas: Use the  powerfull pandas library to transform the dataset from csv format into a structured dataframe.
                pandas helps data manipulation,cleaning,and preprocessing,ensuring that data was ready for analysis.''')
    st.markdown('''MYSQL:with help of SQL to establish a connection to a SQL database,enabling seamless intergration of the transfomed dataset
                and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    st.markdown("Streamlit: Developed an interactive application using Streamlit, a user-friendly framework for data visualization and analysis.")
    st.markdown('<span style="color:blue;">Skill Take:</span>', unsafe_allow_html=True)
    st.subheader(":blue[skill take.")
    st.markdown("Selenium,Python,Pandas,MYSQL,mysql.connector.python,Streamlit.")
    st.subheader(":blue[Developed by:]Gopalakrishnan T")
    
# states and Routes page setting
if web == "States and Routes":
    S = st.selectbox("List of states",["Andhra pradesh","Telugana","Kerala","Goa",
                                       "Rajastan","South Bengal","Uttar pradesh","Haryana","Punjab","Bihar"])
    select_fare = st.radio("chose bus fare range",("50 - 1000","1000 - 2000","2000 and above"))

    # Andhra bus fare filltering
    if S == "Andhra pradesh":
        A = st.selectbox("List of Routes",list_A)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
              
      
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{A}'
                                 and star_rating >='{star_rating}' '''
                                
                                                                                                                                      
                                
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{A}'
                                 and star_rating >='{star_rating}' '''
                                     
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{A}'
                                 and star_rating >='{star_rating}' '''   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
            
    # Telugana bus fare filltering
    if S == "Telugana":
        T = st.selectbox("List of Routes",list_T)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{T}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 and bus_route_name='{T}'
                                 and star_rating >='{star_rating}' '''
                                     
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{T}'
                                 and star_rating >='{star_rating}' '''

                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
    # Kerala bus fare filltering
    if S == "Kerala":
        K = st.selectbox("List of Routes",list_K)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{K}'
                                 and star_rating >='{star_rating}' '''
                                 
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 busroute_name='{K}'
                                 and star_rating >='{star_rating}' '''
                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{K}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)   
            
    # Goa bus fare filltering
    if S == "Goa":
        G = st.selectbox("List of Routes",list_G)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{G}'
                                 and star_rating >='{star_rating}' '''
                        
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{G}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and bus_route_name='{G}'
                                 and star_rating >='{star_rating}' '''
                            
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
    # Rajastan bus fare filltering
    if S == "Rajastan":
        R = st.selectbox("List of Routes",list_R)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{R}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{R}'
                                 and star_rating >='{star_rating}' '''
                                     
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  us_route_name='{R}'
                                 and star_rating >='{star_rating}' '''
                                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
    # South Bengal bus fare filltering
    if S == "South Bengal":
        SB = st.selectbox("List of Routes",list_SB)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{SB}'
                                 and star_rating >='{star_rating}' '''
                                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{SB}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{SB}'
                                 and star_rating >='{star_rating}' '''
                                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
    # Uttar pradesh bus fare filltering
    if S == "Uttar pradesh":
        UP = st.selectbox("List of Routes",list_UP)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{UP}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{UP}'
                                 and star_rating >='{star_rating}' '''
                                  
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{UP}'
                                 and star_rating >='{star_rating}' '''
                                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df) 
            
    # Haryana bus fare filltering
    if S == "Haryana":
        H = st.selectbox("List of Routes",list_H)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{H}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{H}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{H}'
                                 and star_rating >='{star_rating}' '''
                                
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
    # Punjab bus fare filltering
    if S == "Punjab":
        P = st.selectbox("List of Routes",list_P)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{P}'
                                 and star_rating >='{star_rating}' '''
                                     
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{P}'
                                 and star_rating >='{star_rating}' '''
                                     
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{P}'
                                 and star_rating >='{star_rating}' '''
                                    
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)  
            
    # Bihar bus fare filltering
    if S == "Bihar":
        B = st.selectbox("List of Routes",list_B)
        # Select star rating filter
        star_rating = st.slider("Select Star Rating", 1.0, 5.0, 3.0, step=0.1)  # Slider between 1.0 and 5.0 with 0.1 step
    
        # Select departure time filter
        departure_time = st.time_input("Select Departure Time", value=None)  # User can pick a time
    
        # Select reaching time filter
        reaching_time = st.time_input("Select Reaching Time", value=None)  # User can pick a time
        
        if departure_time:
           departure_time_str = departure_time.strftime('%H:%M:%S')
        else:
            departure_time_str = None  # Handle case when no time is selected
    
        if reaching_time:
           reaching_time_str = reaching_time.strftime('%H:%M:%S')
        else:
           reaching_time_str = None  # Handle case when no time is selected
        
        
        if select_fare=="50-1000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 50 and 1000 bus_route_name='{B}'
                                 and star_rating >='{star_rating}' '''
                                   
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="1000-2000":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price between 1000 and 2000 bus_route_name='{B}'
                                 and star_rating >='{star_rating}' '''
                            
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
            
        if select_fare=="2000 and above":
            conn = pymysql.connect(host = "localhost",user = "root",password = "Thiruvesh@2017",database = "RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            Query = f'''select * from bus_details
                                 where price >= 2000 and  bus_route_name='{B}'
                                 and star_rating >='{star_rating}' '''
                                
            
            my_cursor.execute(Query)
            out = my_cursor.fetchall()
            df = pd.DataFrame(["ID","bus_route_name","bus_route_link","bus_name","bus_type","departing_time"
                                          "duration","reaching_time","star_rating","price","seat_availabiility"])
            st.write(df)
             # Close connection
            conn.close()














    
    










    
    
    
    





















