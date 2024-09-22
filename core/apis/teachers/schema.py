from marshmallow import Schema, post_load, EXCLUDE
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema

from core.models.teachers import Teacher


class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=False)
    user_id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    @post_load
    def initate_class(self, data_dict, many, partial):
        return Teacher(**data_dict)