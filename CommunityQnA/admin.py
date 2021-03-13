from django.contrib import admin
from CommunityQnA.models import QnA

# Register your models here.
class QnAAdmin(admin.ModelAdmin):
    list_display = ('question_no', 'question', 'posted_on', 'is_answered', 'answer')
admin.site.register(QnA,QnAAdmin)
