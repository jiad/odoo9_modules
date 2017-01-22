from openerp.osv import fields, osv


class daily_transaction(osv.osv):
    _name = "daily.transaction"
    _description = "Daily Transaction"
      

    _columns = {
        'name': fields.char('Subject', size=128, required=True),
        'date': fields.date('Date',required=True),
        'note': fields.text('Notes'),  
        'amount': fields.float('Amount', required=True),
        'type': fields.selection([
            ('transport', 'Transport'),
            ('household', 'Household'),
            ('personal', 'Personal'),
            ], 'Type', required=True), 
       
    }