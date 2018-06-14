try:
		from io import BytesIO
except ImportError:
		from StringIO import StringIO as BytesIO

from PIL import Image
import requests


def combine_images_vertically(images):
		images = list(images)
		widths, heights = zip(*(im.size for im in images))
		total_width = max(widths)
		total_height = sum(heights)

		new_im = Image.new('RGB', (total_width, total_height))

		y_offset = 0
		for im in images:
				new_im.paste(im, (0, y_offset))
				y_offset += im.height

		return new_im


def images_from_urls(urls):
		for u in urls:
				resp = requests.get(u)
				resp.raise_for_status()
				yield Image.open(BytesIO(resp.content))


PAYLOAD = {
		'rainbow.jpg': [
				'https://iiif.wellcomecollection.org/image/B0008771.jpg/0,500,5184,518/3500,350/0/default.jpg',
				'https://iiif.wellcomecollection.org/image/B0010649.jpg/100,450,5617,562/3500,350/0/default.jpg',
				'https://iiif.wellcomecollection.org/image/L0020852.jpg/100,397,1500,150/3500,350/0/default.jpg',
				'https://iiif.wellcomecollection.org/image/B0007248.jpg/0,0,3500,350/3500,350/0/default.jpg',
				'https://iiif.wellcomecollection.org/image/B0010632.jpg/0,3250,4149,415/3500,350/0/default.jpg',
				'https://iiif.wellcomecollection.org/image/B0008754.jpg/700,2500,3500,350/3500,350/0/default.jpg'
		],
        'bisexual.jpg': [
            'https://iiif.wellcomecollection.org/image/B0008050.jpg/0,0,4414,1059/3500,840/0/default.jpg',

            # 'https://iiif.wellcomecollection.org/image/W0043248.jpg/4500,0,406,3384/420,3500/90/default.jpg',
            # 'https://iiif.wellcomecollection.org/image/B0009850.jpg/600,4200,5000,600/3500,420/0/default.jpg',
            # 'https://iiif.wellcomecollection.org/image/s3%3AB0010000%2FB0010309.jpg/200,1000,2598,312/3500,420/0/default.jpg',
            # 'https://iiif.wellcomecollection.org/image/s3%3AB0010000%2FB0010916.jpg/470,1200,1800,216/3500,420/0/default.jpg',
            'https://iiif.wellcomecollection.org/image/s3%3AB0010000%2FB0010916.jpg/480,1200,1600,192/3500,420/0/default.jpg',

            'https://iiif.wellcomecollection.org/image/B0010096.jpg/0,3000,4266,1023/3500,840/0/default.jpg'
        ]
}

for name, images in PAYLOAD.items():
    combine_images_vertically(images_from_urls(images)).save(name)
