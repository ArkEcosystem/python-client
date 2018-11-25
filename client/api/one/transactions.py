from client.exceptions import ArkParameterException
from client.resource import Resource


class Transactions(Resource):

    def get(self, transaction_id):
        return self.request_get('transactions/get', {'id': transaction_id})

    def all(self, limit=100, offset=None, block_id=None, type=None, order_by=None, sender_public_key=None,
            vendor_field=None, owner_public_key=None, owner_address=None, sender_id=None, recipient_id=None,
            amount=None, fee=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
            'blockId': block_id,
            'type': type,
            'orderBy': order_by,
            'senderPublicKey': sender_public_key,
            'vendorField': vendor_field,
            'ownerPublicKey': owner_public_key,
            'ownerAddress': owner_address,
            'senderId': sender_id,
            'recipientId': recipient_id,
            'amount': amount,
            'fee': fee
        }
        return self.request_get('transactions', params)

    def get_unconfirmed(self, transaction_id):
        return self.request_get('transactions/unconfirmed/get', {'id': transaction_id})

    def all_unconfirmed(self, limit=100, offset=None):
        if limit > 100:
            raise ArkParameterException('Maximum number of objects to return is 100')
        params = {
            'limit': limit,
            'offset': offset,
        }
        return self.request_get('transactions/unconfirmed', params)
