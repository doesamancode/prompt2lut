from parsing.text_utils import split_phrases
from style_mapping.mapping_config import (
    TEMPERATURE_KEYWORDS,
    CONTRAST_KEYWORDS,
    SATURATION_KEYWORDS,
    COLOR_KEYWORDS,
    REGION_KEYWORDS,
    INTENSITY_KEYWORDS
)

def parse_prompt(prompt):
    phrases = split_phrases(prompt)
    parsed = []

    for phrase in phrases:
        entry = {
            "phrase": phrase,
            "region": "global",
            "temperature": None,
            "contrast": None,
            "saturation": None,
            "color": None,
            "intensity": 1.0
        }

        for word, factor in INTENSITY_KEYWORDS.items():
            if word in phrase:
                entry["intensity"] = factor

        for word, region in REGION_KEYWORDS.items():
            if word in phrase:
                entry["region"] = region

        for word, value in TEMPERATURE_KEYWORDS.items():
            if word in phrase:
                entry["temperature"] = value

        for word, value in CONTRAST_KEYWORDS.items():
            if word in phrase:
                entry["contrast"] = value

        for word, value in SATURATION_KEYWORDS.items():
            if word in phrase:
                entry["saturation"] = value

        for word, rgb in COLOR_KEYWORDS.items():
            if word in phrase:
                entry["color"] = rgb

        parsed.append(entry)
    
    return parsed