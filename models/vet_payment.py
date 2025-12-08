from odoo import models, fields

class VetPayment(models.Model):
    _name = 'vet.payment'
    _description = 'Registro de Pagos'
    _order = 'date desc'

    name = fields.Char(string='Descripción', required=True, default='Pago de cita')
    date = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    amount = fields.Float(string='Monto', required=True)

    # Se listan los métodos de pagos
    payment_method = fields.Selection([
        ('cash', 'Efectivo'),
        ('yape', 'Yape'),
        ('plin', 'Plin'),
        ('card', 'Tarjeta de crédito'),
        ('transfer', 'Transferencia')
    ], string='Método de pago', required=True)

    # Se crean estado simples para saber si se cobró o no
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('posted', 'Confirmado')
    ], string='Estado', default='draft')

    # Relaciones
    appointment_id = fields.Many2one('vet.appointment', string='Cita asociada')

    # Se busca el cliente de la cita automáticamente
    partner_id = fields.Many2one(
        related='appointment_id.partner_id',
        string='Cliente',
        store=True,
        readonly=True
    )

    # Botón para confirmar el pago
    def action_confirm(self):
        for record in self:
            record.state = 'posted'