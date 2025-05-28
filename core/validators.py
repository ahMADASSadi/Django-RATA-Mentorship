from django.core.validators import RegexValidator



PHONE_NUMBER_VALIDATOR = RegexValidator(message="Phone number must be in 09XXXXXXXXX format",
                                        regex=r"^09\d{9}$")