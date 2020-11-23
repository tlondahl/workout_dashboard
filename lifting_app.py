import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

#Import the DataFrames
df = pd.read_csv('pr.csv', index_col=0)
sovjet_df = pd.read_csv('Sovjet_standards.csv', index_col=0)
s_std = pd.read_csv('snatch_standards.csv')
cj_std = pd.read_csv('cj_standards.csv')

# lists of the different lifts
snatch = list(sovjet_df[sovjet_df['Of'] == 'Snatch'].iloc[:,0].str.title())
cj = list(sovjet_df[sovjet_df['Of'] == 'Clean & Jerk'].iloc[:,0].str.title())

#Create new columns for the standards
df['goal_min'] = np.nan
df['goal_max'] = np.nan
df.fillna(0, inplace=True)

#Calculate the standards
for i, lift in enumerate(df.Lift):
    if lift in snatch:
        df['goal_min'][i] = round(float(sovjet_df[sovjet_df['Lift']==lift].loc[:,'Min']) \
                                  * float(df[df['Lift']=='Snatch'].loc[:,'Weight (kg)']),2)
        df['goal_max'][i] = round(float(sovjet_df[sovjet_df['Lift'] == lift].loc[:, 'Max']) \
                                  * float(df[df['Lift'] == 'Snatch'].loc[:, 'Weight (kg)']), 2)
    elif lift in cj:
        df['goal_min'][i] = round(float(sovjet_df[sovjet_df['Lift'] == lift].loc[:, 'Min']) \
                                  * float(df[df['Lift'] == 'Clean & Jerk'].loc[:, 'Weight (kg)']), 2)
        df['goal_max'][i] = round(float(sovjet_df[sovjet_df['Lift'] == lift].loc[:, 'Max']) \
                                  * float(df[df['Lift'] == 'Clean & Jerk'].loc[:, 'Weight (kg)']), 2)
    else:
        pass

# My body weight (in kg) for later calculations
bw = 89

# Snatch Standards
s_beginner = float(s_std[s_std['BW'] > bw].iloc[0,1])
s_novice = float(s_std[s_std['BW'] > bw].iloc[0,2])
s_intermediate = float(s_std[s_std['BW'] > bw].iloc[0,3])
s_advanced = float(s_std[s_std['BW'] > bw].iloc[0,4])
s_elite = float(s_std[s_std['BW'] > bw].iloc[0,5])

# Clean & Jerk Standards
cj_beginner = float(cj_std[cj_std['BW'] > bw].iloc[0,1])
cj_novice = float(cj_std[cj_std['BW'] > bw].iloc[0,2])
cj_intermediate = float(cj_std[cj_std['BW'] > bw].iloc[0,3])
cj_advanced = float(cj_std[cj_std['BW'] > bw].iloc[0,4])
cj_elite = float(cj_std[cj_std['BW'] > bw].iloc[0,5])

app = dash.Dash(__name__)
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

colors = {
    'background': '#1e2025',
    'text': '#bbbcbd'
}
guage_snatch = go.Figure(go.Indicator(
        domain = {'x': [0, 0], 'y': [0, 0]},
        value = float(df[df['Lift']=='Snatch'].loc[:,'Weight (kg)']),
        mode = "gauge+number+delta",
        title = {'text': 'Snatch'},
        delta = {'reference': float(df[df['Lift']=='Snatch'].loc[:,'Prev'])},
        gauge = {'axis': {'range': [None, s_elite+25], 'dtick': 25},
                 'steps' : [
                        {'range': [0, s_beginner], 'color': "#de425b"},
                        {'range': [s_beginner, s_novice], 'color': "#d97b5c"},
                        {'range': [s_novice, s_intermediate], 'color': "#cfa57d"},
                        {'range': [s_intermediate, s_advanced], 'color': "#ccc6b4"},
                        {'range': [s_advanced, s_elite], 'color': "#a4b08d"},
                        {'range': [s_elite, s_elite+25], 'color': "#488f31"}],
                 'bar': {'color': "#3c414b"},
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': s_advanced}}))
guage_snatch.update_layout(
                        margin={'t': 0, 'b':5},
                        plot_bgcolor=colors['background'],
                        paper_bgcolor=colors['background'],
                        font_color=colors['text'])

guage_cj = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = float(df[df['Lift']=='Clean & Jerk'].loc[:,'Weight (kg)']),
        mode = "gauge+number+delta",
        title = {'text': 'Clean & Jerk'},
        delta = {'reference': float(df[df['Lift']=='Clean & Jerk'].loc[:,'Prev'])},
        gauge = {'axis': {'range': [None, cj_elite+25], 'dtick': 25},
                 'steps' : [
                        {'range': [0, cj_beginner], 'color': "#de425b"},
                        {'range': [cj_beginner, cj_novice], 'color': "#d97b5c"},
                        {'range': [cj_novice, cj_intermediate], 'color': "#cfa57d"},
                        {'range': [cj_intermediate, cj_advanced], 'color': "#ccc6b4"},
                        {'range': [cj_advanced, cj_elite], 'color': "#a4b08d"},
                        {'range': [cj_elite, cj_elite+25], 'color': "#488f31"}],
                 'bar': {'color': "#3c414b"},
                 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': cj_advanced}}))
guage_cj.update_layout(
                        margin={'t': 0, 'b':5},
                        plot_bgcolor=colors['background'],
                        paper_bgcolor=colors['background'],
                        font_color=colors['text'],
)

# Function for the bullet graphs
def bullet(lift):
    return go.Indicator(
        mode = "number+gauge+delta",
        value = float(df[df['Lift']==lift].loc[:,'Weight (kg)']),
        domain = {'x': [0.1, 1], 'y': [0, 1]},
        title = {'text' :"<b>"+lift+"</b>"},
        title_font = {'size': 20},
        delta = {'reference': float(df[df['Lift']==lift].loc[:,'Prev'])},
        delta_font={'size':15},
        number_font={'size':18},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 200], 'dtick' :25},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 1,
                'value': float(df[df['Lift']==lift].loc[:,'goal_min'])},
            'steps': [
                {'range': [0, float(df[df['Lift'] == str(lift)].loc[:, 'goal_min'])], 'color': '#7e8aa0'},
                {'range': [float(df[df['Lift'] == str(lift)].loc[:, 'goal_min']),
                 float(df[df['Lift'] == str(lift)].loc[:, 'goal_max'])], 'color': "#a2b3cf"}],
            'bar': {'color': "#3c414b", 'thickness':0.5},
            'bgcolor': "#c6ddff",
        })
def update_bullet_layout(bullet):
        return bullet.update_layout(height=110,
                               margin={'t': 0, 'r':0},
                               # width = 200,
                               plot_bgcolor=colors['background'],
                               paper_bgcolor=colors['background'],
                               font_color=colors['text']
                               )

# Bullet for Back Squats
bullet_bs = go.Figure()
bullet_bs.add_trace(bullet('Back Squat'))
update_bullet_layout(bullet_bs)

# Bullet for Front Squats
bullet_fs = go.Figure()
bullet_fs.add_trace(bullet('Front Squat'))
update_bullet_layout(bullet_fs)

# Bullet for Overhead Squats
bullet_ohs = go.Figure()
bullet_ohs.add_trace(bullet('Ohs'))
update_bullet_layout(bullet_ohs)

# Bullet for Power Snatch
bullet_ps = go.Figure()
bullet_ps.add_trace(bullet('Power Snatch'))
update_bullet_layout(bullet_ps)

# Bullet for Hang Snatch
bullet_hs = go.Figure()
bullet_hs.add_trace(bullet('Hang Snatch'))
update_bullet_layout(bullet_hs)

# Bullet for Power Clean
bullet_pc = go.Figure()
bullet_pc.add_trace(bullet('Power Clean'))
update_bullet_layout(bullet_pc)

# Bullet for Clean
bullet_c = go.Figure()
bullet_c.add_trace(bullet('Clean'))
update_bullet_layout(bullet_c)

# Bullet for Hang Clean
bullet_hc = go.Figure()
bullet_hc.add_trace(bullet('Hang Clean'))
update_bullet_layout(bullet_hc)

# Bullet for Jerk From Rack
bullet_j = go.Figure()
bullet_j.add_trace(bullet('Jerk From Rack'))
update_bullet_layout(bullet_j)

# Bullet for Jerk From Rack
bullet_pj = go.Figure()
bullet_pj.add_trace(bullet('Power Jerk'))
update_bullet_layout(bullet_pj)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Div([
        html.H1(
            children='Training Progress',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        html.Div(children='A dashboard to track your training goals', style={
            'textAlign': 'center',
            'color': colors['text']})
    ], className = 'row' ),

# Adding the graphs
    html.Div(
            html.H1(
                children='Olympic Lifts in Relation to Body Weight',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'margin-top': 50
                }),className='row'),
    html.Div([
        html.Div([
        dcc.Graph(id='guage_snatch', figure=guage_snatch),
    ], className= 'six columns'),
        html.Div([
        dcc.Graph(id='guage_cj', figure=guage_cj),
    ], className= 'six columns')], className='row'),

    html.Div(
            html.H1(
                children='Accessory Lifts in relation to your Olympic Lifts',
                style={
                    'textAlign': 'center',
                    'color': colors['text'],
                    'margin-top': 0
                }),className='row'),
    dcc.Graph(
            id='bullet_bs',
            figure=bullet_bs
    ),
    dcc.Graph(
            id='bullet_fs',
            figure=bullet_fs
    ),
    dcc.Graph(
            id='bullet_ohs',
            figure=bullet_ohs
    ),
    dcc.Graph(
            id='bullet_ps',
            figure=bullet_ps
    ),
    dcc.Graph(
            id='bullet_hs',
            figure=bullet_hs
    ),
    dcc.Graph(
            id='bullet_pc',
            figure=bullet_pc
    ),
    dcc.Graph(
        id='bullet_c',
        figure=bullet_c
    ),
    dcc.Graph(
        id='bullet_hc',
        figure=bullet_hc
    ),
    dcc.Graph(
        id='bullet_j',
        figure=bullet_j
    ),
    dcc.Graph(
        id='bullet_pj',
        figure=bullet_pj
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)