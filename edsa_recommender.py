"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Welcome", "Recommender System","About","EDA","Your Feedback"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    
    source = st.sidebar.checkbox("Data Source")
    if source:
        st.subheader("Where did we get the data from?")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/IMDB_Logo_2016.svg/1200px-IMDB_Logo_2016.svg.png", use_column_width=False)
        st.markdown("The data was obtained from the MovieLens which has the several millions 5-star ratings obtained from users using the online recommendation system. The IMBD (imbd_df) was legally scraped from IMDB.")
    
    
    
    
    look = st.sidebar.checkbox("Data")
    if look:
        st.subheader("What did the data consist?")
        st.markdown("* Movies - Movie titles are entered manually or imported from https://www.themoviedb.org/, and include the year of release in parentheses")
        st.markdown("* Genome_scores - is a score mapping the strength between movies and tag-related properties.")
        st.markdown("* Genome_tags - User assigned for the movies within the dataset.")
        st.markdown("* Imdb - Additional movie metadata scraped from IMDB using the links.csv file.")
    

    if page_selection == "Welcome":
        st.title("Welcome to STREAM-X")
        st.info("Brought to you by ByteNest Labs")
       
        

        st.image('https://cdn.discordapp.com/attachments/1218114105395642428/1225045830063493130/16609E66-49C5-4B70-9315-30AB18D02A03.jpg?ex=661fb3d6&is=660d3ed6&hm=ab1c6ad50f8f8fdf9c64b1958a868d9fa9a463e25be90b54c8a1008e3bd09b65&', width=640)

        st.info("Stream-X is a revolutionary movie recommendation algorithm that caters to the needs of visually impaired customers. By utilizing advanced technology, Stream-X is able to recommend up to 10 movies based on the individual preferences of each user. This algorithm takes into account various factors such as genre, actors, directors, and even user ratings to provide a personalized list of movie recommendations. What sets Stream-X apart from other recommendation algorithms is its accessibility features for visually impaired customers. Through the use of audio descriptions and voice commands, users can easily navigate through the recommended movies and select the ones they are interested in watching. This ensures that visually impaired customers can enjoy a seamless movie-watching experience without any barriers. Stream-X is constantly updating its database with the latest movies and user feedback to provide the most accurate and relevant recommendations. Whether you're in the mood for a comedy, drama, action, or horror movie, Stream-X has got you covered. With its user-friendly interface and innovative features, Stream-X is changing the way visually impaired customers discover and enjoy movies. Say goodbye to endless scrolling and indecision, and let Stream-X do the work for you.")
    
    
    if page_selection == "EDA":
        
        st.title("Exploratory Data Analysis (EDA)")
        st.info("Visual Insights into the Dataset")
        
         # Placeholder for images
        image_paths = [
            "resources/imgs/bargraph.png",
            "resources/imgs/bargraph2.png",
            "resources/imgs/bargraph3.png",
            "resources/imgs/bargraph4.png"
        ]

        # Load and display the EDA images with explanations
        for i, image_path in enumerate(image_paths):
            st.image(image_path, caption=f"EDA Image {i+1}", use_column_width=True)
            # Provide explanations for each graph
            if i == 0:
                st.write("1. Documentary stands out as the most abundant genre, with the highest bar")
                st.write("2.Genres like Western and Documentary have significantly lower bars, indicating less content availability or popularity")
            elif i == 1:
                st.write("We observed a decrease in the movies published per year from 2000 Recommendations: It is not clear what accounts for the decrease in movies published but possible reasons for this change include the financial crisis in 2000 and in 2009.")   
            elif i == 2:
                st.write("We can observe that there aren't any signifigant positive correlations amongst the features , aside from timestamp and movieId There is a very clear correlation between movieId and timestamp, this is possibly because movies have different lengths and do not end at exactly the same time.") 
            elif i == 3:
                st.write("This is a line graph which shows the Top 10 high budget movies of which My Way is the Top budget Movie.") 
    
    
            
    if page_selection == "About":
        st.title("Problem Statement")
        st.markdown("""
In today's digital age, where the abundance of movie content makes it challenging for viewers to navigate through endless options, recommender systems play a vital role in enhancing user experience and driving engagement.

Companies like Netflix, Amazon Prime, and Disney leverage sophisticated algorithms to provide personalized movie recommendations tailored to individual preferences. These recommendations are not arbitrary but are based on user behavior and historical preferences.
""")
        st.title("COMPANY INFORMATION")
        st.info("---- This app is developed by ByteNest Pty.ltd ----")
        st.info("Since ---- 05/ November/ 2018 ----")
        
        st.info("Byte Nest, a company founded in November 2018, is a hub for data scientists looking to push the boundaries of technology. Specializing in software architecture, machine learning, and web development, Byte Nest offers a wide range of technical services to meet the needs of its clients. With a team of skilled and experienced professionals, Byte Nest prides itself on staying ahead of the curve in the ever-evolving world of data science. From designing cutting-edge software systems to implementing complex machine learning algorithms, the experts at Byte Nest are dedicated to delivering top-notch solutions that drive innovation and success. At Byte Nest, collaboration is key. The company fosters a culture of teamwork and creativity, encouraging its employees to think outside the box and explore new ideas. By working together to solve complex problems and tackle challenging projects, the team at Byte Nest is able to deliver exceptional results that exceed expectations. One of the core values at Byte Nest is a commitment to excellence. The company is dedicated to providing its clients with the highest quality services and products, ensuring that every project is completed to the highest standards. By maintaining a focus on quality and attention to detail, Byte Nest has earned a reputation as a trusted partner in the world of data science. As technology continues to advance at a rapid pace, the need for skilled data scientists has never been greater. With its focus on software architecture, machine learning, and web development, Byte Nest is well-positioned to meet the growing demand for innovative solutions in the field of data science. By staying at the forefront of technology and embracing new challenges, Byte Nest is poised to lead the way in shaping the future of data science")
        st.title("Meet the team")
        st.markdown("<span style='color: #ff5733; font-size: 32px'><strong><em>BYTENEST</em></strong></span>", unsafe_allow_html=True)

         # Adding an image
        image_paths = ['resources/imgs/godfrey.jpg', 'resources/imgs/sethu.jpg', 'resources/imgs/mp.jpg', 'resources/imgs/confi.jpg', 'resources/imgs/onka.jpg', 'resources/imgs/ayanda.jpg' ]
        st.image(image_paths, caption=['Godfrey', 'Siphosethu', 'Mpho', 'Confidence', 'Onkarabile', 'Ayanda'], use_column_width=True, width=300)
    
        
    if page_selection == "Your Feedback":
        st.title("Feedback")
        st.write("We would appreciate your ratings")

        # Create a slider for rating
        rating = st.slider("Rate our service", min_value=1, max_value=5, step=1)

        # Get feedback from the user
        feedback = st.text_area("Please provide your feedback here:")

        # Save feedback to a file or database when submitted
        if st.button("Submit Feedback"):
            save_feedback(rating, feedback)
            st.success("Thank you for your feedback!")

def save_feedback(rating, feedback):
    with open("feedback.txt", "a") as file:
        file.write(f"Rating: {rating}, Feedback: {feedback}\n")
 


if __name__ == '__main__':
    main()
