<!-- INICIO DE LA DOCUMENTACIÓN DEL PROYECTO -->
<br />
<div align="center">
  <a href="https://github.com/tu-usuario/lummy-vet">
    <!-- Ajusta la ruta de la imagen si es necesario -->
    <img src="static/description/icon.png" alt="Logo Lummy Vet" width="150" height="150">
  </a>

  <h3 align="center">Lummy Vet (VetOdoo)</h3>

  <p align="center">
    Sistema de gestión integral para clínicas veterinarias: Pacientes, Citas, Tratamientos y Pagos.
    <br />
    <br />
    <a href="https://github.com/tu-usuario/lummy-vet"><strong>Explora la documentación »</strong></a>
    <br />
    <br />
    <a href="#">Ver Demostración</a>
  </p>
</div>

<!-- ACERCA DEL PROYECTO -->
## 🐾 Acerca del Proyecto

<br>

**Lummy Vet** es un módulo personalizado para **Odoo 17** diseñado para centralizar la administración de una clínica veterinaria. Este proyecto nace para solucionar la pérdida de trazabilidad en historiales médicos y la gestión manual de citas.

El sistema permite optimizar el flujo de trabajo desde la admisión hasta el cobro, garantizando que los dueños y sus mascotas tengan un expediente claro, y que los doctores cuenten con herramientas rápidas para diagnósticos y recetas.

### Tecnologías
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 10px;">

  [![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![XML](https://img.shields.io/badge/XML-orange?style=for-the-badge&logo=xml&logoColor=white)](https://www.w3.org/XML/)
  [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
  [![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)

</div>

<!-- ARQUITECTURA -->
## 🏗 Arquitectura del Sistema

```text
lummy_vet/
├── models/             # Lógica de negocio y definición de datos (ORM)
│   ├── inherit_res_partner.py  # Extensión de contactos (Dueños/Doctores)
│   ├── vet_appointment.py      # Lógica de Citas
│   ├── vet_patient.py          # Lógica de Mascotas
│   ├── vet_payment.py          # Lógica de Pagos
│   └── ...
├── views/              # Interfaz de usuario (XML)
│   ├── menus.xml               # Estructura de navegación
│   ├── vet_appointment.xml     # Vistas de Citas
│   ├── vet_payment_views.xml   # Vistas de Pagos
│   └── ...
├── security/           # Reglas de acceso (ACLs)
├── static/             # Recursos estáticos (Imágenes, CSS)
├── wizard/             # Asistentes (Wizards)
└── __manifest__.py     # Metadatos del módulo
```

<!-- MIEMBROS DEL EQUIPO -->
## 👥 Miembros del Equipo

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/tu-usuario-alessandro">
        <img src="https://ui-avatars.com/api/?name=Alessandro+Marquina&background=0D8ABC&color=fff&size=128" width="100px" style="border-radius:50%"/>
        <br />
        <sub><b>Alessandro Marquina</b></sub>
      </a>
      <br />
      Software Developer
    </td>
    <td align="center">
      <a href="https://github.com/tu-usuario-geraldo">
        <img src="https://ui-avatars.com/api/?name=Geraldo+Jaramillo&background=0D8ABC&color=fff&size=128" width="100px" style="border-radius:50%"/>
        <br />
        <sub><b>Geraldo Jaramillo</b></sub>
      </a>
      <br />
      Software Developer
    </td>
  </tr>
</table>
