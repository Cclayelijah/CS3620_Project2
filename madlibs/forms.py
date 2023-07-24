from django import forms


# class StoryForm(forms.Form):
#
#     def __init__(self, n, *args, **kwargs):
#         super(StoryForm, self).__init__(*args, **kwargs)
#         for i in range(0, n):
#             self.fields["%d" % i] = forms.CharField(required=False)