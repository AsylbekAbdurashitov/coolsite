from django import forms
from women.models import Women


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Категория не выбрано"
        self.fields["is_published"].initial = True

    class Meta:
        model = Women
        fields = "__all__"











