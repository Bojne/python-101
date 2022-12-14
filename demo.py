import streamlit as st 
from time import time, ctime
import random
from datetime import datetime


t = time()
st.title(ctime(t))
st.button('Refresh')

# A list of the emoji we want to randomize.
colorful_emoji_list = ['๐ป', '๐', 'โ๏ธ', '๐', '๐ฅ', '๐ฅ', '๐', '๐ฏ','โค๏ธ', '๐น', '๐', '๐', '๐', '๐ถ', '๐', '๐น','๐', '๐ฅ', '๐', '๐ง', '๐', '๐', '๐', '๐','๐', '๐ฆ', '๐ฌ', '๐ฆ', '๐', '๐', '๐', 'โ๏ธ','๐', '๐ฆ', '๐ฆ', '๐', '๐', '๐', '๐งก', '๐ฅ','๐', '๐พ', 'โ๏ธ', '๐', '๐', '๐ฎ', '๐', '๐บ','๐คข', '๐ธ', '๐ฆ', '๐', '๐', '๐พ', '๐', '๐ฅ']
human_emoji_list =  ['๐ฉโ๐ป','๐ฉ๐ปโ๐ป','๐ฉ๐ฝโ๐ป','๐ฉ๐ผโ๐ป','๐ฉ๐พโ๐ป','๐ฉ๐ฟโ๐ป','๐จโ๐ป','๐จ๐ปโ๐ป','๐จ๐ผโ๐ป','๐จ๐ฝโ๐ป','๐จ๐พโ๐ป','๐จ๐ฟโ๐ป']


# Randomize the list (in place).
random.shuffle(colorful_emoji_list)

st.title(" ".join(colorful_emoji_list[:13]))

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Time", "Coder Generation", "Youtube/Image", 'Plot', "Map"])

with tab1: 
    from datetime import datetime
    bday_date = st.date_input('Your birthday')
    countdown = bday_date - datetime.now().date()
    st.text("โฐ " + str(countdown.days) + " days until your ๐ ")
    st.code("""with tab1:
    from datetime import datetime
    bday_date = st.date_input('Your birthday')
    countdown = bday_date - datetime.now().date()
    st.text("โฐ " + str(countdown.days) + " days until your ๐ ")
    """)
 
with tab2: 
    import numpy
    import random
    size = st.slider('้ธไธๅๆธๅญ', 1, 100) 
    repeated = numpy.repeat(colorful_emoji_list, size)
    random.shuffle(repeated)
    long_emoji_string = ''.join(repeated)
    st.subheader(long_emoji_string)
    st.code("""
    with tab2:
    import numpy
    import random 
    size = st.slider('Pick a number', 1, 100) 
    repeated = numpy.repeat(human_emoji_list, size)
    random.shuffle(repeated)
    long_emoji_string = ''.join(repeated)
    st.subheader(long_emoji_string)
        """)

with tab3: 
    video_input = st.text_input('Youtube Link', 'https://www.youtube.com/watch?v=4cNWtOaGMgI')
    st.video(video_input)
    img_input = st.text_input('Image/GIF Link', 'https://media.giphy.com/media/Jbb3KS22397YQ/giphy.gif')
    st.image(img_input)
    st.code("""with tab3: 
    video_input = st.text_input('Youtube Link', 'https://www.youtube.com/watch?v=4cNWtOaGMgI')
    st.video(video_input)
    img_input = st.text_input('Image/GIF Link', 'https://media.giphy.com/media/Jbb3KS22397YQ/giphy.gif')
    st.image(img_input)""")

    st.markdown('[![Star History Chart](https://api.star-history.com/svg?repos=streamlit/streamlit&type=Date)](https://star-history.com/#streamlit/streamlit&Date)')

with tab4: 
    import plotly.graph_objects as go
    import pandas as pd
    # Read data from a csv
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    fig = go.Figure(data=[go.Surface(z=z_data.values)])
    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    width=700, height=700,
                    margin=dict(l=65, r=50, b=65, t=90))

    st.plotly_chart(fig, sharing='streamlit')


with tab5:
    df = pd.DataFrame(
    numpy.random.randn(1000, 2) / [50, 50] + [25.0330, 121.5654],
    columns=['lat', 'lon'])
    st.map(df)



st.markdown("""
[![website](https://github.com/codeSTACKr/codeSTACKr/raw/master/img/instagram-light.svg)](https://instagram.com/yuehan__)
""")

# st.checkbox('I agree')
# st.radio('Pick one', ['cats', 'dogs'])
# st.selectbox('Pick one', ['cats', 'dogs'])
# st.multiselect('Buy', ['milk', 'apples', 'potatoes'])

# st.select_slider('Pick a size', ['S', 'M', 'L'])
# st.text_input('First name')
# st.number_input('Pick a number', 0, 10)
# st.text_area('Text to translate')
# st.time_input('Meeting time')
# st.file_uploader('Upload a CSV')
# st.camera_input("Take a picture")
# st.color_picker('Pick a color')

