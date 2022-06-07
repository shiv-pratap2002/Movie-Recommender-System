from fastapi import FastAPI
from model import recommender_system, recommender_system_3
from pydantic import BaseModel

app = FastAPI()

class data(BaseModel):
    moviename: str

class recommender_data(BaseModel):
    userid: int
    moviename:str
    n_similar_users: int
    n_movies:int

@app.get('/')
def index():
    return {'message': 'Hello, World'}



    
@app.post('/recommend')
async def recommend(user_input : data):
    
    # model integration
    products = recommender_system(user_input.moviename)
    
    return products


@app.post('/recommend_3')
async def recommend_3(user_input : recommender_data):
    return recommender_system_3(user_input.userid,user_input.moviename,user_input.n_similar_users,user_input.n_movies)
