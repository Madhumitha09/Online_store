"""connect to db and get category"""
# Create your views here.

import logging
import re
from datetime import date
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Products
from .models import Users

from datetime import datetime

log = logging.getLogger("aspace_logger")
global response_dict
global forward_dict


@api_view(['GET'])
def health(request):
    """check server health"""
    json_response = {"status": "Success", "data": "Server is running"}
    return Response(json_response, status=200)


def get_user_status():
    pass


def get_user_level():
    pass


# Login API to be utilized to login user based on role
@api_view(['GET'])
def login():
    """write login mechanism here using 2F authentication (JSON Web Token)"""
    try:
        user_status = get_user_status()
        if (user_status == 'active'):
            user_level = get_user_level()
            if user_level == 'superadmin':
                print("superadmin user logged in")
            elif user_level == 'admin':
                print("admin user logged in")
            elif user_level == 'buyer':
                print("buyer user logged in")
            elif user_level == 'seller':
                print("seller user logged in")
            else:
                print("invalid user")

        return Response({"status": "Success"}, status=200)
    except Exception as e:
        return Response({"status": "Failure", "failure_reason": str(e)}, status=500)



# APIs to do CRUD operations
#Read operation demonstration
@api_view(['GET'])
def get_products():

    products = Products.objects.values('product_name', 'price', 'seller', 'inverntory_stock')

    data = list(products)

    response_dict = {}

    if len(data) == 0:
        print("No products available in DB")

    else:

        for x in range(len(data)):
            try:
                product_name = data[x]["product_name"]
                price = data[x]["price"]
                seller = data[x]["seller"]
                inverntory_stock = data[x]["inverntory_stock"]

                response_dict[x][product_name] = product_name
                response_dict[x][price] = price
                response_dict[x][seller] = seller
                response_dict[x][inverntory_stock] = inverntory_stock

            except Exception as e:
                print(e)

        return Response(
            {"status": "Success", "products": response_dict},
            status=200)

#Read operation demonstration
@api_view(['GET'])
def get_buyers():

    buyers = Products.objects.filter(user_type='buyer').values('user_id')

    data = list(buyers)

    response_dict = {}

    if len(data) == 0:
        print("No buyers available in DB")

    else:

        for x in range(len(data)):
            try:
                user_id = data[x]["user_id"]
                response_dict[x][user_id] = user_id

            except Exception as e:
                print(e)

        return Response(
            {"status": "Success", "buyers": response_dict},
            status=200)

#Read operation demonstration
@api_view(['GET'])
def get_sellers():

    buyers = Products.objects.filter(user_type='seller').values('user_id')

    data = list(buyers)

    response_dict = {}

    if len(data) == 0:
        print("No sellers available in DB")

    else:

        for x in range(len(data)):
            try:
                user_id = data[x]["user_id"]
                response_dict[x][user_id] = user_id

            except Exception as e:
                print(e)

        return Response(
            {"status": "Success", "sellers": response_dict},
            status=200)


#Create operation demonstration
@api_view(['GET'])
def add_sellers():

    sellers = Users.objects.filter(user_type='seller')
    sellers.objects.create(user_type = 'seller', user_id = 'abc123', password = 'xyz@123')


    return Response(
        {"status": "Success"},
        status=200)



#Update operation demonstration
@api_view(['GET'])
def update_product():
    products = Products.objects
    products.objects.filter(product_name = 'table').update(price='1500')

    return Response(
        {"status": "Success"},
        status=200)



# Delete operation demonstration
@api_view(['GET'])
def delete_product():
    products = Products.objects
    products.objects.filter(product_name='table').delete()

    return Response(
        {"status": "Success"},
        status=200)

