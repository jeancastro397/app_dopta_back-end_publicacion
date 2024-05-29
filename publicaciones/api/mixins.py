from firebase_admin import storage
from PIL import Image
import io

class FirebaseImageMixin:
    def upload_image_to_firebase(self, user, publication_id, imagen):
        # Convertir la imagen a JPG
        image = Image.open(imagen)
        jpg_image = io.BytesIO()
        image.convert("RGB").save(jpg_image, format="JPEG")
        jpg_image.seek(0)

        # Crear el blob para la imagen JPG
        bucket = storage.bucket()
        blob = bucket.blob(f"publicaciones/{user.username}_{publication_id}.jpg")
        blob.upload_from_file(jpg_image, content_type="image/jpeg")
        blob.make_public()

        public_url = blob.public_url
        print("Public URL:", public_url)  # Verifica que la URL es correcta

        return public_url

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["imagen"] = instance.imagen if instance.imagen else None
        return representation