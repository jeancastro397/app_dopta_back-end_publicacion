from firebase_admin import storage
from PIL import Image
import io

class FirebaseImageMixin:
    def upload_image_to_firebase(self, instance, foto):
        try:
            # Convertir la foto a JPG
            image = Image.open(foto)
            jpg_image = io.BytesIO()
            image.convert("RGB").save(jpg_image, format="JPEG")
            jpg_image.seek(0)

            # Crear el blob para la foto JPG
            bucket = storage.bucket()
            blob = bucket.blob(f"pub-mascotas/{instance.usuario.username}_{instance.nom_mascota}.jpg")
            blob.upload_from_file(jpg_image, content_type="image/jpeg")
            blob.make_public()

            public_url = blob.public_url
            print("Public URL:", public_url)  # Verifica que la URL es correcta

            return public_url
        except Exception as e:
            print(f"Error uploading to Firebase: {e}")
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["foto"] = instance.foto if instance.foto else None
        return representation
