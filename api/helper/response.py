from rest_framework.response import Response

def response_data(data=None, message='Success', status=1):
    return Response({
        'status_code': status,
        'message': message,
        'data':data
    })