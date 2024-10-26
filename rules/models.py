from django.db import models

class Node(models.Model):
    NODE_TYPE_CHOICES = [
        ('operator', 'Operator'),
        ('operand', 'Operand'),
    ]

    node_type = models.CharField(max_length=8, choices=NODE_TYPE_CHOICES)
    value = models.CharField(max_length=255, blank=True, null=True)
    left = models.ForeignKey('self', on_delete=models.CASCADE, related_name='left_child', null=True)
    right = models.ForeignKey('self', on_delete=models.CASCADE, related_name='right_child', null=True)

    def __str__(self):
        return f"{self.node_type}: {self.value if self.value else ''}"
