#import imp libraries
import streamlit as st
import pandas as pd

#background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpapercave.com/wp/wp7171924.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://wallpapercave.com/wp/wp7171924.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


#import datasets
aarti = pd.read_csv('spotify Aarti.csv')
navratri = pd.read_csv('spotify Navratri_songs.csv')
devotional = pd.read_csv('spotify---devotional song.csv')
assame = pd.read_csv('spotify_Assamese_music.csv')
english = pd.read_csv('spotify_English_music.csv')
malyalam = pd.read_csv('spotify_Malyalam_music.csv')
marathi = pd.read_csv('spotify_Marathi_music.csv')
hindi2 = pd.read_csv('spotify_musicdev2.csv')
rajasthani = pd.read_csv('spotify_Rajasthani_music.csv')
telugu = pd.read_csv('spotify_Telugu_music.csv')

#defining a main function
def main():
    st.title('Devotional Songs App')
    st.subheader("Welcome to the App - You've selected the below Menu option")

    menu = ['Aarti','Navratri','Devotional','Assame','English','Malyalam','Marathi','Hindi2','Rajasthani','Telugu']
    choice = st.sidebar.selectbox ("Menu", menu)

    if choice == "Aarti":
        st.subheader("Aarti")
        st.text('List of the Aarti Songs')
        aarti['name'].values


        #background image
        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://wallpaperaccess.com/full/1567846.jpg")
            }
           .sidebar .sidebar-content {
                background: url("https://wallpaperaccess.com/full/1567846.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )



        # Aarti song
        aarti_pop = pd.DataFrame(aarti.groupby('name')['popularity'].mean())
        aarti_matrix = aarti.pivot_table(index='album', columns='name', values='popularity')
        aarti_matrix2 = aarti_matrix.fillna(0)
        aarti_pop.sort_values('popularity', ascending=False).head(10)
        #abc1 = aarti_matrix2["Aarti Kije Hanuman"]
        selected_song_name = st.selectbox('Select the Song Name', aarti['name'].values)
        abc1 = aarti_matrix2[selected_song_name]
        similar_to_abc1 = aarti_matrix2.corrwith(abc1)
        corr_abc1 = pd.DataFrame(similar_to_abc1, columns=['corr'])
        corr_abc1.dropna(inplace=True)
        corr_abc_aarti = corr_abc1.join(aarti_pop['popularity'])
        st.text('Selected Aarti Song is')
        st.write(selected_song_name)
        #final_aarti = corr_abc_aarti[corr_abc_aarti['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(aarti['popularity'].unique()))
        final_aar_1 = corr_abc_aarti[corr_abc_aarti['popularity'] > selected_song_popularity].sort_values(by='corr',
                                               
                                                                                                          ascending=False)
        final_aarti_1 = final_aar_1.drop('corr', axis=1)
        #final_aarti = final_aar_1
        final_aarti= final_aarti_1.sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_aarti.index)

    elif choice == "Navratri":
        st.subheader("Navratri")
        st.text('List of the Navratri Songs')
        navratri['name'].values
        
        
        #background image
        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://images.unsplash.com/photo-1614850523060-8da1d56ae167?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGlnaHQlMjBjb2xvdXJ8ZW58MHx8MHx8&w=1000&q=80")
            }
           .sidebar .sidebar-content {
                background: url("https://images.unsplash.com/photo-1614850523060-8da1d56ae167?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGlnaHQlMjBjb2xvdXJ8ZW58MHx8MHx8&w=1000&q=80")
            }
            </style>
            """,
            unsafe_allow_html=True
        )


        # Navratri Song
        nav_pop = pd.DataFrame(navratri.groupby('name')['popularity'].mean())
        nav_matrix = navratri.pivot_table(index='album', columns='name', values='popularity')
        nav_matrix2 = nav_matrix.fillna(0)
        nav_pop.sort_values('popularity', ascending=False).head(10)
        #abc2 = nav_matrix2["Aaj Tera Jagrata Mata"]
        selected_song_name = st.selectbox('Select the Song Name', navratri['name'].values)
        abc2 = nav_matrix2[selected_song_name]
        similar_to_abc2 = nav_matrix2.corrwith(abc2)
        corr_abc2 = pd.DataFrame(similar_to_abc2, columns=['corr'])
        corr_abc2.dropna(inplace=True)
        corr_abc_nav = corr_abc2.join(nav_pop['popularity'])
        st.text('Selected Navratri Song is')
        st.write(selected_song_name)
        #final_nav = corr_abc_nav[corr_abc_nav['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(navratri['popularity'].unique()))
        final_nav = corr_abc_nav[corr_abc_nav['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)
        final_nav_1 = final_nav.drop('corr', axis=1)
        #final_navratri = final_nav_1.head()
        final_navratri = final_nav_1.head().sort_values(by='popularity', ascending=False)


        st.text('Top Popular songs are ')
        st.write(final_navratri.index)


    elif choice == "Devotional":
        st.subheader("Devotional")
        st.text('List of the Devotional Songs')
        devotional['name'].values

        # Devotional song
        devo_pop = pd.DataFrame(devotional.groupby('name')['popularity'].mean())
        devo_matrix = devotional.pivot_table(index='album', columns='name', values='popularity')
        devo_matrix2 = devo_matrix.fillna(0)
        devo_pop.sort_values('popularity', ascending=False).head(10)
        #abc3 = devo_matrix2["Aarti Shree Banke Bihari Ji"]
        selected_song_name = st.selectbox('Select the Song Name', devotional['name'].values)
        abc3 = devo_matrix2[selected_song_name]
        similar_to_abc3 = devo_matrix2.corrwith(abc3)
        corr_abc3 = pd.DataFrame(similar_to_abc3, columns=['corr'])
        corr_abc3.dropna(inplace=True)
        corr_abc_devo = corr_abc3.join(devo_pop['popularity'])
        st.text('Selected Devotional Song is')
        st.write(selected_song_name)
        #final_devo = corr_abc_devo[corr_abc_devo['popularity'] > 10].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(devotional['popularity'].unique()))
        final_devo = corr_abc_devo[corr_abc_devo['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                             ascending=False)
        final_devo_1 = final_devo.drop('corr', axis=1)
        #final_devotional = final_devo_1.head()
        final_devotional = final_devo_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_devotional.index)

    elif choice == "Assame":
        st.subheader("Assame")
        st.text('List of the Assame Songs')
        assame['name'].values

        # Assame song
        assame_pop = pd.DataFrame(assame.groupby('name')['popularity'].mean())
        assame_matrix = assame.pivot_table(index='album', columns='name', values='popularity')
        assame_matrix2 = assame_matrix.fillna(0)
        assame_pop.sort_values('popularity', ascending=False).head(10)
        #abc4 = assame_matrix2["Ramo Gokhai"]
        selected_song_name = st.selectbox('Select the Song Name', assame['name'].values)
        abc4 = assame_matrix2[selected_song_name]
        similar_to_abc4 = assame_matrix2.corrwith(abc4)
        corr_abc4 = pd.DataFrame(similar_to_abc4, columns=['corr'])
        corr_abc4.dropna(inplace=True)
        corr_abc_assame = corr_abc4.join(assame_pop['popularity'])
        st.text('Selected Assame Song is')
        st.write(selected_song_name)
        #final_assame= corr_abc_assame[corr_abc_assame['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(assame['popularity'].unique()))
        final_assame_1 = corr_abc_assame[corr_abc_assame['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                             ascending=False)
        final_assame_1 = final_assame_1.drop('corr', axis=1)
        #final_assame = final_assame_1.head()
        final_assame = final_assame_1.head().sort_values(by='popularity', ascending=False)


        st.text('Top Popular songs are ')
        st.write(final_assame.index)



    elif choice == "English":
        st.subheader("English")
        st.text('List of the English Songs')
        english['name'].values
        
        
        #background image
        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://i.pinimg.com/originals/4c/68/3c/4c683c0460d0f37c20ba2a708bf5f999.jpg")
            }
           .sidebar .sidebar-content {
                background: url("https://i.pinimg.com/originals/4c/68/3c/4c683c0460d0f37c20ba2a708bf5f999.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # English song
        eng_pop = pd.DataFrame(english.groupby('name')['popularity'].mean())
        eng_matrix = english.pivot_table(index='album', columns='name', values='popularity')
        eng_matrix2 = eng_matrix.fillna(0)
        eng_pop.sort_values('popularity', ascending=False).head(10)
        #abc7 = eng_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', english['name'].values)
        abc7 = eng_matrix2[selected_song_name]
        similar_to_abc7 = eng_matrix2.corrwith(abc7)
        corr_abc7 = pd.DataFrame(similar_to_abc7, columns=['corr'])
        corr_abc7.dropna(inplace=True)
        corr_abc_eng = corr_abc7.join(eng_pop['popularity'])
        st.text('Selected English Song is')
        st.write(selected_song_name)
        #final_eng = corr_abc_eng[corr_abc_eng['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(english['popularity'].unique()))
        final_eng = corr_abc_eng[corr_abc_eng['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                        ascending=False)
        final_english_1 = final_eng.drop('corr', axis=1)
        #final_english = final_english_1.head()
        final_english = final_english_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_english.index)


    elif choice == "Malyalam":
        st.subheader("Malyalam")
        st.text('List of the Malyalam Songs')
        malyalam['name'].values
        
        #background image
        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://wallpapercave.com/wp/wp7984501.jpg")
            }
           .sidebar .sidebar-content {
                background: url("https://wallpapercave.com/wp/wp7984501.jpg")
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Malyalam song
        mal_pop = pd.DataFrame(malyalam.groupby('name')['popularity'].mean())
        mal_matrix = malyalam.pivot_table(index='album', columns='name', values='popularity')
        mal_matrix2 = mal_matrix.fillna(0)
        mal_pop.sort_values('popularity', ascending=False).head(10)
        #abc8 = mal_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', malyalam['name'].values)
        abc8 = mal_matrix2[selected_song_name]
        similar_to_abc8 = mal_matrix2.corrwith(abc8)
        corr_abc8 = pd.DataFrame(similar_to_abc8, columns=['corr'])
        corr_abc8.dropna(inplace=True)
        corr_abc_mal = corr_abc8.join(mal_pop['popularity'])
        st.text('Selected Malyalam Song is')
        st.write(selected_song_name)
        #final_mal = corr_abc_mal[corr_abc_mal['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(malyalam['popularity'].unique()))
        final_mal = corr_abc_mal[corr_abc_mal['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)
        final_malyalam_1 = final_mal.drop('corr', axis=1)
        #final_malyalam= final_malyalam_1.head()
        final_malyalam = final_malyalam_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_malyalam.index)


    elif choice == "Marathi":
        st.subheader("Marathi")
        st.text('List of the Marathi Songs')
        marathi['name'].values

        # Marathi song
        mara_pop = pd.DataFrame(marathi.groupby('name')['popularity'].mean())
        mara_matrix = marathi.pivot_table(index='album', columns='name', values='popularity')
        mara_matrix2 = mara_matrix.fillna(0)
        mara_pop.sort_values('popularity', ascending=False).head(10)
        #abc9 = mara_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', marathi['name'].values)
        abc9 = mara_matrix2[selected_song_name]
        similar_to_abc9 = mara_matrix2.corrwith(abc9)
        corr_abc9 = pd.DataFrame(similar_to_abc9, columns=['corr'])
        corr_abc9.dropna(inplace=True)
        corr_abc_mara = corr_abc9.join(mara_pop['popularity'])
        st.text('Selected Marathi Song is')
        st.write(selected_song_name)
        #final_mara = corr_abc_mara[corr_abc_mara['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(marathi['popularity'].unique()))
        final_mara = corr_abc_mara[corr_abc_mara['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                          ascending=False)
        final_marathi_1 = final_mara.drop('corr', axis=1)
        #final_marathi = final_marathi_1.head()
        final_marathi = final_marathi_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_marathi.index)



    elif choice == "Hindi2":
        st.subheader("Hindi")
        st.text('List of the Hindi-2 Songs')
        hindi2['name'].values

        # Hindi2 song
        hin2_pop = pd.DataFrame(hindi2.groupby('name')['popularity'].mean())
        hin2_matrix = hindi2.pivot_table(index='album', columns='name', values='popularity')
        hin2_matrix2 = hin2_matrix.fillna(0)
        hin2_pop.sort_values('popularity', ascending=False).head(10)
        #abc11 = hin2_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', hindi2['name'].values)
        abc11 = hin2_matrix2[selected_song_name]
        similar_to_abc11 = hin2_matrix2.corrwith(abc11)
        corr_abc11 = pd.DataFrame(similar_to_abc11, columns=['corr'])
        corr_abc11.dropna(inplace=True)
        corr_abc_hin2 = corr_abc11.join(hin2_pop['popularity'])
        st.text('Selected Hindi_2 Song is')
        st.write(selected_song_name)
        #final_hin2 = corr_abc_hin2[corr_abc_hin2['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(hindi2['popularity'].unique()))
        final_hin2 = corr_abc_hin2[corr_abc_hin2['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                         ascending=False)

        final_hindi2_1 = final_hin2.drop('corr', axis=1)
        #final_hindi2 = final_hindi2_1.head()
        final_hindi2 = final_hindi2_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_hindi2.index)


    elif choice == "Rajasthani":
        st.subheader("Rajasthani")
        st.text('List of the Rajasthani Songs')
        rajasthani['name'].values
        
        
         #background image
        st.markdown(
            """
            <style>
            .reportview-container {
                background: url("https://www.tourism.rajasthan.gov.in/content/dam/rajasthan-tourism/english/city/explore/521.jpg")
            }
           
            </style>
            """,
            unsafe_allow_html=True
        )

        # Rajasthani song
        rajas_pop = pd.DataFrame(rajasthani.groupby('name')['popularity'].mean())
        rajas_matrix = rajasthani.pivot_table(index='album', columns='name', values='popularity')
        rajas_matrix2 = rajas_matrix.fillna(0)
        rajas_pop.sort_values('popularity', ascending=False).head(10)
        #abc12 = rajas_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', rajasthani['name'].values)
        abc12 = rajas_matrix2[selected_song_name]
        similar_to_abc12 = rajas_matrix2.corrwith(abc12)
        corr_abc12 = pd.DataFrame(similar_to_abc12, columns=['corr'])
        corr_abc12.dropna(inplace=True)
        corr_abc_rajas = corr_abc12.join(rajas_pop['popularity'])
        st.text('Selected Rajasthani Song is')
        st.write(selected_song_name)
        #final_rajas = corr_abc_rajas[corr_abc_rajas['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(rajasthani['popularity'].unique()))
        final_rajas = corr_abc_rajas[corr_abc_rajas['popularity'] > selected_song_popularity].sort_values(
            by='corr',ascending=False)
        final_rajas_1 = final_rajas.drop('corr', axis=1)
        #final_rajasthani = final_rajas_1.head()
        final_rajasthani = final_rajas_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_rajasthani.index)


    elif choice == "Telugu":
        st.subheader("Telugu")
        st.text('List of the Telugu Songs')
        telugu['name'].values

        # Telugu song
        tel_pop = pd.DataFrame(telugu.groupby('name')['popularity'].mean())
        tel_matrix = telugu.pivot_table(index='album', columns='name', values='popularity')
        tel_matrix2 = tel_matrix.fillna(0)
        tel_pop.sort_values('popularity', ascending=False).head(10)
        #abc13 = tel_matrix2[""]
        selected_song_name = st.selectbox('Select the Song Name', telugu['name'].values)
        abc13 = tel_matrix2[selected_song_name]
        similar_to_abc13 = tel_matrix2.corrwith(abc13)
        corr_abc13 = pd.DataFrame(similar_to_abc13, columns=['corr'])
        corr_abc13.dropna(inplace=True)
        corr_abc_tel = corr_abc13.join(tel_pop['popularity'])
        st.text('Selected Telugu Song is')
        st.write(selected_song_name)
        #final_tel = corr_abc_tel[corr_abc_tel['popularity'] > 5].sort_values(by='corr', ascending=False)
        selected_song_popularity = st.selectbox('Popularity Value', sorted(telugu['popularity'].unique()))
        final_tel = corr_abc_tel[corr_abc_tel['popularity'] > selected_song_popularity].sort_values(by='corr',
                                                                                                       ascending=False)
        final_telugu_1 = final_tel.drop('corr', axis=1)
        #final_telugu = final_telugu_1.head()
        final_telugu = final_telugu_1.head().sort_values(by='popularity', ascending=False)

        st.text('Top Popular songs are ')
        st.write(final_telugu.index)


if __name__ == '__main__':
    main()


