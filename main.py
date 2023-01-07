
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
    inventid=db.Column(db.String(100),primary_key=True)
    productname=db.Column(db.String(100))
    stockin=db.Column(db.Integer())
    stockout=db.Column(db.Integer())
    stockavail=db.Column(db.Integer())

class Sales(UserMixin,db.Model):
    sid=db.Column(db.String(100),primary_key=True)
    prodid=db.Column(db.String(100))
    cusname=db.Column(db.String(100))
    sdate=db.Column(db.String(100))
    saleqty=db.Column(db.Integer)

class Receiving(UserMixin,db.Model):
    rdate=db.Column(db.String(100))
    rid=db.Column(db.String(100),primary_key=True)
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
    prodqty=db.Column(db.Integer)

class Supplier(UserMixin,db.Model):
    supid=db.Column(db.String(100),primary_key=True)
    supname=db.Column(db.String(100))
    supcont=db.Column(db.String(100))
    supaddr=db.Column(db.String(100))

class Customer(UserMixin,db.Model):
    cusid=db.Column(db.String(100),primary_key=True)
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
        admins=Admin.query.filter_by(adminid=adminid).first()
        if admins and (admins.adminpw==adminpw):
            return redirect('/inventory')
        else:
            return 'Incorrect Password, Login failed'
    return render_template('adminlogin.html')

@app.route('/inventory')
def inventory():
    
    allproduct=Product.query.all()
    allsale=Sales.query.all()

    allinvents=Inventory.query.all()

    return render_template('inventory.html',allinvents=allinvents,allproduct=allproduct,allsale=allsale)


@app.route('/sales',methods=['POST','GET'])
def sales():
    if request.method=='POST':
        sid=request.form.get('sid')
        prodid=request.form.get('prodid')

        cusname=request.form.get('cusname')
        sdate=request.form.get('sdate')
        saleqty=request.form.get('saleqty')
        cusname=cusname.upper()
        sales=Sales.query.filter_by(sid=sid).first()
        

        if sales:
            flash("Sales ID already Exists","warning")
            return render_template("sales.html")


        new_user=db.engine.execute(f"INSERT INTO `sales` (`sid`,`prodid`,`cusname`,`saleqty`,`sdate`) VALUES ('{sid}','{prodid}','{cusname}','{saleqty}','{sdate}') ")
        flash("Sales Details is Added Successfully","success")

    allproduct=Product.query.all()
    allsales=Sales.query.all()
    return render_template("sales.html",allsales=allsales,allproduct=allproduct)



@app.route('/receiving',methods=['POST','GET'])
def receiving():
    if request.method=='POST':
        rid=request.form.get('rid')
        supname=request.form.get('supname')
        rdate=request.form.get('rdate')
        supname=supname.upper()
        receive=Receiving.query.filter_by(rid=rid).first()
        if receive:
            flash("Receive ID already Exists","warning")
            return render_template("receivig.html")

        
        new_user=db.engine.execute(f"INSERT INTO `receiving` (`rid`,`supname`,`rdate`) VALUES ('{rid}','{supname}','{rdate}') ")
        flash("Sales Details is Added Successfully","success")

    allreceive=Receiving.query.all()
    return render_template('receiving.html',allreceive=allreceive)




@app.route('/category',methods=['POST','GET'])
def category():
    if request.method=='POST':
        cid=request.form.get('cid')
        catname=request.form.get('catname')
        catname=catname.upper()
        category=Category.query.filter_by(cid=cid).first()
        if category:
            flash("Category already Exists","warning")
            return render_template("category.html")

        new_user=db.engine.execute(f"INSERT INTO `category` (`cid`,`catname`) VALUES ('{cid}','{catname}') ")
        flash("Category is Added Successfully","success")
    allcategory=Category.query.all()
    return render_template('category.html',allcategory=allcategory)



@app.route('/productlist',methods=['POST','GET'])
def productlist():
    if request.method=='POST':
        pid=request.form.get('pid')
        catname=request.form.get('catname')
        catname=catname.upper()

        pname=request.form.get('pname')
        pname=pname.upper()

        pdesc=request.form.get('pdesc')
        prodqty=request.form.get('prodqty')
        pprice=request.form.get('pprice')

        product=Product.query.filter_by(pid=pid).first()

        if product:
            flash("Product already Exists","warning")
            return render_template("productlist.html")
        new_user=db.engine.execute(f"INSERT INTO `product` (`pid`,`catname`,`pname`,`pdesc`,`prodqty`,`pprice`) VALUES ('{pid}','{catname}','{pname}','{pdesc}','{prodqty}','{pprice}') ")
        flash("Product is Added Successfully","success")
    allproduct=Product.query.all()
    allcategory=Category.query.all()
    return render_template('productlist.html',allproduct=allproduct,allcategory=allcategory)

@app.route('/supplier',methods=['POST','GET'])
def supplier():
    if request.method=='POST':
        supid=request.form.get('supid')
        supname=request.form.get('supname')
        supname=supname.upper()

        supcont=request.form.get('supcont')
        supaddr=request.form.get('supaddr')

        supplier=Supplier.query.filter_by(supid=supid).first()

        if supplier:
            flash("Supplier already Exists","warning")
            return render_template("productlist.html")

        new_user=db.engine.execute(f"INSERT INTO `supplier` (`supid`,`supname`,`supcont`,`supaddr`) VALUES ('{supid}','{supname}','{supcont}','{supaddr}') ")
        flash("Supplier is Added Successfully","success")
    
    allsupplier=Supplier.query.all()
    return render_template('supplier.html',allsupplier=allsupplier)

@app.route('/customer',methods=['POST','GET'])
def customer():
    if request.method=='POST':
        cusid=request.form.get('cusid')
        cusname=request.form.get('cusname')
        cusname=cusname.upper()

        cuscont=request.form.get('cuscont')
        cusaddr=request.form.get('cusaddr')

        customer=Customer.query.filter_by(cusid=cusid).first()

        if customer:
            flash("Customer already Exists","warning")
            return render_template("customer.html")
        new_user=db.engine.execute(f"INSERT INTO `customer` (`cusid`,`cusname`,`cuscont`,`cusaddr`) VALUES ('{cusid}','{cusname}','{cuscont}','{cusaddr}') ")
        flash("Customer is Added Successfully","success")
    allcustomer=Customer.query.all()
    
    return render_template('customer.html',allcustomer=allcustomer)

@app.route('/iedit/<string:inventid>',methods=['POST','GET'])
def iedit(inventid):
    invents=Inventory.query.filter_by(inventid=inventid).first()

    if request.method=='POST':
        inventid=request.form.get('inventid')
        productname=request.form.get('productname')
        stockin=request.form.get('stockin')
        stockout=request.form.get('stockout')
        stockavail=request.form.get('stockavail')
        db.engine.execute(f"UPDATE `inventory` SET `inventid` ='{inventid}',`productname`='{productname}',`stockin`='{stockin}',`stockout`='{stockout}',`stockavail`='{stockavail}' WHERE `inventid`='{inventid}'")
        flash("Inventory Updated","info")
        return redirect("/inventory")

    return render_template('iedit.html',invents=invents)

@app.route("/idelete/<string:inventid>",methods=['POST','GET'])
def hdelete(inventid):
    db.engine.execute(f"DELETE FROM `inventory` WHERE `inventid`={inventid}")
    flash("Date Deleted","danger")
    return redirect("/inventory")

@app.route('/sedit/<string:sid>',methods=['POST','GET'])
def sedit(sid):
    sales=Sales.query.filter_by(sid=sid).first()

    if request.method=='POST':
        sid=request.form.get('sid')
        prodid=request.form.get('prodid')
        cusname=request.form.get('cusname')
        saleqty=request.form.get('saleqty')
        sdate=request.form.get('sdate')
        db.engine.execute(f"UPDATE `sales` SET `sid` ='{sid}',`prodid`='{prodid}',`cusname`='{cusname}',`saleqty`='{saleqty}',`sdate`='{sdate}' WHERE `sid`='{sid}'")
        flash("Sales Updated","info")
        return redirect("/sales")

    return render_template('sedit.html',sales=sales)

@app.route("/sdelete/<string:sid>",methods=['POST','GET'])
def sdelete(sid):
    db.engine.execute(f"DELETE FROM `sales` WHERE `sid`='{sid}'")
    flash("Data Deleted","danger")
    return redirect("/sales")

    
@app.route('/redit/<string:rid>',methods=['POST','GET'])
def redit(rid):
    receives=Receiving.query.filter_by(rid=rid).first()

    if request.method=='POST':
        rid=request.form.get('rid')
        supname=request.form.get('supname')
        rdate=request.form.get('rdate')
        db.engine.execute(f"UPDATE `receiving` SET `rid` ='{rid}',`supname`='{supname}',`rdate`='{rdate}' WHERE `rid`='{rid}'")
        flash("Rceiving Updated","info")
        return redirect("/receiving")

    return render_template('redit.html',receives=receives)

@app.route("/rdelete/<string:rid>",methods=['POST','GET'])
def rdelete(rid):
    db.engine.execute(f"DELETE FROM `receiving` WHERE `rid`='{rid}'")
    flash("Data Deleted","danger")
    return redirect("/receiving")



@app.route('/pedit/<string:pid>',methods=['POST','GET'])
def pedit(pid):
    products=Product.query.filter_by(pid=pid).first()

    if request.method=='POST':
        pid=request.form.get('pid')
        catname=request.form.get('catname')
        pname=request.form.get('pname')
        pdesc=request.form.get('pdesc')
        prodqty=request.form.get('prodqty')
        pprice=request.form.get('pprice')

        db.engine.execute(f"UPDATE `product` SET `pid` ='{pid}',`catname`='{catname}',`pname`='{pname}',`pdesc`='{pdesc}',`prodqty`='{prodqty}',`pprice`='{pprice}' WHERE `pid`='{pid}'")
        flash("Products Updated","info")
        return redirect("/productlist")

    return render_template('pedit.html',products=products)


@app.route("/pdelete/<string:pid>",methods=['POST','GET'])
def pdelete(pid):
    db.engine.execute(f"DELETE FROM `product` WHERE `pid`='{pid}'")
    flash("Data Deleted","danger")
    return redirect("/productlist")



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