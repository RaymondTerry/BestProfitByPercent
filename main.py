from requests import Request, Session
import json
import api_key


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

headers = {'Accepts':'application/json',
           'X-CMC_PRO_API_KEY': api_key.KEY}

session = Session()
session.headers.update(headers)


class main:

    def __init__(self):
     self.eos_target = 87.00
     self.xrp_target = 9.55
     self.bch_target = 9000.00
     self.dash_target = 2800.00


    def getTarget(self):
        return self.eos_target
        return self.xrp_target
        return self.bch_target
        return self.dash_target

#""" Evaluates if the desired target is still greater than the current price. """
    def __gt__(self):
        if self.eos_target > EOSUSD:
            print('EOS target is not close.')
        else:
            print('EOS TARGET IS CLOSE!')
#------------------------------------------------#
        if self.xrp_target > XRPUSD:
            print('XRP target is not close.')
        else:
            print('XRP TARGET IS CLOSE!')
#------------------------------------------------#
        if self.bch_target > BCHUSD:
            print('BCH target is not close.')
        else:
            print('BCH TARGET IS CLOSE!')
#------------------------------------------------#
        if self.dash_target > DASHUSD:
            print('DASH target is not close.')
        else:
            print('DASH TARGET IS CLOSE!')




#""" Evaluates the highest remaining percentage of profit left in a particular asset based on the predetermined target. """

    def percentEval(self):
        if self.eos_target and self.xrp_target and self.bch_target and self.dash_target != 0:
            
            eos_margin = (abs(self.eos_target - EOSUSD) / EOSUSD) * 100
            xrp_margin = (abs(self.xrp_target - XRPUSD) / XRPUSD) * 100
            bch_margin = (abs(self.bch_target - BCHUSD) / BCHUSD) * 100
            dash_margin = (abs(self.dash_target - DASHUSD) / DASHUSD) * 100


            if eos_margin > max(xrp_margin, bch_margin, dash_margin):
                    print(str("{0:.2f}".format(eos_margin)) + '% on EOS')
            elif xrp_margin > max(eos_margin, bch_margin, dash_margin):
                    print(str("{0:.2f}".format(xrp_margin)) + '% on XRP')
            elif bch_margin > max(eos_margin, xrp_margin, dash_margin):
                    print(str("{0:.2f}".format(bch_margin)) + '% on BCH')
            elif dash_margin > max(eos_margin, xrp_margin, bch_margin):
                    print(str("{0:.2f}".format(dash_margin)) + '% on DASH')


        else:
            return "By some anomaly you have lost 100% on one of your assets or wanted something to go to zero."































#""" Fn's to get asset price data """

def getEosPrice():

    parameters = {
              #Changeable#
        'symbol':'eos',
        'convert':'USD'
    }

    assetData = session.get(url, params=parameters)
                                                ###
    price = json.loads(assetData.text)['data']['EOS']['quote']['USD']['price']
    
    return price


EOSUSD = getEosPrice()

#------------------------------------------------------------------------------#

def getXrpPrice():


        parameters = {
            'symbol':'xrp',
            'convert':'USD'
        }

        assetData = session.get(url, params=parameters)

        price = json.loads(assetData.text)['data']['XRP']['quote']['USD']['price']
        
        return price

XRPUSD = getXrpPrice()

#------------------------------------------------------------------------------#

def getBchPrice():

    parameters = {
        'symbol':'bch',
        'convert':'USD'
        }

    assetData = session.get(url, params=parameters)

    price = json.loads(assetData.text)['data']['BCH']['quote']['USD']['price']
    
    return price

BCHUSD = getBchPrice()

#------------------------------------------------------------------------------#

def getDashPrice():

    parameters = {
        'symbol':'dash',
        'convert':'USD'
        }

    assetData = session.get(url, params=parameters)

    price = json.loads(assetData.text)['data']['DASH']['quote']['USD']['price']
    
    return price

DASHUSD = getDashPrice()





r = main()
r.percentEval()
