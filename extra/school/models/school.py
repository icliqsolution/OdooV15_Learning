from email.policy import default
from operator import index

from tomlkit import document, string
from odoo import fields, models,api

class SchoolProfile(models.Model):
    _name = "school.profile"


    def get_default_rank(self):
        if 1==1:
            return 200
        else:
            return 100

    def default_establish_date(self):
        return fields.Date.today() 


    name = fields.Char(string="School Name", help="This is school Name", required=True ,default="This is default school name" , index=True) 
    email = fields.Char(string="Email", copy=False)
    phone = fields.Char("Phone")
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    school_rank= fields.Integer(string="Rank" ,help="This is school rank", required=True, default=lambda lm:lm.get_default_rank())
    result = fields.Float(string="Result", help="This is tool tip", default=1.1)
    address = fields.Text(string="Address")
    estalish_date = fields.Date(string="Establish Date", default=fields.Date.today())
    open_date = fields.Datetime("Open Date", help="This is tooltip and" "select date and time.", default=lambda lm:lm.default_establish_date())
    school_type=fields.Selection([('public','Public School'),('private','Private School')], help="Please select School Type.", string="SchoolType" )
    documents=fields.Binary(string='Documents')
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100,
                                max_height=100)
    school_description = fields.Html(string="Description", copy=False)
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="AutoRank")

    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank =100
            else:  
                rec.auto_rank = 0  

    @api.model
    def name_create(self,name):
        print("self",self)
        print("School Name",name)
        rtn = self.create({'name':name})
        print("rtn",rtn)
        print("rtn.name_get()[0]",rtn.name_get()[0])
        return rtn.name_get()[0]

    def name_get(self):
        student_list = []
        for school in self:
            name = school.name
            if school.school_type:
                name += "({})".format(school.school_type)
            student_list.append((school.id,  name))
        return student_list



    




