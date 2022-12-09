from fastapi import FastAPI, Path, UploadFile, File
import pandas  as pd


app = FastAPI( 
            title='Proyecto Individual - FastAPI - Docker',
            version="0.0.1",
            contact={
            "name": "Argumedo Héctor",
            "url": "https://github.com/ArgumedoHector",
            "email": "argalhec@gmail.com",},
            description = "En este proyecto pueden realizar distintas consultas con respecto a las plataformas Amazon, Disney, Hulu y netflix. 🚀"
            )

@app.on_event('startup')
def startup():
    global final_df
    final_df=pd.read_csv("final.csv")

@app.get("/")
async def index():
    return 'Henry PI - 01'

@app.get('/get_max_duration({year},{platform},{tipo})')
def get_max_duration(año:int, plataforma:str,  duración:str ):
    df3=final_df[(final_df['release_year']==año) & (final_df['Plataforma']==plataforma)]
    if duración == 'min':
        titulo=df3.loc[df3.movie_duration.idxmax()]['title']
    else:
        titulo=df3.loc[df3.seasson_quantity.idxmax()]['title']
    return titulo


@app.get('/get_count_plataform({platform})')
def get_count_plataform( plataforma:str ):
    resultado1=((final_df['Plataforma']==plataforma) & (final_df['type'].str.contains('Movie'))).sum()
    resultado2=((final_df['Plataforma']==plataforma) & (final_df['type'].str.contains('TV Show'))).sum()
    return  ('Plataforma: '+str(plataforma)
            +'  Movie: '+str(resultado1)
            +'  TV Show: '+str(resultado2)) 


@app.get('/get_listedin({genero})')
def get_listedin(género:str):
    a=((final_df['listed_in'].str.contains(género)) & (final_df['Plataforma']=='amazon')).sum()
    b=((final_df['listed_in'].str.contains(género)) & (final_df['Plataforma']=='disney')).sum()
    c=((final_df['listed_in'].str.contains(género)) & (final_df['Plataforma']=='hulu')).sum()
    d=((final_df['listed_in'].str.contains(género)) & (final_df['Plataforma']=='netflix')).sum()
    lista=[a,b,c,d]
    resultado=max(lista)
    if a == resultado:
        plataforma='Amazon'
    if b == resultado:
        plataforma='Disney'
    if c == resultado:
        plataforma='Hulu'
    if d == resultado:
        plataforma='Netflix'
    return ( plataforma+'    '+str(resultado))


@app.get('/get_actor({plataforma},{anio})')
def get_actor(plataforma:str, año:int):
    df2=final_df[(final_df['Plataforma']==plataforma) & (final_df['release_year']==año)]
    for i in df2['cast']:
        if i != 'Sin dato':
            i=i.replace(', ', ',')
        else:
            continue
    lista=[]
    for i in df2['cast']:
        if i != 'Sin dato':
            s=i.split(',')
            for j in range(len(s)):             
                if s[j] not in lista:
                    lista.append(s[j])
                else:
                    continue
        else:
            continue
    lista=list(set(lista))
    c=0
    dicc={}
    for i in lista:
        c=0
        for j in df2['cast']:
            if i in j.split(','):
                c+=1
        dicc[i]=c
    return (max(dicc, key=dicc.get), str(dicc[max(dicc, key=dicc.get)]))