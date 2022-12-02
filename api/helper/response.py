from rest_framework.response import Response
from math import ceil
from ..configs.variable_response import *

def response_data(data=None, message='Success', status=1):
    return Response({
        'status_code': status,
        'message': message,
        'data':data
    })
    
def response_paginator(sum, per_page, data):
    result = {
        'max_page': ceil(sum/per_page),
        'list_data': data
    }
    return response_data(data=result)\
        
def validate_error(data={}, status=STATUS['TOKEN_EXPIRED']):
    # if data == {}:
    #     return response_data(status=STATUS['TOKEN_EXPIRED'], message='ERROR')
    data = dict(data)
    error_message = ''
    for key, value in data.items():
        error_message += str(key) + ' ' + str(list(value)[0])
    return response_data(status=status, message=error_message)