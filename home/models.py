from django.db import models

from wagtail.core.models import Page

from wagtail.core.fields import RichTextField
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page
from wagtail.search import index

class HomePage(Page):
    """home page main"""

    templates="home/home_page.html"
    max_count =1

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    banner_subtitle = RichTextField(features=["bold","italic"],default="Some String")
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+")
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+")
    
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("blog_image"),
        PageChooserPanel("banner_cta"),
        InlinePanel('gallery_images', label="Gallery images"),
        
    ]
    
    #body = RichTextField(blank=True)
    #content_panels = Page.content_panels + [FieldPanel('body', classname="full"),]
class OrientePage(Page):
    nombre_playa = RichTextField(features=["bold","italic"],default="nombre de la playa")
    ubicacion_playa = RichTextField(features=["bold","italic"],default="direccion de la playa")
    body = RichTextField(blank=True)
    oriente_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+")


    content_panels = Page.content_panels + [
        FieldPanel("nombre_playa"),
        FieldPanel("ubicacion_playa"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel("oriente_image"),

        
    ]

class CentroPage(Page):
    nombre_playa = RichTextField(features=["bold","italic"],default="nombre de la playa")
    ubicacion_playa = RichTextField(features=["bold","italic"],default="direccion de la playa")
    body = RichTextField(blank=True)
    centro_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+")


    content_panels = Page.content_panels + [
        FieldPanel("nombre_playa"),
        FieldPanel("ubicacion_playa"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel("centro_image"),

            
        ]

class OccidentePage(Page):
    nombre_playa = RichTextField(features=["bold","italic"],default="nombre de la playa")
    ubicacion_playa = RichTextField(features=["bold","italic"],default="direccion de la playa")
    body = RichTextField(blank=True)
    occidente_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+")


    content_panels = Page.content_panels + [
        FieldPanel("nombre_playa"),
        FieldPanel("ubicacion_playa"),
        FieldPanel('body', classname="full"),
        ImageChooserPanel("occidente_image"),            
        ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

