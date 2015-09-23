from plone import api
import transaction

portal = api.portal.get()

obj = api.content.create(
      type='tdf.templateuploadcenter.tupcenter',
      title='Templatestest',
      description='Test',
      product_description='A test of a template center',
      product_title = 'Templates',
      container= portal
)

transaction.commit()
