import os
import requests
import pickle
import sklearn
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header

# Streamlit page custom design
class App:

    def model(self):
        # Setting Page Configuration
        st.set_page_config(page_title="Retail-Sales-Forecast | By Vigneshwaran", layout="wide")
        # Creating the option menu in the sidebar
        with st.sidebar:
            selected = option_menu(
                menu_title="RSF",
                options=["Weeklysales_Prediction",],
                icons=['graph-up-arrow', ''],
                menu_icon='alexa',
                default_index=0
            )

        if selected == "Weeklysales_Prediction":
            col1, col2, col3 = st.columns([4, 10, 2])
            with col2:
                st.markdown(
                    "<h1 style='font-size: 80px;'><span style='color: cyan;'>Weeklysales</span><span style='color: white;'> Prediction</span> </h1>",
                    unsafe_allow_html=True)
            col1, col2, col3 = st.columns([4, 10, 5])
            with col2:
                colored_header(
                    label="",
                    description="",
                    color_name="blue-green-70"
                )
            col1, col2, col3 = st.columns([2, 10, 2])
            # Start from options
            col2.write("")
            with col2:
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 30px;'><span style='color: cyan;'>Day </h1>", unsafe_allow_html=True)
                Day = st.selectbox(' ', [5, 12, 19, 26, 2, 9, 16, 23, 30, 7, 14, 21, 28,
                                     4, 11, 18, 25, 6, 13, 20, 27, 3, 10, 17, 24, 1,
                                     8, 15, 22, 29, 31])
                # ________________________________________________________________________

                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Month </h1>", unsafe_allow_html=True)
                Month = st.selectbox('    ',[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1])
                # ________________________________________________________________________

                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Year </h1>", unsafe_allow_html=True)
                Year = st.selectbox('  ', [2010, 2011, 2012, 2013 ])
                #__________________________________________________________________________

                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Store </h1>", unsafe_allow_html=True)
                Store = st.selectbox('  ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
                                             18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                                             35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45])
                #___________________________________________________________________________

                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Department </h1>", unsafe_allow_html=True)
                Dept = st.selectbox('  ', [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18,19, 20,
                                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,36, 37, 38, 40,
                                            41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56, 58, 59, 60, 67, 71, 72,
                                            74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92, 93, 94, 95, 97, 98, 78, 96, 50,
                                            99, 65, 43, 39, 77])
                #___________________________________________________________________________

                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Type </h1>", unsafe_allow_html=True)
                #TT = {'A':1, 'B':2, 'C':3}
                Type = st.selectbox('', [1, 2, 3])
                #____________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Is_Holiday</h1>", unsafe_allow_html=True)
                # IH = {'False':0, 'True':1}
                IsHoliday = st.selectbox('', [0, 1])
                #____________________________________________________________________________
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Size</h1>", unsafe_allow_html=True)
                Size = st.selectbox('  ', [151315, 202307, 37392, 205863, 34875, 202505, 70713, 155078, 125833, 126512,
                                           207499, 112238, 219622, 200898, 123737,  57197, 93188, 120653, 203819, 203742,
                                           140167, 119557, 114533, 128107, 152513, 204184, 206302, 93638, 42988, 203750,
                                           203007, 39690, 158114, 103681, 39910, 184109, 155083, 196321, 41062, 118221])
                #_______________________________________________________________________________
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Temperature</h1>", unsafe_allow_html=True)
                Temperature = st.number_input('', min_value=-7.29, max_value=101.95, value=42.31,)
                #_______________________________________________________________________________
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Fuel_Price</h1>", unsafe_allow_html=True)
                Fuel_Price = st.number_input('', min_value=2.472, max_value=4.468, value=2.572,)
                #________________________________________________________________________________
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>CPI</h1>",
                            unsafe_allow_html=True)
                CPI = st.number_input('', min_value=126.064, max_value=228.9764563, value=211.096358,)
                #_________________________________________________________________________________
                st.write("")
                st.markdown("<h1 style='font-size: 30px;'><span style='color: cyan;'>Unemployment</h1>",
                            unsafe_allow_html=True)
                Unemployment = st.number_input('', min_value=3.684, max_value=14.313, value=8.106,)
                #__________________________________________________________________________________
                st.write("")
                st.write("")
                #predict_weekly_sales            
                predict_data = [Day, Month, Year, Store, Dept, Type, IsHoliday,
                                Size, Temperature, Fuel_Price, CPI, Unemployment]

                # Load the file ID from environment variables
                model_file_id = os.getenv("MODEL_FILE_ID")
                if not model_file_id:
                    raise ValueError("MODEL_FILE_ID not found in environment variables.")

                # Generate the Google Drive download URL
                model_file_url = f"https://drive.google.com/uc?export=download&id={model_file_id}"

                # Stream the file from Google Drive
                response = requests.get(model_file_url, stream=True)
                if response.status_code != 200:
                   #raise ValueError(f"Failed to download the model file: {response.status_code}")#
                   st.error(f"Failed to download the model file: HTTP {response.status_code}")
                   st.write(response.content.decode())  # Display the content to debug

                # Load the model directly from the response content
                model = pickle.loads(response.content)


            col1, col2, col3 = st.columns([10, 1, 10])

            with col1:
                st.write("")
                if st.button('Process'):
                    x = model.predict([predict_data])
                    st.markdown(
                        f"<h1 style='font-size: 30px;'><span style='color: cyan;'>Predicted Weekly_Sales : </span><span style='color: white;'> {x[0]}</span> </h1>",
                        unsafe_allow_html=True)


# Object
Object = App()
Object.model()