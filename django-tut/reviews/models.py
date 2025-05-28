from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer_name} - {self.book.title}"


# from django.db import models

# # Create your models here.
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField()
#     genre = models.CharField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Review(models.Model):
#     book = models.ForeignKey(Book,on_delete=models.CASCADE,related_key='review')
#     title = models.CharField()
#     review = models.TextField()
#     commented_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return f"{self.reviewer_name} - {self.book.title}"
