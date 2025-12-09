{
    'name': 'Lummy Vet',
    'version': '17.0.1.0.0',
    'summary': 'Gestión de clínica veterinaria',
    'description': """Un sistema para Lummy-Vet que permite administrar sus pacientes (mascotas),
                    sus dueños (clientes), las citas médicas y el historial clínico""",
    'author': 'Lummy Vet Team (A. Marquina, G. Jaramillo)',
    'category': 'Servicio médico',

    'depends': [
        'base',
        'contacts',
        'account',
    ],

    'data': [
        'security/ir.model.access.csv',

        'views/vet_appointment_views.xml',
        'views/inherit_res_partner_views.xml',
        
        'views/menus.xml'
    ],

    'demo': [],
    
    'auto_install': True,
    'application': True,
    'web_icon': 'lummy_vet,static/description/icon.png',
}