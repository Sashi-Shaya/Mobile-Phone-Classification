import streamlit as st
import numpy as np
import pickle

# Load saved pickled model
pickle_model = pickle.load(open('A:/ML_Projects/ML_Project_02/Web_App/phone_classification.pkl','rb'))

# Creating prediction function
def mobile_price_classification(input_data):
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = pickle_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "Lower Cost Phone"
    elif prediction[0] == 1:
        return "Medium Cost Phone"
    elif prediction[0] == 2:
        return "High Cost Phone"
    else:
        return "Very High Cost Phone"

def main():
    # Center the title using Markdown with HTML
    st.markdown("<h1 style='text-align: center;'>SmartPriceTag</h1>", unsafe_allow_html=True)

    # Get input data from the user
    battery_power = st.text_input("Battery Power (mAh)")
    blue = st.selectbox("Has Bluetooth?", options=["No", "Yes"]) 
    clock_speed = st.text_input("Clock Speed (GHz)")
    dual_sim = st.selectbox("Has Dual SIM?", options=["No", "Yes"])  
    fc = st.text_input("Front Camera (MP)")
    four_g = st.selectbox("Has 4G?", options=["No", "Yes"])
    int_memory = st.text_input("Internal Memory (GB)")
    m_dep = st.text_input("Mobile Depth (cm)")
    mobile_wt = st.text_input("Mobile Weight (g)")
    n_cores = st.text_input("Number of Cores")
    pc = st.text_input("Primary Camera (MP)")
    px_height = st.text_input("Pixel Resolution Height")
    px_width = st.text_input("Pixel Resolution Width")
    ram = st.text_input("RAM (MB)")
    sc_h = st.text_input("Screen Height (cm)")
    sc_w = st.text_input("Screen Width (cm)")
    talk_time = st.text_input("Talk Time (hours)")
    three_g = st.selectbox("Has 3G?", options=["No", "Yes"])  
    touch_screen = st.selectbox("Has Touch Screen?", options=["No", "Yes"])  
    wifi = st.selectbox("Has WiFi?", options=["No", "Yes"])  

    # Mapping Yes/No selections back to 0 or 1 for processing
    blue_value = 1 if blue == "Yes" else 0
    dual_sim_value = 1 if dual_sim == "Yes" else 0
    four_g_value = 1 if four_g == "Yes" else 0
    three_g_value = 1 if three_g == "Yes" else 0
    touch_screen_value = 1 if touch_screen == "Yes" else 0
    wifi_value = 1 if wifi == "Yes" else 0
    
    # Code for predictions
    price_classification = ''

    # Button to classify mobile phone price
    if st.button('Get the Price Classification'):
        price_classification = mobile_price_classification([battery_power, blue_value, clock_speed, dual_sim_value, fc, four_g_value, 
                               int_memory, m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, 
                               sc_h, sc_w, talk_time, three_g_value, touch_screen_value, wifi_value])
     
    st.success(price_classification)

if __name__ == '__main__':
    main()
