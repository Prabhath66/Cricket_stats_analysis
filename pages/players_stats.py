import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Cricket Dashboard", layout="wide")



# Load data
batting = pd.read_csv("total_teams_batting.csv") 
bowling = pd.read_csv("total_teams_bowling_stats.csv") 

# Header
st.title("🏏 Cricket Player Performance Dashboard")
st.markdown("""
Explore the **Batting** and **Bowling** statistics of your favorite players across **Test**, **ODI**, **T20**, and **IPL** formats.  
Use the filters below to select a country and a player.
""")

# --- Country selection ---
with st.sidebar:
    st.header("🌍 Select Country and Player")
    country = st.selectbox("Select a Country", sorted(batting["country"].unique()), index=None, placeholder="Start typing...")

if country:
    # Filter based on selected country
    player_batting = batting[batting["country"] == country]
    player_bowling = bowling[bowling["country"] == country]
    players = sorted(player_batting["name"].unique())

    with st.sidebar:
        player = st.selectbox("Select a Player", players, index=None, placeholder="Choose a player")

    if player:
        # Extract stats
        batting_stats = player_batting[player_batting['name'] == player][["ROWHEADER", "Test", "ODI", "T20", "IPL"]].set_index("ROWHEADER").T
        bowling_stats = player_bowling[player_bowling['name'] == player][["ROWHEADER", "Test", "ODI", "T20", "IPL"]].set_index("ROWHEADER").T

        # --- Format tab view ---
        st.subheader(f"📊 Overview: {player}'s Performance Summary")
        formats = ["Test", "ODI", "T20", "IPL"]
        selected_format = st.radio("📁 Choose a format:", formats, horizontal=True)

        # Display key metrics
        st.markdown("#### 🧮 Batting Key Performance Metrics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Matches", int(batting_stats.loc[selected_format, "Matches"]))
        col2.metric("Runs", int(batting_stats.loc[selected_format, "Runs"]))
        col3.metric("Average", batting_stats.loc[selected_format, "Average"])
        col4.metric("Strike Rate", batting_stats.loc[selected_format, "SR"])


        # Display key metrics
        st.markdown("#### 🧮 Bowling Key Performance Metrics")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Wickets", int(bowling_stats.loc[selected_format, "Wickets"]))
        col2.metric("Average", bowling_stats.loc[selected_format, "Avg"])
        col3.metric("Economy", bowling_stats.loc[selected_format, "Eco"])
        col4.metric("Strike Rate", bowling_stats.loc[selected_format, "SR"])

        # --- Tabbed layout ---
        st.markdown("---")
        tabs = st.tabs(["🏏 Batting", "🎯 Bowling", "📘 Both"])

        with tabs[0]:
            st.subheader(f"🏏 Batting Stats - {player}")
            with st.expander("Show Batting Table", expanded=False):
                st.dataframe(batting_stats)

            col1,col2=st.columns(2)
            with col1:
                fig = px.pie(batting_stats, names=batting_stats.index, values=batting_stats["Matches"], title=f"{player}'s Matches Across Formats")
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                fig = px.bar(batting_stats, x=batting_stats.index, y=batting_stats['Runs'].values, title=f"{player}'s Runs Across Formats")
                st.plotly_chart(fig, use_container_width=True) 
                
        with tabs[1]:
            st.subheader(f"🎯 Bowling Stats - {player}")
            with st.expander("Show Bowling Table", expanded=False):
                st.dataframe(bowling_stats)

            fig = px.pie(bowling_stats, names=bowling_stats.index, values=bowling_stats["Matches"], title=f"{player}'s Matches Across Formats")
            st.plotly_chart(fig, use_container_width=True)


            fig = px.bar(bowling_stats, x=bowling_stats.index, y=bowling_stats['Wickets'].values, title=f"{player}'s Wickets Across Formats")
            st.plotly_chart(fig, use_container_width=True)

        with tabs[2]:
            st.subheader(f"📘 Combined View - {player}")
            col1, col2 = st.columns(2)

            with col1:
                metric_bat = st.selectbox("🏏 Batting metric", batting_stats.columns, key="bat_metric")
                fig1 = px.pie(batting_stats, names=batting_stats.index, values=batting_stats[metric_bat],
                              title=f"{player}'s Batting - {metric_bat}")
                st.plotly_chart(fig1, use_container_width=True)

            with col2:
                metric_bowl = st.selectbox("🎯 Bowling metric", bowling_stats.columns, key="bowl_metric")
                fig2 = px.pie(bowling_stats, names=bowling_stats.index, values=bowling_stats[metric_bowl],
                              title=f"{player}'s Bowling - {metric_bowl}")
                st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("👤 Please select a player to continue.")
else:
    st.info("🌍 Please select a country from the sidebar.")













# import streamlit as st
# import pandas as pd
# import plotly.express as px

# batting = pd.read_csv("total_teams_batting.csv") 
# bowling = pd.read_csv("total_teams_bowling_stats.csv") 



# st.subheader("🌍 Select a Country")
# country = st.selectbox("Select the Country", list(batting.groupby("country").groups.keys()), index=None, placeholder="Enter the Country Name",)

# #player = st.selectbox("Select the Player", list(teams.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)

# if country in list(batting.groupby("country").groups.keys()):
#     player_batting=batting.groupby("country").get_group(country)
#     player_bowling=bowling.groupby("country").get_group(country)

#     st.subheader("👤 Select a Player")
#     player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)
#     if player in list(player_batting.groupby("name").groups.keys()) :
  
#         batting_stats=player_batting[player_batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         # st.write(batting_stats)
    
#         bowling_stats=player_bowling[player_bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         # st.write(bowling_stats)

#         # Format Selection
#         st.markdown("####### 📂 Choose a Format to View Summary")
#         formats = ["Test", "ODI", "T20", "IPL"]
#         format_selection = st.segmented_control(f"View {player}'s Stats by Format",options=formats,default="Test", selection_mode="single")

#         # Display Key Metrics 
#         st.markdown(f"##### 📊 {format_selection} Performance Stats")              
#         col1, col2, col3, col4 = st.columns(4) 
#         col1.metric(label="Matches", value=int(batting_stats.loc[format_selection,"Matches"]))
#         col2.metric(label="Runs", value=int(batting_stats.loc[format_selection,"Runs"]))
#         col3.metric(label="Average", value=batting_stats.loc[format_selection,"Average"])
#         col4.metric(label="Strike Rate", value=batting_stats.loc[format_selection,"SR"])


#         # View Type Selection
#         st.markdown("#### 🧭 Select Type of Stats to Explore") 
#         view_selection = st.segmented_control(f"Explore {player}'s Stats", options=["Bat", "Bowl", "Both"], default="Bat", selection_mode="single")
#         # Batting Only
#         if view_selection == "Bat":
#             st.markdown(f"##### 🏏 Batting Statistics of **{player}**")  
#             if st.button(f"Show Batting Stats of {player}", type="tertiary"):
#                 st.write(batting_stats)
            
#             # selecting the columns to analyze
#             col=st.selectbox("🎯 Choose a Batting Metric to Visualize", options=list(batting_stats.columns), placeholder="Select a batting metric")
#             if col in batting_stats.columns:
#                fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
#                # fig.show() 
#                st.plotly_chart(fig)
#         # Bowling Only
#         elif view_selection == "Bowl": 
#             st.markdown(f"#### 🎯 Bowling Statistics of **{player}**") 
#             if st.button(f" Show Bowling Stats of {player}", type="tertiary"):
#                 st.write(bowling_stats) 
                    
#             # selecting the columns to analyze
#             col = st.selectbox("🎯 Choose a Bowling Metric to Visualize", options=list(bowling_stats.columns), placeholder="Select a bowling metric")
#             if col in bowling_stats.columns:
#               fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}') 
#               st.plotly_chart(fig)

#         # Both Batting and Bowling
#         elif view_selection == "Both":
#             st.markdown(f"#### 📘 Batting & Bowling Statistics of **{player}**")
#             if st.button(f"Show {player}'s Batting & Bowling Stats", type="tertiary"):
#                 st.markdown("##### 🏏 Batting Stats")
#                 st.write(batting_stats)
                    
#                 st.markdown("##### 🎯 Bowling Stats")
#                 st.write(bowling_stats)
                
#             col1, col2 = st.columns(2)

#             with col1:

#                 col = st.selectbox("📌 Select Batting Metric", options=list(batting_stats.columns),  placeholder="Choose an option")
#                 if col:
#                     fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} - {col}')
#                     st.plotly_chart(fig)

#             with col2:  

#                 col = st.selectbox("📌 Select Bowling Metric",options=list(bowling_stats.columns), placeholder="Choose an option")
#                 if col:
#                     fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} - {col}')
#                     st.plotly_chart(fig)

