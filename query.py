"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

"""The data type that will be returned is a list of tuples."""

# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

"""An association table is a table that acts as the glue between two
tables. It sits in between two tables that with out the association
table would have no meaningful rows shared between them. It allows both 
of the tables to have a one to many relationship. Typically you would 
put an """


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the brand_id of ``ram``.
q1 = Brand.query.filter_by(brand_id='ram').all()

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year>1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with ``Cor``.
q5 = Model.query.filter(Model.name.like('Car%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded=1903, Brand.discontinued != None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded<1950)).all()

# Get all models whose brand_id is not ``for``.
q8 = Model.query.filter(Model.brand_id.isnot('for')).all()



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    #year_input = raw_input('Please enter the model year you are looking for: ')

    model_info = Model.query.all()

    for model in model_info:
        if model.brand.year=year:
            print "\n%s %s %s\n" % (model.brand.name, model.name, model.headquarters)


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brand_model = Brand.query.all()

    for brand in brand_model:
        brand_name = brand.name
        if brand.name = brand_name:
            print "\n%s" % (brand.name)
        else:
            print "\n%s, %s" % (brand.brand.name, brand.brand.year)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    #name_input = raw_input("Please enter the brand you are looking for: ")

    brand_string = Brand.query.filter(Brand.name.like(%mystr%)).all()

    for brand in brand_string:
        print '\n%s' % (brand.name)



def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    # start_year = raw_input("Please enter your start year: ")
    # end_year = raw_input("Please enter your end year: ")

    start_end = Model.query.filter((Model.year >= start_year) & (Model.year <= end_year)).all()

    for start in start_end:
        print '\n%s' % (Model.name)

