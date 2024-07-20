from PyKakao import Karlo

api = Karlo(service_key="24985f6faf1ba51637d0c511e3e5caa8")


class KarloService:
    @staticmethod
    def get_text_to_images_url(translated_text: str):
        img_dict = api.text_to_image(translated_text, 1)
        if img_dict is None or img_dict.get("images") is None:
            return None
        img_str = img_dict.get("images")[0].get('image')
        return img_str
