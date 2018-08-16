import json
from pythonrestsdk.orders import OrdersAuthorizeRequest
from pythonrestsdk.core.skeleton import Skeleton


class Authorize(Skeleton):
    @staticmethod
    def build_request_body():
        return json.loads('{}')

    def authorize_order(self, order_id, debug=False):
        request = OrdersAuthorizeRequest(order_id)
        request.authorization('Bearer ' + self.authToken())
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Order ID: ', response.result.id
            print 'Authorization ID:', response.result.purchase_units[0].payments.authorizations[0].id
            print 'Links:'
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print 'Authorization Links:'
            for link in response.result.purchase_units[0].payments.authorizations[0].links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print "Buyer:"
            print "\tEmail Address: {}\n\tName: {}\n\tPhone Number: {}".format(response.result.payer.email_address,
                                                                               response.result.payer.name.given_name + " " + response.result.payer.name.surname,
                                                                               response.result.payer.phone.phone_number.national_number)
        return response


if __name__ == "__main__":
    order_id = '1AL141024Y8279459'
    Authorize().authorize_order(order_id, debug=True)