# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Todo Task & Activity'
    _order = 'priority desc, deadline asc, id desc'

    # Field Data
    name = fields.Char(string='Judul Tugas', required=True)
    description = fields.Text(string='Detail / Catatan Tambahan')
    deadline = fields.Date(string='Batas Waktu (Deadline)')
    is_important = fields.Boolean(string='Penting?', default=False)
    
    priority = fields.Selection([
        ('0', 'Rendah'),
        ('1', 'Normal'),
        ('2', 'Tinggi'),
        ('3', 'Sangat Mendesak'),
    ], string='Prioritas', default='1')

    state = fields.Selection([
        ('draft', 'Baru'),
        ('in_progress', 'Sedang Dikerjakan'),
        ('done', 'Selesai'),
        ('cancel', 'Dibatalkan'),
    ], string='Status', default='draft', required=True)

    # Action Buttons untuk mengubah status
    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_reset(self):
        for rec in self:
            rec.state = 'draft'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
