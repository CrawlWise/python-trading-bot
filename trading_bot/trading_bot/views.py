from django.shortcuts import render
from .form import TradeInputForm, TradeMarketForm, TradeStopLossForm

def landing(request):
    # Initialize form with request data (if any)
    form_stop_loss = TradeStopLossForm(request.POST or None)
    form_market = TradeMarketForm(request.POST or None)
    form = TradeInputForm(request.POST or None)

    if request.method == "POST":        
        if form.is_valid():
            # Access cleaned form data
            show_all_stocks = form.cleaned_data.get('limit_stop_values')
            show_limit_price = form.cleaned_data.get('limit_price')
            show_qty_price = form.cleaned_data.get('quantity_field')
            total = form.cleaned_data.get('total')

            print(show_qty_price)
            print(show_all_stocks)
            print(show_limit_price)
            print(total)
            
        if form_market.is_valid():
            # Process TradeMarketForm data
            market_price = form_market.cleaned_data.get('market_price')
            quantity_field = form_market.cleaned_data.get('quantity_field_market')
            market_total = form_market.cleaned_data.get('market_total')
            print(market_price, quantity_field, market_total)
            
        if form_stop_loss.is_valid():
            triggers = form_stop_loss.cleaned_data.get('triggers')
            distance = form_stop_loss.cleaned_data.get('distance')
            stop_loss_totatl = form_stop_loss.cleaned_data.get('stop_loss_quantity')
            stop_loss_total = form_stop_loss.cleaned_data.get('stop_loss_total')
            print(triggers, distance,stop_loss_totatl, stop_loss_total )
        else:
            print(form_stop_loss.errors)
    
        

    return render(request, 'landing.html', {'form': form, 'form_market': form_market, 'form_stop_loss': form_stop_loss})
