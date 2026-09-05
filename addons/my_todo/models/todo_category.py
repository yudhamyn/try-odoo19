# pyrefly: ignore [missing-import]
from odoo import models, fields

class TodoCategory(models.Model):
    _name = 'todo.category'
    _description = 'Kategori Tugas'
    _order = 'name asc'

    name = fields.Char('Nama Kategori', required=True)
    color= fields.Selection([
        ('putih', 'Putih'),
        ('abu_abu_muda', 'Abu-abu Muda'),
        ('biru_muda', 'Biru Muda'),
        ('kuning_muda', 'Kuning Muda'),
        ('oranye_muda', 'Oranye Muda'),
        ('pink_muda', 'Pink Muda'),
        ('hijau_muda', 'Hijau Muda'),
        ('ungu_muda', 'Ungu Muda'),
        ('merah_muda', 'Merah Muda'),
        ('abu_abu_tua', 'Abu-abu Tua'),
        ('biru_tua', 'Biru Tua'),
        ('kuning_tua', 'Kuning Tua'),
        ('oranye_tua', 'Oranye Tua'),
        ('pink_tua', 'Pink Tua'),
        ('hijau_tua', 'Hijau Tua'),
        ('ungu_tua', 'Ungu Tua'),
        ('merah_tua', 'Merah Tua'),
    ], string='Warna')
    description = fields.Text(string='Deskripsi')
    