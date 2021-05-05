from flask import Flask, abort, request
from flask_restful import Api, Resource, fields, marshal_with, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
api = Api(app)
db = SQLAlchemy(app)

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
}


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


# db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="views on the video")
video_put_args.add_argument("likes", type=int, help="likes on the video")

video_update_agrs = reqparse.RequestParser()
video_update_agrs.add_argument("name", type=str, help="Name of the video")
video_update_agrs.add_argument("views", type=int, help="views on the video")
video_update_agrs.add_argument("likes", type=int, help="likes on the video")


""" names = {"kumar": {"age": 21, "gender": "male"},
        "shanu": {"age": 20, "gender": "male"},
}
class HelloWorld(Resource):
    def get(self, name):
        return {"data": name}

    def post(self):
        return {"data": "posted"}
"""

# videos = {}
""" def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, "Cloud not found video with that ID....")


def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, "Video already exists with that ID") """


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        # return videos[video_id]
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, "Could not found video with that ID....")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        # abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        # videos[video_id] = args
        # return videos[video_id], 200
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, "video id taken.....")
        video = VideoModel(
            id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_agrs.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, "Video doesnot exists, cannot update....")

        if args["name"]:
            result.name = args["name"]
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

    def delete(self, video_id):
        # abort_if_video_id_doesnt_exist(video_id)
        # del videos[video_id]
        result = VideoModel.query.filter_by(id=video_id).first()
        db.session.delete(result)
        db.session.commit()
        return '', 204


# api.add_resource(HelloWorld, "/helloworld/<string:name>/")
api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
    app.run(debug=True)
