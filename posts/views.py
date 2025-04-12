from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Post
from .serializers import PostSerializer

@api_view(['POST'])
def create_post(request):
    data = request.data.copy()

    post = Post(
        title=data.get('title'),
        content=data.get('content'),
        user=request.user if request.user.is_authenticated else None,
        is_anonymous=data.get('is_anonymous', False)  # 👈 THÊM DÒNG NÀY
    )
    post.save()

    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({"message": "Post deleted"}, status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer