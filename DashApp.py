# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from turtle import title
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

GGSDF=pd.read_csv("C:\\DataAnalytics\\GroupedFile\\MYGroupedFile.csv")
#Best Selling Category and Most Profitable
best_selling_Category=GGSDF.groupby('Category')[['Sales','Profit_Margin']].sum().reset_index()
best_selling_Category=best_selling_Category.sort_values(by=['Sales'], ascending=False).sort_values(by=['Profit_Margin'],ascending=False)
fig=px.bar(best_selling_Category,x=best_selling_Category.index,y=[best_selling_Category.Sales,best_selling_Category.Profit_Margin], title="Best Selling Category And Most Profitable",color="Category",barmode='group')


#Best Selling And Most Profitable Sub-Category
best_selling_Sub_Category=GGSDF.groupby('Sub_Category')[['Sales','Profit_Margin']].sum().reset_index()
best_selling_Sub_Category=best_selling_Sub_Category.sort_values(by=['Sales'], ascending=False).sort_values(by=['Profit_Margin'],ascending=False)
fig1=px.bar(best_selling_Sub_Category,x=best_selling_Sub_Category.index,y=[best_selling_Sub_Category.Sales,best_selling_Sub_Category.Profit_Margin], title="Best Selling Category And Most Profitable",color="Sub_Category")

#top_selling_sub-category
top_selling_sub_category=GGSDF.groupby('Sub_Category')[['Sales']].sum().reset_index()
top_selling_sub_category=top_selling_sub_category.sort_values(by=['Sales'],ascending=False)
fig2=px.bar(top_selling_sub_category, x=top_selling_sub_category.index, y=top_selling_sub_category.Sales,title="Top Selling Sub-Category ", color='Sub_Category' )


#Most_Profitable_Customer_Segment
Most_Profitable_Customer_Segment=GGSDF.groupby('Segment')[['Profit_Margin']].sum().reset_index()
Most_Profitable_Customer_Segment=Most_Profitable_Customer_Segment.sort_values(by=['Profit_Margin'],ascending=False)
fig3=px.bar(Most_Profitable_Customer_Segment, x=Most_Profitable_Customer_Segment.index, y=Most_Profitable_Customer_Segment.Profit_Margin, title=" Most Profitable Customer Segment ", color='Segment')

#prefered_Ship_Mode
Prefered_Ship_Mode=GGSDF.groupby('Ship_Mode')[['Count']].count()
Prefered_Ship_Mode=Prefered_Ship_Mode.sort_values(by=['Count'], ascending=False).reset_index()
fig4=px.bar(Prefered_Ship_Mode,x=Prefered_Ship_Mode.index,y=Prefered_Ship_Mode.Count, title='Prefered ship Mode', color='Ship_Mode')


#Most Profitable Region
Most_Profitable_Region=GGSDF.groupby('Region')[['Profit_Margin']].sum()
Most_Profitable_Region=Most_Profitable_Region.sort_values(by=['Profit_Margin'], ascending=False).reset_index()
fig5=px.bar(Most_Profitable_Region, x=Most_Profitable_Region.index, y=Most_Profitable_Region.Profit_Margin, title='Most Profitable Region', color='Region')


#City which highest number of sales
Highest_City_Sales=GGSDF.groupby('City')[['Sales']].sum()
Highest_City_Sales=Highest_City_Sales.sort_values(by=['Sales'], ascending=False).head(10).reset_index()
fig6=px.bar(Highest_City_Sales, x=Highest_City_Sales.index, y=Highest_City_Sales.Sales, title='City Which Highest Number of sales', color='City')



















app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        DBC 26.1 Project By GunDem
    '''),

    dcc.Graph(
        id='best_selling_Category',
        figure=fig
    ),

    dcc.Graph(
        id='best_selling_Sub_Category',
        figure=fig1
    ),

    dcc.Graph(
        id='top_selling_Sub_Category',
        figure=fig2
    ),
    dcc.Graph(
        id='Most_Profitable_Customer_Segment',
        figure=fig3
    ),
    dcc.Graph(
        id='Prefered_Ship_Mode',
        figure=fig4
    ),
    dcc.Graph(
        id='Most_Profitable_Region',
        figure=fig5
    ),

    dcc.Graph(
        id='Highest_City_Sales',
        figure=fig6
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)


# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

# from operator import index
# from dash import Dash, html, dcc,Input,Output,callback
# import plotly.express as px
# import pandas as pd
# import os 

# app = Dash(__name__)

# path="C:\\DataAnalytics\\GroupedFile"
# fpath=os.path.join(path,"MYGroupedFile.csv")
# GGSdf=pd.read_csv(fpath)







# app.layout = html.Div(children=[
#     html.H1(children="GunDem's DashApp"),

#     html.Div(children=['''
#         Hello, THis IS my ANAlysis
#     ''', html.Link( href="DashApp.py")]),
    
    

#     dcc.Dropdown(
#         id="State-dropdown",
#         options=[{"label":i,"value":i} for i in GGSdf["State"].unique()],
#         placeholder="select a State",
#         multi=True


#     ),

#     dcc.Graph(
#         id='bar-graph',
       
#     )
# ])

# @app.callback(
#     Output("bar-graph","figure"),
#     Input("State-dropdown","value")
# )

# def display_category(category):

#     if category==None:
#         New_GGSdf=GGSdf[GGSdf["State"]=="New York"]
#         New_GGSdf=New_GGSdf.groupby("Day_Ordered").Sales.sum().reset_index()
#         fig=px.bar(New_GGSdf, x=New_GGSdf.Day_Ordered , y=New_GGSdf.Sales, barmode="group", color="Day_Ordered", width=1000)
#         return fig

#     else:
#         New_GGSdf=GGSdf[GGSdf["State"].isin(category)]
#         New_GGSdf=New_GGSdf.groupby("Day_Ordered").Sales.sum().reset_index()
#         fig=px.bar(New_GGSdf, x=New_GGSdf.Day_Ordered , y=New_GGSdf.Sales, barmode="group", color="Day_Ordered", width=1000)
#         return fig









# if __name__ == '__main__':
#     app.run_server(debug=True)
