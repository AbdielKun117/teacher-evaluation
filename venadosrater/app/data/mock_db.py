professors = [
    {
        "id": "1",
        "name": "Dr. Juan Pérez",
        "role": "docente",
        "department": "Ingeniería en Sistemas",
        "avatar_url": None,
        "rating": 4.5,
        "difficulty": 3.2,
        "reviews": 12,
        "reviews_list": [
            {"id": 101, "quality": 5, "difficulty": 3, "comment": "Excelente profesor, explica muy claro y sus clases son amenas.", "date": "10 Ene 2024", "tags": ["Inspirador", "Claro"]},
            {"id": 102, "quality": 4, "difficulty": 4, "comment": "Deja mucha tarea pero aprendes bastante. Prepárate para estudiar.", "date": "15 Dic 2023", "tags": ["Mucha Tarea"]},
        ]
    },
    {
        "id": "2",
        "name": "M.C. María López",
        "role": "docente",
        "department": "Ciencias Básicas",
        "avatar_url": None,
        "rating": 3.8,
        "difficulty": 4.5,
        "reviews": 8,
        "reviews_list": [
            {"id": 201, "quality": 4, "difficulty": 5, "comment": "Es estricta pero justa. Si no estudias repruebas.", "date": "20 Nov 2023", "tags": ["Estricta"]},
        ]
    },
    {
        "id": "3",
        "name": "Ing. Carlos Ruiz",
        "role": "docente",
        "department": "Ingeniería Industrial",
        "avatar_url": None,
        "rating": 2.5,
        "difficulty": 1.5,
        "reviews": 25,
        "reviews_list": [
            {"id": 301, "quality": 2, "difficulty": 1, "comment": "Es muy barco, casi no va a clases.", "date": "05 Oct 2023", "tags": ["Barco", "Faltista"]},
            {"id": 302, "quality": 3, "difficulty": 2, "comment": "Pasa lista y se va. Fácil pasar.", "date": "12 Sep 2023", "tags": ["Barco"]},
        ]
    },
    {
        "id": "4",
        "name": "Lic. Ana García",
        "role": "docente",
        "department": "Desarrollo Empresarial",
        "avatar_url": None,
        "rating": 4.9,
        "difficulty": 2.0,
        "reviews": 4,
        "reviews_list": [
            {"id": 401, "quality": 5, "difficulty": 2, "comment": "La mejor maestra, muy amable y comprensiva.", "date": "14 Ene 2024", "tags": ["Amable", "Respetuosa"]},
        ]
    },
    {
        "id": "5",
        "name": "Dr. Pedro Sánchez",
        "role": "docente",
        "department": "Ingeniería Mecánica",
        "avatar_url": None,
        "rating": 3.0,
        "difficulty": 3.0,
        "reviews": 0,
        "reviews_list": []
    },
    {
        "id": "6",
        "name": "Ing. Roberto Director",
        "role": "directivo",
        "department": "Dirección General",
        "avatar_url": None,
        "rating": 3.5,
        "difficulty": 0,
        "reviews": 2,
        "reviews_list": []
    },
    {
        "id": "7",
        "name": "Lic. Laura Escolares",
        "role": "administrativo",
        "department": "Servicios Escolares",
        "avatar_url": None,
        "rating": 1.5,
        "difficulty": 5.0,
        "reviews": 50,
        "reviews_list": [
             {"id": 701, "quality": 1, "difficulty": 5, "comment": "Nunca contestan el teléfono y siempre están de mal humor.", "date": "10 Ene 2024", "tags": ["Lentos", "Burocracia"]},
        ]
    }
]

def get_all_professors():
    return professors

def get_professor_by_id(prof_id):
    return next((p for p in professors if p["id"] == prof_id), None)
