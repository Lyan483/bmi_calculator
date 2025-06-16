import os
import streamlit as st
# import pickle
import pandas as pd

# A Simple BMI Calculator, calculate User BMI and print a user_friendly output with status according to theri BMI.

st.title(" 🧮 BMI Calculator")
st.text("\nDefinition: BMI = weight (kg) ÷ height (m²)")
st.text("It's a numerical value that classifies individuals into categories like underweight,normal weight, overweight, and obese.")
st.subheader("\nCheck You BMI with Status")

#BMI Calculator
def bmi_cal(height_cm, weight): 
    height_m = height_cm/100
    bmi = weight / (height_m**2)

# status checker    
    if bmi < 18.5: 
        user_category ='Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        user_category = 'Normal Weight'
    elif bmi >= 25 and bmi <= 29.9: 
        user_category = 'Overweight'
    elif bmi >= 30 and bmi <= 34.9: 
        user_category = 'Obesity Class I'
    elif bmi >= 35 and bmi <= 39.9: 
        user_category = 'Obesity Class II'
    else:
        user_category = 'Obesity Class III'
    return round(bmi, 2), user_category


# user_input field
user_name = st.text_input('Name: ')
user_age = st.number_input('Age: ', min_value=1, max_value=120, step=1)
height = st.text_input('Height (cm): ')
weight = st.text_input('Weight (kg): ')


#load the previously saved data
# if os.path.exists('bmi_web.pkl'):
#     with open('bmi_web.pkl', 'rb') as f:
#      user_bmi_record = pickle.load(f)
# else:
#     user_bmi_record = []


# run for new user
if st.button("Check My BMI"):
    try:
        height = float(height)
        weight = float(weight)
        if height <= 0 or weight <= 0 :
            raise ValueError
        bmi, status = bmi_cal(height,weight)
        st.write(f" Your BMI is **{bmi}**, it's  means  your are **{status}**. ")

        #record saving  
        # user_bmi_record.append({'Name': user_name.title(), 'Age' : user_age ,'BMI' : bmi , 'Status': status})

        # date pickling
        # with open('bmi_web.pkl', 'wb') as f:
        #     pickle.dump(user_bmi_record, f)
    
        # st.info("Your record has been saved")
    except ValueError:
     st.warning("Invalid Input!, Please provide vaild numeric data to calculate.")

#previous record
# if user_bmi_record:
#     st.subheader("Your Previous Record")
# #    for i, record in enumerate(user_bmi_record, 1):
#     df = pd.DataFrame(user_bmi_record)
#     df.index = range(1, len(df) + 1)
#     st.dataframe(df)


    
# data deletion
# if st.button("Clear My Data"):
#     if os.path.exists('bmi_web.pkl'):
#       os.remove('bmi_web.pkl')
#       user_bmi_record.clear()
#       st.success("Your Data have been cleared Successfully")
#     else:
#         st.warning("We don't have any datat about you!")

#BMI category table
catgeory = [['>18.5', 'Underweight'], ['18.5 - 24.9', 'Normal Weight'],
            ['25.0 - 29.9', 'Overweight'], ['30.0 - 34.9', 'Obesity Class I'],
            ['35.0 - 39.9', 'Obesity Class II'], ['>40', 'Obesity Class III']]
bmi_cat = pd.DataFrame(catgeory, columns = ['BMI', 'Category'])
bmi_cat.index = range(1, len(bmi_cat) + 1)


# BMI info
if st.button("Know About BMI"):
    st.header("What You Should Know About BMI")
    st.subheader('BMI Categories (Adults)\n')
    st.write(bmi_cat)
    st.markdown("\nThese ranges are for adults; different criteria apply to children and teens, " \
    "using age and sex-specific percentiles.")
    st.header('\n⚠️ Limitations of BMI')
    st.markdown('''Doesn't differentiate between muscle and fat (e.g., athletes may have high BMI but low fat). 
                Doesn’t account for fat distribution (e.g., belly fat vs. hip fat).
    \nLess accurate for:
    - Older adults (loss of muscle mass)
    - Very muscular people
    - People from certain ethnic backgrounds (e.g., some Asian populations face health risks at lower BMIs)''')
    st.subheader("🧠 Why It's Still Useful")
    st.markdown('''It's quick, easy, and widely used in public health and clinical settings. 
                It gives a general estimate of whether a person is at risk of weight-related health issues.''')
    st.info('🔍 Browse the Internet for more Information')
