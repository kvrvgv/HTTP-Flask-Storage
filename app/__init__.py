

from hashlib import sha256
from functools import wraps
from models import configure_database, User, File
from flask import Flask, request, send_from_directory
from utils import delete_io_file, find_io_file, create_file


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "storage"
db = configure_database(app)


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if auth:
            user = User.authenticate(auth)
            if user:
                kwargs["user"] = user
                return f(**kwargs)
        return 'Unauthorized', 401
    return wrapped_view


@app.route('/upload', methods=["POST"])
@login_required
def upload_view(user: User):
    if not request.files:
        return {'error': 'files not attached'}, 400

    names = list()
    for file in request.files.values():
        content = file.stream.read()
        file_hash = sha256(content).hexdigest()
        if not File.get(file_hash):
            create_file(file_hash, app.config["UPLOAD_FOLDER"], content)
            names.append(file_hash)

    File.add_files(names, user)
    return names[0] if len(names) == 1 else names


@app.route('/download', methods=["GET"])
def download_view():
    file_hash = request.args.get("hash")
    file_hash = f"{file_hash[:2]}/{file_hash}"
    if find_io_file(file_hash, app.config["UPLOAD_FOLDER"]):
        return send_from_directory(app.config['UPLOAD_FOLDER'], file_hash)
    return {'error': 'file not found'}, 418


@app.route('/delete')
@login_required
def delete_view(user: User):
    file_hash = request.args.get("hash")
    if not file_hash:
        return {"error": "arguments are not passed"}, 400
    file = File.get(file_hash)
    if not file:
        return {"error": "file not found"}, 400
    if file.owner != user.id:
        return {"error": "Access Denied"}, 403

    delete_io_file(file_hash, app.config["UPLOAD_FOLDER"])
    File.delete(file_hash)
    return {"status": "deleted"}, 200


if __name__ == '__main__':
    app.run()
