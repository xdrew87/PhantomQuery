import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Define color codes (ANSI escape codes for terminal colors)
Wh = "\033[97m"  # White
Gr = "\033[92m"  # Green
Re = "\033[91m"  # Red

def phoneGW():
    User_phone = input(
        f"\n{Wh}Enter phone number (e.g., +6281xxxxxxxxx): {Gr}"
    )
    default_region = "ID"  # Default country is Indonesia
    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number_flag = phonenumbers.is_valid_number(parsed_number)
        is_possible_number_flag = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
            parsed_number, default_region, with_formatting=True
        )
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n{Wh}========== {Gr}PHONE NUMBER INFORMATION {Wh}==========")
        print(f"\n{Wh}Location             :{Gr} {location}")
        print(f"{Wh}Region Code          :{Gr} {region_code}")
        print(f"{Wh}Timezone             :{Gr} {timezoneF}")
        print(f"{Wh}Operator             :{Gr} {jenis_provider}")
        print(f"{Wh}Valid number         :{Gr} {is_valid_number_flag}")
        print(f"{Wh}Possible number      :{Gr} {is_possible_number_flag}")
        print(f"{Wh}International format :{Gr} {formatted_number}")
        print(f"{Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f"{Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f"{Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"{Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f"{Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line or mobile number")
        elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
            print(f"{Wh}Type                 :{Gr} This is a toll-free number")
        elif number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
            print(f"{Wh}Type                 :{Gr} This is a premium-rate number")
        elif number_type == phonenumbers.PhoneNumberType.SHARED_COST:
            print(f"{Wh}Type                 :{Gr} This is a shared-cost number")
        elif number_type == phonenumbers.PhoneNumberType.VOIP:
            print(f"{Wh}Type                 :{Gr} This is a VOIP number")
        elif number_type == phonenumbers.PhoneNumberType.UNKNOWN:
            print(f"{Wh}Type                 :{Gr} Unknown number type")
    except (phonenumbers.phonenumberutil.NumberParseException, phonenumbers.NumberParseException):
        print(f"{Re}Invalid phone number format.{Wh}")
