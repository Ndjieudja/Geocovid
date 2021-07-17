from django.contrib import admin
from .models import ProfileUser, TestCovid, Result, Gender

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('surname', 'address', 'gender', 'age', 'phone',
                    'user_create', 'idtestnumber')
    list_filter = ('idtestnumber', 'surname', 'address')

    queryset = ('idtestnumber', 'surname')


admin.site.register(ProfileUser, UserAdmin)


class IdAdmin(admin.ModelAdmin):
    list_display = ('idtestnumber', 'test_center', 'locate',
                    'result_test')
    list_filter = ('idtestnumber', )
    queryset = ('idtestnumber', )


admin.site.register(TestCovid, IdAdmin)

admin.site.register(Result)


admin.site.register(Gender)