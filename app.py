import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import tools
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from plotly import tools
import pandas as pd

# Graph Section Begin
specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}], [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]

fig_pie = make_subplots(rows = 2, cols=5, specs=specs, subplot_titles=('Batman V Superman', 'Civil War', 'Deadpool', 'Fantastic Beasts', 'Finding Dory', 'Jungle Book', 'Rogue One', 'Secret Life of Pets', 'Suicide Squad', 'Zootopia'))

fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[77, 23]),
    row=1,
    col=1,
)
fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[72, 83]),
    row=1,
    col=2,
)

fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[83, 17]),
    row=1,
    col=3,
)
fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[68, 32]),
    row=1,
    col=4,
)

fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[47, 53]),
    row=1,
    col=5,
)
fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[90, 10]),
    row=2,
    col=1,
)

fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[83, 17]),
    row=2,
    col=2,
)
fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[81, 19]),
    row=2,
    col=3,
)

fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[68, 32]),
    row=2,
    col=4,
)
fig_pie.add_trace(
    go.Pie(labels=['Male', 'Female'], values=[54, 46]),
    row=2,
    col=5,
)


fig_pie.update_layout(
    title_text="Percentage of Words said by Men vs Women",
    title_x= 0.5,
    # Add annotations in the center of the donut pies.
    annotations=[
                dict(showarrow= False,text= 'Batman V Superman',x= 0.225,xanchor= 'center',xref= 'paper',y= 1.0,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Civil War',x= 0.775,xanchor= 'center',xref= 'paper',y= 1.0,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Deadpool',x= 0.225,xanchor= 'center',xref= 'paper',y= 0.78,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Fantastic Beasts',x= 0.775,xanchor= 'center',xref= 'paper',y= 0.78,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Finding Dory',x= 0.225,xanchor= 'center',xref= 'paper',y= 0.56,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Jungle Book',x= 0.775,xanchor= 'center',xref= 'paper',y= 0.56,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Rogue One',x= 0.225,xanchor= 'center',xref= 'paper',y= 0.33999999999999997,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Secret Life of Pets',x= 0.775,xanchor= 'center',xref= 'paper',y= 0.33999999999999997,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Suicide Squad',x= 0.225,xanchor= 'center',xref= 'paper',y= 0.12,yanchor= 'bottom',yref= 'paper'),
                dict(showarrow= False,text= 'Zootopia',x= 0.775,xanchor= 'center',xref= 'paper',y= 0.12,yanchor= 'bottom',yref= 'paper'),
                dict(text='', x=0.5, y=0.5, font_size=14, showarrow=False)]
)

movieTitles=['Batman V Superman', 'Civil War', 'Deadpool', 'Fantastic Beasts', 'Finding Dory', 'Jungle Book', 'Rogue One', 'Secret Life of Pets', 'Suicide Squad', 'Zootopia']

fig_stackBarplot = go.Figure(data=[
    go.Bar(name='Men', x=movieTitles, y=[77, 72, 83, 68, 47, 90, 83, 81, 68, 54]),
    go.Bar(name='Women', x=movieTitles, y=[23, 28, 17, 32, 53, 10, 17, 19, 32, 46])
])

fig_stackBarplot.update_layout(title_text='Percentage of Words said by Men vs Women', title_x=0.5, barmode='stack', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

# data = pd.read_csv('CombinedSpreadsheet.csv')

# fig_bubble = go.Figure(
#     data=[
#         go.Scatter(
#             x=data['speaking_turns'],
#             y=data['Total_Words'],
#             mode='markers',
#             marker=dict(
#                 size=data['diameter'],
#                 color=data['Color']
#             ),
#             hoverinfo = 'none',
#             hovertemplate = "Character: " + data['Character'] + "<br>Movie: " + data['Movie'] + "<br>Turns Speaking: " + data['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data['Total_Words'].astype(str) + '<extra></extra>'
#         )
#     ],
# )

# fig_bubble.update_xaxes(title_text='Turns Speaking')
# fig_bubble.update_yaxes(title_text='Total Words Spoken')
# fig_bubble.update_layout(title={
#                     'text': "Turns Speaking vs Total Words Spoken",
#                     'x':0.5,
#                     'xanchor': 'center',
#                     'yanchor': 'top'
#                 },
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)'
#             )

data = pd.read_csv('CombinedSpreadsheet.csv')
data_batman_v_superman = pd.read_csv('MovieData\BatmanVSuperman - BatmanVSuperman.csv')
data_civl_war = pd.read_csv('MovieData\CivilWar - CivilWar.csv')
data_deadpool = pd.read_csv('MovieData\Deadpool - Deadpool.csv')
data_fantastic_beasts = pd.read_csv('MovieData\FantasticBeasts - FantasticBeasts.csv')
data_finding_dory = pd.read_csv('MovieData\FindingDory - FindingDory.csv')
data_junglebook = pd.read_csv('MovieData\JungleBook - JungleBook.csv')
data_rogue_one = pd.read_csv('MovieData\RogueOne - RogueOne.csv')
data_secret_life_of_pets = pd.read_csv('MovieData\SecretLifeofPets - SecretLifeofPets.csv')
data_suicide_squad = pd.read_csv('MovieData\SuicideSquad - SuicideSquad.csv')

fig_bubble = go.Figure()

# All movies
fig_bubble.add_trace(
    go.Scatter(
        x=data['speaking_turns'],
        y=data['Total_Words'],
        mode='markers',
        marker=dict(
            size=data['diameter'],
            color=data['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data['Character'] + "<br>Movie: " + data['Movie'] + "<br>Turns Speaking: " + data['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data['Total_Words'].astype(str) + '<extra></extra>',
        visible=True
    )
)

#Batman v Superman
fig_bubble.add_trace(
    go.Scatter(
        x=data_batman_v_superman['speaking_turns'],
        y=data_batman_v_superman['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_batman_v_superman['diameter'],
            color=data_batman_v_superman['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_batman_v_superman['Character'] + "<br>Movie: " + data_batman_v_superman['Movie'] + "<br>Turns Speaking: " + data_batman_v_superman['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_batman_v_superman['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Civil War
fig_bubble.add_trace(
    go.Scatter(
        x=data_civl_war['speaking_turns'],
        y=data_civl_war['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_civl_war['diameter'],
            color=data_civl_war['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_civl_war['Character'] + "<br>Movie: " + data_civl_war['Movie'] + "<br>Turns Speaking: " + data_civl_war['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_civl_war['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Deadpool
fig_bubble.add_trace(
    go.Scatter(
        x=data_deadpool['speaking_turns'],
        y=data_deadpool['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_deadpool['diameter'],
            color=data_deadpool['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_deadpool['Character'] + "<br>Movie: " + data_deadpool['Movie'] + "<br>Turns Speaking: " + data_deadpool['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_deadpool['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Fantastic Beasts
fig_bubble.add_trace(
    go.Scatter(
        x=data_fantastic_beasts['speaking_turns'],
        y=data_fantastic_beasts['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_fantastic_beasts['diameter'],
            color=data_fantastic_beasts['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_fantastic_beasts['Character'] + "<br>Movie: " + data_fantastic_beasts['Movie'] + "<br>Turns Speaking: " + data_fantastic_beasts['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_fantastic_beasts['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Finding Dory
fig_bubble.add_trace(
    go.Scatter(
        x=data_finding_dory['speaking_turns'],
        y=data_finding_dory['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_finding_dory['diameter'],
            color=data_finding_dory['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_finding_dory['Character'] + "<br>Movie: " + data_finding_dory['Movie'] + "<br>Turns Speaking: " + data_finding_dory['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_finding_dory['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Jungle Book
fig_bubble.add_trace(
    go.Scatter(
        x=data_junglebook['speaking_turns'],
        y=data_junglebook['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_junglebook['diameter'],
            color=data_junglebook['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_junglebook['Character'] + "<br>Movie: " + data_junglebook['Movie'] + "<br>Turns Speaking: " + data_junglebook['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_junglebook['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Rogue One
fig_bubble.add_trace(
    go.Scatter(
        x=data_rogue_one['speaking_turns'],
        y=data_rogue_one['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_rogue_one['diameter'],
            color=data_rogue_one['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_rogue_one['Character'] + "<br>Movie: " + data_rogue_one['Movie'] + "<br>Turns Speaking: " + data_rogue_one['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_rogue_one['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Secret Life Of Pets
fig_bubble.add_trace(
    go.Scatter(
        x=data_secret_life_of_pets['speaking_turns'],
        y=data_secret_life_of_pets['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_secret_life_of_pets['diameter'],
            color=data_secret_life_of_pets['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_secret_life_of_pets['Character'] + "<br>Movie: " + data_secret_life_of_pets['Movie'] + "<br>Turns Speaking: " + data_secret_life_of_pets['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_secret_life_of_pets['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

#Suicide Squad
fig_bubble.add_trace(
    go.Scatter(
        x=data_suicide_squad['speaking_turns'],
        y=data_suicide_squad['Total_Words'],
        mode='markers',
        marker=dict(
            size=data_suicide_squad['diameter'],
            color=data_suicide_squad['Color']
        ),
        hoverinfo = 'none',
        hovertemplate = "Character: " + data_suicide_squad['Character'] + "<br>Movie: " + data_suicide_squad['Movie'] + "<br>Turns Speaking: " + data_suicide_squad['speaking_turns'].astype(str) + "<br>Total Words Spoken: " + data_suicide_squad['Total_Words'].astype(str) + '<extra></extra>',
        visible=False
    )
)

fig_bubble.update_xaxes(title_text='Turns Speaking')
fig_bubble.update_yaxes(title_text='Total Words Spoken')
fig_bubble.update_layout(title={
                    'text': "Turns Speaking vs Total Words Spoken All Movies'",
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'
                },
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)')

fig_bubble.update_layout(
    updatemenus=[
        dict(
            type='buttons',
            direction='right',
            active=0,
            x=0.8,
            y=1.4,
            buttons=list([
                dict(label='All Movies',
                     method='update',
                     args=[{'visible': [True, False, False, False, False, False, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken All Movies'}]),
                dict(label='Batman Vs Superman',
                     method='update',
                     args=[{'visible': [False, True, False, False, False, False, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Batman Vs Superman'}]),
                dict(label='Civil War',
                     method='update',
                     args=[{'visible': [False, False, True, False, False, False, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Civil War'}]),
                dict(label='Deadpool',
                     method='update',
                     args=[{'visible': [False, False, False, True, False, False, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Deadpool'}]),
                dict(label='Fantastic Beasts',
                     method='update',
                     args=[{'visible': [False, False, False, False, True, False, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Fantastic Beasts'}]),
                dict(label='Finding Dory',
                     method='update',
                     args=[{'visible': [False, False, False, False, False, True, False, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Finding Dory'}]),
                dict(label='Jungle Book',
                     method='update',
                     args=[{'visible': [False, False, False, False, False, False, True, False, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Jungle Book'}]),  
                dict(label='Rogue One',
                     method='update',
                     args=[{'visible': [False, False, False, False, False, False, False, True, False, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Rogue One'}]),  
                dict(label='Secret Life Of Pets',
                     method='update',
                     args=[{'visible': [False, False, False, False, False, False, False, False, True, False]},
                     {'title': 'Turns Speaking vs Total Words Spoken Secret Life Of Pets'}]),  
                dict(label='Suicide Squad',
                     method='update',
                     args=[{'visible': [False, False, False, False, False, False, False, False, False, True]},
                     {'title': 'Turns Speaking vs Total Words Spoken Suicide Squad'}]),  
            ])
        )
    ]
)
# Graph Section End


print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL]) #LUX

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


splash_page = html.Div([
    html.Br(),
    html.Br(),
    html.H1('An Analysis of Film Dialogue by Gender', style={'text-align':'center'}),
    html.H4('By Ashank Kumar and Jack Caldwell', style={'text-align':'center'}),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Button('Navigate to Data Visualizations', href='/data-viz', outline=True, color='dark', size='lg')],
        justify='center',
    )
])


data_viz_page = html.Div([
    dbc.Tabs(
        [
            dbc.Tab(label='Pie Chart', tab_id='pie'),
            dbc.Tab(label='Stacked Bar Chart', tab_id='bar'),
            dbc.Tab(label='Bubble Chart', tab_id='bubble')
        ],
        id="tabs",
    ),
    html.Div(id="tab-content", className="p-4"), #style={'height': '80vh'}
    html.P('For our group project, we decided to focus on the discrepancy of representation of male and female characters in popular movies from the current day. To conduct our research, we collected information from the top 10 blockbusters of 2016, specifically looking at the number of large roles portrayed as male and female. Seven of the ten movies were dominated by male characters with five of them featuring over 75% male character. In fact, The Jungle Book featured 90% males compared to only 10% female, making the discrepancy visible to the uninterested eye. The remaining three movies were close to 50% male and female, with two of them favoring more females than males and one with males out on top. These results were not necessarily surprising to us when considering the films that we analyzed. Six of the ten can be generalized as action movies and it is typical for these movies to exhibit male lead and support roles as that is what the industry as a whole has subscribed to. The other four can be generalized as family movies, two of which fall near to 50/50 representation. Surprisingly the other two are extremely dominated by males which must have just been from the direction the director wanted to take the movie. Overall, the top 10 blockbusters of 2016 underrepresented female characters as male role heavily dominated the big screen.', style={'text-align': 'center', 'margin-left': '5%', 'margin-right': '5%', 'margin-bottom': '5%'}),
    dbc.Row([
        dbc.Button('Navigate Home', href='/', outline=True, color='dark', size='lg')],
        justify='center'
    )
])

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab")],
    # [Input("tabs", "active_tab"), Input('tab_content', 'data')]
)
def render_tab_content(active_tab):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    # if active_tab and data is not None:
    #     if active_tab == "pie":
    #         return dcc.Graph(figure=fig_pie)
    #     elif active_tab == "bar":
    #         return dcc.Graph(figure=fig_stackBarplot)
    # return data
    if active_tab == 'pie':
        return dcc.Graph(figure=fig_pie, config=dict(displayModeBar=False), style={'height': 500})
    if active_tab == 'bar':
        return dcc.Graph(figure=fig_stackBarplot, config=dict(displayModeBar=False), style={'height': 500})
    return dcc.Graph(figure=fig_bubble, config=dict(displayModeBar=False), style={'height': 500})


# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/data-viz':
        return data_viz_page
    else:
        return splash_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=True)