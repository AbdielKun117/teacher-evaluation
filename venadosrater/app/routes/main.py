from flask import Blueprint, render_template, request
from app.services import get_all_professors, get_professor_by_id

bp = Blueprint('main', __name__)

@bp.route('/profesor/<id>')
def professor(id):
    professor = get_professor_by_id(id)
    if not professor:
        # Handling for now with a simple 404
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
    staff = get_all_professors() # Service fetches all, filter in template loop ideally or service
    return render_template('directory.html', staff=staff)

@bp.route('/')
def index():
    professors = get_all_professors()
    
    # Basic search filter (Python side for now, can move to DB later)
    query = request.args.get('q')
    if query:
        professors = [p for p in professors if query.lower() in p['name'].lower()]

    return render_template('index.html', professors=professors)

