import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv('Data/admission_data.csv')
    return df

df = load_data()

def show_exp_page():
    st.title('Exploratory Data Analysis')

    
    st.subheader('Boxplots for dataset features')
    fig1, ax1 = plt.subplots(3,2, figsize=(18, 18))

    for ax in ax1:
        for ax in ax:
            ax.set(
            axisbelow=True,  # Hide the grid behind plot objects
            ylabel='Distribution',
            xlabel='Value',
            )
            ax.xaxis.grid(True),

    ax1[0,0].boxplot(df['GRE Score'],patch_artist = True, notch ='True', vert = 0)
    ax1[0,0].set_title('GRE')

    ax1[0,1].boxplot(df['TOEFL Score'],patch_artist = True, notch ='True', vert = 0)
    ax1[0,1].set_title('TOEFL Score')

    ax1[1,0].boxplot(df['University Rating'],patch_artist = True, notch ='True', vert = 0)
    ax1[1,0].set_title('University Rating')

    ax1[1,1].boxplot(df['SOP'],patch_artist = True, notch ='True', vert = 0)
    ax1[1,1].set_title('SOP')

    ax1[2,0].boxplot(df['LOR '],patch_artist = True, notch ='True', vert = 0)
    ax1[2,0].set_title('LOR')

    ax1[2,1].boxplot(df['Chance of Admit '],patch_artist = True, notch ='True', vert = 0)
    ax1[2,1].set_title('Chance of Admit')

    st.pyplot(fig1)
    st.subheader('Histograms for dataset features')
    fig2, ax2 = plt.subplots(3,2, figsize=(15, 15))
    plt.tight_layout()


    ax2[0,0].hist(df['GRE Score'],color = ['lightblue'])
    ax2[0,0].set_title('GRE')

    ax2[0,1].hist(df['TOEFL Score'],color = ['lightblue'])
    ax2[0,1].set_title('TOEFL Score')

    ax2[1,0].hist(df['University Rating'],color = ['lightblue'])
    ax2[1,0].set_title('University Rating')

    ax2[1,1].hist(df['SOP'],color = ['lightblue'])
    ax2[1,1].set_title('SOP')

    ax2[2,0].hist(df['LOR '],color = ['lightblue'])
    ax2[2,0].set_title('LOR')

    ax2[2,1].hist(df['Chance of Admit '],color = ['lightblue'])
    ax2[2,1].set_title('Chance of Admit')
    st.pyplot(fig2)

    st.subheader('Features correlation matrix')
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(9, 7))
    ax = sns.heatmap(corr,mask=mask,square=True,annot=True,fmt='0.2f',linewidths=.8,cmap="hsv")
    st.pyplot(f)