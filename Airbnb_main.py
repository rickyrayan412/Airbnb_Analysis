import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


# Streamlit part

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: #FF5A5F;'>Airbnb Analysis</h1>", unsafe_allow_html=True)
st.write("")

def datafr():
    df= pd.read_csv(r"C:\Users\Admin\Downloads\GUVI_Python\Airbnb\Airbnb.csv")
    return df

df= datafr()

select = option_menu(
    menu_title = None,
    options = ["Home","Data Exploration"],
    icons =["house","bar-chart"],
    default_index=0,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "Lightgreen","size":"cover", "width": "200"},
        "icon": {"color": "black", "font-size": "25px"},
            
        "nav-link": {"font-size": "25px", "text-align": "center", "margin": "-2px", "--hover-color": "#00A699"},
        "nav-link-selected": {"background-color": "#FF5A5F",  "font-family": "YourFontFamily"}})

st.markdown("<hr style='border: 2px solid #FF5A5F;'>", unsafe_allow_html=True)

if select == "Home":
    col1,col2,col3= st.columns(3)
    with col2:
        img1 = Image.open(r"C:\Users\Admin\Downloads\GUVI_Python\Airbnb\airbnb.png")
        st.image(img1, width=450)
        st.write("")

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header(":globe_with_meridians: Domain :")
        st.write("- **Travel Industry**")
        st.write("- **Property Management**")
        st.write("- **Tourism**")
    with col2:
        st.header(":desktop_computer: Technologies Used :")
        st.write("- **Github Cloning**")
        st.write("- **Python**")
        st.write("- **Pandas**")
        st.write("- **streamlit**")
        st.write("- **plotly**")
        st.write("- **Matplotlib**")
        st.write("- **Seaborn**")
        st.write("- **MongoDB**")
        
    with col3:        
        st.header(":page_with_curl: About this Project")
        st.write("- **Data Collection**")
        st.write("- **Data Cleaning and Preprocessing**")
        st.write("- **Exploratory Data Analysis (EDA)**")
        st.write("- **Visualization**")
        st.write("- **plotly**")
        st.write("- **Geospatial Analysis**")
        
    st.markdown("<hr style='border: 2px solid #FF5A5F;'>", unsafe_allow_html=True)  

    col1,col2,col3 = st.columns(3)
    with col2:
        st.header(":dart: About Airbnb")
    col1,col2 = st.columns(2)
    with col1:
        st.write('''**Airbnb is an online marketplace that connects people who want to rent out
                  their property with people who are looking for accommodations,
                  typically for short stays. Airbnb offers hosts a relatively easy way to
                  earn some income from their property.Guests often find that Airbnb rentals
                  are cheaper and homier than hotels.**''')
        st.write('''**Airbnb was born in 2007 when two Hosts welcomed three guests to their
                  San Francisco home, and has since grown to over 4 million Hosts who have
                    welcomed over 1.5 billion guest arrivals in almost every country across the globe.**''') 
    with col2:
        st.write('''**Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                      The company provides a mobile application (app) that enables users to list,
                      discover, and book unique accommodations across the world.
                      The app allows hosts to list their properties for lease,
                      and enables guests to rent or lease on a short-term basis,
                      which includes vacation rentals, apartment rentals, homestays, castles,
                      tree houses and hotel rooms. The company has presence in China, India, Japan,
                      Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                      Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                      Airbnb is headquartered in San Francisco, California, the US.**''')
      

if select == "Data Exploration":

    select = option_menu(
    menu_title = None,
    options = ["Pricing","Availability","Location Based","Geospatiality","Top Insights"],
    icons = ["credit-card", "calendar-check", "compass", "globe-americas", "exclamation-triangle"],
    default_index=0,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "Lightgreen","size":"cover", "width": "200"},
        "icon": {"color": "black", "font-size": "25px"},
            
        "nav-link": {"font-size": "25px", "text-align": "center", "margin": "-2px", "--hover-color": "#00A699"},
        "nav-link-selected": {"background-color": "#FF5A5F",  "font-family": "YourFontFamily"}})

    if select == "Pricing":
        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>Price Difference</h2>", unsafe_allow_html=True)
        col1,col2= st.columns(2)

        with col1:
             
            country= st.selectbox("**Select the Country**",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("**Select the Room Type**",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        
        with col2: 
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_ty= st.selectbox("**Select the Property_type**",df2["property_type"].unique())

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)
        with col1:
            hostresponsetime = st.selectbox("**Select the host_response_time**", df4["host_response_time"].unique())

            df5 = df4[df4["host_response_time"] == hostresponsetime]
            
            df_do_bar = pd.DataFrame(df5.groupby("bed_type")[["minimum_nights", "maximum_nights", "price"]].sum())
            df_do_bar.reset_index(inplace=True)
            
            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'],
                                title='MINIMUM NIGHTS AND MAXIMUM NIGHTS', hover_data=['price'],
                                barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            
            st.plotly_chart(fig_do_bar)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2 = pd.DataFrame(df5.groupby("bed_type")[["bedrooms", "beds", "accommodates", "price"]].sum())
            df_do_bar_2.reset_index(inplace=True)
            
            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
                                  title='BEDROOMS AND BEDS ACCOMMODATES', hover_data=['price'],
                                  barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=600, height=500)
                       
            st.plotly_chart(fig_do_bar_2)

    if select == "Availability":

        def datafr():
            df_a= pd.read_csv(r"C:\Users\Admin\Downloads\GUVI_Python\Airbnb\Airbnb.csv")
            return df_a

        df_a= datafr()

        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>Availability Analysis</h2>", unsafe_allow_html=True)

        col1,col2= st.columns(2)
        with col1:            
            country_a= st.selectbox("**Select the Country_a**",df_a["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            property_ty_a= st.selectbox("**Select the Property Type**",df1_a["property_type"].unique())
            
            df2_a= df1_a[df1_a["property_type"] == property_ty_a]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
            st.plotly_chart(df_a_sunb_30)
        
        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)
        with col1:
            
            df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_a_sunb_365)
            
        col1,col2 = st.columns(2)
        with col1:
            roomtype_a = st.selectbox("**Select the Room Type_a**", df2_a["room_type"].unique())

        df3_a = df2_a[df2_a["room_type"] == roomtype_a]
        
        df_mul_bar_a = pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30", "availability_60", "availability_90", "availability_365", "price"]].sum())
        df_mul_bar_a.reset_index(inplace=True)
        
        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
                                  title='AVAILABILITY BASED ON HOST RESPONSE TIME', hover_data=['availability_30', 'availability_60', 'availability_90', "availability_365"],
                                  barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
        
        st.plotly_chart(fig_df_mul_bar_a)


    if select == "Location Based":

        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>Location Analysis</h2>", unsafe_allow_html=True)
        st.write("")

        def datafr():
            df= pd.read_csv(r"C:\Users\Admin\Downloads\GUVI_Python\Airbnb\Airbnb.csv")
            return df

        df_l= datafr()

        col1,col2 = st.columns(2)
        with col1:
            country_l= st.selectbox("**Select the Country_l**",df_l["country"].unique())

        df1_l= df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        col1,col2 = st.columns(2)
        with col1:
            proper_ty_l= st.selectbox("**Select the Property_type_l**",df1_l["property_type"].unique())

        df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):

                df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop= True, inplace= True)
                return df_val_30

            elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
            
                df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop= True, inplace= True)
                return df_val_60_1
            
            elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):

                df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop= True, inplace= True)
                return df_val_100
            
        differ_max_min= df2_l['price'].max()-df2_l['price'].min()

        val_sel= st.radio("**Select the Price Range**",[str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                    
                                                    str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),

                                                    str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])
                                          
        df_val_sel= select_the_df(val_sel)

        st.dataframe(df_val_sel)

        # checking the correlation

        df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                            "room_type", "bed_type","cancellation_policy",
                                            "images","host_url","host_name", "host_location",                   
                                            "host_response_time", "host_thumbnail_url",            
                                            "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                            "host_picture_url","host_neighbourhood",
                                            "host_identity_verified","host_verifications",
                                            "street", "suburb", "government_area", "market",                        
                                            "country", "country_code","location_type","is_location_exact",
                                            "amenities"]).corr()
        
        st.dataframe(df_val_sel_corr)

        df_val_sel_gr = pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee", "bedrooms", "beds", "extra_people"]].sum())
        df_val_sel_gr.reset_index(inplace=True)
        
        fig_1 = px.bar(df_val_sel_gr, x="accommodates", y=["cleaning_fee", "bedrooms", "beds"], title="ACCOMMODATES",
                       hover_data=["cleaning_fee", "bedrooms", "beds"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
        st.plotly_chart(fig_1)
        
        col1,col2 = st.columns(2)
        with col1:
            room_ty_l= st.selectbox("**Select the Room_Type_l**", df_val_sel["room_type"].unique())

        df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                    hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1200)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                    hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1200)
        st.plotly_chart(fig_3)


    if select == "Geospatiality":

        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>Geospatial Visualization</h2>", unsafe_allow_html=True)
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1600,height=800,title='Geospatial Distribution of Listings')
        fig_4.update_traces(hovertemplate='<b>%{hovertext}</b><br>' +
                                  'Price: $%{marker.color:.2f}<br>' +
                                  'Accommodates: %{marker.size}<br>' +
                                  'Latitude: %{lat}<br>' +
                                  'Longitude: %{lon}<extra></extra>')
        st.plotly_chart(fig_4) 


    if select == "Top Insights":
        st.markdown("<h2 style='text-align: center; color: #FF5A5F;'>Top Insights</h2>", unsafe_allow_html=True)
        
        col1,col2 = st.columns(2)
        with col1:
            country_t= st.selectbox("**Select the Country_t**",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        col1,col2 = st.columns(2)
        with col1:
            property_ty_t= st.selectbox("**Select the Property_type_t**",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        col1,col2 = st.columns(2)
        with col1:
            room_type_t= st.selectbox("**Select the Room_Type_t**",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)

