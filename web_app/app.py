from flask import Flask, render_template, request
from recommender import recommend_random,recommend_with_NMF
from utils import movies

app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html',name='Markov Canes',movies = movies.title.to_list())
@app.route('/recommendation')
def random_recommendation():
    titles = request.args.getlist("title")
    ratings = request.args.getlist("rating")

    print(titles, ratings)

    user_rating = dict(zip(titles, ratings))
    for keys in user_rating:
        user_rating[keys] = int(user_rating[keys])

    print(user_rating)
    if request.args['method'] == 'Random':
        recs = recommend_random(k=3).to_list()
        return render_template('recommender.html',values = recs)
    else:
        return 'Fuction not defined' 
    

if __name__=='__main__':
    app.run(port=5000,debug=True)