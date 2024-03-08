from django.db import models


class Activity(models.Model):
    """Model representing an activity."""

    # Fields
    name = models.CharField(max_length=100, unique=True, help_text="Enter the name of the activity.")

    # Metadata
    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Record(models.Model):
    """Model representing a record of activity."""

    # Fields
    name = models.CharField(max_length=100)
    date = models.DateField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # ForeignKey relationship
    hours = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    travel = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    mileage = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    wait = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    expense = models.DecimalField(max_digits=10, decimal_places=2,
                                  verbose_name='Expense ($)',
                                  default=0) # Define verbose_name for better readability
    comments = models.TextField()  # Allow comments to be optional

    # Methods
    def __str__(self):
        """String representation of the record."""
        return f"{self.name} - {self.date}"
