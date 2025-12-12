from odoo import models, fields, api, _

class VetAppointment(models.Model):
    _name = 'vet.appointment'
    _description = 'Cita Veterinaria'
    _rec_name = 'code'

    code = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: _('Nuevo'))
    
    date_time = fields.Datetime(string='Fecha y hora', default=fields.Datetime.now, required=True)
    
    partner_id = fields.Many2one('res.partner', string="Dueño", required=True)
    
    pet_id = fields.Many2one('vet.patient', string='Paciente', required=True)
    
    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_vet_doctor', '=', True)])
    
    state = fields.Selection(
        [
            ('draft', 'Borrador'),
            ('confirmed', 'Confirmado'),
            ('done', 'Realizado'),
            ('cancel', 'Cancelado')
        ], default='draft', string="Estado"
    )
    
    description = fields.Text(string='Observaciones iniciales')

    amount_total = fields.Monetary(string='Total', currency_field='currency_id', default=0.0)
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.company.currency_id)

    payment_ids = fields.One2many(
        'account.payment',
        'vet_appointment_id',
        string='Pagos realizados'
    )

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            if rec.code == 'Nuevo':
                rec.code = self.env['ir.sequence'].next_by_code('vet.appointment') or 'CITA-000'

    def action_done(self):
        for rec in self:
            rec.state = 'done'