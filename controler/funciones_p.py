import datetime
import uuid
def generate_unique_filename(filename):
    # Genera un nombre único utilizando la marca de tiempo y un identificador único
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4().hex)[:6]
    return f"{timestamp}_{unique_id}_{filename}"