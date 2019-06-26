from django import forms

from dinner.models import DinnerInfo


class DinnerInfoForm(forms.ModelForm):
    class Meta:
        model = DinnerInfo
        fields = (
            'dinner_title',
            'price',
            'number',
            'dinner_date',
            'deadline',
            'activities_play',
            'activities_photo',
            'intro'
        )
