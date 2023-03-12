from . import db
#from werkzeug.security import generate_password_hash




class Properties(db.Model):
    
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(80))
    rooms = db.Column(db.Integer)
    baths = db.Column(db.Integer)
    location = db.Column(db.String(80))
    price = db.Column(db.String(15))
    propType = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(200)) 
    
    
    
    def __init__ (self, title, rooms, baths, location, price, propType, description, image = None):
        self.title = title
        self.rooms = rooms
        self.baths = baths
        self.location = location
        self.price = price
        self.propType = propType
        self.description = description
        self.image = image