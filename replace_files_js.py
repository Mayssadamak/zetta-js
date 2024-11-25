import os

# Chemin vers le répertoire de votre projet Django
project_directory = "/zettaspark3/zettaspark/"

# Liste des remplacements exacts
replacements = [
    ('<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
     '<script src="{% static \'js/chart.js\' %}"></script>'),

    ('<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>',
     '<script src="{% static \'js/sweetalert2@11.js\' %}"></script>'),

    ('<script src="https://cdnjs.cloudflare.com/ajax/libs/js-cookie/3.0.1/js.cookie.min.js"></script>',
     '<script src="{% static \'js/js.cookie.min.js\' %}"></script>'),

    ('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>',
     '<script src="{% static \'js/jquery.min.js\' %}"></script>'),

    ('<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>',
     '<script src="{% static \'js/jquery-3.2.1.slim.min.js\' %}"></script>'),

    ('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>',
     '<script src="{% static \'js/jquery-3.6.0.min.js\' %}"></script>'),

    ('<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>',
     '<script src="{% static \'js/jquery-3.6.4.min.js\' %}"></script>'),

    ('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.blockUI/2.70/jquery.blockUI.min.js"></script>',
     '<script src="{% static \'js/jquery.blockUI.min.js\' %}"></script>'),

    ('<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>',
     '<script src="{% static \'js/popper.min.js\' %}"></script>'),

    ('<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>',
     '<script src="{% static \'js/popper-1.12.9.min.js\' %}"></script>'),

    ('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>',
     '<script src="{% static \'js/bootstrap.min.js\' %}"></script>'),

    ('<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>',
     '<script src="{% static \'js/bootstrap-4.0.0.min.js\' %}"></script>')
]

# Fonction pour remplacer les occurences dans un fichier
def replace_in_file(file_path):
    # Essayer d'ouvrir le fichier avec différents encodages
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        # Si 'utf-8' échoue, essayer avec 'latin-1'
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            content = file.read()
    
    # Appliquer les remplacements
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Sauvegarder les modifications dans le fichier
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Fonction pour parcourir les fichiers du projet
def update_project_files(project_directory):
    for root, dirs, files in os.walk(project_directory):
        for file_name in files:
            if file_name.endswith('.html') or file_name.endswith('.js'):
                file_path = os.path.join(root, file_name)
                replace_in_file(file_path)

# Mettre à jour les fichiers du projet
update_project_files(project_directory)
