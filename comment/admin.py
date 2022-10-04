from atexit import register
from django.contrib import admin
from comment.models import ReplayCommentModel,CommentModel

# Register your models here.




# class ReplayAdmin(admin.TabularInline):
#     model = ReplayCommentModel

# @admin.register(CommentModel)
# class CommentAdmin(admin.ModelAdmin):
#     inlines = (ReplayAdmin,)


admin.site.register(ReplayCommentModel)
admin.site.register(CommentModel)

