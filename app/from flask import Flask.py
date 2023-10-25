from flask import Flask, render_template, request
import dao
app = Flask(__name__)
@app.route("/")

def index():
    kw=request.args.get('kw')
    loai= dao.load_loaiSanPhan()
    sanPham=dao.load_products(kw)
    return render_template('index.html', categories = loai, products=sanPham)

if __name__ == "__main__":
    app.run(debug=True)