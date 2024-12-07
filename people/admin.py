from django.contrib import admin

from people.models import CertificateType, Person, PersonCertificate

@admin.register(CertificateType)
class CertificateTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the certificate type
    search_fields = ('name',)

class PersonCertificateInline(admin.TabularInline):
    model = PersonCertificate
    extra = 1  # Display one empty row for new certificates

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')  # Display person's name and email
    search_fields = ('name', 'email')
    inlines = [PersonCertificateInline]
    list_filter = ('certificates__expiration_date',)  # Filter by expiration date in the admin panel
