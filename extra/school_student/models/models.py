# -*- coding: utf-8 -*-
from email.policy import default
from locale import currency
import datetime
from tomlkit import string
from odoo import models, fields, api, _
from odoo.exceptions  import UserError
from lxml import etree
import random


class student_test_fees(models.Model):
    _name = "student.test.fees"
    _table = "student_fees_testing"

class school_student(models.Model):
    _name = "student.test"


    name = fields.Char(string="Test")


class school_student(models.Model):
    _name = 'school_student.school_student'
    _description = 'school_student.school_student'

    id = fields.Integer(string= 'id')
    name = fields.Char (copy=False,default='studentcopy')
    school_id = fields.Many2one('school.profile', string="School", copy=False)
    hobby_list = fields.Many2many("hobby","school_hobby_rel","student_id","hobby_id", srting="Hobbies", required=True)
    is_virtual_school = fields.Boolean(related='school_id.is_virtual_class', string = "Is Virtual Class")
    school_address = fields.Text(related='school_id.address', string="Address")
    currency_id = fields.Many2one("res.currency", string="Currency")
    student_fees = fields.Monetary(string='Student Fees')
    total_fees = fields.Float(string="Total Fees")
    ref_id = fields.Reference([('school.profile','School'),('account.move', 'Invoice')],string="Reference Field")
    active = fields.Boolean(string="Active", default=True)
    bdate = fields.Date(string="Date Of Birth", defualt=fields.Date.today())
    student_age = fields.Char(string="Total Age",compute="_get_age_from_student")

    def wiz_open(self):
        
        return {'type': 'ir.actions.act_window',
                'res_model':'student.feees.update.wizard',
                'view_mode': 'form',
                'target': 'new'}

    def custom_button_method(self):

        # self.env._cr.execute("insert into school_student(name, active) values('from button click',True)")
        # self.env._cr.commit()

        print("hello this is custom_button_method called by you.........",self)
        self.custom_new_method(random.randint(1,1000))
        self.custom_method()

    def custom_new_method(self, total_fees):
        self.total_fees = total_fees

    def custom_method(self):
        try:
            self.ensure_one()
            print(self.name)
            print(self.bdate)
            print(self.school_id.name)
        except ValueError:
            pass
    
    def fields_view_get(self,view_id=None, view_type='from', toolbar=False, submenu=False):
        # print("View id",view_id)
        # print("View Type",view_type)
        # print("toolbar",toolbar)
        # print("submenu",submenu)
        res = super(school_student,self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        # print("Return Disc",res)
        if view_type == "form":
            doc = etree.XML(res['arch'])
            name_field = doc.xpath("//field[@name='name']")
            if name_field:
                # Added one label in form view.
                name_field[0].addnext(etree.Element('label', {'string':'Hello this is custom label from fields_view_get method'}))

            #override attribute
            address_field = doc.xpath("//field[@name='school_address']")
            if address_field:
                address_field[0].set("string", "Hello This is School Address.")
                address_field[0].set("nolabel", "0")


            res['arch'] = etree.tostring(doc, encoding='unicode')

            if view_type == 'tree':
                doc = etree.XML(res['arch'])
                school_field = doc.xpath("//field[@name='school_id']")
                if school_field:
                    # Added one field in tree view.
                    school_field[0].addnext(etree.Element('field', {'string':'Total Fees',
                                                                    'name': 'total_fees'}))
                res['arch'] = etree.tostring(doc, encoding='unicode')
        return res

    @api.model
    def default_get(self, fields_list=[]):
        print("fields list",fields_list)
        rtn = super(school_student, self).default_get(fields_list)    
        print(rtn)
        return rtn
        
    
        class Meta:
            abstract = True
    

    @api.depends("bdate")
    def _get_age_from_student(self):
        """Age Calculation"""
        today_date = datetime.date.today()
        for stud in self:
            if stud.bdate:
                currentDate = datetime.date.today()

                deadlineDate= fields.Datetime.to_datetime(stud.bdate).date()
                # print (deadlineDate)
                daysLeft = currentDate - deadlineDate
                # print(daysLeft)

                years = ((daysLeft.total_seconds())/(365.242*24*3600))
                yearsInt=int(years)

                months=(years-yearsInt)*12
                monthsInt=int(months)

                days=(months-monthsInt)*(365.242/12)
                daysInt=int(days)

                hours = (days-daysInt)*24
                hoursInt=int(hours)

                minutes = (hours-hoursInt)*60
                minutesInt=int(minutes)

                seconds = (minutes-minutesInt)*60
                secondsInt =int(seconds)

                stud.student_age = 'You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
                 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt)
            else:
                stud.student_age = "Not Providated...."


    # @api.model_create_multi
    # def create(self, values):
    #     rtn = super(school_student, self).create(values)
    #     rtn.active = True
    #     return rtn


    # def write(self, values):
    #     print("-------",values)
    #     rtn = super(school_student, self).write(values)
    #     return rtn  

    # @api.returns('self', lambda value: value.id)
    # def copy(self, default={}):
    #     default['name'] = "copy ("+self.name+")"
    #     rtn = super(school_student, self).copy(default=default) 
    #     print("return statement",rtn)
    #     rtn.total_fees = 500
    #     return rtn 

    def unlink(self):
        print("self statement",self)
        rtn= super(school_student,self).unlink()
        print("return statement",rtn)
        return rtn



class schoolprofile(models.Model):
    _inherit = "school.profile"

    school_list = fields.One2many("school_student.school_student", "school_id", string = "School List")

    school_number = fields.Char("school code")

    # @api.model
    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     print("Name",name)
    #     print("operator",operator)
    #     print("limit",limit)
    #     if name:
    #         records = self.search(['|','|',('name',operator,name),('email',operator,name),('school_number',operator,name),('school_type',operator,name)])
    #         return records.name_get()
    #     return super(schoolprofile, self).name_search(name=name, args=args, operator=operator, limit=limit)


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):

        args = args or []
        domain = []
        print("Name",name)
        print("Args",args)
        print("operator",operator)
        print("limit",limit)
        print("name_get_uid ",name_get_uid)
        domain = []
        if name:
            domain = ['|','|','|',('name', operator, name), ('email', operator, name),('school_number', operator, name), ('school_type', operator, name)]

        school_ids = self.with_user(name_get_uid).search(domain+args, limit=limit)
        return school_ids.ids
        
        





    # @api.model
    # def create(self, vals):
    #     rtn = super(schoolprofile, self).create(vals)
    #     if not rtn.school_list:
    #         raise UserError(_("student list is empty!"))
    #     return rtn  

class Hobbies(models.Model):
    _name = "hobby"


    name = fields.Char(string="Hobby")  





    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.vclass defMixin(models.Model):odel):
    
class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        # Agregar codigo de validacion aca
        
        print("User Env",self.env)
        print("User Env",self.env.user)
        print("User Env",self.env.company)
        print("User Env",self.env.companies)
        print("User Env",self.env.context)

        print("partner values",vals)

        return super(Partner, self).create(vals)