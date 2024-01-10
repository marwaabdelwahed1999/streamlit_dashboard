import streamlit.components.v1 as com
import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd




# page settings
 
st.set_page_config(
    page_title="Bike Sales Dashboard",
    page_icon="images/bicycle.png",
    layout="wide",
)

# dashboard styling css

# page background color 


st.markdown("""
         <style>
        .st-emotion-cache-uf99v8 {
    background-color: black;
    width: 100%;
    padding: 6rem 1rem 10rem;
    min-width: auto;
    max-width: initial;
                          }  
                          
   .st-emotion-cache-vk3wp9 {
           position: relative;
           top: 92px;
           user-select: auto;
           width: 244px;
           height: 742px;
           box-sizing: border-box;
           flex-shrink: 0;
           background-color:#e9bd01 ;
   }               
   
   img {
      border-radius: 50%;
      width: 169px; 
      height: 163px; 
      object-fit: cover; 
      position:relative;
      top: -54px;
      left: 10px;

        }      
       
        .st-emotion-cache-16idsys p{
          font-size: 20px; 
          font-weight: bold;
        }
        
        .st-emotion-cache-1dtefog{
         
          font-weight:bold;
          background-color:#e9bd01
        }
        
        .st-emotion-cache-p5msec{
          position: relative;
          top: -125px; 
              }
              
              .st-cr {
                        background-color: #212529;
                     }
                     
                     .st-cu {
                        background-color: rgb(233 189 1);
                           }


                    .st-ct {
                        color: #000;
                          font-size: 20px; 
                           font-weight: bold;
                    }
                    .st-emotion-cache-1clstc5{
                      position: relative;
                      top: -130px;
                      background-color:black
                    }
                    
                   .st-emotion-cache-5rimss p{
                     font-weight:bold
                   }
                  
                  .st-emotion-cache-ocqkz7{
                    position: relative;
                    top: -115px
                  }
                  
                  .st-emotion-cache-1wivap2{
                     font-weight:bold
                  }
                  
                  .user-select-none svg-container{
                     position: relative;
                     top: -91px;
                     left:-72px
                  }
                  .st-emotion-cache-1wivap2{
                    color: black
                  }
                  
                  .user-select-none svg-container{
                     position: relative;
                     top: -1531px;
                     left:750px
                  }
                  
                  .user-select-none svg-container{
                    position: relative;
                     top: -1523px;
                     left:750px
                  }
                  
                  .user-select-none svg-container{
                    position: relative;
                    top: -905px;
                  }
                  
                  .user-select-none svg-container{
                     position: relative;
                     top: -1432px;
                     left:750px
                  }
                  .user-select-none svg-container{
                     position: relative;
                     top: -1800px;
                  }
                  .user-select-none svg-container{
                      position: relative;
                      right:-1576px

                  }
                  
                  .user-select-none svg-container{
                     position: relative;
                    right:-1854px
                  }
                  
                  .user-select-none svg-container{
                     position: relative;
                     top:-2276px;
                     right:--650px
                  }
                
        </style>
         
         
         """,unsafe_allow_html=True)



# nav_bar start 
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown(""" 
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #e9bd01;position:fixed; top:46px;height:48px">
  <a class="navbar-brand" href="" target="_blank" style= "color: black; font-weight: bold">Bike Sales Analysis Dasboard</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#"> <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://youtube.com/dataprofessor" target="_blank"></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/thedataprof" target="_blank"></a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# nav_bar end 


# dataset 
bikes = pd.read_csv('cleaned_bikes_sales.csv')



# sidebar start 

# sidebar logo image
st.sidebar.image("images/Leonardo_Diffusion_XL_logo_for_bike_sales_company_yello_0.jpg")

# filiters

# Year 
Year = st.sidebar.multiselect(
    label='Year',
    options=bikes['Year'].unique(),
    default=bikes["Year"].unique()

    

)


# Category

Category = st.sidebar.multiselect(
    label='Product Category',
    options=bikes['Product_Category'].unique(),
    default=bikes["Product_Category"].unique()
)


#Country
Country = st.sidebar.multiselect(
    label='Country',
    options=bikes['Country'].unique(),
    default=bikes["Country"].unique()

)

# gender

Gender = st.sidebar.multiselect(
    label='Gender',
    options=bikes['Customer_Gender'].unique(),
    default=bikes["Customer_Gender"].unique()

)

bikes_selection = bikes.query(
    "Year == @Year & Product_Category ==@Category &Country == @Country& Customer_Gender == @Gender"
)

# if bikes_selection.empty:
#     st.warning("No data available based on the current filter settings!")
#     st.stop() # This will halt the app from further execution.

#sidebar end

# display dataset start

def show_data():
  with st.expander('Dataset'):
    showData = st.multiselect('Filiter: ', bikes_selection.columns,default=['Date', 'Day', 'Month', 'Year', 'Customer_Age', 'Age_Group',
'Customer_Gender', 'Country', 'State', 'Product_Category',
'Sub_Category', 'Product', 'Order_Quantity', 'Unit_Cost', 'Unit_Price',
'Profit', 'Cost', 'Revenue', 'Age_Category', 'Age_Range'])
    st.write(bikes_selection[showData])
  
show_data()

# display dataset end

# Kpik's
total_sales = bikes_selection['Order_Quantity'].sum()
total_cost = bikes_selection['Cost'].sum()
total_profit = bikes_selection['Profit'].sum()
total_revenue = bikes_selection['Revenue'].sum()
total_orders_count = len(bikes_selection['Date'])
total1, total2, total3, total4, total5 = st.columns(5, gap='small')

# Define CSS styles
card_style = "background-color: white; color: black; padding: 10px; border: 1px solid yellow; border-radius: 5px; box-shadow: 2px 2px 5px yellow;font-weight:bold;text-align:center"

# Display metrics in each column with Markdown styling and inline CSS
with total1:
    st.markdown(f"<div style='{card_style}'>Total Quantity<br> {total_sales:,.0f}</div>", unsafe_allow_html=True)

with total2:
    st.markdown(f"<div style='{card_style}'>Total Cost<br> $ {total_cost:,.0f}</div>", unsafe_allow_html=True)

with total3:
    st.markdown(f"<div style='{card_style}'>Total Revenue<br> $ {total_revenue:,.0f}</div>", unsafe_allow_html=True)

with total4:
    st.markdown(f"<div style='{card_style}'>Total Profit<br> $ {total_profit:,.0f}</div>", unsafe_allow_html=True)

with total5:
    st.markdown(f"<div style='{card_style}'>Total Orders<br> {total_orders_count:,.0f}</div>", unsafe_allow_html=True)

# graphs

# display total profit by year

yearly_profit = bikes_selection.groupby('Year')['Profit'].sum().reset_index()

# line_color_options = ['#e9bd01', 'red', 'blue', 'green']
# selected_line_color = st.selectbox('Select Line Color', line_color_options, index=0)

fig = px.line(yearly_profit, x='Year', y='Profit',
              markers=True,
              title='Yearly Total Profit',
              labels={'Year': 'Year', 'Profit': 'Profit'},
              line_shape='linear',
              line_dash_sequence=['solid'],
              template='plotly_dark',  
              color_discrete_sequence=['#e9bd01']
              )

fig.update_layout(
    template='plotly_dark',  
    xaxis=dict(showgrid=False), 
    yaxis=dict(showgrid=False),  
    plot_bgcolor='black', 
    title='Profit by Year',
    title_font_size=20,
    title_font_color='white',
    width=500,  
    height=400,  
    margin=dict(l=50, r=50, t=50, b=50),
    paper_bgcolor='black',
    
)


st.plotly_chart(fig)

# Product category distribution 

category_distribution = bikes_selection.groupby('Product_Category')['Order_Quantity'].sum().reset_index()

fig = px.pie(category_distribution, names='Product_Category', values='Order_Quantity', title='Product Category Distribution')

fig.update_layout(
    template='plotly_dark',  
    title_font_size=20,  
    title_font_color='white',  
    width=600,  
    height=400, 
    paper_bgcolor='black',
    plot_bgcolor='black',
    legend=dict(
        title=dict(text='Product Category', font=dict(color='white')),
        traceorder='normal',  
        title_font=dict(color='#e9bd01'),  
        bgcolor='#f3ecec',  
        
    ),
 
)
fig.update_traces(
    marker=dict(colors=['#e9bd01', 'grey', 'white']),
    hovertemplate='<b>%{label}</b><br>%{percent}',
)

st.plotly_chart(fig)

# sales by country 

total_sales_by_country = bikes_selection.groupby('Country')['Order_Quantity'].sum().reset_index()
geojson_data = {
    "type": "FeatureCollection",
    "features": [
        {"type": "Feature", "properties": {"name": "USA"}, "geometry": {"type": "Polygon", "coordinates": [[[-130, 25], [-65, 25], [-65, 50], [-130, 50], [-130, 25]]]}},
        {"type": "Feature", "properties": {"name": "Canada"}, "geometry": {"type": "Polygon", "coordinates": [[[-130, 50], [-65, 50], [-65, 75], [-130, 75], [-130, 50]]]}},
        {"type": "Feature", "properties": {"name": "France"}, "geometry": {"type": "Polygon", "coordinates": [[[2, 42], [8, 42], [8, 51], [2, 51], [2, 42]]]}},
        {"type": "Feature", "properties": {"name": "Australia"}, "geometry": {"type": "Polygon", "coordinates": [[[112, -44], [154, -44], [154, -10], [112, -10], [112, -44]]]}},
        {"type": "Feature", "properties": {"name": "Germany"}, "geometry": {"type": "Polygon", "coordinates": [[8, 47], [14, 47], [14, 55], [8, 55], [8, 47]]}},
        {"type": "Feature", "properties": {"name": "United Kingdom"}, "geometry": {"type": "Polygon", "coordinates": [[-10, 50], [2, 50], [2, 60], [-10, 60], [-10, 50]]}}
    ]
}

fig = px.scatter_geo(
    total_sales_by_country,
    geojson=geojson_data,
    featureidkey="properties.name",
    locations='Country',
    locationmode='country names',
    color='Order_Quantity',  
    size='Order_Quantity',  
    size_max=80,  
    hover_name='Country',
    text='Country',
    template='plotly_dark',
    color_continuous_scale='YlOrBr', 
    projection='natural earth',  
    title='Total Sales by Country',
)

# Customize layout
fig.update_layout(
    geo=dict(bgcolor='black'),  
    paper_bgcolor='black',  
    title_font=dict(size=20, color='white'), 
    width=1100, 
    height=600,  
    coloraxis_showscale=False,

)

st.plotly_chart(fig)



gender_sales_count = bikes_selection.groupby('Customer_Gender')['Order_Quantity'].sum().reset_index()

fig = px.pie(
    gender_sales_count,
    names='Customer_Gender',  
    values='Order_Quantity',   
    template='plotly_dark',  
    title='Distribution of Gender by Sales Count',
    hover_data=['Order_Quantity'],

)

fig.update_traces(
    hovertemplate='%{label}: <b>%{value}</b>',
)



# Customize layout
fig.update_layout(
    paper_bgcolor='black',  
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),  
    font=dict(color='white'), 
    legend=dict(
        title=dict(text='Customer Gender', font=dict(color='white')),
        traceorder='normal',  
        title_font=dict(color='#e9bd01'),  
        bgcolor='#f3ecec',  
        
    ), 
)
fig.update_traces(
    marker=dict(colors=['#e9bd01', 'grey']),
    hovertemplate='<b>%{label}</b><br>%{percent}',
)


st.plotly_chart(fig)

# Age category by sales

age_category_sales = bikes_selection.groupby('Age_Category')['Order_Quantity'].sum().reset_index()
age_category_sales = age_category_sales.sort_values(by='Order_Quantity', ascending=False)

fig = px.bar(
    age_category_sales,
    x='Age_Category',
    y='Order_Quantity',
    template='plotly_dark',  
    title='Age Category Sales',
    labels={'Order_Quantity': 'Total Sales'},  
    color_discrete_sequence=['#e9bd01'],  
)

fig.update_layout(
    paper_bgcolor='black',  
    plot_bgcolor='black',  
    title_font=dict(size=20, color='white'),  
    xaxis_title='Age Category',  
    yaxis_title='Total Sales',  
    font=dict(color='white'),  
    xaxis=dict(showgrid=False),  
    yaxis=dict(showgrid=False),  
)

fig.update_traces(marker=dict(line=dict(width=20)))  


st.plotly_chart(fig)


# Top ten product name by sales 
top_products = bikes_selection.groupby('Product')['Order_Quantity'].sum().reset_index()
top_products = top_products.sort_values(by='Order_Quantity', ascending=True).head(10)

fig_top_products_horizontal = px.bar(
    top_products,
    x='Order_Quantity',
    y='Product',
    title='Top Ten Products by Sales',
    labels={'Order_Quantity': 'Total Sales'},
    color='Order_Quantity',
    color_continuous_scale='YlOrBr',
    orientation='h',
    width= 600,
    height=500
)

# Customize layout
fig_top_products_horizontal.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),
    font=dict(color='white'),  
    coloraxis_showscale=False,
)

st.plotly_chart(fig_top_products_horizontal)

# Top ten sub category by sales 
top_subcategories = bikes_selection.groupby('Sub_Category')['Order_Quantity'].sum().reset_index()

top_subcategories = top_subcategories.sort_values(by='Order_Quantity', ascending=True)

fig_top_subcategories_horizontal = px.bar(
    top_subcategories,
    x='Order_Quantity',
    y='Sub_Category',
    title='Top Ten Subcategories by Sales',
    labels={'Order_Quantity': 'Total Sales'},
    color='Order_Quantity',
    color_continuous_scale='YlOrBr',
    orientation='h',
     width= 600,
     height=500

)

# Customize layout
fig_top_subcategories_horizontal.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),
    font=dict(color='white'),  
    coloraxis_showscale=False,
)

st.plotly_chart(fig_top_subcategories_horizontal)


scatter_fig = px.scatter(
    bikes_selection,
    x='Unit_Price',
    y='Unit_Cost',
    color='Cost',
    color_continuous_scale=['yellow', 'grey'],  # Yellow to Grey color scale
    template='plotly_dark',  # Black background
    title='Unit Price vs.Unit Cost',
    labels={'Cost': 'Cost'},
    width=400
)

# Customize layout
scatter_fig.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),
    font=dict(color='white'),
    xaxis=dict(showgrid=False),  
    yaxis=dict(showgrid=False),  
    coloraxis_colorbar=dict(outlinewidth=0, bordercolor='white'),  
    coloraxis_showscale=False,

)


st.plotly_chart(scatter_fig)



# profit by category

profit_by_category = bikes_selection.groupby('Product_Category')['Profit'].sum().reset_index()

# Define custom colors for each category
custom_colors = ['#e9bd01', 'grey', 'white']

# Donut chart for Profit by Category
donut_fig = px.pie(
    profit_by_category,
    names='Product_Category',
    values='Profit',
    hole=0.4,  # Size of the hole (0.4 means 40% of the center is empty, creating a donut)
    color_discrete_sequence=custom_colors,  # Custom colors for categories
    template='plotly_dark',  # Black background
    title='Profit Distribution by Category',
)

# Customize layout
donut_fig.update_layout(
    paper_bgcolor='black',
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),
    font=dict(color='white'),
    legend=dict(
        bgcolor='#f3ecec',  # Legend background color
        bordercolor='black',  # Legend border color
        borderwidth=1,  # Legend border width
    ),
)

# Display the donut chart using Streamlit
st.plotly_chart(donut_fig)



# yearly revenue 

yearly_revenue = bikes_selection.groupby('Year')['Revenue'].sum().reset_index()

# line_color_options = ['#e9bd01', 'red', 'blue', 'green']
# selected_line_color = st.selectbox('Select Line Color', line_color_options, index=0)

fig = px.line(yearly_revenue, x='Year', y='Revenue',
              markers=True,
              title='Yearly Total Revenue',
              labels={'Year': 'Year', 'Revenue': 'Revenue'},
              line_shape='linear',
              line_dash_sequence=['solid'],
              template='plotly_dark',  
              color_discrete_sequence=['#e9bd01']
              )

fig.update_layout(
    template='plotly_dark',  
    xaxis=dict(showgrid=False), 
    yaxis=dict(showgrid=False),  
    plot_bgcolor='black', 
    title='Revenue by Year',
    title_font_size=20,
    title_font_color='white',
    width=500,  
    height=400,  
    margin=dict(l=50, r=50, t=50, b=50),
    paper_bgcolor='black',
    
)


st.plotly_chart(fig)



# monthly sales 

monthly_sales = bikes_selection.groupby(['Month'], as_index=False)['Order_Quantity'].sum()
# Create a bar chart for Monthly Sales
bar_fig = px.bar(
    monthly_sales,
    x='Month',
    y='Order_Quantity',
    color='Order_Quantity',
    labels={'Order_Quantity': 'Sales Quantity'},
    template='plotly_dark',
    title='Monthly Sales',
)

# Customize layout
bar_fig.update_layout(
    xaxis_title='Month',
    yaxis_title='Sales Quantity',
    paper_bgcolor='black',
    plot_bgcolor='black',
    title_font=dict(size=20, color='white'),
    font=dict(color='white'),
    coloraxis_showscale=False,
)

# Display the bar chart using Streamlit
st.plotly_chart(bar_fig)