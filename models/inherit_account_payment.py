from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    # Se crea la relación inversa hacia la cita
    vet_appointment_id = fields.Many2one(
        'vet.appointment',
        string='Cita Veterinaria',
        readonly=True
    )

    vet_payment_method_type = fields.Selection([
        ('cash', 'Efectivo'),
        ('yape', 'Yape'),
        ('plin', 'Plin'),
        ('credit_card', 'Tarjeta de Credito'),
        ('debit_card', 'Tarjeta de Debito'),
        ('transfer', 'Transferencia'),
    ], string='Tipo de Pago')