import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Cricket Player Stats Analyzer", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #f0f0f0;
}
h1, h2, h3, h4, h5 {
    color: #00ffd5 !important;
    text-shadow: 1px 1px 4px rgba(0,255,213,0.3);
}
.stApp {
    animation: fadeIn 0.8s ease-in-out;
}
@keyframes fadeIn {
    0% { opacity: 0; transform: translateY(10px); }
    100% { opacity: 1; transform: translateY(0); }
}
.stButton > button {
    background-color: #00ffd5;
    color: black;
    font-weight: 600;
    border-radius: 8px;
    padding: 8px 20px;
    box-shadow: 0 0 10px #00ffd5;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background-color: #00e6c1;
    transform: scale(1.05);
}
.stSelectbox label, .stDataFrame {
    color: #ffffff !important;
}
.stPlotlyChart {
    background: rgba(255, 255, 255, 0.03);
    padding: 1rem;
    border-radius: 15px;
    box-shadow: 0 0 12px rgba(0,255,213,0.1);
    transition: all 0.3s ease;
}
.stPlotlyChart:hover {
    transform: scale(1.01);
    box-shadow: 0 0 25px rgba(0,255,213,0.15);
}
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.title("🏏 Cricket Player Stats Analyzer")
st.markdown("""
Welcome to the **Cricket Player Stats Dashboard**!  
Explore individual player performances across formats: **Test**, **ODI**, **T20**, and **IPL**.

---

### 🔍 How to Use:
- 🌍 Select a **Country**
- 🧍 Choose a **Player**
- 📊 View **Key Stats** and Format-wise performance
- 📈 Interact with **Pie Charts** and Metrics

---
""")



import streamlit as st
import pandas as pd
import plotly.express as px

batting = pd.read_csv("total_teams_batting.csv") 
bowling = pd.read_csv("total_teams_bowling_stats.csv") 

# # --- App Header ---
# st.title("🏏 Cricket Player Stats Dashboard")
# st.markdown("""
# Welcome to the **Cricket Player Stats Dashboard**!  
# Explore batting and bowling performances of your favorite players across different formats: **Test**, **ODI**, **T20**, and **IPL**.

# ---

# 🔍 **Instructions:**
# - Select a **Country**
# - Choose a **Player**
# - View stats in different **formats**
# - Analyze data through interactive **charts** and key **metrics**

# ---
# """)


st.subheader("🌍 Select a Country")
country = st.selectbox("Select the Country", list(batting.groupby("country").groups.keys()), index=None, placeholder="Enter the Country Name",)

#player = st.selectbox("Select the Player", list(teams.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)

if country in list(batting.groupby("country").groups.keys()):
    player_batting=batting.groupby("country").get_group(country)
    player_bowling=bowling.groupby("country").get_group(country)

    st.subheader("👤 Select a Player")
    player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)
    if player in list(player_batting.groupby("name").groups.keys()) :
  
        batting_stats=player_batting[player_batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
        # st.write(batting_stats)
    
        bowling_stats=player_bowling[player_bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
        # st.write(bowling_stats)

        # Format Selection
        st.markdown("####### 📂 Choose a Format to View Summary")
        formats = ["Test", "ODI", "T20", "IPL"]
        format_selection = st.segmented_control(f"View {player}'s Stats by Format",options=formats,default="Test", selection_mode="single")

        # Display Key Metrics 
        st.markdown(f"##### 📊 {format_selection} Performance Stats")              
        col1, col2, col3, col4 = st.columns(4) 
        col1.metric(label="Matches", value=int(batting_stats.loc[format_selection,"Matches"]))
        col2.metric(label="Runs", value=int(batting_stats.loc[format_selection,"Runs"]))
        col3.metric(label="Average", value=batting_stats.loc[format_selection,"Average"])
        col4.metric(label="Strike Rate", value=batting_stats.loc[format_selection,"SR"])


        # View Type Selection
        st.markdown("#### 🧭 Select Type of Stats to Explore") 
        view_selection = st.segmented_control(f"Explore {player}'s Stats", options=["Bat", "Bowl", "Both"], default="Bat", selection_mode="single")
        # Batting Only
        if view_selection == "Bat":
            st.markdown(f"##### 🏏 Batting Statistics of **{player}**")  
            if st.button(f"Show Batting Stats of {player}", type="tertiary"):
                st.write(batting_stats)
            
            # selecting the columns to analyze
            col=st.selectbox("🎯 Choose a Batting Metric to Visualize", options=list(batting_stats.columns), placeholder="Select a batting metric")
            if col in batting_stats.columns:
               fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
               # fig.show() 
               st.plotly_chart(fig)
        # Bowling Only
        elif view_selection == "Bowl": 
            st.markdown(f"#### 🎯 Bowling Statistics of **{player}**") 
            if st.button(f" Show Bowling Stats of {player}", type="tertiary"):
                st.write(bowling_stats) 
                    
            # selecting the columns to analyze
            col = st.selectbox("🎯 Choose a Bowling Metric to Visualize", options=list(bowling_stats.columns), placeholder="Select a bowling metric")
            if col in bowling_stats.columns:
              fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}') 
              st.plotly_chart(fig)

        # Both Batting and Bowling
        elif view_selection == "Both":
            st.markdown(f"#### 📘 Batting & Bowling Statistics of **{player}**")
            if st.button(f"Show {player}'s Batting & Bowling Stats", type="tertiary"):
                st.markdown("##### 🏏 Batting Stats")
                st.write(batting_stats)
                    
                st.markdown("##### 🎯 Bowling Stats")
                st.write(bowling_stats)
                
            col1, col2 = st.columns(2)

            with col1:

                col = st.selectbox("📌 Select Batting Metric", options=list(batting_stats.columns),  placeholder="Choose an option")
                if col:
                    fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
                    st.plotly_chart(fig)

            with col2:  

                col = st.selectbox("📌 Select Bowling Metric",options=list(bowling_stats.columns), placeholder="Choose an option")
                if col:
                    fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}')
                    st.plotly_chart(fig)














#         elif selection == "Both":
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button(f"Batting Stats of {player}", type="tertiary"):
#                     st.write(batting_stats)

#                 # selecting the columns to analyze
#                 col = st.selectbox("🎯 Choose a Bowling Metric to Visualize", options=list(bowling_stats.columns), placeholder="Select a bowling metric")
#                 if col in batting_stats.columns:
#                   fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
#                   # fig.show() 
#                   st.plotly_chart(fig)
                    
#             with col2:
#                 if st.button(f"Bowling Stats of {player}", type="tertiary"):
#                     st.write(bowling_stats)
                    
#                 # if st.toggle(f"Bowling Stats of {player}"):
#                 #     st.write(bowling_stats) 

#                 # selecting the columns to analyze
#                 col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), placeholder="Enter the Column Name to Analyze",)
#                 if col in bowling_stats.columns:
#                   fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}')
#                   # fig.show() 
#                   st.plotly_chart(fig)
    

                

#     #select_stats=st.selectbox("Select the option (Batting / Bowling"),["Batting", "Bowling"],index)  









# # --- App Header ---
# st.title("🏏 Cricket Player Stats Dashboard")
# st.markdown("""
# Welcome to the **Cricket Player Stats Dashboard**!  
# Explore batting and bowling performances of your favorite players across different formats: **Test**, **ODI**, **T20**, and **IPL**.

# ---

# 🔍 **Instructions:**
# - Select a **Country**
# - Choose a **Player**
# - View stats in different **formats**
# - Analyze data through interactive **charts** and key **metrics**

# ---
# """)

   





        # # Both Batting and Bowling
        # elif view_selection == "Both":
        #     st.markdown(f"#### 📘 Batting & Bowling Statistics of **{player}**")
        #     if st.button(f"Show {player}'s Batting & Bowling Stats", type="tertiary"):
        #         st.markdown("##### 🏏 Batting Stats")
        #         if st.button(f"Show Batting Table", type="tertiary"):
        #             st.write(batting_stats)
                    
        #         st.markdown("##### 🎯 Bowling Stats")
        #         if st.button(f"Show Bowling Table", type="tertiary"):
        #             st.write(bowling_stats)
                
        #     col1, col2 = st.columns(2)

        #     with col1:

        #         col = st.selectbox("📌 Select Batting Metric", options=list(batting_stats.columns),  placeholder="Choose an option")
        #         if col:
        #             fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
        #             st.plotly_chart(fig)

        #     with col2:  

        #         col = st.selectbox("📌 Select Bowling Metric",options=list(bowling_stats.columns), placeholder="Choose an option")
        #         if col:
        #             fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}')
        #             st.plotly_chart(fig)
                    



    