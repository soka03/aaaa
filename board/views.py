from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
def post_list(request): #게시글 모두 불러오기
	if request.method == 'GET':
		boards = Board.objects.all()
		serializer = BoardSerializer(boards, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_create(request): #게시글 작성하기
	if request.method == 'POST': #create
		serializer = BoardSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
	return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) 
def post_detail(request, pk): #게시글 상세 페이지 불러오기
    try: 
        board = Board.objects.get(pk=pk)
        serializer = BoardSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Board.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def post_update(request, pk): #게시글 수정하기
    try:
        board = Board.objects.get(pk=pk)
        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE']) #게시글 삭제하기
def post_delete(request, pk):
    try:
        board = Board.objects.get(pk=pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        