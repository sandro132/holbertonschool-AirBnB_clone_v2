#!/usr/bin/python3
"""This is the place class"""


import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """This is the class for Place"""
    __tablename__ = "places"
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column('amenity_id', String(60), ForeignKey
                                 ('amenities.id'), primary_key=True,
                                 nullable=False),
                          Column('place_id', String(60), ForeignKey
                                 ('places.id'), primary_key=True,
                                 nullable=False))

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # amenities = relationship("Amenity",
    # secondary="place_amenity", viewonly=False, back_populates="my_places")
    reviews = relationship("Review", cascade="all,delete", backref="place")
    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity",
                                 secondary="place_amenity", viewonly=False)

    else:

        @property
        def amenities(self):
            """
            amenety list with append method
            :return: list of amenity instances
            """
            amenity_list = []
            results = models.storage.all(Amenity)
            for amenity in results.values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """
            :param obj: ppends place id for amenities
            """
            if obj and isinstance(obj, Amenity):
                type(self).amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """
        Getter attribute reviews
        :return: the list of reviews
        """
        review_dict = {}
        objs_ = models.storage.all(Review)
        for key, value in objs_.items():
            if value.place_id == self.id:
                review_dict[key] = value
        return review_dict
