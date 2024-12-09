from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from app import settings

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class Movie(models.Model):
	"""
	The Movie class represents a film with various descriptive attributes.

	This class manages detailed information about a movie, including its title, release year, cast, genres, and more. It is
	designed to work within a Django application using models. The Movie class stores attributes such as the director, actors,
	runtime, and plot, among others. This class also handles the creation of a unique URL slug for the movie based on its title.

	Attributes:
		title: The title of the movie.
		year: The release year of the movie, optional.
		rated: The movie's rating, such as PG-13, optional.
		released: The release date of the movie, optional.
		runtime: The runtime of the movie, optional.
		genres: A many-to-many relationship field for associating genres with the movie.
		director: The director of the movie, optional.
		writer: The writer of the movie, optional.
		actors: A many-to-many relationship for associating actors with the movie.
		plot: The plot summary of the movie, optional.
		language: The language of the movie, optional.
		country: The country where the movie was produced, optional.
		awards: Awards won by the movie, optional.
		poster: A URL to the movie's poster image, optional.
		metascore: The metascore rating of the movie, optional.
		imdb_rating: The IMDb rating of the movie, optional.
		imdb_votes: The number of votes the movie has received on IMDb, optional.
		imdb_id: The unique IMDb identifier for the movie, optional.
		type: The type of the movie (e.g., movie, series), optional.
		dvd: The DVD release date, optional.
		box_office: Box office earnings, optional.
		production: Foreign key relationship to the Production company, optional.
		website: The official website URL for the movie, optional.
		slug: A unique slug URL for the movie.
		status: An integer to represent publishing status.
		created_on: The date and time when the movie record was created.
		updated_on: The date and time when the movie record was last updated.

	Methods:
		__str__: Returns the string representation of a Movie instance.
		save: Overrides the save method to ensure a unique slug is generated before saving.
		slug_to_title: Converts a slug back to the original movie title.
		generate_unique_slug: Generates a unique slug for the movie based on its title while ensuring uniqueness in the database.
	"""
	title = models.CharField(max_length=255)
	year = models.CharField(max_length=10, blank=True, null=True)
	rated = models.CharField(max_length=10, blank=True, null=True)
	released = models.CharField(max_length=50, blank=True, null=True)
	runtime = models.CharField(max_length=20, blank=True, null=True)
	genres = models.ManyToManyField(
		"Genre", related_name="movies", blank=True
		)  # ManyToMany for Genres
	director = models.CharField(max_length=255, blank=True, null=True)
	writer = models.CharField(max_length=255, blank=True, null=True)
	actors = models.ManyToManyField(
		"Actor", related_name="movies", blank=True
		)  # ManyToMany for actors
	plot = models.TextField(blank=True, null=True)
	language = models.CharField(max_length=100, blank=True, null=True)
	country = models.CharField(max_length=100, blank=True, null=True)
	awards = models.TextField(blank=True, null=True)
	poster = models.URLField(blank=True, null=True)
	metascore = models.CharField(max_length=10, blank=True, null=True)
	imdb_rating = models.CharField(max_length=10, blank=True, null=True)
	imdb_votes = models.CharField(max_length=20, blank=True, null=True)
	imdb_id = models.CharField(max_length=20, unique=True, blank=True,
	                           null=True)
	type = models.CharField(max_length=50, blank=True, null=True)
	dvd = models.CharField(max_length=50, blank=True, null=True)
	box_office = models.CharField(max_length=50, blank=True, null=True)
	production = models.ForeignKey(
		"Production",
		related_name="movies",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		)  # ForeignKey для студии
	website = models.URLField(blank=True, null=True)
	slug = models.SlugField(
		max_length=250, unique=True, blank=True, null=True, verbose_name="URL"
		)
	status = models.IntegerField(choices=STATUS, default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "movie"
		verbose_name = "Movie"
		verbose_name_plural = "Movies"
		ordering = ("id",)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug or self.title != self.slug_to_title(self.slug):
			self.slug = self.generate_unique_slug()
		super().save(*args, **kwargs)

	def slug_to_title(self, slug):
		# Returns the original title из slug
		return slug.replace(
			"-", " "
			).title()

	def generate_unique_slug(self):
		original_slug = slugify(self.title)
		unique_slug = original_slug
		counter = 1

		# Check whether such a slug already exists in the database
		while Movie.objects.filter(slug=unique_slug).exists():
			unique_slug = f"{original_slug}-{counter}"
			counter += 1

		return unique_slug


class Rating(models.Model):
	"""
	Represents a movie rating sourced from an external provider.

	The Rating class models the rating of a movie, capturing the source of the
	rating and its value. It is linked to a Movie instance and exists for the
	purpose of associating various ratings from different sources with the
	corresponding movie. The ratings are dependent on external data, e.g.,
	critics' reviews, user ratings, etc.

	Attributes
	----------
	movie : models.ForeignKey
		A foreign key field that links to the Movie class, allowing ratings to be associated with a specific movie.
	source : models.CharField
		A string field that represents the source from which the rating is coming, such as a website or reviewer.
	value : models.CharField
		A string field that holds the rating itself, which could be a number, a grade, or any form of rating indication.

	Methods
	-------
	__str__()
		Provides a readable string representation of the Rating object, typically indicating the source and the value of the rating.
	"""
	movie = models.ForeignKey("Movie", related_name="ratings",
	                          on_delete=models.CASCADE)
	source = models.CharField(max_length=100)
	value = models.CharField(max_length=20)

	class Meta:
		db_table = "rating"

	def __str__(self):
		return f"{self.source}: {self.value}"


class Actor(models.Model):
	"""
	Model representing an actor with capabilities to auto-generate a slug.

	The Actor class is a Django model that represents an actor entity with a
	name and slug fields. The class provides functionality to automatically
	generate a slug from the name if the slug is not provided before saving
	the model instance to the database.

	Attributes:
		name (str): The name of the actor, stored as a CharField with a
			maximum length of 255 characters.
		slug (str): A unique slug for the actor, stored as a SlugField with a
			maximum length of 270 characters. It's optional and can be null
			or blank.

	Meta:
		db_table: Specifies the database table name for the model as "actor".

	Methods:
		save(*args, **kwargs): Overrides the default save method. Before saving
			the instance, it ensures that a slug is generated from the name if
			the slug is not already set.
		__str__(): Provides a string representation of the actor instance,
			returning the actor's name.
	"""
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=270, unique=True, blank=True, null=True)

	class Meta:
		db_table = "actor"

	def save(self, *args, **kwargs):
		if not self.slug:
			# Generate a slug from the name
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Genre(models.Model):
	"""
	Represents a music genre with a name and a slug for URL usage.

	The Genre class is a Django model used to define the structure of a database table
	that stores information about different music genres. Each genre has a name
	and a unique slug generated from the name when saved to the database. The slug
	is used for creating URLs that are easy to read and share.

	Attributes:
		name: A CharField that stores the name of the genre with a maximum length
			  of 100 characters. It has a default value of "without_genre".
		slug: A SlugField that stores a URL-friendly slug representation of the
			  genre name. It has a maximum length of 250 characters and is unique.

	Methods:
		save: Saves the genre to the database, automatically generating a slug
			  from the name if it is not provided.
		__str__: Returns the string representation of the genre, which is the name.
	"""
	name = models.CharField(max_length=100, default="without_genre")
	slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)

	class Meta:
		db_table = "genre"

	def save(self, *args, **kwargs):
		if not self.slug:
			# Generate a slug from the name
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Production(models.Model):
	"""
	Represents a production entity for storing production-related data.

	This Django model is used to define and manage production entries in the
	database. It includes fields for storing the name of the production and a
	unique slug that can be auto-generated if not provided. The class also defines
	a string representation for instances and contains specifications for database
	table attributes.

	Attributes:
		name (CharField): The name of the production with a maximum length of 255
			characters.
		slug (SlugField): A unique slug for the production used for URLs, which
			can be set to blank or null and defaults to being auto-generated from
			the name if not provided.
	"""
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=270, unique=True, blank=True, null=True)

	class Meta:
		db_table = "production"

	def save(self, *args, **kwargs):
		if not self.slug:
			# Generate a slug from the name
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class MovieComment(models.Model):
	"""
	Represents a comment related to a specific movie within a film database system.

	The MovieComment class is designed to manage and store user comments on movies.
	Each comment is linked to a particular movie and is authored by a registered
	user. The class allows for categorization of comments as approved or not, and
	captures the timestamp of when the comment was created. The data is stored in
	a dedicated database table named "movie_comment" with specific ordering
	preferences.

	Attributes:
		movie: A foreign key referencing the associated Movie, allowing one-to-many
			   relationship between movies and comments.
		author: A foreign key to the user model specifying the author of the
				comment.
		body: A text field containing the main content of the comment.
		approved: A boolean indicating if the comment has been approved for
				  display.
		created_on: Automatically populated timestamp marking when the comment was
					created.

	Meta:
		db_table: Name of the database table used to store the comment data.
		verbose_name: Human-readable singular name of the class representation.
		verbose_name_plural: Human-readable plural name of the class representation.
		ordering: Default ordering of comment instances.
	"""

	movie = models.ForeignKey(
		Movie, on_delete=models.CASCADE, related_name="movie_comments"
		)
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="comment_author",
		)
	body = models.TextField()
	approved = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "movie_comment"
		verbose_name = "Movie comment"
		verbose_name_plural = "Movie comments"
		ordering = [
			"-created_on",
			"author",
			"approved",
			]

	def __str__(self):
		return f"Comment {self.body} | written by {self.author}"
