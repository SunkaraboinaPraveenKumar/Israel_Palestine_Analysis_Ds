import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title("Upload dataset")

upload_file = st.sidebar.file_uploader("Choose CSV File", type='csv')

def nationality_incident(df):
    nationalityIncident = df.groupby('citizenship').size().reset_index(name='incident_count')
    return nationalityIncident


if upload_file is not None:
    df = pd.read_csv(upload_file)
    no_event = len(df)
    citizenship_counts = df['citizenship'].value_counts()
    event_location_region = df['event_location_region'].value_counts()
    hostilities_counts = df[df['took_part_in_the_hostilities'] == 'Yes']['citizenship'].value_counts()
    no_hostilities_counts = df[df['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()

    st.sidebar.write("No of Events : ", no_event)

    col1, col2, col3, col4 = st.sidebar.columns(4)
    with col1:
        st.sidebar.subheader('citizenship_counts')
        st.sidebar.write(citizenship_counts)

    with col2:
        st.sidebar.subheader('event_location_region')
        st.sidebar.write(event_location_region)

    with col3:
        st.sidebar.subheader('hostilities_counts')
        st.sidebar.write(hostilities_counts)

    with col4:
        st.sidebar.subheader('no_hostilities_counts')
        st.sidebar.write(no_hostilities_counts)

    weapons_counts = df['ammunition'].value_counts()
    st.sidebar.write("Weapon Counts : ", weapons_counts)

    # Data Analysis part
    st.title("Israel Palestine Conflict Analysis")
    st.write("Data Sample", df.head(100))

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Types of Injuries")
        type_of_injury = df['type_of_injury'].value_counts()
        st.bar_chart(type_of_injury)

    with col2:
        st.subheader("Gender Count")
        gender_count = df['gender'].value_counts()
        st.bar_chart(gender_count, color='#FF0000')

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age Summary")
        age = df['age'].describe()
        st.write(age)
    with col2:
        st.subheader("Event Location Region Count")
        event_region = df['event_location_region'].value_counts()
        st.bar_chart(event_region)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Residence Percentage by Region")
        residence_count_by_reg = df.groupby('event_location_region')['place_of_residence'].nunique()
        fig, ax = plt.subplots()
        ax.pie(residence_count_by_reg, labels=residence_count_by_reg.index, autopct='%1.1f%%')
        st.pyplot(fig)

    with col2:
        st.subheader("Type Injury Analysis")
        type_of_injury = df['type_of_injury'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(type_of_injury, labels=type_of_injury.index, autopct='%1.1f%%')
        st.pyplot(fig)

    region_avg_age = df.groupby('event_location_region')['age'].mean()
    st.subheader("Avg Age by Region")
    st.bar_chart(region_avg_age)

    col1, col2 = st.columns(2)
    with col1:
        Incident_CountBy_region = df.groupby('citizenship').size().reset_index(name='incident_count')
        st.subheader('Incident Count by Nationality')
        st.write(Incident_CountBy_region)

    with col2:
        Gender_Inc = df.groupby('gender').size().reset_index(name='incident_count')
        st.subheader('Incident Count by Gender')
        st.write(Gender_Inc)

    # Time-based Analysis of events

    df['date_of_event'] = pd.to_datetime(df['date_of_event'])
    df['year'] = df['date_of_event'].dt.year
    df['month'] = df['date_of_event'].dt.month
    time_events = df.groupby(['year', 'month']).size().reset_index(name='incident_count')
    time_events['year_month'] = time_events['year'].astype(str) + '-' + time_events['month'].astype(str)

    st.subheader('Time-Based Events')
    st.line_chart(time_events.set_index('year_month')['incident_count'])





