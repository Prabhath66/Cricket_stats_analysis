import streamlit as st
import pandas as pd
import plotly.express as px

batting = pd.read_csv("total_teams_batting.csv") 
bowling = pd.read_csv("total_teams_bowling_stats.csv") 


# #st.write(teams.groupby("Country").get_group("West Indies") )


country = st.selectbox("Select the Country", list(batting.groupby("country").groups.keys()), index=None, placeholder="Enter the Country Name",)

#player = st.selectbox("Select the Player", list(teams.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)

if country in list(batting.groupby("country").groups.keys()):
    player_batting=batting.groupby("country").get_group(country)
    player_bowling=bowling.groupby("country").get_group(country)
    player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)
    if player in list(player_batting.groupby("name").groups.keys()) :
        # st.write("Batting Stats of {}".format(player))
        batting_stats=player_batting[player_batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
        st.write(batting_stats)
        # st.write("Bowling Stats of {}".format(player))
        bowling_stats=player_bowling[player_bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
        # st.write(bowling_stats)


        col1, col2, col3, col4 = st.columns(4) 
        col1.metric(label="Matches", value=int(batting_stats.loc["Test","Matches"]))
        col2.metric(label="Runs", value=int(batting_stats.loc["Test","Runs"]))
        col3.metric(label="Average", value=batting_stats.loc["Test","Average"])
        col4.metric(label="Strike Rate", value=batting_stats.loc["Test","SR"])

        options = ["Bat", "Bowl", "Both"]
        selection = st.segmented_control(f"Stats of {player}", options, selection_mode="single")
        if selection == "Bat":
            if st.button(f"Batting Stats of {player}", type="tertiary"):
                st.write(batting_stats)
            
            # selecting the columns to analyze
            col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), placeholder="Enter the Column Name to Analyze",)
            if col in batting_stats.columns:
              fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
              # fig.show() 
              st.plotly_chart(fig)
                
        elif selection == "Bowl": 
            if st.button(f"Bowling Stats of {player}", type="tertiary"):
                st.write(bowling_stats) 
                    
            # selecting the columns to analyze
            col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), placeholder="Enter the Column Name to Analyze",)
            if col in bowling_stats.columns:
              fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}') 
              st.plotly_chart(fig)

    
        elif selection == "Both":
            col, col0 = st.columns(2)
            with col:
                if st.button(f"Batting Stats of {player}", type="tertiary"):
                    st.write(batting_stats)
            with col0:
                if st.button(f"Bowling Stats of {player}", type="tertiary"):
                    st.write(bowling_stats)
                    
                # if st.toggle(f"Bowling Stats of {player}"):
                #     st.write(bowling_stats)            
    
            
            col1, col2 = st.columns(2)
            with col1:
                # selecting the columns to analyze
                col=st.selectbox("Select the Column Name to Analyze ", options=list(batting_stats.columns), placeholder="Enter the Column Name to Analyze",)
                if col in batting_stats.columns:
                  fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
                  # fig.show() 
                  st.plotly_chart(fig)
                
            with col2:                
                # selecting the columns to analyze
                col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), placeholder="Enter the Column Name to Analyze",)
                if col in bowling_stats.columns:
                  fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}')
                  # fig.show() 
                  st.plotly_chart(fig)
                

    #select_stats=st.selectbox("Select the option (Batting / Bowling"),["Batting", "Bowling"],index)  

    # col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)






# import streamlit as st
# import pandas as pd
# import plotly.express as px

# teams_batting = pd.read_csv("total_teams_batting.csv")
# teams_bowling = pd.read_csv("total_teams_bowling.csv")

# teams=pd.concat([west_indies,england])
# teams_bowl=pd.read_csv("teams_bowling_stats.csv")

# #st.write(teams.groupby("Country").get_group("West Indies") )


# country = st.selectbox("Select the Country", list(teams.groupby("Country").groups.keys()), index=None, placeholder="Enter the Country Name",)

#player = st.selectbox("Select the Player", list(teams.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)

# if country in list(teams.groupby("Country").groups.keys()):
#     player_batting=teams.groupby("Country").get_group(country)
#     player_bowling=teams_bowl.groupby("Country").get_group(country)
#     player = st.selectbox("Select the Player", list(player_batting.groupby("name").groups.keys()), index=None, placeholder="Enter the Player Name",)
#     if player in list(player_batting.groupby("name").groups.keys()) :
#         st.write("Batting Stats of {}".format(player))
#         batting_stats=player_batting[player_batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         st.write(batting_stats)
#         st.write("Bowling Stats of {}".format(player))
#         bowling_stats=player_bowling[player_bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T
#         st.write(bowling_stats)




# st.write(batting_stats["Matches"].values, batting_stats.index)
# st.write(px.pie(data=batting_stats,values=batting_stats["Matches"].values, labels=batting_stats.index ))



    