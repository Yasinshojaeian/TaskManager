from django.core.exceptions import ValidationError


def limit_file_size(value): 
    limit = 0.5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('فایل شما بیش از ۵۰۰ کیلوبایت حجم دارد ')
    