import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
batting = pd.read_csv("total_teams_batting.csv")
bowling = pd.read_csv("total_teams_bowling_stats.csv")

# Preprocess data to avoid repetitive groupby calls
batting_groups = batting.groupby("country")
bowling_groups = bowling.groupby("country")

# Set page title and layout
st.set_page_config(page_title="Player Stats Analysis", layout="wide")

# Custom styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 12px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stMetric>div {
            background-color: #f4f4f4;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #4CAF50;
            font-size: 36px;
            text-align: center;
            padding-bottom: 20px;
        }
        .stSelectbox>div>div>input {
            font-size: 16px;
        }
        .stTextInput>div>div>input {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Heading
st.title("Player Stats Analysis")

# Country Selection with Error Handling
country = st.selectbox("Select the Country", list(batting_groups.groups.keys()), index=None, placeholder="Enter the Country Name")

if not country:
    st.warning("Please select a country.")
else:
    # Player selection with error handling
    try:
        player_batting = batting_groups.get_group(country)
        player_bowling = bowling_groups.get_group(country)
    except KeyError:
        st.error(f"No data available for the country: {country}")
        st.stop()

    player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name")

    if not player:
        st.warning("Please select a player.")
    else:
        try:
            batting_stats = player_batting[player_batting['name'] == player][["ROWHEADER", "Test", "ODI", "T20", "IPL"]].set_index("ROWHEADER").T
            bowling_stats = player_bowling[player_bowling['name'] == player][["ROWHEADER", "Test", "ODI", "T20", "IPL"]].set_index("ROWHEADER").T
        except KeyError:
            st.error(f"No data available for the player: {player}")
            st.stop()

        # Display player stats across different formats
        options = ["Test", "ODI", "T20", "IPL"]
        selection = st.radio(f"Stats of {player} across different Formats", options, index=0)

        if selection == "Test":               
            col1, col2, col3, col4 = st.columns(4) 
            col1.metric(label="Matches", value=int(batting_stats.loc[selection,"Matches"]))
            col2.metric(label="Runs", value=int(batting_stats.loc[selection,"Runs"]))
            col3.metric(label="Average", value=batting_stats.loc[selection,"Average"])
            col4.metric(label="Strike Rate", value=batting_stats.loc[selection,"SR"])

        elif selection == "ODI":               
            col1, col2, col3, col4 = st.columns(4) 
            col1.metric(label="Matches", value=int(batting_stats.loc[selection,"Matches"]))
            col2.metric(label="Runs", value=int(batting_stats.loc[selection,"Runs"]))
            col3.metric(label="Average", value=batting_stats.loc[selection,"Average"])
            col4.metric(label="Strike Rate", value=batting_stats.loc[selection,"SR"])

        elif selection == "T20":               
            col1, col2, col3, col4 = st.columns(4) 
            col1.metric(label="Matches", value=int(batting_stats.loc[selection,"Matches"]))
            col2.metric(label="Runs", value=int(batting_stats.loc[selection,"Runs"]))
            col3.metric(label="Average", value=batting_stats.loc[selection,"Average"])
            col4.metric(label="Strike Rate", value=batting_stats.loc[selection,"SR"])

        elif selection == "IPL":               
            col1, col2, col3, col4 = st.columns(4) 
            col1.metric(label="Matches", value=int(batting_stats.loc[selection,"Matches"]))
            col2.metric(label="Runs", value=int(batting_stats.loc[selection,"Runs"]))
            col3.metric(label="Average", value=batting_stats.loc[selection,"Average"])
            col4.metric(label="Strike Rate", value=batting_stats.loc[selection,"SR"])

        # Stats Visualization (Batting, Bowling, or Both)
        stats_options = ["Bat", "Bowl", "Both"]
        stats_selection = st.radio(f"Choose stats to visualize for {player}", stats_options, index=0)

        if stats_selection == "Bat":
            st.subheader(f"Batting Stats of {player}")
            st.write(batting_stats)

            col = st.selectbox("Select the Column to Analyze", options=list(batting_stats.columns))
            if col in batting_stats.columns:
                fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting Stats of {player} - {col}', hover_data=[batting_stats.index])
                st.plotly_chart(fig)

        elif stats_selection == "Bowl":
            st.subheader(f"Bowling Stats of {player}")
            st.write(bowling_stats)

            col = st.selectbox("Select the Column to Analyze", options=list(bowling_stats.columns))
            if col in bowling_stats.columns:
                fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling Stats of {player} - {col}', hover_data=[bowling_stats.index])
                st.plotly_chart(fig)

        elif stats_selection == "Both":
            col1, col2 = st.columns(2)

            with col1:
                st.subheader(f"Batting Stats of {player}")
                st.write(batting_stats)

                col = st.selectbox("Select the Column to Analyze (Batting)", options=list(batting_stats.columns))
                if col in batting_stats.columns:
                    fig = px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting Stats of {player} - {col}', hover_data=[batting_stats.index])
                    st.plotly_chart(fig)

            with col2:
                st.subheader(f"Bowling Stats of {player}")
                st.write(bowling_stats)

                col = st.selectbox("Select the Column to Analyze (Bowling)", options=list(bowling_stats.columns))
                if col in bowling_stats.columns:
                    fig = px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling Stats of {player} - {col}', hover_data=[bowling_stats.index])
                    st.plotly_chart(fig)

