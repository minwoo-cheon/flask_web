from flask import Flask , render_template
from data import Articles

app = Flask(__name__)

app.debug = True #개발끝나고 퍼블릭할때 반드시 false로둬야함

@app.route('/', methods=['GET'])
def index():
    #return "Hello World"
    return render_template("index.html",data="CHEON")

@app.route('/about')
def about():
    return render_template("about.html", Hello = "Gary Cheon")

@app.route('/articles')
def articles():
    articles = Articles()
    #print(articles)
    return render_template("articles.html",  articles = articles)


@app.route('/article/<int:id>')
def article(id):
    articles = Articles()
    article = articles[id-1]
    print(articles[id-1])
    return render_template("article.html",article=article)

if __name__ == '__main__':
    app.run()
    