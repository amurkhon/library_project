from rest_framework import serializers
from  .models import Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data['title']
        print(type(title))
        author = data['author']

        # check title if it contains only alphabetical chars
        if not type(title) == str:
            raise serializers.ValidationError(
                {"status": "False",
                 "message": "Kitobning sarlavhasi harfdan tashkil topkan bo'lish kerak!"}
            )

        # check title and author from database
        if Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError(
                {"status": "False",
                 "message": "Siz qo'shmoqchi bo'lgan kitob mavjud!"}
            )
        return data

    def validate_price(self, price):

        if price < 0 or price > 10000000000:
            raise serializers.ValidationError(
                {"status": "False",
                 "message":f"Siz kiritgan {price} qiymat mavjud emas!"}
            )
