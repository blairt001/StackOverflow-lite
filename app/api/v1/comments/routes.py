from flask import Blueprint, request, make_response, jsonify, session
from flask.views import MethodView
from app.comments.models import Comment
from ....utils import jwt_required

comments_blueprint = Blueprint('comments', __name__)


class CommentsListAPIView(MethodView):
    """ Update Instance api resource """

    @jwt_required
    def post(self, answer_id=None):
        data = request.get_json(force=True)
        data['answer_id'] = answer_id
        data['user_id'] = session.get('user_id')
        response = Comment(data).save()
        if response:
            response_object = {
                'message': 'Your comment was successful',
                'user_id' : session.get('user_id')
            }
            return make_response(jsonify(response_object)), 201

        response_object = {
            'message': 'Some error occurred. Please try again.'
        }
        return make_response(jsonify(response_object)), 400


# Define the API resources
comment_view = CommentsListAPIView.as_view('comment_api')

# API endpoint rule to enable a user comment on an answer
comments_blueprint.add_url_rule(
    '/api/v1/questions/answers/comment/<string:answer_id>',
    view_func=comment_view,
    methods=['POST']
)