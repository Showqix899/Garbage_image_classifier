from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedImage, UserSession
from .serializers import UploadedImageSerializer

from PIL import Image
import torch
from transformers import AutoFeatureExtractor, AutoModelForImageClassification

# Load prebuilt model (free, no training)
MODEL_NAME = "google/vit-base-patch16-224"
feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)
model.eval()


# Keywords for garbage detection
TRASH_KEYWORDS = ['bottle', 'can', 'paper', 'plastic', 'garbage', 'cup', 'trash']


def classify_image(image_path):

    image = Image.open(image_path).convert("RGB")
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_idx = torch.argmax(logits, dim=1).item()
    label = model.config.id2label[predicted_idx]
    is_garbage = any(keyword in label.lower() for keyword in TRASH_KEYWORDS)
    return is_garbage



class UploadImageAPIView(APIView):
    def post(self, request):
        # Get or create a UUID session
        session_id = request.data.get('session_id')
        if session_id:
            user, _ = UserSession.objects.get_or_create(id=session_id)
        else:
            user = UserSession.objects.create()
        
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_image = serializer.save(user=user)
            # Classify image
            uploaded_image.is_garbage = classify_image(uploaded_image.image.path)
            uploaded_image.save()
            return Response({
                'session_id': str(user.id),
                'image_id': uploaded_image.id,
                'is_garbage': uploaded_image.is_garbage
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ListImagesView(APIView):
    def get(self, request):
        images = UploadedImage.objects.all().order_by('-created_at')
        serializer = UploadedImageSerializer(images, many=True)
        return Response(serializer.data)