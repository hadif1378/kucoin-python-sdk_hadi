
#%% import libs
import kucoin.client as kc

#%% api keys
api_key = "64441c25ba02b40001f977cb"
api_secret = '8aaf99d1-ae1d-4b9f-abab-6b79afa5ade6'
api_passphrase = "@9628983Hadi"



#%% making market object
market = kc.Market(url='https://openapi-sandbox.kucoin.com')

# client = kc.Market(is_sandbox=True)
# client = Market(url='https://api.kucoin.com')

#%% get symbol kline

klines = market.get_kline('BTC-USDT','5min')
# get symbol ticker
server_time = market.get_server_timestamp()

#%% making trade object 

trade = kc.Trade(api_key, api_secret,
                  api_passphrase, is_sandbox=True)

#%% making trade order
# client = Trade(key='', secret='', passphrase='', is_sandbox=False, url='')
# or connect to Sandbox

print(trade.get_recent_orders())

# place a limit buy order
# place a market buy order   Use cautiously
order_id = trade.create_market_order('BTC-USDT', 'buy', size='1' )

#%% cancel order
trade.cancel_order(order_id)

#%% making user object

user = kc.User(api_key, api_secret, api_passphrase , is_sandbox=True)

#%% checking assest
accs = user.get_account_list()
print(accs)

# # or connect to Sandbox
# # client = User(api_key, api_secret, api_passphrase, is_sandbox=True)

# address = client.get_withdrawal_quota('KCS')
# %%
