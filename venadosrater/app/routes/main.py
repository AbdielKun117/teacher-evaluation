from flask import Blueprint, render_template, request
from app.data.mock_db import get_all_professors

bp = Blueprint('main', __name__)

@bp.route('/profesor/<id>')
def professor(id):
    from app.data.mock_db import get_professor_by_id
    professor = get_professor_by_id(id)
    if not professor:
        return render_template('404.html'), 404 # Assuming a 404 page or just handling generic error
        # simpler for now:
        return "Profesor no encontrado", 404
    return render_template('professor.html', professor=professor)

@bp.route('/politicas')
def policies():
    return render_template('policies.html')

@bp.route('/contacto')
def contact():
    return render_template('contact.html')

@bp.route('/directorio')
def directory():
    from app.data.mock_db import get_all_professors
    staff = get_all_professors() # We will use the same list as it now contains all roles
    return render_template('directory.html', staff=staff)

@bp.route('/')
def index():
    professors = get_all_professors()
    
    # Basic search filter (mock)
    query = request.args.get('q')
    if query:
        professors = [p for p in professors if query.lower() in p['name'].lower()]

    return render_template('index.html', professors=professors)

