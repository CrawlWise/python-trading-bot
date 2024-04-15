from django import forms
    
# create my python form class
class TradeInputForm(forms.Form):
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
    # buy_sell_btn = forms.BooleanField(label='Buy or Sell', required=False)
    limit_price = forms.DecimalField(label="Limit Price", decimal_places=2)
    quantity_field = forms.DecimalField(label="Quantity", decimal_places=2)
    limit_stop_values = forms.ChoiceField(choices=STOP_LIMIT_OPTIONS)
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