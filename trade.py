#!/usr/local/bin/python
# coding: latin-1
import os, sys, time
import mercadobitcoin
mbtc2 = mercadobitcoin.Api()
 
from mercadobitcoin import TradeApi
mbtc = TradeApi("b1922f932cdacbd4a342b5fa3cd45e9c","69ef037e86dd30e37edf7609976c6130d341657c3feca236941e7a70b109ed1d")

for i in range(1,10):
    print("Contador: " + str(i))
    # Acessa o Ticker
    vticker = mbtc2.ticker()

    # Pega o último preco
    vlastprice = vticker["ticker"]["last"]
    # Coloca o preco novo (Ticker+2%)
    vnewprice = str(round(float(vlastprice)*2/100+float(vlastprice),5))
    print("Preco do Ticker   : " + vlastprice)
    print("Preco do Ticker 2%: " + vnewprice)
    time.sleep(5)

    # Coloca ordem de compra no preco do Ticker
    if i == 1:
        vbuyorder = mbtc.place_buy_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vlastprice.encode('ascii'))
        vlastprice2 = vlastprice
        print("Ordem de compra: " + vbuyorder)
        time.sleep(5)

        if vbuyorder["order"]["status"] == 2:
            vsellorder = mbtc.place_sell_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vnewprice.encode('ascii'))
        elif vbuyorder["order"]["status"] == 4:
            vsellorder = mbtc.place_sell_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vnewprice.encode('ascii'))
        print("Ordem de venda: " + vsellorder)
        time.sleep(5)

        print("Preco do Ticker         : " + vlastprice)
        print("Preco do Ticker anterior: " + vlastprice2)
        time.sleep(5)

    elif i > 1 and vlastprice < vlastprice2:
        vbuyorder = mbtc.place_buy_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vlastprice.encode('ascii'))
        vlastprice2 = vlastprice
        print("Ordem de compra: " + vbuyorder)
        time.sleep(5)

        if vbuyorder["order"]["status"] == 2:
            vsellorder = mbtc.place_sell_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vnewprice.encode('ascii'))
        elif vbuyorder["order"]["status"] == 4:
            vsellorder = mbtc.place_sell_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vnewprice.encode('ascii'))
        print("Ordem de venda: " + vsellorder)
    
        print("Preco do Ticker         : " + vlastprice)
        print("Preco do Ticker anterior: " + vlastprice2)
        time.sleep(5)

    time.sleep( 30 )

