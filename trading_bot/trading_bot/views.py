from django.shortcuts import render
from .form import TradeInputForm, TradeMarketForm, TradeStopLossForm, BtnSellBuyTradeOption, StocksTable, Filters
from . import app


def landing(request):
    # Initialize form with request data (if any)
    # trading_app = app.start_trading()
    SellBuyTradeOption = BtnSellBuyTradeOption(request.POST or None)
    form_stop_loss = TradeStopLossForm(request.POST or None)
    form_market = TradeMarketForm(request.POST or None)
    form = TradeInputForm(request.POST or None)
    stock_table = StocksTable(request.POST or None)
    filters_option = Filters(request.POST or None)

    # Initialize limit_options with a default value
    limit_options = None  # Or use any appropriate default value
    if request.method == "POST":
        if SellBuyTradeOption.is_valid():
            limit_options = SellBuyTradeOption.cleaned_data.get('limit_stop_values')

        if form.is_valid():
            # Access cleaned form data
            show_limit_price = form.cleaned_data.get('limit_price')
            show_qty_price = form.cleaned_data.get('quantity_field')
            total = form.cleaned_data.get('total')

            print(show_qty_price)
            print(show_limit_price)
            print(total)
            print(limit_options)  # Check the value of limit_options here

        if form_market.is_valid():
            # Process TradeMarketForm data
            market_order = 'market'
            market_price = form_market.cleaned_data.get('market_price')
            quantity_field = form_market.cleaned_data.get('quantity_field_market')
            market_total = form_market.cleaned_data.get('market_total')
            print(market_price, quantity_field, market_total, market_order)
           

        if form_stop_loss.is_valid():
            market_order = 'stop_loss'
            triggers = form_stop_loss.cleaned_data.get('triggers')
            distance = form_stop_loss.cleaned_data.get('distance')
            stop_loss_quantity = form_stop_loss.cleaned_data.get('stop_loss_quantity')
            stop_loss_total = form_stop_loss.cleaned_data.get('stop_loss_total')
            print(f"{triggers}\n{distance}\n{stop_loss_quantity}\n{stop_loss_total}\n{market_order}")

        if stock_table.is_valid():
            get_stock_name = stock_table.cleaned_data.get('stock_name')
            get_stock_quantity = stock_table.cleaned_data.get('stock_quantity')
            get_stock_open = stock_table.cleaned_data.get('stock_open')
            get_stock_close = stock_table.cleaned_data.get('stock_close')

            print(get_stock_name)
            print(get_stock_quantity)
            print(get_stock_open)
            print(get_stock_close)

        if filters_option.is_valid():
            get_start_date = filters_option.cleaned_data.get('start_date')
            get_end_date = filters_option.cleaned_data.get('end_date')

            print(get_start_date)
            print(get_end_date)
            
    # Setting up the app to buy get all stocks in the Alpaca platform
    

    return render(request, 'landing.html', {
        'form': form,
        'form_market': form_market,
        'form_stop_loss': form_stop_loss,
        'SellBuyTradeOption': SellBuyTradeOption,
        'limit_options': limit_options,  # Pass limit_options to the template context
        'stock_table': stock_table
        # 'app': trading_app
    })

def history(request):
    return render(request, 'history.html')
def portfolio(request):
    return render(request, 'portfolio.html')