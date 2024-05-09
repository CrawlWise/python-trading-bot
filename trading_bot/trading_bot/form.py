from django import forms
    
# create my python form class

class BtnSellBuyTradeOption(forms.Form):
    STOP_LIMIT_OPTIONS = (
        ('limit', 'Limit'),
        ('market', 'Market'),
        ('stop_loss', 'Stop Loss'),
        # ('stop_loss_limit', 'Stop Loss Limit'),
        # ('take_profit', 'Take Profit'),
        # ('Take_profit_limit', 'Take Profit Limit'),
        # ('Iceberg', 'Iceberg'),
        # ('Trailing_stop', 'Trailing Stop'),
        
    )
    limit_stop_values = forms.ChoiceField(choices=STOP_LIMIT_OPTIONS)
    
class TradeInputForm(forms.Form):
    limit_price = forms.DecimalField(label="Limit Price", decimal_places=2)
    quantity_field = forms.DecimalField(label="Quantity", decimal_places=2)
    total = forms.DecimalField(label='Total', decimal_places=2)
    
    
class TradeMarketForm(forms.Form):
     # buy_sell_btn = forms.BooleanField(label='Buy or Sell', required=False)
    market_price = forms.DecimalField(label="Market Price", decimal_places=2)
    quantity_field_market = forms.DecimalField(label="Quantity", decimal_places=2)
    market_total = forms.DecimalField(label='Total', decimal_places=2)
    
class TradeStopLossForm(forms.Form):
    triggers = forms.DecimalField(label="Trigger", decimal_places=2)
    distance = forms.DecimalField(label="Distance", decimal_places=2)
    stop_loss_quantity = forms.DecimalField(label="Quantity", decimal_places=2)
    stop_loss_total = forms.DecimalField(label="Total", decimal_places=2)
    
    
class StocksTable(forms.Form):
    stock_name = forms.CharField(max_length=50)
    stock_quantity = forms.DecimalField(decimal_places=2)
    stock_open = forms.DecimalField(decimal_places=2)
    stock_close = forms.DecimalField(decimal_places=2)


class Filters(forms.Form):
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()