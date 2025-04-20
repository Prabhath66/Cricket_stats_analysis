# import streamlit as st
# import pandas as pd
# import plotly.express as px

# batting = pd.read_csv("total_teams_batting.csv") 
# bowling = pd.read_csv("total_teams_bowling_stats.csv") 


# # #st.write(teams.groupby("Country").get_group("West Indies") )

# st.subheader("🌍 Select a Country")
# country = st.selectbox("Select the Country", list(batting.groupby("country").groups.keys()), index=None, placeholder="Enter the Country Name",)

# #player = st.selectbox("Select the Player", list(teams.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)

# if country in list(batting.groupby("country").groups.keys()):
#     player_batting=batting.groupby("country").get_group(country)
#     player_bowling=bowling.groupby("country").get_group(country)

#     st.subheader("👤 Select a Player")
#     player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)
#     if player in list(player_batting.groupby("name").groups.keys()) :
#         # st.write("Batting Stats of {}".format(player))
#         batting_stats=player_batting[player_batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         # st.write(batting_stats)
#         # st.write("Bowling Stats of {}".format(player))
#         bowling_stats=player_bowling[player_bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         # st.write(bowling_stats)

#         options = ["Test", "ODI", "T20", "IPL"]
#         selection = st.segmented_control(f"Stats of {player} across different Format", options, default="Test", selection_mode="single")
#         # if selection == "Test":               
#         col1, col2, col3, col4 = st.columns(4) 
#         col1.metric(label="Matches", value=int(batting_stats.loc[selection,"Matches"]))
#         col2.metric(label="Runs", value=int(batting_stats.loc[selection,"Runs"]))
#         col3.metric(label="Average", value=batting_stats.loc[selection,"Average"])
#         col4.metric(label="Strike Rate", value=batting_stats.loc[selection,"SR"])



#         options = ["Bat", "Bowl", "Both"]
#         selection = st.segmented_control(f"Stats of {player}", options, default="Bat", selection_mode="single")
#         if selection == "Bat":
#             if st.button(f"Batting Stats of {player}", type="tertiary"):
#                 st.write(batting_stats)
            
#             # selecting the columns to analyze
#             col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), placeholder="Enter the Column Name to Analyze",)
#             if col in batting_stats.columns:
#               fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
#               # fig.show() 
#               st.plotly_chart(fig)
                
#         elif selection == "Bowl": 
#             if st.button(f"Bowling Stats of {player}", type="tertiary"):
#                 st.write(bowling_stats) 
                    
#             # selecting the columns to analyze
#             col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), placeholder="Enter the Column Name to Analyze",)
#             if col in bowling_stats.columns:
#               fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}') 
#               st.plotly_chart(fig)

    
#         elif selection == "Both":
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button(f"Batting Stats of {player}", type="tertiary"):
#                     st.write(batting_stats)

#                 # selecting the columns to analyze
#                 col=st.selectbox("Select the Column Name to Analyze ", options=list(batting_stats.columns), placeholder="Enter the Column Name to Analyze",)
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








import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
batting = pd.read_csv("total_teams_batting.csv") 
bowling = pd.read_csv("total_teams_bowling_stats.csv") 

# --- App Header ---
st.title("🏏 Cricket Player Stats Dashboard")
st.markdown("""
Welcome to the **Cricket Player Stats Dashboard**!  
Explore batting and bowling performances of your favorite players across different formats: **Test**, **ODI**, **T20**, and **IPL**.

---

🔍 **Instructions:**
- Select a **Country**
- Choose a **Player**
- View stats in different **formats**
- Analyze data through interactive **charts** and key **metrics**

---
""")

# --- Country Selection ---
st.subheader("🌍 Select a Country")
country = st.selectbox(
    "Choose from the list of cricket-playing nations:",
    list(batting.groupby("country").groups.keys()),
    index=None,
    placeholder="Enter the Country Name",
)

# --- Player Selection ---
if country:
    player_batting = batting.groupby("country").get_group(country)
    player_bowling = bowling.groupby("country").get_group(country)

    st.subheader("👤 Select a Player")
    player = st.selectbox(
        "Choose a player to view detailed stats:",
        list(player_batting.groupby("name").groups.keys()),
        index=None,
        placeholder="Enter the Player Name",
    )

    if player:
        # Extract batting and bowling data
        batting_stats = player_batting[player_batting['name'] == player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
        bowling_stats = player_bowling[player_bowling['name'] == player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T

        # Format Selection
        st.markdown("### 📂 Choose a Format to View Summary")
        formats = ["Test", "ODI", "T20", "IPL"]
        format_selection = st.segmented_control(
            f"View {player}'s Stats by Format",
            options=formats,
            default="Test",
            selection_mode="single"
        )

        # Display Key Metrics 
        st.markdown(f"#### 📊 {format_selection} Performance Highlights")
        col1, col2, col3, col4 = st.columns(4) 
        col1.metric(label="Matches", value=int(batting_stats.loc[format_selection,"Matches"]))
        col2.metric(label="Runs", value=int(batting_stats.loc[format_selection,"Runs"]))
        col3.metric(label="Average", value=batting_stats.loc[format_selection,"Average"])
        col4.metric(label="Strike Rate", value=batting_stats.loc[format_selection,"SR"])

        # View Type Selection
        st.markdown("### 🧭 Select Type of Stats to Explore") 
        view_selection = st.segmented_control(
            f"Explore {player}'s Stats",
            options=["Bat", "Bowl", "Both"],
            default="Bat",
            selection_mode="single"
        )

        # Batting Only
        if view_selection == "Bat":
            st.markdown(f"#### 🏏 Batting Statistics of **{player}**")
            if st.button(f"Show Batting Table", type="tertiary"):
                st.dataframe(batting_stats)

            col = st.selectbox(
                "🎯 Choose a Batting Metric to Visualize",
                options=list(batting_stats.columns),
                placeholder="Select a batting metric"
            )
            if col:
                fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
                st.plotly_chart(fig)

        # Bowling Only
        elif view_selection == "Bowl":
            st.markdown(f"#### 🎯https://cdn-icons-png.flaticon.com/128/1099/1099680.png Bowling Statistics of **{player}**")
            if st.button(f"Show Bowling Table", type="tertiary"):
                st.dataframe(bowling_stats)

            col = st.selectbox(
                "🎯 Choose a Bowling Metric to Visualize",
                options=list(bowling_stats.columns),
                placeholder="Select a bowling metric"
            )
            if col:
                fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}')
                st.plotly_chart(fig)

        # Both Batting and Bowling
        elif view_selection == "Both":
            st.markdown(f"#### 📘 Batting & Bowling Statistics of **{player}**")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("##### 🏏 Batting Stats")
                if st.button(f"Show Batting Table", type="tertiary", key="bat_table"):
                    st.dataframe(batting_stats)

                col = st.selectbox(
                    "📌 Select Batting Metric",
                    options=list(batting_stats.columns),
                    key="bat_both"
                )
                if col:
                    fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
                    st.plotly_chart(fig)

            with col2:
                st.markdown("##### 🎯 Bowling Stats")
                if st.button(f"Show Bowling Table", type="tertiary", key="bowl_table"):
                    st.dataframe(bowling_stats)

                col = st.selectbox(
                    "📌 Select Bowling Metric",
                    options=list(bowling_stats.columns),
                    key="bowl_both"
                )
                if col:
                    fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}')
                    st.plotly_chart(fig)

# Footer
st.markdown("""
---

🧠 **Note:**  
- Data is derived from two CSV files.
- This app supports performance comparison across formats and disciplines.
- Visualizations are powered by [Plotly](https://plotly.com/python/) and app is built with [Streamlit](https://streamlit.io/).

---
""")

    