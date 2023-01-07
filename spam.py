
from flask import Flask, render_template, redirect,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_manager,login_required,login_user,logout_user,LoginManager,current_user



local_server=True

app = Flask(__name__)
app.secret_key="suhilkhan"

#app.config['SQL_ALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:suhilkhan@localhost/company'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
#connection of app with the database
#<=====Login Manager====>


login_manager=LoginManager(app)         

#this is for getting unique useraccess

login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

#<=====End Login Manager=====>

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class Admin(UserMixin,db.Model):
    adminid=db.Column(db.Integer,primary_key=True)
    adminname=db.Column(db.String(100))
    adminpw=db.Column(db.String(100))

class Inventory(UserMixin,db.Model):
    productname=db.Column(db.String(100),primary_key=True)
    stockin=db.Column(db.Interger())
    stockout=db.Column(db.Integer())
    stockavail=db.Column(db.Integer())

class Sales(UserMixin,db.Model):
    sid=db.Column(db.String(100),primary_key=True)
    supname=db.Column(db.String(100))
    sdate=db.Column(db.String(100))

class Receiving(UserMixin,db.Model):
    rdate=db.Column(db.String(100))
    rid=db.Column(db.String(100))
    supname=db.Column(db.String(100))


class Category(UserMixin,db.Model):
    cid=db.Column(db.String(100),primary_key=True)
    catname=db.Column(db.String(100))
    
class Product(UserMixin,db.Model):
    pid=db.Column(db.String(100),primary_key=True)
    catname=db.Column(db.String(100))
    pname=db.Column(db.String(100))
    pdesc=db.Column(db.String(100))
    pprice=db.Column(db.String(100))

class Supplier(UserMixin,db.Model):
    supname=db.Column(db.String(100))
    supcont=db.Column(db.String(100))
    supaddr=db.Column(db.String(100))

class Customer(UserMixin,db.Model):
    cusname=db.Column(db.String(100))
    cuscont=db.Column(db.String(100))
    cusaddr=db.Column(db.String(100))




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin', methods=['POST','GET'])
def adminlogin():
    if request.method=='POST':
        adminid=request.form.get('adminid')
        adminpw=request.form.get('adminpw')
        admins=Admin.query.filter_by(id=adminid).first()
        if admins and (admins.password==adminpw):
            return redirect('/brand')
        else:
            return 'login failed'
    return render_template('adminlogin.html')

@app.route('/category',methods=['POST','GET'])
def category():
    if request.method=='POST':
        bcode=request.form.get('bcode')
        bname=request.form.get('bname')
        brand=Brand.query.filter_by(bcode=bcode).first()

        if brand:
            flash("Brand is Already Present You Can Add Products","warning")
            return render_template('brand.html')

        db.engine.execute(f"INSERT INTO `brand` (`bcode`,`bname`) VALUES ('{bcode}','{bname}') ")
        flash("Brand is Added Successfully","success")
    allbrands=Brand.query.all()
    return render_template('brand.html',allbrands=allbrands)

@app.route('/category',methods=['POST','GET'])
def category():
    if request.method=='POST':
        cid=request.form.get('cid')
        bcode=request.form.get('bcode')
        catname=request.form.get('catname')
        brand=Brand.query.filter_by(bcode=bcode).first()
        category=Category.query.filter_by(cid=cid).first()

        if category:
            flash("Category is Already Present You Can Add Products","warning")
            return render_template('brand.html')

        if brand:
            db.engine.execute(f"INSERT INTO `category` (`bcode`,`catname`,`cid`) VALUES ('{bcode}','{catname}','{cid}') ")
            flash("Brand is Added Successfully","success")

        if not brand:
            flash("ADD Your Brand First And then ADD Category","warning")
            return redirect('/brand')
        
    allcategory=Category.query.all()
    allbrands=Brand.query.all()
    return render_template('category.html',allcategory=allcategory,allbrands=allbrands)

@app.route('/products',methods=['POST','GET'])
def products():
    if request.method=='POST':
        pid=request.form.get('pid')
        bcode=request.form.get('bcode')
        catname=request.form.get('catname')
        pname=request.form.get('pname')
        pcode=request.form.get('pcode')
        pdesc=request.form.get('pdesc')
        pcost=request.form.get('pcost')
        punit=request.form.get('punit')

        category=Category.query.filter_by(catname=catname).first()
        brand=Brand.query.filter_by(bcode=bcode).first()
        products=Product.query.filter_by(pid=pid).first()
        if products:
            flash("Product ID Already Exists","warnig")

        if category and brand:
            db.engine.execute(f"INSERT INTO `product` (`pid`,`bcode`,`catname`,`pname`,`pcode`,`pdesc`,`pcost`,`punit`) VALUES ('{pid}','{bcode}','{catname}','{pname}','{pcode}','{pdesc}','{pcost}','{punit}') ")
            flash("Product Is Successfully Added","success")
        else:
            flash("Brand Or Category Dosent Exist")
            return redirect('/brand')
    allcategory=Category.query.all()
    allproducts=Product.query.all()
    return render_template('products.html',allproducts=allproducts,allcategory=allcategory)

@app.route('/orders',methods=['POST','GET'])
def orders():
    if request.method=='POST':
        oid=request.form.get('oid')
        cname=request.form.get('cname')
        cpno=request.form.get('cpno')
        cemail=request.form.get('cemail')
        cadd=request.form.get('cadd')
        ccost=request.form.get('ccost')


        ooid=Orders.query.filter_by(oid=oid).first()

        if ooid:
            flash("Order ID Already Present, Please Chose Unique","warning")
            return redirect('/orders')

        db.engine.execute(f"INSERT INTO `orders` (`oid`,`cname`,`cpno`,`cemail`,`cadd`,`ccost`) VALUES ('{oid}','{cname}','{cpno}','{cemail}','{cadd}','{ccost}') ")
        flash("Order Considered, Now u can Checkout","success")

    allproducts=Product.query.all()
    return render_template('orders.html',allproducts=allproducts)



@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/test')
def test():
    try:
        a = Test.query.all()
        print(a)
        return f'database is connected'

    except Exception as e:
        print(e)
        return f'My database is not connected {e}'



if __name__=="__main__":
    app.run(debug=True)                  