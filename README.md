# Customization
Add in account.move.line model new field call size, must install account module

Add in stock.move model new field call size, must install Stock module

Add in sale.order.line model new field call size

Then ;
Need when Create Transfer ‘stock.picking’ From SO send the the size value to

Transfer Lines ‘stock.move’

Need when Create Invoice ‘account.move’ From SO send the the size value to Invoice

Lines ‘account.move.line’
