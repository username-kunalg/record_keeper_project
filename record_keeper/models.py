from django.db import models


class Record(models.Model):
    """Model representing a record of activity."""

    # Fields
    name = models.CharField(max_length=100)
    date = models.DateField()
    activity = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=4, decimal_places=1)
    travel = models.DecimalField(max_digits=4, decimal_places=1)
    mileage = models.DecimalField(max_digits=5, decimal_places=1)
    wait = models.DecimalField(max_digits=4, decimal_places=1)
    expense = models.DecimalField(max_digits=10, decimal_places=2,
                                  verbose_name='Expense ($)')  # Define verbose_name for better readability
    comments = models.TextField(blank=True)  # Allow comments to be optional

    # Methods
    def __str__(self):
        """String representation of the record."""
        return f"{self.name} - {self.date}"
