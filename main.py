from turtle import title
import streamlit as st
import hydralit_components as hc
import datetime
import snscrape.modules.twitter as scrap
import pandas as pd



def scrapTweets(filter):
    tweets = []
    for n, k in enumerate(filter):
        for i, tweet in enumerate(scrap.TwitterSearchScraper(f"{k}").get_items()):
            # print(str(i) + " " + k +" | " + str(tweet.date))
            tweets.append([k, tweet.date, tweet.id, tweet.content,
            tweet.user.username, tweet.user.followersCount,
            tweet.likeCount, tweet.lang])

    df = pd.DataFrame(tweets,columns=['key', 'Date', 'Tweet_id', 'Content',
                                    'Username','Followers','Likes', 'Language'])
    return df

#make it look nice from the start
st.set_page_config(page_title='Home' ,layout='wide')

# specify the primary menu definition
def NavBar():
    menu_data = [
        {'id':"getdata", 'label':"data analysis"},
        {'label':"wordcloud"},
    ]
    over_theme = {'txc_inactive': '#FFFFFF', 'menu_background':'#39C0ED'}
    menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=True, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    )
    return menu_id

def scrapData():
    keyList = ["#nato", '#NATO', '#otan', '#OTAN', '#russia','#RUSSIA', '#EMSI']
    with st.form('Getting Data Section'):
        col1, col2, col3, col4 = st.columns((1,1,1,1))
        with col1:
            options = st.multiselect('select...',keyList)
        submitted = st.form_submit_button("Submit")
    if submitted:
        st.spinner("Loading...")
        df_data = scrapTweets(options)
        st.write(df_data)
        st.success(" Done !")
        return df_data

def analyseData(df):
    df = df.drop_duplicates()    
    return df




menu_id = NavBar()

st.info(f"{menu_id}")
if menu_id == 'wordcloud':
    st.write('hello Mother Fuckers')
elif menu_id == 'getdata':
    df_data = scrapData()
    analyseData(df_data)





        

