from django.contrib import admin

from position.models import Position


class EmployeeInline(admin.TabularInline):
    model = Position.employee.through
    extra = 0
    can_delete = False
    verbose_name = "Employee"
    verbose_name_plural = "Employees"
    fields = ('user_details',)
    readonly_fields = ('user_details',)

    def user_details(self, instance):
        return f"Username: {instance.user.username}  -  Email: {instance.user.email}  -  First Name: {instance.user.first_name}  -  Last Name: {instance.user.last_name}"

    user_details.short_description = "Employee Details"

    def has_add_permission(self, request, obj):
        return False


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'valid_date', 'working_hours', 'salary', 'category', 'employer')
    inlines = [EmployeeInline]

    exclude = ['employee','employer']
    # fields = ['title','working_hours']

    def save_model(self, request, obj, form, change):
        obj.employer = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(employer=request.user)

# admin.site.register(Position, PositionAdmin)
# admin.site.register(Position, PositionAdmin)
# admin.site.register(Position) is happy with Position fields
