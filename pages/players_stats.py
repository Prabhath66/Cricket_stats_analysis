import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Cricket Dashboard", layout="wide")



# Load data
batting = pd.read_csv("total_teams_batting.csv") 
bowling = pd.read_excel("Bowling_Stats_Excel.xlsx") 

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
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Matches", int(batting_stats.loc[selected_format, "Matches"]))
        col2.metric("Runs", int(batting_stats.loc[selected_format, "Runs"])) 
        col3.metric("Average", batting_stats.loc[selected_format, "Average"])
        col4.metric("Strike Rate", batting_stats.loc[selected_format, "SR"])
        col5.metric("Highest Score",int(batting_stats.loc[selected_format,"Highest"]))

        # Display key metrics
        st.markdown("#### 🧮 Bowling Key Performance Metrics")
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Wickets", int(bowling_stats.loc[selected_format, "Wickets"]))
        col2.metric("Average", bowling_stats.loc[selected_format, "Avg"])
        col3.metric("Economy", bowling_stats.loc[selected_format, "Eco"])
        col4.metric("Strike Rate", bowling_stats.loc[selected_format, "SR"])
        col5.metric("Best Bowling",bowling_stats.loc[selected_format,"BBM"])

        # --- Tabbed layout ---
        st.markdown("---")
        tabs = st.tabs(["🏏 Batting", "🎯 Bowling"])

        with tabs[0]:
            st.subheader(f"🏏 Batting Stats - {player}")
            with st.expander("Show Batting Table", expanded=False):
                st.dataframe(batting_stats)

            col1,col2=st.columns(2)
            with col1:
                fig = px.pie(batting_stats, names=batting_stats.index, values=batting_stats["Matches"], title=f"{player}'s Matches Across Formats")
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                fig = px.bar(batting_stats, x=batting_stats.index, y=batting_stats['Runs'].values, labels={'x':'Format', 'y':'Runs'}, title=f"{player} Runs Across Formats")
                st.plotly_chart(fig, use_container_width=True) 

            players_4s_6s=batting_stats[["Fours","Sixes"]]
            players_4s_6s=players_4s_6s.reset_index().rename(columns={'index': 'Format'})
            fours_sixes = pd.melt(players_4s_6s, id_vars='Format', value_vars=['Fours', 'Sixes'],
                         var_name='Shot Type', value_name='Count')   # melt is used to make long format of dataset like T20 four count, t20 six count
            fig_grouped = px.bar(fours_sixes, x='Format', y='Count', color='Shot Type', barmode='group', 
                                 text='Count', title=f"{player} Fours and Sixes Across Formats") 
            st.plotly_chart(fig_grouped, use_container_width=True)  
                
        with tabs[1]:
            st.subheader(f"🎯 Bowling Stats - {player}")
            with st.expander("Show Bowling Table", expanded=False):
                st.dataframe(bowling_stats)

            col1,col2=st.columns(2)
            with col1:
                fig = px.pie(bowling_stats, names=bowling_stats.index, values=bowling_stats["Matches"], title=f"{player}'s Matches Across Formats")
                st.plotly_chart(fig, use_container_width=True)
            with col2:    
                fig = px.bar(bowling_stats,x=bowling_stats.index, y=bowling_stats['Wickets'].values, labels={'x':'Format', 'y':'Wickets'}, title=f"{player} Wickets Across Formats")
                st.plotly_chart(fig, use_container_width=True) 

            balls_maidens=bowling_stats[["Balls","Maidens"]]
            balls_maidens["Overs"]=[int(i/6) for i in [int(balls) for balls in bowling_stats['Balls'].values]]
            balls_maidens=balls_maidens.reset_index().rename(columns={'index': 'Format'})
            overs_maidens = pd.melt(balls_maidens, id_vars='Format', value_vars=['Overs', 'Maidens'], var_name='Bowled_type', value_name='Count') 
            fig_grouped = px.bar(overs_maidens, x='Format', y='Count', color='Bowled_type', barmode='group', 
                                 text='Count', title=f"{player} Overs and Maiden Overs Across Formats")  
            st.plotly_chart(fig_grouped, use_container_width=True)  

    else:
        st.info("👤 Please select a player to continue.")
else:
    st.info("🌍 Please select a country from the sidebar.")
