from flask_restful import Resource
from models.skill import SkillModel


class Skill(Resource):

    def get(self,name):
        skill=SkillModel.find_by_name(name)
        if skill:
            return skill.json()
        return{'message':'Skill not found'},404

    def put(self,name):
        if SkillModel.find_by_name(name):
            return {'message': "A Skill with name'{}' already Exists.".format(name)}, 400
        skill=SkillModel(name)
        try:
            skill.save_to_db()
        except:
            return {'message':'An Error has occured while creating the skill'},500
        return skill.json(),200
    def delete(self,name):
        skill=SkillModel.find_by_name(name)
        if skill:
            skill.delete_from_db()
        return {'message':'Skill has been deleted'}

class SkillList(Resource):
    def get(self):
        return {'skills':[skill.json() for skill in SkillModel.query.all()]}