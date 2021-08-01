from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    sum=['たこやき','おいしい','マヨネーズ','と','ソース','いつも','かけてる','まじで',"おいしい"]
    return render_template("index.html",sum=sum)




if __name__ == '__main__':
    app.run(debug=True)
