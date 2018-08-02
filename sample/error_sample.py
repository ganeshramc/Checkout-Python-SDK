from skeleton import Skeleton
import os
import json
from pythonsdk.orders import OrdersCreateRequest
from braintreehttp.http_error import HttpError
class CreateError(Skeleton):

    def create_error_1(self):
        """
        Body has no required parameters (intent, purchase_units)
        """
        body = """{}"""
        request = OrdersCreateRequest()
        request.authorization(os.environ.get('PAYPAL_AUTHENTICATION_TOKEN'))
        request.request_body(json.loads(body))
        print "Request Body:", body
        print "Response:"
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code: ", h.status_code
            message = json.loads(h.message)
            print "Debug ID: ", message['debug_id']
            print "Details:\n\tName: ", message['name']
            print "\tMessage:", message['message']
            print "\tProblems:"
            for i, detail in enumerate(message['details']):
                print "\t\t{}. Field: \"{}\"\tIssue: {}".format(i+1,detail['field'], detail['issue'])

    def create_error_2(self):
        """
        Authorization header has an empty string
        """
        body = """\n{\n\t"intent": "CAPTURE",\n\t"purchase_units": [\n\t\t{"amount": \n\t\t\t{\n\t\t\t\t"currency_code": "USD",\n\t\t\t\t"value": "100.00"\n\t\t\t}\n\t\t}\n\t]\n}"""
        print "Request Body:", body
        request = OrdersCreateRequest()
        request.authorization("")
        request.request_body(json.loads(body))
        print "Response:"
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code: ", h.status_code
            message = json.loads(h.message)
            print "Details:\n\tName: ", message['name']
            print "\tMessage:", message['message']


    #Todo: dump all in the response
    def create_error_3(self):
        """
        Body has invalid parameter value
        """
        body = """\n{\n\t"intent": "INVALID",\n\t"purchase_units": [\n\t\t{"amount": \n\t\t\t{\n\t\t\t\t"currency_code": "USD",\n\t\t\t\t"value": "100.00"\n\t\t\t}\n\t\t}\n\t]\n}"""
        request = OrdersCreateRequest()
        request.authorization(os.environ.get('PAYPAL_AUTHENTICATION_TOKEN'))
        request.request_body(json.loads(body))
        print "Request Body:", body
        print "Response:"
        response = ""
        try:
            response = self.client.execute(request)
        except HttpError as h:
            print "Status Code: ", h.status_code
            message = json.loads(h.message)
            print "Debug ID: ", message['debug_id']
            print "Details:\n\tName: ", message['name']
            print "\tMessage:", message['message']
            print "\tProblems:"
            for i, detail in enumerate(message['details']):
                print "\t\t{}. Field: \"{}\"\tIssue: {}".format(i+1,detail['field'], detail['issue'])


print "Calling create_error_1..."
CreateError().create_error_1()

print "\nCalling create_error_2..."
CreateError().create_error_2()

print "\nExecuting create_error_3..."
CreateError().create_error_3()