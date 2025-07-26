from flask import Flask , render_template,request
from scraper import scrape_data
import csv

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    products = []
    if request.method == 'POST':
        url = request.form['url']
        products = scrape_data(url)

        # csv open

        with open('F:\python\product_scraper\products.csv','w',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Product Name','Price','Rating'])
            writer.writerows(products)

    return render_template('index.html',products=products)

if __name__=='__main__':
    app.run(debug=True)