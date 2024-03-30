{
    'name': 'Custom Fields',
    'version': '1.0',
    'summary': 'Add custom fields to various models',
    'description': """
    This module adds custom fields to the account.move.line, stock.move, and sale.order.line models.
    """,
    'category': 'Customization',
    'author': 'mohamed',
    'depends': ['account', 'stock', 'sale'],
    'data': ['views/views_inherit.xml'],
    'installable': True,
    'auto_install': False,
}
