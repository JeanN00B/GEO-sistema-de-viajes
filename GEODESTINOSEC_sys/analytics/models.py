from django.db import models


"""
Save forms options as a json?
Save forms onptions as a model that contains the form options?
Better save the model as a:
    - name
    - description / objective
    - json / xml content
"""
class FilterAsJSON(models.Model):
    name = models.CharField(max_length=51)
    description = models.TextField(blank=False, null=False, editable=True)
    json_content = models.JSONField(blank=False, null=False, editable=True)
    
    def __str__(self):
        return self.name