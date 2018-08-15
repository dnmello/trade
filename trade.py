#!/usr/local/bin/python
# coding: latin-1
import os, sys, time
import mercadobitcoin
mbtc2 = mercadobitcoin.Api()
 
from mercadobitcoin import TradeApi
mbtc = TradeApi("key","secret")

vprecocompra = input('Qual valor vc quer comprar: ')

for i in range(1,1000):
    print("Contador: " + str(i))
    # Acessa o Ticker
    vticker = mbtc2.ticker()
    # Pega o último preco
    vprecoticker = vticker["ticker"]["last"]
    # Coloca o preco novo (Ticker+2%)
    vprecovenda = str(round(float(vprecocompra)*2/100+float(vprecocompra),5))
    print("Preco de Compra   : " + str(vprecocompra))
    print("Preco do Ticker   : " + vprecoticker)
    print("Preco de Venda    : " + vprecovenda)
    time.sleep(5)

    # Coloca ordem de compra no preco do Ticker
    if float(vprecoticker) < float(vprecocompra):
        vprecocompra = vprecoticker
        vbuyorder = mbtc.place_buy_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vprecoticker.encode('ascii'))
        print("Ordem de compra: " + str(vbuyorder))
        time.sleep(5)

        if vbuyorder["order"]["status"] == 4 or vbuyorder["order"]["status"] == 2:
            vsellorder = mbtc.place_sell_order(coin_pair="BRLBTC", quantity="0.001", limit_price=vprecovenda.encode('ascii'))
            print("Ordem de venda: " + str(vsellorder))
            time.sleep(5)
        else:
             vcancelorder = mbtc.cancel_order(coin_pair="BRLBTC", order_id=int(vbuyorder["order"]["order_id"]))
             print("Ordem de venda cancelada: "+ str(vcancelorder))
             time.sleep(5)
    time.sleep( 30 )