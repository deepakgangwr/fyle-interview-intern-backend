from flask import Blueprint

from core import db
from core.apis import decorators
from core.apis.assignments.schema import AssignmentSchema, AssignmentGradeSchema
from core.apis.responses import APIResponse
from core.models.assignments import Assignment


principal_assignments_resources = Blueprint("principal_assignments_resources", __name__)

@principal_assignments_resources.route("/", methods=["GET"], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    principal_assignments = Assignment.get_assignments_by_principal()
    principal_assignments_dump = AssignmentSchema().dump(
        principal_assignments, many=True
    )
    return APIResponse.respond(data=principal_assignments_dump)


@principal_assignments_resources.route("/grade", methods=["POST"], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assingment(p, incoming_payload):
    """Grade an assignment"""
    grade_assingment_payload = AssignmentGradeSchema().load(incoming_payload)

    grade_assingment = Assignment.mark_grade(
        _id=grade_assingment_payload.id,
        grade=grade_assingment_payload.grade,
        auth_principal=p,
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(grade_assingment)
    return APIResponse.respond(data=graded_assignment_dump)