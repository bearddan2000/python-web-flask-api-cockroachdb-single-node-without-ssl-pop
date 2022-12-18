from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "cockroachdb://root@db:26257/beverage"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PopModel(db.Model):
    __tablename__ = 'pop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    color = db.Column(db.String())

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"<Pop {self.name}>"


@app.route('/')
def hello():
	return {"hello": "world"}


@app.route('/pop', methods=['POST', 'GET'])
def handle_beverage():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_pop = PopModel(name=data['name'], color=data['color'])

            db.session.add(new_pop)
            db.session.commit()

            return {"message": f"Beverage {new_pop.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        beverages = PopModel.query.all()
        results = [
            {
                "name": pop.name,
                "color": pop.color
            } for pop in beverages]

        return {"count": len(results), "pop": results, "message": "success"}


@app.route('/pop/<pop_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_pop(pop_id):
    pop = PopModel.query.get_or_404(pop_id)

    if request.method == 'GET':
        response = {
            "name": pop.name,
            "color": pop.color
        }
        return {"message": "success", "beverage": response}

    elif request.method == 'PUT':
        data = request.get_json()
        pop.name = data['name']
        pop.color = data['color']

        db.session.add(pop)
        db.session.commit()

        return {"message": f"Beverage {pop.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(pop)
        db.session.commit()

        return {"message": f"Beverage {pop.name} successfully deleted."}

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
