import streamlit as st
import pandas as pd
import plotly.express as px

batting = pd.read_csv("8teams_batting_stats.csv") 
bowling = pd.read_csv("8teams_bowling_stats.csv") 


# player selection 
player = st.selectbox("Select the Player", list(set(batting['name'])), index=None, placeholder="Enter the Player Name",) 
if player in list(set(batting['name'])) :
    #st.write("Batting Stats of {}".format(player))
    batting_stats=batting[batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T 
    #st.write(batting_stats)
    #st.write("Bowling Stats of {}".format(player))
    bowling_stats=bowling[bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T 
    #st.write(bowling_stats) 


    options = ["Bat", "Bowl", "Both"]
    selection = st.segmented_control(f"Stats of {player}", options, selection_mode="single")
    if selection == "Bat":
        if st.button(f"Batting Stats of {player}", type="tertiary"):
            st.write(batting_stats)
        
        # selecting the columns to analyze
        col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)
        if col in batting_stats.columns:
          fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
          # fig.show() 
          st.plotly_chart(fig)
            
    elif selection == "Bowl": 
        if st.button(f"Bowling Stats of {player}", type="tertiary"):
            st.write(bowling_stats) 
                
        # selecting the columns to analyze
        col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)
        if col in bowling_stats.columns:
          fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}')
          # fig.show() 
          st.plotly_chart(fig)

    
    elif selection == "Both":
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Batting Stats of {player}", type="tertiary"):
                st.write(batting_stats)
            
            # selecting the columns to analyze
            col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)
            if col in batting_stats.columns:
              fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
              # fig.show() 
              st.plotly_chart(fig)
        with col2:
            if st.button(f"Bowling Stats of {player}", type="tertiary"):
                st.write(bowling_stats) 
            
            if st.toggle(f"Bowling Stats of {player}"):
                st.write("Feature activated!")
                
            # selecting the columns to analyze
            col=st.selectbox("Select the Column to Analyze ", options=list(bowling_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)
            if col in bowling_stats.columns:
              fig=px.pie(values=bowling_stats[col].values, names=bowling_stats.index, title=f'Bowling stats of {player} {col}')
              # fig.show() 
              st.plotly_chart(fig)
            

    #select_stats=st.selectbox("Select the option (Batting / Bowling"),["Batting", "Bowling"],index)  

    # col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)

    # if col in batting_stats.columns:
    #   fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
    #   # fig.show() 
    #   st.plotly_chart(fig)



















# import streamlit as st
# import pandas as pd
# import plotly.express as px

# batting = pd.read_csv("8teams_batting_stats.csv") 
# bowling = pd.read_csv("8teams_bowling_stats.csv") 


# # player selection 
# player = st.selectbox("Select the Player", list(set(batting['name'])), index=None, placeholder="Enter the Player Name",) 
# if player in list(set(batting['name'])) :
#     #st.write("Batting Stats of {}".format(player))
#     batting_stats=batting[batting['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T 
#     #st.write(batting_stats)
#     #st.write("Bowling Stats of {}".format(player))
#     bowling_stats=bowling[bowling['name']==player][["ROWHEADER","Test","ODI","T20","IPL"]].set_index("ROWHEADER").T 
#     #st.write(bowling_stats) 


#     options = ["Bat", "Bowl", "Both"]
#     selection = st.segmented_control(f"Stats of {player}", options, selection_mode="single")
#     if selection == "Bat":
#         st.write("Batting Stats of {}".format(player))
#         st.write(batting_stats)
#     elif selection == "Bowl": 
#         st.write("Bowling Stats of {}".format(player)) 
#         st.write(bowling_stats) 
#     elif selection == "Both": 
#         st.write("Batting Stats of {}".format(player))
#         st.write(batting_stats)
#         st.write("Bowling Stats of {}".format(player))
#         st.write(bowling_stats)

#     select_stats=st.selectbox("Select the option (Batting / Bowling"),["Batting", "Bowling"],index)  

#     col=st.selectbox("Select the Column to Analyze ", options=list(batting_stats.columns), index=None, placeholder="Enter the Column Name to Analyze",)

#     if col in batting_stats.columns:
#       fig=px.pie(values=batting_stats[col].values, names=batting_stats.index, title=f'Batting stats of {player} {col}')
#       # fig.show() 
#       st.plotly_chart(fig)
   
    