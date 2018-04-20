from django.forms import forms
from django.shortcuts import render
from DjangoUeditor.forms import UEditorField


# Create your views here.

class TestUEditorForm(forms.Form):
    content = UEditorField('内容', width=600, height=300, toolbars="full", imagePath="images/", filePath="files/",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={})


def index(request):
    form = TestUEditorForm()
    return render(request, 'index.html', {'form': form})
