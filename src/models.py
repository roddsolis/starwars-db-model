from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

# Resto de tus importaciones y definiciones de clases


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200),  nullable=False)

    # Relación uno a muchos con Planets, Characters y Vehicles
    planets = relationship('Favorites', backref='user')
    characters = relationship('Favorites', backref='user')
    vehicles = relationship('Favorites', backref='user')


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    birth_year = Column(String, nullable=False)

    # Relación uno a muchos con Favorites
    favorites = relationship('Favorites', backref='character')


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    population = Column(String, nullable=False)
    terrain = Column(String, nullable=False)

    # Relación uno a muchos con Favorites
    favorites = relationship('Favorites', backref='planet')


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    passengers = Column(String, nullable=False)

    # Relación uno a muchos con Favorites
    favorites = relationship('Favorites', backref='vehicle')


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))

    # Relaciones muchos a uno con User, Planets, Characters y Vehicles
    user = relationship('User', backref='planets')
    planet = relationship('Planets', backref='favorites')
    character = relationship('Characters', backref='favorites')
    vehicle = relationship('Vehicles', backref='favorites')


def to_dict(self):
    return {}
