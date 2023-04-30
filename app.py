import streamlit as st
import plotly.express as px

df = px.data.tips()
st.set_page_config(
    layout='wide',
    page_title='Dash board',
    page_icon='💰'

)



page = st.sidebar.radio('Select Page', ['Dataset Overview', 'Describtive Statistics', 'Charts'])

if page == 'Dataset Overview':
    st.write('<h1 style = "text-align: center; color: GoldenRod;">Tips DashBoard</h1>',unsafe_allow_html=True)
    space1, col, space2 = st.columns([2, 4, 2])
    col.dataframe(df, width=600, height=700)
elif page == 'Describtive Statistics':
    col1, space, col2 = st.columns([5,1, 5])
    with col1:
        with st.container():
            space, col, space2 = st.columns([1, 2, 1])
            sun = df[df['day'] == 'Thur']['total_bill'].mean()
            sat = df[df['day'] == 'Fri']['total_bill'].mean()
            col.metric('Average bills of Trus', round(sun, 2), round(sun - sat, 2))
        st.dataframe(df.describe(include='number'), width= 350, height=200)
    with col2:
        with st.container():
            spac, col, spac2 = st.columns([1, 2, 1])
            thur = df[df['day'] == 'Thur']['total_bill'].mean()
            fri = df[df['day'] == 'Fri']['total_bill'].mean()
            col.metric('Average bills of firday'.title(), round(fri, 2), round(fri - thur, 2))
        st.dataframe(df.describe(include='O'), width=350, height=200)
        
elif page == 'Charts':
    tab1, tab2 = st.tabs(['UniVariate', 'BiVariate'])
    with tab1:
        with st.container():
            space, col, space2 = st.columns([3, 4, 3])
            col_name = col.selectbox('select Column to show its distribution'.title(), df.columns)
        if col_name in df.select_dtypes(include='number'):
            col1, space, col2 = st.columns([5, 3, 5])
            fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                title=f'{col_name} hist distibution', width=550)
            fig2 = px.box(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Bold,
                          title=f'{col_name} boxplot distibution',width =  550)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2)
        else:
            col1, space, col2 = st.columns([5, 2, 5])
            fig1 = px.histogram(df, x = col_name, color_discrete_sequence=px.colors.qualitative.Antique,
                                title=f'{col_name} hist distibution', width=550)
            fig2 = px.pie(df, names = col_name, color_discrete_sequence=px.colors.qualitative.Bold, hole= 0.3,
                          title=f'{col_name} boxplot distibution',width =  550)
            col1.plotly_chart(fig1)
            col2.plotly_chart(fig2)
        with tab2:
            col1, space, col2 = st.columns([5,2,5])
            with col1:
                fig = px.histogram(df, x = 'total_bill', color = 'sex',
                                   color_discrete_sequence=px.colors.qualitative.Antique, width=550,
                                  title='total_bill distibution separated to each gender')
                st.plotly_chart(fig)
                fig2 = px.scatter(df, x = 'total_bill', y = 'tip',color='day', size = 'size', size_max = 40,
                                  color_discrete_sequence = px.colors.qualitative.Antique, width=550,
                                 title='correlation between tips and total bill according to each day')
                st.plotly_chart(fig2)
            with col2:
                fig = px.sunburst(df, path=['day', 'time', 'sex'], color_discrete_sequence=px.colors.qualitative.Antique,
                                 width=550)
                st.plotly_chart(fig)
                fig2 = px.histogram(df, x='day', y='total_bill', color='time', histfunc='sum',
                                   color_discrete_sequence = px.colors.qualitative.Antique, width=550)
                st.plotly_chart(fig2)
