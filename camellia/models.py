from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    main_image = models.FileField()

    def __str__(self):
        return self.name


class projectImage(models.Model):
    image = models.FileField()
    is_video = models.BooleanField()
    is_image = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.project.name}"


class Material(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str_(self):
        return self.name


class Door(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    additionalInfo = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class doorColor(models.Model):
    color_name = models.CharField(max_length=255)
    color_image = models.ImageField()
    door = models.ForeignKey(Door, on_delete=models.CASCADE)

    def __str__(self):
        return self.color_name

class Location(models.Model):
    branch_name = models.CharField(max_length=255)
    google_url = models.URLField(max_length=255)