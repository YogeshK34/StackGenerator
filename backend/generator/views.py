from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TechStackCard

# to generate the card 
class GenerateCard(APIView):
    def post(self, request):
        name = request.data.get('name')
        stacks = request.data.get('stacks')
        return Response({
            "message": f"Card generated for {name} with {len(stacks)} tech stacks"
        })
    
# to save the card
class SaveCard(APIView):
    def post(self, request):
        name = request.data.get('name')
        stacks = request.data.get('stacks')

        # check if all the constraints are avail are not
        if not name or stacks:
            return Response({
                "error": "Name and stacks are required"},status=status.HTTP_400_BAD_REQUEST)
        
        card = TechStackCard.objects.create(name=name, stacks=stacks)
        return Response({
            "message": "Card saved successfully", "id": card.id
        }, status=status.HTTP_201_CREATED)