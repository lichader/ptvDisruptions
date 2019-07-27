from hashlib import sha1
import hmac
import binascii

host = "timetableapi.ptv.vic.gov.au"
api_version = "v3"

disruption_at_stop = "disruptions/route/5/stop/1192"

class UrlBuilder:

    def __init__(self, api_key, developer_id):
        self.__api_key = api_key
        self.__developer_id = developer_id

    def calculateSignature(self, url): 
        url = url + ('&' if ('?' in url) else '?')
        
        raw = url+'devid={0}'.format(self.__developer_id)

        key_bytes = bytes(self.__api_key, 'latin-1')
        url_bytes = bytes(raw, 'latin-1')
        hashed = hmac.new(key_bytes, url_bytes, sha1)
        signature =  hashed.hexdigest()
        return signature.upper()
    
    def compose(self, resouce):
        pass
