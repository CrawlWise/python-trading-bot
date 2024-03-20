# mport Alpaca api
import time
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest, QueryOrderStatus
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.requests import LimitOrderRequest
import alpaca_trade_api as tradeapi
from alpaca_trade_api import TimeFrame, TimeFrameUnit
import os
import requests
from dotenv import load_dotenv


# Load .env files that stores the API key, API secret, and base URL
load_dotenv()

# Import the API key, API secret, and the base URL
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
base_url = os.getenv("BASE_URL")

api = tradeapi.REST(api_key, api_secret, base_url, api_version="v2")
trading_client = TradingClient(api_key=api_key, secret_key=api_secret, paper=True)

# Get users data
def get_user_account():
    try:
        account = api.get_account()
        print(account)
    except Exception as e:
        print(e)

def limit_buy_sell_stock(symbol, limit_price, quantity,order_side,time_in_force):

    """
    If you have a specific target price at which you want to buy or sell an asset,
    a limit order allows you to specify that price and wait for the market to reach it.
    This is particularly useful when you have a target entry or exit point based on your
    analysis or trading strategy.

    type: str("Limit")
    symbol: "SPY", "AAPL"
    limit_price: float
    qty: float
    side: OrderSide.BUY, OrderSide.SELL #This returns a function
    time_in_force: TimeInForce.DAY, TimeInFocrc.FOK # this returns a function
    :return 0:
    """
    limit_order_data = LimitOrderRequest(
        type="Limit", # value: Limit
        symbol=symbol, # value: SPY, AAPL
        limit_price=int(limit_price), # the limit price of the stock
        qty=int(quantity), # value: 1, 10, or 200
        side=order_side, # this takes a function of OrderSide.BUY or orderSide.SELL
        time_in_force=time_in_force # this takes a function of TimeInForce.DAY, TimeInForce.FOK, TimeInForce.GTC etc
    )
    # Limit order
    limit_order = trading_client.submit_order(
        order_data=limit_order_data
    )

def query_all_order(order_status, order_side):
    """
    status: QueryOrderStatus.OPEN, QueryOrderStatus.CLOSED #This requires a function
    side: OrderSide.SELL, OrderSide.BUY #This requires a functions
    :return:
    """
    # params to filter orders by
    request_params = GetOrdersRequest(
        status=order_status,  # value: QueryOrderStatus.CLOSED or QueryOrderStatus.OPEN
        side=order_side  # value: OrderSide.SELL or OrderSide.BUY
    )
    # orders that satisfy params
    orders = trading_client.get_orders(filter=request_params)
    print(orders)

def cancel_submitted_orders(self):
    # attempt to cancel all open orders
    cancel_statuses = trading_client.cancel_orders()
    return cancel_statuses

def create_order_request(side, type, time_in_force, symbol, qty):
    url = "https://paper-api.alpaca.markets/v2/orders"

    payload = {
        "side": side,  # Sell
        "type": type,  # Market
        "time_in_force": time_in_force,  # day
        "symbol": symbol,  # TSLA
        "qty": str(qty),  # 10
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": api_secret,
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)


# Get barset from Alpaca API
def get_candles():
    symbol = "SPY"
    candles = api.get_bars(
        symbol, TimeFrame(1, TimeFrameUnit.Minute), "2024-02-17", adjustment="raw"
    ).df
    return candles


def signal_generator(df):
    data_frame = df
    open = data_frame.iloc[-1].open
    close = data_frame.iloc[-1].close
    high = data_frame.iloc[-1].high
    low = data_frame.iloc[-1].low

    previous_open = data_frame.iloc[-2].open
    previous_close = data_frame.iloc[-2].close
    previous_high = data_frame.iloc[-2].high
    previous_low = data_frame.iloc[-2].low
    
    
    # Checking for bullish and bearish engulfing pattern
    bullish_body_size = abs(open) - close
    bearish_body_size = abs(previous_open) - previous_close

    if (
        bullish_body_size > bearish_body_size
        and open > previous_close
        and close > previous_open
    ):
        print(f'Bearish: {bearish_body_size} bullish: {bullish_body_size}\nOpen:{open} Previous_open {previous_open}\nClose: {close} Previous_close {previous_close}')
        return 1
    elif (
        bearish_body_size > bullish_body_size
        and open < previous_open
        and close < previous_open
    ):
        print(f'Bearish: {bearish_body_size} bullish: {bullish_body_size}\nOpen:{open} Previous_open {previous_open}\nClose: {close} Previous_close {previous_close}')
        return 2
    else:
        return 0


# print(signal_generator(get_candles()))
# # print(get_candles())
def start_trading():
    # Get the signal
    signal = signal_generator(get_candles())
    if signal == 1:
        print("Bullish Pattern identify. Start buying")
    elif signal == 2:
        print("Bearish patter has been identify. Good time to buy")
    else:
        print("Market is unstable at this time")

if __name__ == "__main__":
    while True:
        start_trading()
        time.sleep(2 * 60)
  
# create_order_request("buy", "market", "day", "AAPL", 10)
