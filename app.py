
# the app is built to mainly explore data on a web browser available for each aims-cameroon student...
# name of app: AIMS-instat
import streamlit as st
import os
from os.path import splitext
#now we import vizualization packages and exploratory packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
from io import BytesIO, StringIO
#defining the main function:
STYLE="""
<style>
img {
    max-width: 100%;
}
</style>
"""
st.image("aimsHeader.PNG", use_column_width=True)
st.set_option('deprecation.showPyplotGlobalUse', False)
def uploader():
    # I start by defining a data uploader file to load our data
    file=st.file_uploader("Upload file of type csv ",type=["csv"])
    show_file=st.empty()
    if not file:
        show_file.info("Please upload a file:{} ".format(', '.join(["csv"])))
        return
    content__=file.getvalue()
    #if file.type=='csv':
    data=pd.read_csv(file)
    #st.dataframe(data.head(10))
    #file.close()
    return data
def main():
    st.title("AIMS DATA ANALYSIS WEB APP V1.0")
    #"""Run this function to display the streamlit app"""
    # I start by defining a data uploader:
    #st.info(__doc__)
    #st.markdown(STYLE,unsafe_allow_html=True)
    data=uploader()
    if st.checkbox("Show Dataset"):
        number=int(st.number_input('Number of rows to view',value=1))
        st.dataframe(data.head(number))
    #shozing columns names
    if st.button("Column Names"):
        st.write(data.columns)
    #showing shape of dataset by rows and by columns
    if st.checkbox("Shape of Dataset"):
        st.write(data.shape)
        data_dim=st.radio("Show Dimension By",("Rows","Columns"))
        if data_dim=="Columns":
            st.text("Number of Columns")
            st.write(data.shape[1])
        elif data_dim=="Rows":
            st.text("Number of Rows")
            st.write(data.shape[0])
        else:
            st.write(df.shape)
    #Select columns
    if st.checkbox("Select Column To Show"):
        all_columns=data.columns.tolist()
        selected_columns=st.multiselect("Select",all_columns)
        new_df=data[selected_columns]
        st.dataframe(new_df)

    #Show Values
    if st.button("Value Counts"):
        st.text("Value Counts By Target/Class")
        st.write((data.iloc[:,-1]).value_counts())
    #Show Datatypes
    if st.button("Data Types"):
        st.write(data.dtypes)
    fig, ax = plt.subplots()
    #ax.scatter([1, 2, 3], [1, 2, 3])
    #st.pyplot(fig)
    #Data summary
    if st.checkbox("Data Summary"):
        st.write(data.describe())

    #Data vizualization
    st.subheader("Customizable Plot")
    if st.checkbox("Univariate Analysis"):
        all_columns_names=data.columns.tolist()
        type_of_plot=st.selectbox("Select Type of Plot",["area","bar","line","hist","box"])
        selected_columns_names=st.multiselect("Selected Columns To Plot on x-axis",all_columns_names)
    if st.checkbox("Bivariate Analysis"):
        all_columns_names=data.columns.tolist()
        col1=st.selectbox('which feature on x?',data.columns[:])
        col2=st.selectbox('which feature on y?', data.columns[:])
    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))
    #Plot by streamlit
        if type_of_plot=="area":
            cust_data=data[selected_columns_names]
            st.area_chart(cust_data)
            #st.pyplot()
        elif type_of_plot=="bar":
            cust_data=data[selected_columns_names]
            st.bar_chart(cust_data)
            #st.pyplot()
        elif type_of_plot=="line":
            cust_data=data[selected_columns_names]
            st.line_chart(cust_data)
        elif type_of_plot=="hist":
            cust_plot=data[selected_columns_names]#.plot(kind=type_of_plot)
            cust_plot.hist()
            #plt.show()
            st.pyplot()
        elif type_of_plot=="box":
            cust_data=data[selected_columns_names].plot(kind=type_of_plot)
            #ax.scatter(cust_data)
            st.write(cust_data)
            st.pyplot()
    #correlation plot with seaborn
    if st.checkbox("correlation Plot[Seaborn]"):
        st.write(sns.heatmap(data.corr(),annot=True))
        st.pyplot()

    #


main()
#
#    st.subheader("AIMS-INSTAT")
#    html_temp=""
