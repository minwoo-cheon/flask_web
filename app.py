from flask import Flask , render_template, request, redirect
from data import Articles
#render_template html과 만나면 해당 템플릿으로 변환시켜 줌.
import pymysql

app = Flask(__name__)
app.debug = True

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='1234',
    db='busan'
)

# cursor = db.cursor()
@app.route('/', methods=['GET']) #데커레이터  경로 라우팅, 방식(지금은 리스트)
def index():
    # return "Hello World"
    return render_template("index.html", data= "DONG")
    # 첫번째 인자 html경로, 두번째는 전달할 데이터
@app.route('/about')
def about():
    return render_template("about.html", hello = "Gary Kim")
@app.route('/articles')
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    # articles = Articles()
    # print(articles[0]['title'])
    return render_template("articles.html", articles = topics)
@app.route('/article/<int:id>')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    # articles = Articles()
    # article = articles[id-1]
    # articles = Articles()
    # article = articles[id-1]
    # print(articles[id-1])
    return render_template("article.html", article = topic)
@app.route('/add_articles', methods = ["GET","POST"])
def add_articles():
    cursor = db.cursor()
    if request.method == "POST":
        author = request.form['author']
        title = request.form['title']
        desc = request.form['desc']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]
        print(request.form['desc'])
        #이건 vscode오류라서 변수를 사용하고 있지 않아서 생기는 경고창이라
        #오류라고 볼순 없어영
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        # db.close()
        return redirect("/articles")
        # return "Success"
    else:
        return render_template("add_articles.html")
# @app.route('/add_articles')
# def add_articles():
#     # return "<h1>글쓰기 페이지</h1>"
#     return render_template("add_articles.html")
# @app.route('/add_articles', methods = ["POST"])
# def insert_articles():
#     return "Success"
@app.route('/delete/<int:id>', methods = ['POST'])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = {};'.format(id)
    cursor.execute(sql)
    # sql = 'DELETE FROM topic WHERE id = %s;'
    # id = [id]
    # cursor.execute(sql, id)
    db.commit()
    return redirect("/articles")


@app.route('/<int:id>/edit', methods=["GET","POST"])
def edit(id):

    cursor = db.cursor()
    if request.method == "POST":
        return "Success"

    else:
        sql="SELECT * FROM topic WHERE id ={}".format(id)
        cursor.execute(sql)
        topic = cursor.fetchone()
        print(topic[1])
        return render_template("edit_article.html", article = topic)


if __name__ == '__main__':
  app.run()