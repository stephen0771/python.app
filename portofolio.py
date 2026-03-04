"""from datetime import datetime
class User(db.model):
    id=db.colomn(db.integer,primary_key=True)
    username=db.column(db.string(64),unique=True,nullable=False)
    email=db.column(db.string(128),unique=True,nullable=False)
    password_hash=db.column(db.string(128),nullable=False)
    budgets=db.relationship('Investment',backref='user',lazy=True)
    investments=db.relationship('investment',backref='user',lazy=True)
class Budget(db.model):
    id=db.column(db.integer,primary_key=True)
    user_id=db.column(db.integer,db.foreignkey('user.id'),nullable=False)
    category=db.column(db.string(64),nullable=False)
    amount=db.column(db.float,nullable=False)
    created_at=db.column(db.Datetime,nullable=False,default=datetime.utcnow)


class investment(db.model):
    id=db.column(db.integer,primary_key=True)
    user_id=db.column(db.integer,db.foreignkey('user.id'),nullable=False)
    symbol=db.column(db.string(10),nullable=False)
    shares  =db.column(db.float,nullable=False)
    purchase_price=db.column(db.float,nullable=False)
    created_at=db.column(db.Datetime,nullable=False,default=datetime.utcnow)

class loans(db.model):
    id=db.column(db.integer,primary_key=True)
    user_id=db.column(db.integer,db.foreignkey('user.id'),nullable=False)
    amount=db.column(db.string(10),nullable=False)
    installment =db.column(db.float,nullable=False)
    new.amount=db.column(db.float,nullable=False)
    created_at=db.column(db.Datetime,nullable=False,default=datetime.utcnow)"""


from turtle import*
width(2)
circle(radius=64)
write("hello Bro")
bgcolor("black")
colormode(255)
speed(0)
hideturtle()
pencolor("chartreuse")
for i in range(260):
    r = (i * 2) % 255
    g = (i *3) % 245
    b =(i * 3) % 255
    forward(i * 1.5)
    right(151)
done()

